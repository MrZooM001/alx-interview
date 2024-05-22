#!/usr/bin/env node

const request = require('request');
const argv = process.argv;
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const filmUrl = `${apiUrl}${argv[2]}/`;

request(filmUrl, function (error, response, body) {
  if (error) {
    console.error('Failed to fetch movie data:', error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  if (characters && characters.length > 0) {
    fetchCharacters(characters, 0);
  } else {
    console.log('No characters found for this movie.');
  }
});

function fetchCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (error) {
      console.error('Failed to fetch character data:', error);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    }
    fetchCharacters(characters, index + 1);
  });
}
