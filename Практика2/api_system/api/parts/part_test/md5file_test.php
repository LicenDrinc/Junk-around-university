#!/usr/bin/php
<?php

require_once "./../../lib/apiedbcheck.php";
require_once "./../../../api_security/security.php";

//$address='https://vc.shspu.ru/release/current/api';
$address='http://pra-conv.shgpi/api_system/api';

$command='/part_test/md5file';

$data = [
//    "apikey" => $api_guest_key,
    "apikey" => $api_super_key,
    "filename" => $argv[0],
    "file" => base64_encode(file_get_contents($argv[0])),
];

$result=edb_api_check($address,$command,$data);

var_dump($result);
