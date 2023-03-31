/* Write a program that prompts the user for five numbers and prints them in the reverse order they were entered.
Save the numbers to an array, then use for-loop to iterate in reverse order.
Do not use array.reverse() function.
Print the result to the console.(2p)
 */
'use strict'

const nums = 5;
const numsAr = [];

alert("Enter 5 numbers: ");

for (let i = 0; i < nums; i++) {
  const tulos = +prompt("Enter number: ");
  numsAr[i] = tulos;
}
for (let i = nums -1; i >= 0; i--) {
  document.write(' ' + ' ' + numsAr[i]);
}