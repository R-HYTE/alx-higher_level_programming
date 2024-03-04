/* global $ */

// Ensure the DOM is fully loaded before executing the script
$(document).ready(function () {
  // Define the URL for fetching movie information
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Select the UL#list_movies element using jQuery
  const $listMovies = $('#list_movies');

  // Fetch movie information from the API
  $.get(apiUrl, function (data) {
    // Loop through each movie and append its title to the list
    data.results.forEach(function (movie) {
      // Create a new <li> element with the movie title
      const movieItem = $('<li>').text(movie.title);

      // Append the new <li> element to the UL#list_movies
      $listMovies.append(movieItem);
    });
  });
});
