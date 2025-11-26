#!/usr/bin/php
<?php

require_once "./../../lib/apiedbcheck.php";
require_once "./../../../api_security/security.php";

//$address='https://vc.shspu.ru/release/current/api';
$address='http://localhost/api_system/api';
//$address='http://pra-conv.shgpi/api_system/api';

$command='/part_conv/conv';

$data = [
//    "apikey" => $api_guest_key,
    "apikey" => $api_super_key,
    "filename" => substr($argv[1],strrpos($argv[1],'/')+1),
    "file" => base64_encode(file_get_contents($argv[1])),
    "fileformat" => $argv[2],
];

$result=edb_api_check($address,$command,$data);

if ($result['error'] == 0)
{
    if (!file_put_contents(substr($argv[1],0,strrpos($argv[1],'/')+1).$result['filename'], base64_decode($result['file'])))
	var_dump($result);
}
else
    var_dump($result);
