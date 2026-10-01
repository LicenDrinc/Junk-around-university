<?php
function errorReturnExit($t)
{
    print $t;
    exit;
}
if (isset($_POST))
{
    if (isset($_POST['image']))
    {
	print '<p>YES Base 64';
	//print ' => '.$_POST['image'];
	print '</p>';
    }
    else
    {
	errorReturnExit('<p>NOT Base 64</p>');
    }
    if (!isset($_POST['format']))
    {
	errorReturnExit('<p>NO FORMAT</p>');
    }
    if (!isset($_POST['fileDoc1']))
    {
	errorReturnExit('<p>NO FILE</p>');
    }
}
else
{
    errorReturnExit('<p>NOT OK</p>');
}

$base64Data = json_decode($_POST['image']);
$fileData = base64_decode($base64Data);

$fileName = '/tmp/'.$_POST['fileDoc1'];

$fileNewName = '';
for ($i = 0; $i <= strripos($fileName,'.',-1); $i++)
{
    $fileNewName = $fileNewName.$fileName[$i];
}
$fileNewName = $fileNewName.$_POST['format'];

file_put_contents($fileName,$fileData);

exec('convert '.$fileName.' '.$fileNewName);
unlink($fileName);

$fileName = '';
for ($i = 0; $i < strripos($_POST['fileDoc1'],'.',-1); $i++)
{
    $fileName = $fileName.$_POST['fileDoc1'][$i];
}

if (!file_exists($fileNewName))
{
    print '<p>файл не сканвертировался</p>';
    exit;
}

header('Content-Description: File Transfer');
header('Content-type: application/octet-stream');
header('Content-Disposition: attachment; filename='.$fileName.'.'.$_POST['format']);
//header('Content-Transfer-Encoding: binary');
//header('Expires: 0');
//header('Cache-Control: must-revalidate');
//header('Pragma: public');
header('Content-Length: '.filesize($fileNewName));

if (ob_get_level())
{
    ob_end_clean();
}

readfile($fileNewName);
unlink($fileNewName);
exit;
?>