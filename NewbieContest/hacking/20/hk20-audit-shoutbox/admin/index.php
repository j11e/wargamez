<?php
session_start();

include("../common.php");

$login=nettoie($login);

if(!empty($login) && !empty($password))
{
	
	$sql="SELECT * FROM shootbox_admin WHERE login = '".$login."' AND password = '".md5($password)."'";
	$query=mysql_query($sql) or die("Erreur SQL");
	$verif=mysql_num_rows($query);
	
	if($verif==1)
	{
		$sql="SELECT rank FROM shootbox_admin WHERE login = '".$login."'";
		$query=mysql_query($sql) or die("Erreur SQL");
		$data=mysql_fetch_array($query);
		$_SESSION['rank']=$data['rank'];
		echo "<script>document.location='admin.php';</script>";
	}
	else
	{
		echo "<center>Login/Password invalide<br><a href='javascript:history.go(-1);'>Retour</a></center>";
	}
}
else
{
	echo'<div align="center"><p><strong>Espace administration </strong></p><form action="" method="post"><table width="235" border="0"><tr>
         <td width="75">Login : </td> <td width="144"><input name="login" type="text" id="login"></td></tr> <tr><td>Password : </td>  <td><input name="password" type="password" id="password"></td>
         </tr> </table><p><input type="submit" name="Submit" value="Envoyer"></form> </p></div>';
}
mysql_close();
?>