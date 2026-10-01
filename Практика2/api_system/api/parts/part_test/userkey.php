<?php

# проверка наличия обязательных полей для этой команды
$req=api_check_request(["apikey"]);
if (!$req) return true;
list($apikey)=$req;

# проверка корректности ключа
$userid=apikey_check($apikey);
if (!$userid) return api_error(EFIELDBAD,"apikey");

# все норм, утверждаем это
$res['errors']="";
$res['error']=0;
$res['login']=userid2login($userid);
return api_json_result($res);
