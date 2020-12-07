<?php

function setPuzzleCookie($puzzleID){
       
    setcookie(
      "CurrentPuzzle",
      $puzzleID,
      time() + (10 * 365 * 24 * 60 * 60),
      '/'
    );
}
 
function redirectToPuzzle($link, $newID) {
    setPuzzleCookie($newID);
    header("Location: https://innovumhunt.nl/$link");
    exit();
}

function wrongAnswer(){
    header("Location: https://innovumhunt.nl/ThatAnswerWasWrong");
    exit(); 
}

// Insert the generated file here

