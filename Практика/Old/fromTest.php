<?php
print '<html>';
print '<head><title>fromTest</title></head>';
print '<body>';
print '<p>test</p><p>';
/*print_r($_POST);*/
/*print '</p><p>';*/
if ($_SERVER["REQUEST_METHOD"] == "POST")
{
    print 'yes';
}
else
{
    print 'no';
}
/*print_r($_FILES);*/
print '</p>';
print '</body>';
print '</html>';
?>