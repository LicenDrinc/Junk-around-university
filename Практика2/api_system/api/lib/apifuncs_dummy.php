<?php
 function apilog_sql(){
  return "INSERT dummy";
 }

 define("EDBAPI_MAXLOGLEN",100);
 function is_apilog(){ global $EDBAPI; return $EDBAPI["base"]["logs"]!='none'; }
 function is_apilog_debug(){ global $EDBAPI; return ($EDBAPI["base"]["logs"]=='debug')or($EDBAPI["base"]["logs"]=='dbase-debug'); }
 function is_apilog_dbase(){ global $EDBAPI; return ($EDBAPI["base"]["logs"]=='dbase')or($EDBAPI["base"]["logs"]=='dbase-debug'); }

 function apilog_prepare(&$val) {
  if (is_string($val)and($len=(strlen($val)>EDBAPI_MAXLOGLEN))){
    $conv="Строка урезана: ";
    $val=$conv.substr($val, 0, EDBAPI_MAXLOGLEN-strlen($conv)-3).'...';
    return;
  }
  if (is_array($val)) foreach ($val as $key=>&$v1) if($key=='apikey')$v1="***";else apilog_prepare($v1);
 }

 function apilog($name,$value){
    if (!is_apilog()) return;
    global $LOGS;
    apilog_prepare($value);
    $LOGS[$name]=$value;
 }


function api_json_result($value) {
    global $response_body,$EDBAPI;
    $response_body=json_encode($value,JSON_UNESCAPED_UNICODE);
    $EDBAPI["json_result"]=true;
    if (is_apilog()) $EDBAPI["src_result"]=$value;
    return true;
 }

 function apipart(){
    $dir=dirname($_SERVER['PHP_SELF']);
    $uri=$_SERVER['REQUEST_URI'];
    $path = substr($uri, strlen($dir));
    return substr($path,0,strrpos($path,'/'))."/";
 }

 function apicommand(){
    $dir=dirname($_SERVER['PHP_SELF']);
    $uri=$_SERVER['REQUEST_URI'];
    $path = substr($uri, strlen($dir));
    $command = substr($path,strrpos($path,'/')+1);
    $parse=parse_url($command);
    @parse_str($parse["query"],$parse["query"]);
    return [$parse["path"],$parse["query"]];
 }

 function index_gen(){
    global $EDBAPI;
    $res=$EDBAPI["base"];
    $apidir=$EDBAPI["apidir"];
    $part=$res["part"];
    foreach ($EDBAPI["parts"][$part] as $cmd){
        if (!$cmd)continue;
        $cdir=$apidir.$part.$cmd;
        @include $cdir."_config.php";
        //$config["part"]=$part;
        $config["command"]=$cmd;
        if (isset($help))$config["help"]=$help;
        if (isset($config))$res["valid_commands"][$cmd]=$config;
        unset($config);
        unset($help);
    }
    return $res;
 }


 function apiexec_command($part,$command,$request,$request_errors){
    global $EDBAPI,$api_errors,$response_header,$response_body,$request;
    $defcommand=$EDBAPI["defcommand"];
    $apidir=$EDBAPI["apidir"];

    if (!$command) {
        $EDBAPI["base"]["command"]=$defcommand;
        $command=$defcommand;
    }
    $cdir=$apidir.$part.$command;

    if (!file_exists($cdir."_config.php") ||
        !file_exists($cdir.".php")){
        $error=api_estring(ECOMCONF,$part,$command) ; //"\nВ разделе $part недоступна команда $command или ее конфигурация";
        $part="/";
        $command="";
        apiexec_command($part,$command,$request,$request_errors.($request_errors?"\n":"").$error);
        return false;
    }
    if ($request_errors) {
        $EDBAPI["error"]=1;
        $EDBAPI["errors"]=$request_errors;
    }
    return require_once $cdir.".php";
 }

 function apiexec(){
    global $EDBAPI,$api_errors;
    $defcommand=$EDBAPI["defcommand"];
    $req_part=$EDBAPI["base"]["part"];//apipart();
    $req_command=$EDBAPI["base"]["command"];//apicommand();
    if (!isset($EDBAPI["parts"][$req_part])){
        $part="/";
        $command=$defcommand;
        $error=api_estring(EPARTDEFCOM,$req_part,$defcommand);//"Раздел $req_part недоступен, выполняется команда $defcommand основного раздела";
        apiexec_command($part,$command,[],$error);
        return false;
    }
    elseif (!in_array($req_command,$EDBAPI["parts"][$req_part])){
        $part="/";
        $command=$defcommand;
        $error=api_estring(EPARTCOMDEFCOM,$req_part,$req_command,$defcommand);//"В разделе $req_part недоступна команда $req_command, выполняется команда $defcommand основного раздела";
        apiexec_command($part,$command,[],$error);
        return false;
    }
    return apiexec_command($req_part,$req_command,[],"");
 }

# возращает либо значение запрошенного поле, либо массив запрошенных
# полей
# при escape==true возврат подмассивов в исходном виде невозможен
# так как все данные возвращаются как экранированные строки
function api_get_request($fields,$escape=true){
    global $request;
    if (!is_array($fields))
        if ($escape) return @mysql_escape($request[$fields]);
        else return @$request[$fields];
    foreach ($fields as &$value){
        @$value=$request[$value];
        if ($escape) $value=mysql_escape($value);
    }
    return $fields;
}

# возращает либо значение запрошенного поле, либо массив запрошенных
# полей. Про отсутствии хотя-бы одного поля генерирует ошибку в
# json-ответе и возвращает false
# при escape==true возврат подмассивов в исходном виде невозможен
# так как все данные возвращаются как экранированные строки
function api_check_request($fields,$escape=true){
    global $request;

    if (!is_array($fields))
        if(isset($request[$fields]))return $request[$fields];
        else return !api_error(EFIELDNONE,$fields);

    foreach ($fields as &$value){
	$val=$value;
        @$value=$request[$value];
        if (is_null($value)) return !api_error(EFIELDNONE,$val);
        if ($escape) $value=mysql_escape($value);
    }
    return $fields;

}

