'use strict'
  let name
  name = prompt('Enter your name and the sorting hat will assign your class: ');
  const MAX = 4;

  let randomNum = 1 + Math.floor(Math.random()*MAX);

  if (randomNum == 1) {
    document.write('' +name+ ', Gryffindor');
  }
  else if (randomNum == 2) {
    document.write('' +name+ ', Ravenclaw');
  }
  else if (randomNum == 3) {
    document.write('' +name+ ', Slytherin');
  }
  else if (randomNum == 4) {
    document.write('' +name+ ', Hufflepuff');
  }