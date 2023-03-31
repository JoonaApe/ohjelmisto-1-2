/*Write a program that asks the user for numbers until he gives zero.
The given numbers are printed in the console from the largest to the smallest. (2p)
 */
'use strict'

let numsAr = [];
let test = true;

document.write('<ul>');
while (test==true){
  let luku = +prompt("Enter numbers, if you want to stop enter 0: ");
  numsAr.push(luku);
  if (luku === 0)
    test = false;
  }
numsAr.pop();
numsAr.sort((a,b) => a-b);
numsAr.reverse();
for (let i = 0; i < numsAr.length; i++){
  document.write('<li>' +numsAr[i]+ '</li>');
}
document.write('</ul>');