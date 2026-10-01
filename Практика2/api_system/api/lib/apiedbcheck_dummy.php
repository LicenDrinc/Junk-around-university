<?php
// права суперпользователя EDUBASE/api или выше
function is_apisuper($userid)
{
    global $api_super;
    return ($userid==$api_super);
}

// права суперпользователя EDUBASE, пользователя api или выше
function is_apiuser($userid)
{
    global $api_user;
    return is_apisuper($userid)||($userid==$api_user);
}

// права оператора EDUBASE, суперпользователя api или выше
function is_apioper($userid)
{
    global $api_oper;
    return is_apiuser($userid)||($userid==$api_oper);
}

function get_userpwd($login)
{
    return "";
}

function userid2login($userid)
{
    return $userid;
}

function apikey_check($apikey){
    global $api_super,$api_user,$api_oper;
    global $api_super_key,$api_user_key,$api_oper_key;
    if ($apikey==$api_super_key) return $api_super;
    if ($apikey==$api_user_key) return $api_user;
    if ($apikey==$api_oper_key) return $api_oper;
    return "";
 }



function edb_api_check($address,$command,$data,$ssl_verify=false)
{
    $data_string = json_encode ($data, JSON_UNESCAPED_UNICODE);
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $address.$command);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER,$ssl_verify);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST,$ssl_verify);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_HTTPHEADER, [
       'Content-Type: application/json',
       'Content-Length: ' . strlen($data_string)
    ]);
    $result = curl_exec($curl);
    curl_close($curl);
    return json_decode($result,true);
}

function edb_api_checkA($address,$command,$data,$ssl_verify=false)
{
    $data_string = json_encode ($data, JSON_UNESCAPED_UNICODE);
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $address.$command);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER,$ssl_verify);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST,$ssl_verify);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_HTTPHEADER, [
       'Content-Type: application/json',
       'Content-Length: ' . strlen($data_string)
    ]);
    $result = curl_exec($curl);
    curl_close($curl);
    return $result;
}
