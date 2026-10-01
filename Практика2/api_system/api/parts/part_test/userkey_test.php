#!/usr/bin/php
<?php

require_once "./../../lib/apiedbcheck.php";
require_once "./../../../api_security/security.php";

//$address='https://vc.shspu.ru/release/current/api';
$address='https://localhost/api_system/api';

$command='/test/userkey';

$data = [
//    "apikey" => $api_guest_key,
    "apikey" => $api_super_key,
];

$result=edb_api_check($address,$command,$data);

var_dump($result);
