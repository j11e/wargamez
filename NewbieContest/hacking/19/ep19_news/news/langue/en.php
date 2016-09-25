<?php

$msg=array();
$msg['erreur_sql']="We are sorry, but a problem occured in our database.";
$msg['title']="- [News] -";
$msg['title_commentaire']="Comments";
$msg['lire_suite']="Read the entire news(...)";
$msg['react']="React";
$msg['post']="Posted by";
$msg['no_comment']="No comment has been posted for this news!";
$mgs['add_comment']="Add a comment";
$msg['name']="Name";
$msg['message']="Message";
$msg['comment_save']="Your comment has been saved! <br><a href='commentaire.php?id=".strip_tags($_GET['id'])."'>Go back</a>";
$msg['empty_field']="All the fields must be completed!<br><a href='javascript:history.go(-1);'>Go back</a>";
$msg['error']="An error occured on the page ".$_SERVER['HTTP_REFERER']." due to a bad SQL request \$sql=".strip_tags($_GET['id']);
$msg['invalid_id']="Invalid login!";
$msg['copyright']="Powered by NC News &copy;";

?>