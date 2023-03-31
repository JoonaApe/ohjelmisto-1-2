/*Write a program that asks the user for the number of participants.
After this, the program asks for the names of all participants.
Finally, the program prints the names of the participants on the web page in an ordered list (<ol>) in alphabetical order. (2p)
 */
'use strict'

alert('Enter the number of participants: ');
let participants = +prompt('How many participants? ');
let participantsAr = [];

document.write('<ol>');
for(let i = 0; i < participants; i++) {
  let participantsNames = prompt("Enter the name of the participant: ");
  participantsAr.push(participantsNames)
}
participantsAr.sort();

for (let i = 0; i <participantsAr.length; i++) {
        document.write('<li>'+participantsAr[i] + "</li>");
}

document.write('</ol>');