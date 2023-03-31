  'use strict'
  let num
  if (confirm("Should i calculate the square root? ") == true)
  {
    num = prompt('Enter number: ')
    if(num >0) {
      document.write(num+' squareroot is '+Math.sqrt(num).toFixed(2));
    }
    else {
      document.write('The square root of a negative number is not defined')
    }
  }
  else {
    document.write('The square root is not calculated')
  }

