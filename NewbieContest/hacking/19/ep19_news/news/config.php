<?php

if(ereg("config.php", $_SERVER['REQUEST_URI'])) 
{
	die("Accès direct interdit");
}
/* Variables à configurer pour la connection à la base de données */
$host="localhost";
$login_bdd="l0g1n";
$pass_bdd="p455w0rd";
$bd="d4t4b453";
?>
