#!/usr/bin/node

const request = require('request');

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function getCharacters (movieid) {
  const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

  try {
    const filmResponse = await makeRequest(apiURL);
    const filmData = JSON.parse(filmResponse);
    const characters = filmData.characters;

    const characterPromises = characters.map(async (characterUrl) => {
      const characterResponse = await makeRequest(characterUrl);
      const characterData = JSON.parse(characterResponse);
      return characterData.name;
    });

    const characterNames = await Promise.all(characterPromises);

    characterNames.forEach((characterName) => {
      console.log(characterName);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}

const movieid = process.argv[2];

if (!movieid || isNaN(Number(movieid))) {
  console.log('Usage: .js_file.js <film_number>');
  process.exit(1);
}

getCharacters(movieid);
