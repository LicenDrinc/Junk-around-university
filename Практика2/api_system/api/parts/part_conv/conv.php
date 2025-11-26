<?php

# проверка наличия обязательных полей для этой команды
$req = api_check_request(["apikey","file","filename","fileformat"]);
if (!$req) return true;
list($apikey,$file,$filename,$fileformat) = $req;

# проверка корректности ключа
$userid = apikey_check($apikey);
if (!$userid) return api_error(EFIELDBAD,"apikey");

# создание временного файл: $n название файла, $d данные файла, возращает путь к файлу
function creatingATemporaryFile($n, $d)
{
    $n = '/tmp/'.$n;
    $filedata = base64_decode($d);
    file_put_contents($n, $filedata);
    return $n;
}

# создание пути или имяни файла: $f формат файла, $fN пути или имея файла, возращает путь к файлу
function creatingAPathToConvertedFile($f ,$fN)
{
    $fNN = '';
    for ($i = 0; $i <= strripos($fN,'.',-1); $i++) $fNN = $fNN.$fN[$i];
    return $fNN.$f;
}

$filenametmp = $filename;
# создание временного файл
$filenametmp = creatingATemporaryFile($filenametmp, $file);
# создание пути конвертированого файла
$filenewnametmp = creatingAPathToConvertedFile($fileformat, $filenametmp);

# проверка временого файла
if (!file_exists($filenametmp))
{
    $res['errors'] = "файл не создался";
    $res['error'] = 900;
    return api_json_result($res);
}

# дабовление пораметры конвертации
$porametrs = '';
/*
if ($fileformat == "pdf")
{
    if ($data['dpi'] != null)
	$porametrs = $porametrs.'-density '.$data['dpi'].' ';
    if ($data['compress'] != "none")
	$porametrs = $porametrs.'-quality '.$data['qua'].' -compress '.$data['compress'].' ';
    if ($data['mono'] == 'true')
        $porametrs = $porametrs.'-monochrome ';
}
*/

# конвертирование временого вайла
$execlog = exec('convert '.$porametrs.$filenametmp.' '.$filenewnametmp);
# удаление временого файла
unlink($filenametmp);

# создание название конвертированого файла для отправки
$filenewname = creatingAPathToConvertedFile($fileformat,$filename);

# проверка сканвертированого
if (!file_exists($filenewnametmp))
{
    $res['errors'] = "конвертация прошла не успешно";
    $res['error'] = 800;
    return api_json_result($res);
}

$newfile = base64_encode(file_get_contents($filenewnametmp));
unlink($filenewnametmp);

# все норм, утверждаем это
$res['errors'] = ""; $res['error'] = 0;
$res['file'] = $newfile;
$res['filename'] = $filenewname;

return api_json_result($res);
