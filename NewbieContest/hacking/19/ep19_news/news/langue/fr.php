<?php

$msg=array();
$msg['erreur_sql']="Probl�me avec la base de donn�e, veuillez nous en excuser";
$msg['title']="- [Les News] -";
$msg['title_commentaire']="Commentaires";
$msg['lire_suite']="Lire la suite(...)";
$msg['react']="R�agir";
$msg['post']="Post� par";
$msg['no_comment']="Aucun commentaire n'a �t� post� pour cette nouvelle !";
$mgs['add_comment']="Ajouter un commentaire";
$msg['name']="Nom";
$msg['message']="Message";
$msg['comment_save']="Votre commentaire a bien �t� enregistr� ! <br><a href='commentaire.php?id=".strip_tags($_GET['id'])."'>Retour</a>";
$msg['empty_field']="Tous les champs sont obligatoires !<br><a href='javascript:history.go(-1);'>Retour</a>";
$msg['error']="Une erreur s'est produite au niveau de la page ".$_SERVER['HTTP_REFERER']." � cause d'une mauvaise utilisation de la requ�te SQL \$sql=".strip_tags($_GET['id']);
$msg['invalid_id']="L'identifiant est invalide !";
$msg['copyright']="Powered by NC News &copy;";

?>