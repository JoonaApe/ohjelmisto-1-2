  'use strict'
  let year
  year = prompt('Enter year and i will tell you if its leap year: ')

 if (year % 4 == 0 && (year% 400 == 0 || year% 100 != 0)) {
   document.write(year + ' is leap year')
 }
 else {
   document.write(year+ ' is not leap year')
 }
