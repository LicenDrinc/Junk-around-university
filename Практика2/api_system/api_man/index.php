<?php
//$api = "https://localhost/api_system/api";

$proto="http";
if (isset($_SERVER["HTTPS"]) and $_SERVER["HTTPS"]=="on") $proto="https";
$server=$_SERVER['SERVER_NAME'];
$dir=dirname(dirname($_SERVER['SCRIPT_NAME']));
$api="$proto://$server$dir/api";

$url = (!isset($_GET['url'])) ? "$api/" : $_GET['url'];

function get_data($url)
{

    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER,false);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST,false);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $result = curl_exec($curl);
    curl_close($curl);
    return json_decode($result, true);
}
$data = get_data($url);
$main = get_data("$api/");
?>

<!DOCTYPE html>
<html lang="ru">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Man Edubase</title>
  <link href="./bootstrap.min.css" rel="stylesheet">
  <link href="./style.css" rel="stylesheet">
  <link rel="icon" type="image/x-icon" href="./favicon.ico">
</head>

<body >
<nav class="navbar navbar-expand-lg" style="background-color: #073772;">
      <div class="container-fluid">
        <a class="navbar-brand" href='<?php echo (empty($_SERVER['HTTPS']) ? 'http' : 'https') . "://$_SERVER[HTTP_HOST]".strtok($_SERVER["REQUEST_URI"],'?')?>'><?=$main['info']?> <?=$main['version']?> <?php echo ($main['ready']) ? "🟢" : "🔴"?></a>
        <ul class="navbar-nav">
          <li class="nav-item px-2">
            <span><?="Раздел (part): "."<b>".$data['part']."</b>"?></span>
          </li>
          <li class="nav-item px-2">
            <span><?="Команда (command): "."<b>".$data['command']."</b>"?></span>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container-fluid mt-3">
      <div class="row align-items-start">
        <div class="col-4">
          <h4>Доступные разделы: </h4>
          <ul>
          <?php foreach($main['valid_parts'] as $part):
            $href = (empty($_SERVER['HTTPS']) ? 'http' : 'https') . "://$_SERVER[HTTP_HOST]".strtok($_SERVER["REQUEST_URI"],'?')."?url=$api".$part['index']['part']; ?>
            <li><?php if ($part['index']['part'] == $data['part']):?><b>
            <?php endif;?><?=$part['index']['info']?> <?php if ($part['index']['part'] == $data['part']):?></b><?php endif;?>: <a href="<?=$href?>"><?=$part['index']['part']?></a></li>
          <?php endforeach; ?>
          </ul>
        </div>
      <div class="col">
        <div class="row">
          <?php if (isset($data['valid_commands'])): ?>
            <div class="col">
              <h4>Доступные команды: </h4>
              <ul>
                <?php foreach ($data['valid_commands'] as $command): ?>
                  <li><b><?= $command['info'] ?></b> : <a href="<?= $api.$data['part'] . $command['command'] ?>"><?= $data['part'] . $command['command'] ?></a></li>
                  <?php if (isset($command['help'])):
                    foreach ($command['help'] as $help): ?>
                      <pre><?= $help ?></pre>
                <?php endforeach;
                  endif;
                endforeach; ?>
              </ul>
            </div>
        </div>
      <?php endif; ?>
      <?php if (isset($data['help'])): ?>
        <div class="col">
          <?php if (isset($data['help']['request'])): ?>
            <h4>Запрос</h4>
            <pre>
            <?= $data['help']['request'] ?>
          </pre>
          <?php endif; ?>
          <?php if (isset($data['help']['response'])): ?>
            <h4>Ответ</h4>
            <pre>
            <?= $data['help']['response'] ?>
          </pre>
          <?php endif; ?>
        </div>
      <?php endif;
      if (isset($data['error']) && $data['error'] != 0): ?>
        <div class="col">
          <h4 style="text-align: center;">Ошибка</h4>
          <pre>
            <?= $data['errors'] ?>
          </pre>
        </div>
      <?php endif; ?>
      </div>
    </div>
  </div>
  <script src="./bootstrap.bundle.min.js"></script>
</body>

</html>