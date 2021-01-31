<?php

function logIP()
{
     $ipLog="../log.txt";

     $register_globals = (bool) ini_get('register_gobals');
     if ($register_globals) $ip = Egetenv(RMOTE_ADDR);
     else $ip = $_SERVER['REMOTE_ADDR'];

     $date=date ("l dS F Y h:i:s A");
     $log=fopen("$ipLog", "a+");

     fputs($log, "$ip - $date \n");
     fclose($log);
}