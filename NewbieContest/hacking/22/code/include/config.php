<?php
// a changer
$dbhost = "localhost";
$dbname="d4t4b453";
$dbuser = "r00t";
$dbpass = "t00r";
// fin des changements a faire
$allowed_pages_log=array("memberlist","logout","profile");
$allowed_pages_nolog=array("register","login");
if (file_exists("include/fonctions.php")) include("include/fonctions.php");
else die("Il manque un fichier");
$db = mysql_connect($dbhost, $dbuser, $dbpass) or die(mysql_error());
mysql_select_db($dbname, $db) or die(mysql_error());
appel("include/header.php");
appel("langue/" . LANGUAGE . ".php");
?>