<?php
 $EDBAPI_ENTER = true;
 $EDBAPI_READY = (require_once __DIR__."/EDBconnect.php");
 require_once __DIR__."/../api_security/security.php";
 require_once __DIR__."/lib/apierrors.php";
 require_once __DIR__."/lib/apiedbcheck.php";
 require_once __DIR__."/lib/apierrorcheck.php";
 require_once __DIR__."/lib/apifuncs.php";
 require_once __DIR__."/config.php";

// +++ журнал +++
if (is_apilog()){
/*
    Журналирование запросов.
    Контролируется параметром $EDBAPI["base"]["logs"]
    с возможными значениями none,dbase,debug,dbase-debug
     none - не ведется
     dbase - ведется с сохранением в базе данных
     debug - ведется с возвратом только в json-ответе полем 'logs'
     dbase-debug - dbase+debug))
*/
 $LOGS=[];

 $LOGS['version']=$EDBAPI['base']["version"];
 $LOGS['part']="";
 $LOGS['command']="";
 $LOGS['uid']="0";

 $LOGS['remote_addr']=$_SERVER['REMOTE_ADDR'];
 @$LOGS['user_agent']=($_SERVER['HTTP_USER_AGENT'])?$_SERVER['HTTP_USER_AGENT']:"";

 $LOGS['date_start']=date("Y-m-d H:i:s");
 $LOGS['time_begin']=hrtime(true);
 $LOGS['time_work']='';

 $LOGS['request_method']=$_SERVER['REQUEST_METHOD'];
 $LOGS['request_data_get']='';
 $LOGS['request_data_post']='';
 $LOGS['request_data_stream']='';
 $LOGS['request_data']='';

 $LOGS['response_error']='';
 $LOGS['response_errors']='';
}
// --- журнал ---


 $session_path=$EDBAPI["base"]["basedir"];
 session_set_cookie_params (0,$session_path,$_SERVER['HTTP_HOST'],true);

 $response_headers=[
    'Content-Type: application/json; charset=utf-8',
 ];


 $request=[];
 if ($_SERVER['REQUEST_METHOD']=="POST" || $_SERVER['REQUEST_METHOD']=="GET") {
    if (count($_GET)) {$request=$_GET;apilog('request_data_get',$_GET);} else $request=$EDBAPI["base"]["query"];
    $request=array_diff_key($request,array_fill_keys($EDBAPI["sec_fields"],''));
    if (count($_POST)) {$request=array_replace($request,$_POST);apilog('request_data_post',$_POST);}
    $jsondec=json_decode(file_get_contents("php://input"),true);
    if ($jsondec && count($jsondec)) {$request=array_replace($request,$jsondec);apilog('request_data_stream',$jsondec);}
 }
 apilog('request_data',$request);


 header('Access-Control-Allow-Origin: *');
 apiexec();

 if (!isset($response_headers)||!isset($response_body)) die('API error: EDUBASE unavailable');

 foreach ($response_headers as $header) header($header);

// +++ журнал +++
 if (is_apilog()){
  if ($EDBAPI["json_result"]) {

        if (isset($EDBAPI["src_result"]['error'])) 
             $LOGS['response_error']=$EDBAPI["src_result"]['error'];
        else $LOGS['response_error']="0";

        if (isset($EDBAPI["src_result"]['errors'])) 
             $LOGS['response_errors']=$EDBAPI["src_result"]['errors'];
        else $LOGS['response_errors']="";

//        $LOGS['response_error']="errrrr";//$EDBAPI["src_result"]['error'];
//        $LOGS['response_error']=$EDBAPI["src_result"]['errors'];

        apilog('response_data',$EDBAPI["src_result"]);
  }
  $LOGS['version']=$EDBAPI['base']["version"];
  $LOGS['part']=$EDBAPI['base']["part"];
  $LOGS['command']=$EDBAPI['base']["command"];
  $LOGS['time_work']=(hrtime(true)-$LOGS['time_begin'])/1000000000;
  unset($LOGS['time_begin']);
 }

 if (is_apilog_debug() and $EDBAPI["json_result"]) {
    $EDBAPI["src_result"]['logs']=$LOGS;
    $response_body=json_encode($EDBAPI["src_result"],JSON_UNESCAPED_UNICODE);
 }

 if (is_apilog_dbase()) {
    mysql_execute(apilog_sql());
 }

// --- журнал ---

 echo $response_body;

 return true;
