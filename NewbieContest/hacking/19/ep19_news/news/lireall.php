<?php

include("common.php");

if(isset($_GET['id']) && is_numeric($_GET['id']))
{
	$sql="SELECT * FROM news WHERE id=".$_GET['id'] ;
	$query=mysql_query($sql) or die(erreur($sql));
	$data=mysql_fetch_array($query);

	echo'<br><center><table width="456" border="1" style="border-collapse:collapse;">
    	 <tr bgcolor="#CCCCCC">
   		 <td width="215" >News du : '.$data['date'].'</td>
  	     <td width="225">Post&eacute;e par : '.$data['pseudo'].'</td>
   		 </tr>
   	     <tr>
   	     <td colspan="2">'.stripslashes($data['text']).'</td>
   	     </tr>
   	     </table><br>
   	     <a href="javascript:history.go(-1);">Retour</a></center>';
}
else
{
	echo $msg['invalid_id'];
}
?>