<?php

if(ereg("fonction.php", $_SERVER['REQUEST_URI'])) 
{
	die("Accès direct interdit");
}

function erreur($var)
{
@session_start();
session_register("end");
header("Location: erreur.php?id=$var");
}


function select_lang($nav)
{
	if(ereg("fr", $nav))
	{
	$lg="fr.php";
	}
	elseif(ereg("en", $nav))
	{
	$lg="en.php";
	}
	elseif(is_readable("langue/".$nav))
	{
	$lg=$nav;
	}
	else
	{
	$lg="fr.php";
	}
  return $lg;
}

?>