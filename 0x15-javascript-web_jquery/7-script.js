/* global $ */

// Ensure the DOM is fully loaded before executing the script
$(document).ready(function () {
  // Define the URL for fetching character information
  const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Select the DIV#character element using jQuery
  const $characterDiv = $('#character');

  // Fetch character information from the API
  $.get(apiUrl, function (data) {
    // Extract the character name from the response
    const characterName = data.name;

    // Display the character name in the DIV#character element
    $characterDiv.text(characterName);
  });
});
