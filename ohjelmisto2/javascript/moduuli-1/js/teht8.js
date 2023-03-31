  /*Write a program that prompts the user for the start and end year. The program prints all leap years from the interval given by the user.
   Printing is done in an unordered list to the HTML document.
  */
    'use strict'
  let starYr,endYr;
  starYr = +prompt('Enter the starting year for the list');
  endYr = +prompt('Enter the ending year for the list');
  document.write('<ul>');

  for(let i = starYr; i <= endYr; i++) {
    if (i % 400 == 0 ||(i % 4 == 0 && i % 100 != 0)) {
      document.write("<li>" + i + "</li>");
    }
  }

  document.write("</ul>")