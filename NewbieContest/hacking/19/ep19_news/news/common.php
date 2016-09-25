<?php

if(ereg("common.php", $_SERVER['REQUEST_URI'])) 
{
	die("Accès direct interdit");
}

include("config.php");
$db=mysql_connect($host, $login_bdd, $pass_bdd);
mysql_select_db($bd,$db);

$sql="SELECT * FROM news";
$query=mysql_query($sql) or die(erreur($sql));
$nb_total=mysql_num_rows($query);
$end="5";

require("fonction.php");

if(function_exists("select_lang"))
{
	require_once("langue/".select_lang($_SERVER['HTTP_ACCEPT_LANGUAGE']));
}

?>