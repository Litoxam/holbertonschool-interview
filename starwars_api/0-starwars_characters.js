#!/usr/bin/node

const request = require('request');

// get argv2
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const film = JSON.parse(body);
  // each character is a URL
  const characters = film.characters;

  function displayCharacters(index) {
    if (index === characters.length) {
      return;
    }

    request(characters[index], function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
// incrementation
      displayCharacters(index + 1);
    });
  }
// run the function
  displayCharacters(0);
});
