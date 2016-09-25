<?php

$enc = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw=";
$dec = base64_decode($enc);

$raw=array( "showpassword"=>"no", "bgcolor"=>"#000000");
$raw=json_encode($raw);

echo $raw;
echo "<br><br>";
echo $dec;
echo "<br><br>";

$clear='{"showpassword":"no","bgcolor":"#000000"}';
$clear_arr=str_split($clear);

$cipher=$dec;
$cipher=str_split($cipher);

for($i=0; $i<count($cipher); $i++){
    $ordciph = ord($cipher[$i]);
    $ordclear = ord($clear_arr[$i]);
    $deduced = $ordciph ^ $ordclear;
    $deducedChar = chr($deduced);
    echo "clear code : $ordclear ; cipher code : $ordciph ====> code = $deduced ($deducedChar)";
    echo "<br>";
}
