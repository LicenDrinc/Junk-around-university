<?php

# проверка наличия обязательных полей для этой команды
$req=api_check_request(["apikey","file","filename"]);
if (!$req) return true;
list($apikey,$file,$filename)=$req;

# проверка корректности ключа
$userid=apikey_check($apikey);
if (!$userid) return api_error(EFIELDBAD,"apikey");

$md5=md5(base64_decode($file));
# все норм, утверждаем это
$res['errors']="";
$res['error']=0;
$res['md5']=$md5;
$res['check']="для проверки запустить md5sum $filename";

return api_json_result($res);
