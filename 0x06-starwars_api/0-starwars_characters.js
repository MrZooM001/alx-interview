#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
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
  const characters = new Array(characterUrls.length);
  let CompletedRequests = 0;

  characterUrls.forEach((url, index) => {
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
      characters[index] = characterData.name;
      CompletedRequests++;
      if (CompletedRequests === characterUrls.length) {
        characters.forEach(character => console.log(character));
      }
    });
  });
});
