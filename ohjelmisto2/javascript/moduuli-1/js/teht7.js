  /* Write a program that rolls user defined number of dice and displays the sum of the results of the dice rolls.(2p)
  First, program asks the user for the number of dice rolls.
  Then the program throws a die as many times as the user defined.
  Print the sum of the results in the console or in the HTML document.*/



'use strict'

    let diceNum,sum;
    diceNum = +prompt("How many dices would you like to roll?")
    sum = 0;

    for (let i = 0; i < diceNum; i++) {
      let diceRoll = Math.floor(Math.random() * 6) +1;
      sum = sum + diceRoll;
    }
    document.write("You rolled " +diceNum+  " dices, the sum of them is " +sum);