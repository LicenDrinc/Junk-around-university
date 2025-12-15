<?php

# прикрощение работы и отправки ошибки: $n информация об ошибке, $b номер ошибки
function exitError($n, $b) { $res['errors'] = $n; $res['error'] = $b; return api_json_result($res); }

# создание временного файл: $n название файла, $d данные файла, возращает путь к файлу
function createTmpFile($n, $d) { $n = '/tmp/'.md5(time().rand()).$n; file_put_contents($n, base64_decode($d)); return $n; }

# праверка входящих файлов: $n массив из типо файлов
function checkSeveralFromFile($n) {
    global $filename, $typeconvert;
    if (count($filename) < 1) return exitError("небыло передоны файлы", 98);
    for ($i = 0; $i < count($filename); $i++) {
        $fileformat = substr($filename[$i],strrpos($filename[$i],'.')+1);
        if (!in_array($fileformat, $n)) return exitError("неправельный тип входящего файла для правила ".$typeconvert, 100+$i);
    }
    return 0;
}

# праверка входящего файла: $n массив из типо файлов
function checkOneFromFile($n) {
    global $filename, $typeconvert;
    if (count($filename) < 1) return exitError("небыло передоны файлы", 98);
    if (count($filename) > 1) return exitError("передано несколько файлов, а требуется один", 99);
    $fileformat = substr($filename[0],strrpos($filename[0],'.')+1);
    if (!in_array($fileformat, $n)) return exitError("неправельный тип входящего файла для правила ".$typeconvert, 100);
    return 0;
}

# праверка выходящего файла: $n массив из типо файлов
function checkOneInFile($n) {
    global $fileout, $typeconvert, $fileformat;
    if ($fileout == null) return exitError("небыло передоны файлы", 96);
    //if (count($fileout) > 1) return exitError("передано несколько файлов, а требуется один", 97);
    $fileformat = substr($fileout,strrpos($fileout,'.')+1);
    if (!in_array($fileformat, $n)) return exitError("неправельный тип выходящего файла для правила ".$typeconvert, 100);
    return 0;
}

# создание временных файлов
function createSeveralTmpFile() {
    global $filenamelist, $filenametmp, $filename, $file; $filenamelist = '';
    for ($i = 0; $i < count($filename); $i++) {
        $filenametmp[$i] = createTmpFile($filename[$i], $file[$filename[$i]]);
        chmod($filenametmp[$i], 0777);
        $filenamelist .= '"'.$filenametmp[$i].'" '; # добавление в список файлов для конвертации
        if (!file_exists($filenametmp[$i])) { # проверка временого файла
	        for ($j = 0; $j < $i; $j++) unlink($filenametmp[$j]);
	        return exitError("создание временого файла прошла не успешно", 900+$i);
        }
    }
    return 0;
}

# создание временого файла
function createOneTmpFile() {
    global $filenamelist, $filenametmp, $filename, $file;
    $filenametmp[0] = createTmpFile($filename[0], $file[$filename[0]]);
    chmod($filenametmp[0], 0777);
    $filenamelist = '"'.$filenametmp[0].'" '; # добавление в список файлов для конвертации
    # проверка временого файла
    if (!file_exists($filenametmp[0])) return exitError("создание временого файла прошла не успешно", 900);
    return 0;
}

# создание пути одного сконвертированого файла
function createOneConvFile() { global $filenewnametmp, $fileout; $filenewnametmp = "/tmp/".md5(time().rand()).$fileout; }

# обработка входящих параметров. Для правил: ImageToImage, ImageToPDF, ImageToGIF
function paraForConvImage() {
    global $parametrs, $imagetopara, $imageparaname; $parametrs = '';
    for ($i = 0; $i < count($imageparaname); $i++) {
        $reqpara = api_check_request($imageparaname[$i]);
        if ($reqpara !== false) $parametrs .= $imagetopara[$imageparaname[$i]].' '.$reqpara.' ';
    }
}

# обработка входящих параметров. Для правил: WriterToPdf
function paraForConvLibre() {
    global $parametrs, $libretopara, $libreparaname; $parametrs = '';
    for ($i = 0; $i < count($libreparaname); $i++) {
        $reqpara = api_check_request($libreparaname[$i]);
        if ($reqpara !== false) $parametrs .= $libretopara[$libreparaname[$i]].' '.$reqpara.' ';
    }
}

