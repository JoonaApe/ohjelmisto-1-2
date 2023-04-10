'use strict'

function dice() {
return Math.floor(Math.random() * 6) +1;
}


document.write('<ul>');
let diceRoll = 0;
while (diceRoll !== 6){
  diceRoll = dice();
  document.write('<li>' +diceRoll+ '</li>');
}
document.write('</ul>');
document.write('Congratulations! You rolled 6!');
