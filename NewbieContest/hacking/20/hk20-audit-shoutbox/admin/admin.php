<?php
if (isset($_REQUEST['_SESSION']) || isset($_REQUEST['SESSION']))
    die("<center>o_O pas si vite (merci à N00B pr avoir trouvé ce bug !)</center>");

session_start();

include("../common.php");

$rank=isset($_SESSION['rank']) ? $_SESSION['rank'] : NULL;

if(!session_is_registered("rank"))
{
	die("<center>Vous devez �tre loggu� pour acc�der � cette partie !<br><a href='javascript:history.go(-1);'>Retour</a></center>");
}

if($action=="supprimer" && verif_id($id))
{
	mysql_query("DELETE FROM shootbox WHERE id =".$id) or die("Erreur SQL");
	echo "<center>Message supprim� avec succ�s<br><a href='javascript:history.go(-1);'>Retour</a></center>";
}
elseif($action=="ajouter_admin" && $rank=="admin" && !empty($login) && !empty($password) && !empty($rank2) && ($rank2=="admin" || $rank2=="modo"))
{
	mysql_query("INSERT INTO shootbox_admin VALUES ('','".nettoie($login)."','".md5($password)."','".nettoie($rank2)."')") or die("Erreur SQL");
	echo "<center>Nouvel administrateur/mod�rateur ajout� avec succ�s<br><a href='javascript:history.go(-1);'>Retour</a></center>";
}
elseif($action=="supprimer_admin" && $rank=="admin" && !empty($login))
{
	mysql_query("DELETE FROM shootbox_admin WHERE login = '".nettoie($login)."'") or die("Erreur SQL");
	echo "<center>Administrateur/mod�rateur supprim� avec succ�s<br><a href='javascript:history.go(-1);'>Retour</a></center>";
}
else
{
	$rank();
}
mysql_close();
?>
