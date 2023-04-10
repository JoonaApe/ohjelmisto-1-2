'use strict'

let numbers = [100,203,13,2,4,5,200,140];
let evenNums = [];

  function even() {
    for (let i = 0; i < numbers.length; i++) {
      if (numbers[i] % 2 === 0) {
        evenNums.push(numbers[i]);
      }
    }
    document.write("Muokattu lista: "+evenNums);
    document.write("<br>Alkuperäinen lista: " +numbers);
  }
  even();