# конвертация для правил: ImageToImage, ImageToPDF, ImageToGif
function convImage() {
    global $execlog, $filenamelist, $parametrs, $filenewnametmp;
    $execlog = "convert " . exec('convert '.$filenamelist.$parametrs.'"'.$filenewnametmp.'"');
}

# конвертация для правил: WriterToPdf
function convLibre($n) {
    global $execlog, $filenamelist, $parametrs, $filenewnametmp, $dirnewnametmp, $fileformat, $filenametmp;
    $execlog = "libre ". exec('libreoffice --headless '.$parametrs.'--convert-to "'.$fileformat.':'.$n.'" '.$filenamelist.'--outdir '.$dirnewnametmp);
    $f = $dirnewnametmp.'/'.substr($filenametmp[0],strrpos($filenametmp[0],'/')+1);
    $f1 = substr($f,0,strrpos($f,'.')).'.'.$fileformat;
    $execlog .= "\nmv " . exec('mv "'.$f1.'" "'.$filenewnametmp.'"');
}

# удаление временого файла
function deleteOneTmpFile() { global $filenametmp; unlink($filenametmp[0]); }

# удаление временых файлов
function deleteSeveralTmpFile() { global $filenametmp; for ($i = 0; $i < count($filenametmp); $i++) unlink($filenametmp[$i]); }

# проверка и отправка одного сконвертированого файла
function pushOneNewFile() {
    global $filenewnametmp, $fileout;
    # проверка сканвертированого
    if (!file_exists($filenewnametmp)) return exitError("конвертация прошла не успешно", 800);
    $newfile = base64_encode(file_get_contents($filenewnametmp)); # полученое содержимого сконвертированого файла
    unlink($filenewnametmp); # удаление сконвертированого временого файла
    # все норм, утверждаем это
    $res['errors'] = ""; $res['error'] = 0; $res['file'] = $newfile; $res['filename'] = $fileout;
    return api_json_result($res);
}

global $apikey, $typeconvert, $file, $filename, $fileout;
global $filenametmp, $execlog, $parametrs, $filenamelist, $filenewnametmp, $dirnewnametmp, $fileformat;

$dirnewnametmp = '/tmp/out';
# проверка наличия обязательных полей для этой команды
$req = api_check_request(["apikey","typeconvert","file","filename","fileout"]); if (!$req) return true;
list($apikey,$typeconvert,$file,$filename,$fileout) = $req;

# проверка корректности ключа
$userid = apikey_check($apikey); if (!$userid) return api_error(EFIELDBAD,"apikey");

# типы файлов. Стандартный: тип = array(форматы);
$image = array('png','jpeg','jpg','gif','bmp','tiff','tif','webp','avif','heif', 'heic','raw','jxl','svg','eps','pdf','ai','cdr');
$writer = array('odt','doc','docx','rtf','txt','html');
$calc = array('ods','xls','xlsx','csv');
$impress = array('odp','ppt','pptx');
$pdf = array('pdf');

# форматы, в которые можно сконвертироавть: тип конвертации => array(форматы)
$informats = [
    "ImageToImage"=>$image, "ImageToGif"=>array('gif'),
    "WriterToOdt"=>array('odt'), "WriterToDoc"=>array('doc') "WriterToDocx"=>array('docx'), "WriterToRtf"=>array('rtf'), "WriterToHtml"=>array('html'),
    "CalcToOds"=>array('ods'), "CalcToXls"=>array('xls'), "CalcToXlsx"=>array('xlsx'), "CalcToCsv"=>array('csv'),
    "ImpressToOdp"=>array('odp'), "ImpressToPpt"=>array('ppt'), "ImpressToPptx"=>array('pptx'),
    "ImageToPdf"=>$pdf, "WriterToPdf"=>$pdf, "CalcToPdf"=>$pdf, "ImpressToPdf"=>$pdf
];

# фильтры для libreoffice: тип конвертации => фильтр
$librefilter = ["WriterToPdf"=>"writer_pdf_Export", "WriterToOdt"=>"writer8", "WriterToDoc"=>"MS Word 97",
    "WriterToDocx"=>"MS Word 2007 XML", "WriterToRtf"=>"Rich Text Format", "WriterToHtml"=>"HTML (StarWriter)",
    "CalcToOds"=>"calc8", "CalcToXls"=>"MS Excel 97", "CalcToXlsx"=>"Calc MS Excel 2007 XML",
    "CalcToCsv"=>"Text - txt - csv (StarCalc)", "CalcToPdf"=>"calc_pdf_Export",
    "ImpressToOdp"=>"impress8", "ImpressToPpt"=>"MS PowerPoint 97",
    "ImpressToPptx"=>"impress_ms_pptx_Export", "ImpressToPdf"=>"impress_pdf_Export"
];

