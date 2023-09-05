#!/usr/bin/node

const request = require('request');

// Check if a number argument was provided
if (process.argv.length !== 3 || isNaN(Number(process.argv[2]))) {
  console.error('Usage: ./js_file.js <film_number>');
  process.exit(1); // Exit with a non-zero status code to indicate an error
}

const filmNumber = process.argv[2]; // Get the film number from command-line argument

// Construct the API endpoint with the film number
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmNumber}`;

// Make a request to the constructed endpoint
request(apiUrl, function (error, response, body) {
  // Check for errors and HTTP status code
  if (!error && response.statusCode === 200) {
    // Parse the JSON response
    const filmsJson = JSON.parse(body);

    // Get the list of characters URLs
    const charactersUrls = filmsJson.characters;

    // Iterate through the character URLs
    charactersUrls.forEach(function (characterUrl) {
      // Make a request to each character's URL
      request(characterUrl, function (characterError, characterResponse, characterBody) {
        // Check for errors and HTTP status code
        if (!characterError && characterResponse.statusCode === 200) {
          // Parse the JSON response for each character
          const characterData = JSON.parse(characterBody);

          // Get the character's name and print it
          const characterName = characterData.name;
          console.log(characterName);
        } else {
          console.log(`Failed to retrieve character data from URL: ${characterUrl}`);
        }
      });
    });
  } else {
    console.log('Failed to retrieve film data.');
  }
});
