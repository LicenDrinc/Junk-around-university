<?php
// процедура для прекращение работы php и отправки результата клиенту
// $r название результата, $t результат
function returnExit($t, $r)
{
    header('Content-type: application/json');
    echo json_encode([$r => $t]);
    exit;
}

// создание временного файл
// $n название файла, $d данные файла
$fileName = '';
function creatingATemporaryFile($n, $d)
{
    global $fileName;
    $fileName = '/tmp/'.$n;
    $fileData = base64_decode($d);
    file_put_contents($fileName, $fileData);
}

// создание пути или имяни файла
// $f формат файла, $fN пути или имея файла
function creatingAPathToConvertedFile($f ,$fN)
{
    $fNN = '';
    for ($i = 0; $i <= strripos($fN,'.',-1); $i++)
        $fNN = $fNN.$fN[$i];
    $fNN = $fNN.$f;
    return $fNN;
}

// отправка файла в json и прекращение работу
function sendingFileInJson()
{
    global $fileNewName, $fileDoc2, $data;
    header('Content-type: application/json');
    $data['image'] = base64_encode(file_get_contents($fileNewName));
    $data['fileDoc1'] = $fileDoc2;
    echo json_encode($data);
    unlink($fileNewName);
    exit;
}

// проверка POST
if ($_SERVER['REQUEST_METHOD'] === 'POST')
{
    // получение json
    $input = file_get_contents('php://input');
    $data = json_decode($input,true);
    //returnExit($data['fileDoc1'],"debug");
    
    // проверка base64
    if (isset($data['image']))
	    $base64Data = $data['image'];
    else
	    returnExit("нет файла","error");
    // проверка формата
    if (!isset($data['format']))
	    returnExit("нет формата","error");
    // проверка названия исходного файла
    if (!isset($data['fileDoc1']))
	    returnExit("нет имени файла","error");
}
else
{
    returnExit("POST пустой или нету","error");
}

// создание временного файл
creatingATemporaryFile($data['fileDoc1'], $base64Data);
// создание пути конвертированого файла
$fileNewName = creatingAPathToConvertedFile($data['format'],$fileName);

// дабовление пораметры конвертации
$porametrs = '';
if ($data['format'] == "pdf")
{
    if ($data['dpi'] != null)
        $porametrs = $porametrs.'-density '.$data['dpi'].' ';
    if ($data['compress'] != "none")
        $porametrs = $porametrs.'-quality '.$data['qua'].' -compress '.$data['compress'].' ';
    if ($data['mono'] == 'true')
        $porametrs = $porametrs.'-monochrome ';
}

// конвертирование временого вайла
exec('convert '.$porametrs.$fileName.' '.$fileNewName);
// удаление временого файла
unlink($fileName);

// создание название конвертированого файла для отправки
$fileDoc2 = creatingAPathToConvertedFile($data['format'],$data['fileDoc1']);

// проверка сканвертированого
if (!file_exists($fileNewName))
    returnExit("файл не сканвертировался","error");

sendingFileInJson();
?>