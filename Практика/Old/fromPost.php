<?php
print '<html>';
print '<head><title>fromPost</title></head>';
print '<body>';
function errorReturnExit($t)
{
    print $t;
    print '<form action="index.html"><button>вернутся</button></form>';
    exit;
}
if (isset($_POST))
{
    if (isset($_POST['format']))
    {
	print '<p>YES FORMAT => '.$_POST['format'].'</p>';
    }
    else
    {
	errorReturnExit('<p>NOT FORMAT</p>');
    }
    if (is_uploaded_file($_FILES['fileDoc']['tmp_name']))
    {
	$file = $_FILES['fileDoc'];
	print '<p>YES FILE ';
	//print $_FILES['fileDoc']['tmp_name'].' '.$file['tmp_name'];
	print '</p>';
    }
    else
    {
	errorReturnExit('<p>NOT FILE</p>');
    }
}
else
{
    errorReturnExit('<p>NOT OK</p>');
}

$JsonDataExport = json_encode(Base64_encode(file_get_contents($file['tmp_name'])));

$url = 'http://pra-conv.shgpi/';
//$url = 'http://localhost/';

print '<form action="'.$url.'fromGet.php'.'" method="post">';
print '<input type="hidden" value="'.$_POST['format'].'" name="format">';
print "<input type='hidden' value='".$JsonDataExport."' name='image'>";
print '<input type="hidden" value="'.$file['name'].'" name="fileDoc1">';
print '<button>получить</button>';
print '</form>';

print '<form action="index.html"><button>вернутся</button></form>';

print '</body>';
print '</html>';
?>
