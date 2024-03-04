/* global $ */

// Ensure the DOM is fully loaded before executing the script
$(document).ready(function () {
  // Define the URL for fetching translation
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Select the DIV#hello element using jQuery
  const $helloDiv = $('#hello');

  // Fetch translation from the API
  $.get(apiUrl, function (data) {
    // Display the translation in the DIV#hello element
    $helloDiv.text(data.hello);
  });
});
