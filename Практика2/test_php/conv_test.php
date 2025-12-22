#!/usr/bin/php
<?php

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

$api_guest='api_guest'; $api_guest_key='api_guest_key';
$api_user='api_user'; $api_user_key='api_user_key';
$api_oper='api_oper'; $api_oper_key='api_oper_key';
$api_super='api_super'; $api_super_key='api_super_key';

//$address='https://vc.shspu.ru/release/current/api';
$address='http://localhost/api_system/api';
//$address='http://pra-conv.shgpi/api_system/api';
$command='/part_conv/conv';

require_once "./from_test.php";

for ($i1 = 0; $i1 < count($from); $i1++) {
	echo $i1."\n";
	$data = [];
	$data["apikey"] = $api_super_key;
	$i = 0;

	for ($j = 0; $i != count($from[$i1]) - 1 && strpos($from[$i1][$i], '-') !== 0; $j++, $i++) {
		$k = strrpos($from[$i1][$i],'/');
		if ($k === false) $data["filename"][$j] = $from[$i1][$i];
		else $data["filename"][$j] = substr($from[$i1][$i], $k+1);
		$data["file"][$data["filename"][$j]] = base64_encode(file_get_contents($from[$i1][$i]));
	}

	for (; $i < count($from[$i1]) - 1; $i++) {
		if (strpos($from[$i1][$i], '-') === 0) {
			switch ($from[$i1][$i]) {
				case "-typeconvert": $i++; $data["typeconvert"] = $from[$i1][$i]; break;
				case "-resize": $i++; $data["resize"] = $from[$i1][$i]; break;
				case "-quality": $i++; $data["quality"] = $from[$i1][$i]; break;
				case "-rotate": $i++; $data["rotate"] = $from[$i1][$i]; break;
				case "-blur": $i++; $data["blur"] = $from[$i1][$i]; break;
				case "-bordercolor": $i++; $data["bordercolor"] = $from[$i1][$i]; break;
				case "-border": $i++; $data["border"] = $from[$i1][$i]; break;
				case "-delay": $i++; $data["delay"] = $from[$i1][$i]; break;
				case "-loop": $i++; $data["loop"] = $from[$i1][$i]; break;
				default: print($from[$i1][$i]." нету того параметра\n");
			}
		}
	}

	$k = strrpos($from[$i1][$i],'/');
	if ($k === false) $data["fileout"] = $from[$i1][$i];
	else $data["fileout"] = substr($from[$i1][$i], $k+1);

	//echo "--------\n"; var_dump($data);
	//echo "--------\n"; var_dump($result);
	//echo "--------\n";

	$result = edb_api_check($address,$command,$data);
	if ($result['error'] == 0)
	{
		if (!file_put_contents(($k === false ? "" : substr($from[$i1][$i],0,$k+1)).$result['filename'], base64_decode($result['file'])))
			var_dump($result);
	}
	else var_dump($result);
}