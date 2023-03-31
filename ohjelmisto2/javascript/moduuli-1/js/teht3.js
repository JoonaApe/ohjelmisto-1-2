  'use strict'
  let num1
      num1 = +prompt('Anna ensimmäinen luku: ');
  let num2
      num2 = +prompt('Anna toinen luku: ');
  let num3
      num3 = +prompt('Anna kolmas luku: ');

  let summa
  summa = num1 + num2 + num3
  let tulo
  tulo = num1 * num2 * num3
  let keskiarvo
  keskiarvo = (num1 + num2 + num3) / 3


  console.log('lukujen summa on '+summa);
  console.log('lukujen tulo on '+tulo);
  console.log('lukujen keskiarvo '+keskiarvo);