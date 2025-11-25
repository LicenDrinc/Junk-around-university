<?php

$url = "https://vc.shspu.ru/release/current/api/";
$url1 = readline();
if ($url1 == "+") $url = $url.readline();
if ($url1 != "" && $url1 != "+") $url = $url1;
print_r($url."\n");

$parts = curl_init($url);
curl_setopt($parts, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($parts);
curl_close($parts);
$data = json_decode($response, true);

$data1 = $data;
while (true)
{
	$t = readline();
	if ($t == "")
	{
		if (is_array($data1))
		{
			foreach($data1 as $key => $value)
				print_r($key."\n");
		}
		else print_r($data1."\n");
		break;
	}
	else $data1 = $data1[$t];
}

?>
