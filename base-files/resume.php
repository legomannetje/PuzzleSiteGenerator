<?php

function redirectToPuzzle($link) {
    header("Location: https://innovumhunt.nl/$link");
    exit();
}
 
$cookie = "CurrentPuzzle";

if(isset($_COOKIE[$cookie])){
