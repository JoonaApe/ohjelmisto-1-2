/* Write a program that asks for the names of six dogs. The program prints dog names to unordered list <ul> in reverse alphabetical order. (2p)*/
'use strict'
let dogsAr = [];
document.write("<ul>");

for (let i = 0; i < 6; i++) {
    let dogs = prompt("Enter the name of the dog: ");
    dogsAr.push(dogs);
}
dogsAr.sort();
dogsAr.reverse();

for (let i = 0; i < dogsAr.length; i++) {
  document.write('<li>' +dogsAr[i]+ '</li>');
}
document.write("</ul>");
