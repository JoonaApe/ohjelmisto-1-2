'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

console.log(students[0].name,students[0].id);

for (let i = 0; i < 3 ; i++) {
  const target = document.getElementById('target');

  const option = document.createElement('option');
  option.value = students[i].id;
  option.textContent = students[i].name;

  target.appendChild(option);
}


