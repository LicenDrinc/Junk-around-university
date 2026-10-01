<?php
define('EDBAPISID','edbapi_sid');

// базовая информация об api, остальная собирается из конфигурационных файлов команд
$EDBAPI["base"]=[
    "info"=>"EDUBASE-API-DUMMY",
    "version"=>"2025.11.24.0",
    "ready"=>$EDBAPI_READY,
    "htmlman"=>"../api_man/",
    "basedir"=>dirname($_SERVER['PHP_SELF'])."/",
    "part"=>apipart(),
    "logs"=>'none',// none,dbase,debug,dbase-debug
];
list($EDBAPI["base"]["command"],$EDBAPI["base"]["query"])=apicommand();

$EDBAPI["error"]=0;
$EDBAPI["errors"]="";

// устанавливает в true, если response_body в формате json
// при этом устанавливает src_result в не преобразованное response_body
$EDBAPI["json_result"]=false;

// разрешенные разделы и команды api, индекс всегд разрешен
$EDBAPI["parts"]=[
    "/"=>[],
    "/part_test/"=>["userkey","md5file"],
    "/part_conv/"=>["conv"],
];

// скрытые от самодокументирования разделы
$EDBAPI["hidden_parts"]=["/0/"];

// поля, запрещенные к передаче открытым способом (GET, query)
$EDBAPI["sec_fields"]=[//'edbapi_sid',
                        'apikey', 'pwd','oldpwd','newpwd'];

// команда по умолчанию "" эквивалентна команде "index"
// ни ту, ни другую не следует указывать в списке, добавляются автоматически
$EDBAPI["defcommand"]="index";
foreach($EDBAPI["parts"] as $key=>$value){ array_unshift($EDBAPI["parts"][$key],"",$EDBAPI["defcommand"]); }

$EDBAPI["apidir"]=__DIR__."/parts";
