<?php

require("common.php");

if(intval($_REQUEST['start']))
{
	$start=$_GET['start'];
}
else
{
	$start="0";
}

//echo "<center><h2>".$msg['title']."</h2></center><br>";

if($err==1)
{
	echo "<center><font color='red'>".$msg['erreur_sql']."</font></center>";
	exit();
}

$sql="SELECT * FROM news ORDER BY id DESC LIMIT $start,$end";
$query=mysql_query($sql) or die(erreur($sql));

echo '<SCRIPT language="javascript">
      function popup(page) 
	  {
      window.open(page,"'.$msg['title_commentaire'].'","toolbar=0,location=0,directories=0,status=0,scrollbars=1,resizable=0,copyhistory=0,menuBar=0,width=270,height=350");
      }
      </SCRIPT>';
	  
while($data=mysql_fetch_array($query))
{
	echo' <center><table width="456" border="1" style="border-collapse:collapse;">
  	 	  <tr bgcolor="#CCCCCC">
   		  <td width="215" >News du : '.$data['date'].'</td>
   		  <td width="225">'.$msg['post'].' : '.ucfirst($data['pseudo']).'</td>
  	      </tr>
    	  <tr>
   		  <td colspan="2">'.stripslashes(substr($data['text'],0,160)).' ...</td>
   		  </tr>
     	  <tr bgcolor="#CCCCCC">
    	  <td><a href="lireall.php?id='.$data['id'].'">'.$msg['lire_suite'].'</a></td>
   	 	  <td><a href=\'javascript:popup("commentaire.php?id='.$data['id'].'");\'>'.$msg['react'].'</a> <img src="images/commentaire.gif"></td>
   		  </tr>
   		  </table></center><br><br>';
}

echo '<center><table border = "0" ><tr>'."\n";

$nbpages=ceil($nb_total/$end);
$limite=0;
for($i=1;$i<=$nbpages; $i++)
{
	echo '<a href ="news.php?start='.$limite.'">'.$i.'</a>&nbsp;';
	$limite=$limite+10 ;
}

echo '</tr></table></center>'."\n";
echo '<br><center><i>'.$msg['copyright'].'</i></center>';

mysql_close();
?>
