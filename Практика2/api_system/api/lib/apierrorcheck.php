<?php

function api_estring($error){
    global $api_errors;
    $args=func_get_args();
    array_shift($args);
    return(vsprintf($api_errors[$error],$args));
}

function api_error($error) {
    global $api_errors,$response_body;
    $args=func_get_args();
    array_shift($args);
    $res['errors']=vsprintf($api_errors[$error],$args);
    $res['error']=$error;
    return api_json_result($res);
}

function api_app_error($error,$errors) {
    global $response_body;
    $res['errors']=$error.": ".$errors;
    $res['error']=$error;
    return api_json_result($res);
}

