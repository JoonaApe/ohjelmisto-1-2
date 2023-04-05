/*Write a function called concat(), which receives an array of strings as a parameter.
 The function returns a string formed by concatenating the elements of the array. (2p)
 */
'use strict'

let ar = [];

for(let i = 0; i < 4; i++){
  let names = prompt('Enter names: ');
  ar.push(names);
}
function concat() {
  for (let i = 0; i < ar.length; i++){
    document.write(ar[i]);
  }
}
concat();



