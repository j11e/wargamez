<?php

include("common.php");

echo "<b><center>".$msg['title_commentaire']."</center></b><br>";

if(is_numeric($_GET['id'])&& empty($_GET['ajout']))
{
	$sql="SELECT * FROM comm_news WHERE id_news = ".$_GET['id']." ORDER BY id DESC" ;
	$query=mysql_query($sql) or die(erreur($sql));
	$num=mysql_num_rows($query);

		if($num==0) 
		{
 			echo"<b><center><img src='images/ecrire.gif'></center></b><br>
 			<center>".$msg['no_comment']."</center><br>";
		}
		else
		{
 			while($data=mysql_fetch_array($query))
 			{
 			echo '<table width="240" border="1" style="border-collapse:collapse;">
  			     <tr bgcolor="#CCCCCC">
     			  <td >'.$msg['post'].' : '.ucfirst($data[auteur]).'</td>
     			  <td >Le : '.$data['date'].'</td>
     			  </tr>
     			 <tr>
    			  <td height="35" colspan="2">'.stripslashes($data[text]).'</td>
    			  </tr>
     			 </table><br><br>';
 			}
		}

	echo "<center><a href='commentaire.php?ajout=ok&id=".intval($_GET['id'])."'>".$mgs['add_comment']."</a></center>";
}
elseif(is_numeric($_GET['id']) && !empty($_GET['ajout']))
{
	echo'<form action="commentaire.php" method="POST"><table width="245" height="127" border="0">
  	   <tr>
  	   <td width="231" height="36" colspan="2"><div align="center">
  	   '.$msg['name'].' :<br>
  	   <input name="nom" type="text" id="nom" size="30">
  	   </div></td>
  	   </tr>
  	   <tr>
  	   <td><div align="center">
  	   '.$msg['message'].' :<br>
  	   <textarea name="message" cols="25" rows="8" id="message"></textarea> 
  	   </div></td>
  	   </tr>
  	   </table>
	   <input type="hidden" name="id" value="'.$_GET['id'].'">
    	<p>
   	   <center><input type="submit" name="Submit" value="Envoyer"></center>
   	   </p></form>';
}

elseif(!empty($_POST['nom']) && !empty($_POST['message']) && !empty($_POST['id']))
{
	$nom=addslashes(stripslashes(trim(strip_tags($_POST['nom']))));
	$message=addslashes(stripslashes(nl2br(strip_tags($_POST['message']))));
	$date=date("d/m/y")." à ".date("h:i");
	$id=intval($_POST['id']);
	$sql="INSERT INTO comm_news VALUES ('','$date','$nom','$message','$id')";
	mysql_query($sql) or die(erreur($sql));
	echo"<center><br>".$msg['comment_save']."</center>";
}
else
{
	echo"<br><center>".$msg['empty_field']."</center>";
}
mysql_close();
?>

