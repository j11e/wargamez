<?php

if(ereg("config.php", $_SERVER['REQUEST_URI'])) 
{
	die("Acc�s direct interdit");
}
/* Variables � configurer pour la connection � la base de donn�es */
$host="localhost";
$login_bdd="l0g1n";
$pass_bdd="p455w0rd";
$bd="d4t4b453";
?>
