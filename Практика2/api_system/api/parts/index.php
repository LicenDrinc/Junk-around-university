<?php

$errors="";
$apidir=$EDBAPI["apidir"];
$res=$EDBAPI["base"];
$currpart=$res["part"];
$currcmd=$res["command"];
$res["error"]=$EDBAPI["error"];
$res["errors"]=$EDBAPI["errors"];

foreach ($EDBAPI["parts"] as $part=>$commands){
    if (in_array($part,$EDBAPI["hidden_parts"])) continue;
    foreach ($commands as $cmd){
        if (!$cmd)continue;
        $cdir=$apidir.$part.$cmd;
        @include $cdir."_config.php";
        if($part==$currpart && $cmd==$currcmd) $res["help"]=$help;
        $config["part"]=$part;
        $config["command"]=$cmd;
        $res["valid_parts"][$part][$cmd]=$config;
        unset($config);
        unset($help);
    }
}

return api_json_result($res);
