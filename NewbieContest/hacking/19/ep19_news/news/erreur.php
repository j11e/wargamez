<?php

$msg = array();
include("common.php");

@session_start();
if(!session_is_registered("end")) { die("Accès interdit"); }
$id=strip_tags($_GET['id']);
$fichier=fopen("erreur/".date("H-i").rand(0,5).date("dm-y").".log", "w");
fwrite($fichier,$msg['error']);
fclose($fichier);
session_destroy();
header("Location: news.php?err=1");

?>
