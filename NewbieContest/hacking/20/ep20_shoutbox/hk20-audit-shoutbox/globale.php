<?php

 foreach ($_GET as $key => $value) 
 {
   $$key = $value;
 }
 
  foreach ($_POST as $key => $value) 
 {
   $$key = $value;
 }
?>