/*
Write a program that prompts the user for numbers.
When the user enters one of the numbers he previously entered,
the program will announce that the number has already been given and stops its operation and then prints all the given numbers to the console
in ascending order.
 */
'use strict'
let numsAr  = [];
let test = true;

document.write('<ul>');
while (test) {
  let num = +prompt("Enter number, if you enter same number twice the program will stop");
  if (numsAr.includes(num)) {
    break;
  }
  numsAr.push(num);
  numsAr.sort((a,b) => a-b);

  }

alert("You've entered the same number second time and the program ended.");
for (let i = 0; i < numsAr.length; i++){
  document.write('<li>' +numsAr[i]+ '</li>');
}
document.write('</ul>');