<?php

# проверка наличия обязательных полей для этой команды
$req = api_check_request(["apikey","file","filename","fileout"]);
if (!$req) return true;
list($apikey,$file,$filename,$fileout) = $req;

# проверка корректности ключа
$userid = apikey_check($apikey);
if (!$userid) return api_error(EFIELDBAD,"apikey");

# создание временного файл:
# $n название файла, $d данные файла, возращает путь к файлу
function creatingATemporaryFile($n, $d) {
    $n = '/tmp/'.md5(time().rand()).$n;
    file_put_contents($n, base64_decode($d));
    return $n;
}

# создание временных файлов
$filenamelist = '';
for ($i = 0; $i < count($filename); $i++) {
    $filenametmp[$i] = creatingATemporaryFile($filename[$i], $file[$i]);
    $filenamelist .= $filenametmp[$i].' '; # добавление в список файлов для конвертации
    # проверка временого файла
    if (!file_exists($filenametmp[$i])) {
        $res['errors'] = "создание временого файла прошла не успешно";
        $res['error'] = 900+$i;
	for ($j = 0; $j < $i; $j++) unlink($filenametmp[$j]);
	return api_json_result($res);
    }
}

# создание пути конвертированого файла
$filenewnametmp = "/tmp/".md5(time().rand()).$fileout;

# дабовление пораметры конвертации
$parametrs = '';
$fileformat = substr($fileout,strrpos($fileout,'.')+1);
$image = array('png','jpeg','jpg','gif','bmp','tiff','tif','webp','avif','heif','heic','raw','jxl','svg','eps','pdf','ai','cdr');
$imageparaname = array('resize','quality','rotate','blur','bordercolor','border');
$imagetopara = [
    'resize'=>'-resize','quality'=>'-quality','rotate'=>'-rotate',
    'blur'=>'-blur','bordercolor'=>'-bordercolor','border'=>'-border'
];
if (in_array($fileformat, $image)) {
    for ($i = 0; $i < count($imageparaname); $i++) {
        $reqpara = api_check_request($imageparaname[$i]);
        if ($reqpara !== false) $parametrs .= $imagetopara[$imageparaname[$i]].' '.$reqpara.' ';
    }
}

# конвертирование временого вайла
$execlog = exec('convert '.$filenamelist.$parametrs.$filenewnametmp);

# удаление временых файлов
for ($i = 0; $i < count($filenametmp); $i++) unlink($filenametmp[$i]);

# проверка сканвертированого
if (!file_exists($filenewnametmp)) {
    $res['errors'] = "конвертация прошла не успешно";
    $res['error'] = 800; return api_json_result($res);
}

# полученое содержимого сконвертированого файла
$newfile = base64_encode(file_get_contents($filenewnametmp));
unlink($filenewnametmp); # удаление сконвертированого временого файла

# все норм, утверждаем это
$res['errors'] = ""; $res['error'] = 0;
$res['file'] = $newfile; $res['filename'] = $fileout;

return api_json_result($res);
