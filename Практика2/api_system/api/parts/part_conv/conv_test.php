#!/usr/bin/php
<?php

require_once "./../../lib/apiedbcheck.php";
require_once "./../../../api_security/security.php";

//$address='https://vc.shspu.ru/release/current/api';
$address='http://localhost/api_system/api';
//$address='http://pra-conv.shgpi/api_system/api';

$command='/part_conv/conv';

$i = 1;
function casePara($n) {
    global $i, $data, $argv;
    $i++; $data[$n] = $argv[$i];
}

for ($j = 0; $i != $argc - 1 && strpos($argv[$i], '-') !== 0; $j++, $i++) {
    $k = strrpos($argv[$i],'/');
    if ($k === false) $data["filename"][$j] = $argv[$i];
    else $data["filename"][$j] = substr($argv[$i], $k+1);
    $data["file"][$j] = base64_encode(file_get_contents($argv[$i]));
}

for (; $i < $argc - 1; $i++) {
    if (strpos($argv[$i], '-') === 0) {
	switch ($argv[$i]) {
	    case "-resize"; casePara("resize"); break;
	    case "-quality"; casePara("quality"); break;
	    case "-rotate"; casePara("rotate"); break;
	    case "-blur"; casePara("blur"); break;
	    case "-bordercolor"; casePara("bordercolor"); break;
	    case "-border"; casePara("border"); break;
	    default; print($argv[$i]." нету того параметра\n");
	}
    }
}

//$data["apikey"] = $api_guest_key;
$data["apikey"] = $api_super_key;
$k = strrpos($argv[$i],'/');
if ($k === false) $data["fileout"] = $argv[$i];
else $data["fileout"] = substr($argv[$i], $k+1);
$result=edb_api_check($address,$command,$data);

//var_dump($data);
//var_dump($result);

if ($result['error'] == 0)
{
    if (!file_put_contents(($k === false ? "" : substr($argv[$i],0,$k+1)).
	$result['filename'], base64_decode($result['file'])))
	var_dump($result);
}
else var_dump($result);
