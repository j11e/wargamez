<?php

include("globale.php");
include("config.php");
include("function.php");


$db=mysql_connect($host,$login_bdd,$pass_bdd) or die("Connexion � la base de donn�es impossible");
mysql_select_db($bd,$db) or die("S�lection de la base de donn�es impossible");


?>