# параметыры для конвертации
# для проверки входящих параметров. Стандартный: $<тип>paraname = array(название параметров);
# преоброзование входящих параметров для утилыт. Стандартный: $<тип>topara = ["название параметра" => "параметры для утилиты"]
global $imagetopara, $imageparaname, $docparaname, $doctopara;
$imageparaname = array('resize','quality','rotate','blur','bordercolor','border','delay','loop');
$libreparaname = array('');

$imagetopara = ['resize'=>'-resize','quality'=>'-quality','rotate'=>'-rotate','blur'=>'-blur','bordercolor'=>'-bordercolor',
    'border'=>'-border','delay'=>'-delay','loop'=>'-loop'];
$librertopara = [''=>''];

//return exitError("test",404);
switch ($typeconvert) {
    case 'ImageToImage': case 'ImageToPdf': case 'ImageToGif':
        $error = checkSeveralFromFile($image); break;
    case 'WriterToPdf': case 'WriterToOdt': case 'WriterToDoc': case 'WriterToDocx': case 'WriterToRtf': case 'WriterToHtml': 
        $error = checkOneFromFile($writer); break;
    case 'CalcToOds': case 'CalcToXls': case 'CalcToXlsx': case 'CalcToCsv': case 'CalcToPdf':
        $error = checkOneFromFile($calc); break;
    case 'ImpressToOdp': case 'ImpressToPpt': case 'ImpressToPptx': case 'ImpressToPdf':
        $error = checkOneFromFile($impress);
    default: return exitError($typeconvert." нету такого правила конвертирования", 95);
} if ($error !== 0) return $error;

$error = checkOneInFile($informats[$typeconvert]);
if ($error !== 0) return $error;

switch ($typeconvert) {
    case 'ImageToPdf': case 'ImageToGif':
        $error = createSeveralTmpFile(); break;
    case 'ImageToImage': case 'WriterToPdf': case 'WriterToOdt': case 'WriterToDoc': case 'WriterToDocx': case 'WriterToRtf': case 'WriterToHtml':
    case 'CalcToOds': case 'CalcToXls': case 'CalcToXlsx': case 'CalcToCsv': case 'CalcToPdf':
    case 'ImpressToOdp': case 'ImpressToPpt': case 'ImpressToPptx': case 'ImpressToPdf':
        $error = createOneTmpFile(); break;
} if ($error !== 0) return $error; 

createOneConvFile();

switch ($typeconvert) {
    case 'ImageToImage': case 'ImageToPdf': case 'ImageToGif':
        paraForConvImage(); break;
    case 'WriterToPdf': case 'WriterToOdt': case 'WriterToDoc': case 'WriterToDocx': case 'WriterToRtf': case 'WriterToHtml':
    case 'CalcToOds': case 'CalcToXls': case 'CalcToXlsx': case 'CalcToCsv': case 'CalcToPdf':
    case 'ImpressToOdp': case 'ImpressToPpt': case 'ImpressToPptx': case 'ImpressToPdf':
        paraForConvLibre(); break;
}

switch ($typeconvert) {
    case 'ImageToImage': case 'ImageToPdf': case 'ImageToGif':
        convImage(); break;
    case 'WriterToPdf': case 'WriterToOdt': case 'WriterToDoc': case 'WriterToDocx': case 'WriterToRtf': case 'WriterToHtml':
    case 'CalcToOds': case 'CalcToXls': case 'CalcToXlsx': case 'CalcToCsv': case 'CalcToPdf':
    case 'ImpressToOdp': case 'ImpressToPpt': case 'ImpressToPptx': case 'ImpressToPdf':
        convLibre($librefilter[$typeconvert]); break;
}

switch ($typeconvert) {
    case 'ImageToPdf': case 'ImageToGif':
        deleteSeveralTmpFile(); break;
    case 'ImageToImage': case 'WriterToPdf': case 'WriterToOdt': case 'WriterToDoc': case 'WriterToDocx': case 'WriterToRtf': case 'WriterToHtml':
    case 'CalcToOds': case 'CalcToXls': case 'CalcToXlsx': case 'CalcToCsv': case 'CalcToPdf':
    case 'ImpressToOdp': case 'ImpressToPpt': case 'ImpressToPptx': case 'ImpressToPdf':
        deleteOnetmpFile(); break;
}

return pushOneNewFile();