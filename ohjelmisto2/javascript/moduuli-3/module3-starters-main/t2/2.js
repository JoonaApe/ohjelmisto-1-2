const div = document.getElementById('target');

//creating items for the list
const first = document.createElement('li');
const second = document.createElement('li');
const third = document.createElement('li');

//adding values for the items.
first.textContent = "First Item";
second.textContent = "Second Item";
third.textContent = "Third Item";



// appending the items to the u-list
div.appendChild(first);
div.appendChild(second);
div.appendChild(third);


