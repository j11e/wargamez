<?php

$msg=array();
$msg['erreur_sql']="Problème avec la base de donnée, veuillez nous en excuser";
$msg['title']="- [Les News] -";
$msg['title_commentaire']="Commentaires";
$msg['lire_suite']="Lire la suite(...)";
$msg['react']="Réagir";
$msg['post']="Posté par";
$msg['no_comment']="Aucun commentaire n'a été posté pour cette nouvelle !";
$mgs['add_comment']="Ajouter un commentaire";
$msg['name']="Nom";
$msg['message']="Message";
$msg['comment_save']="Votre commentaire a bien été enregistré ! <br><a href='commentaire.php?id=".strip_tags($_GET['id'])."'>Retour</a>";
$msg['empty_field']="Tous les champs sont obligatoires !<br><a href='javascript:history.go(-1);'>Retour</a>";
$msg['error']="Une erreur s'est produite au niveau de la page ".$_SERVER['HTTP_REFERER']." à cause d'une mauvaise utilisation de la requête SQL \$sql=".strip_tags($_GET['id']);
$msg['invalid_id']="L'identifiant est invalide !";
$msg['copyright']="Powered by NC News &copy;";

?>