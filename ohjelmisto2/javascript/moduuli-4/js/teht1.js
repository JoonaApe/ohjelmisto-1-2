'use strict'


const apiUrl = "https://api.tvmaze.com/search/shows?q=";
const searchButton = document.querySelector('input[type="button"]');
const results = document.getElementById("results");
let imageUrl;
let apiCall;

searchButton.addEventListener('click', apiSearch);
searchButton.addEventListener('click', newSearch);

function apiSearch() {
  let searchword = document.getElementById('query').value;
    apiCall = apiUrl + searchword;
    console.log("Lähetettävä kysely: " + apiCall);
    request(apiCall);
}

//funktio joka tekee apihaun.
function request(apiCall) {
  fetch(apiCall).then(function(response) {
    return response.json();
  }).then(function(json) {
    showResponseConsole(json);
    showResponse(json);
  }).catch(function(error) {
    console.log(error);
  });
}

//funktio joka tulostaa haun tulokset consoleen.
function showResponseConsole(jsonData) {
  console.log("test");
  console.log(jsonData);
  console.log("testinen");
}
//funktio joka tulostaa haun tuloksen html tiedostoon.
function showResponse(jsonData) {

//for looppi jolla tarkastetaan onko ohjelmalle kuvaa sekä antaa html koodille oikeat tiedot.
  for (let i = 0; 0 < jsonData.length; i++) {
    try {
      imageUrl = jsonData[i].show.image.medium;
    } catch (error) {
      imageUrl = 'https://via.placeholder.com/210x295?text=Not%20Found';
    }

// html koodi joka lisätään html tiedostoon.
    let htmlCode = `
        <article>
                <h2>${jsonData[i].show.name}</h2>
            
            <figure>
                <img src=${imageUrl} alt="Medium image">
            </figure>
            <div>${jsonData[i].show.summary}</div>
            <a href=${jsonData[i].show.officialSite} target="_blank">Official link to tv shows website</a> 
        </article> `
    results.innerHTML += htmlCode;
  }
}
//funktio joka tyhjentää aikasemman haun tuloksen html tiedostosta.
function newSearch() {
  results.innerHTML = '';
}