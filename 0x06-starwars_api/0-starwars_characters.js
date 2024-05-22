#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Enter the movie ID');
  process.exit(1);
}

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to fetch film data');
    return;
  }
  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;
  characterUrls.forEach(url => {
    request(url, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }
      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character data');
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
