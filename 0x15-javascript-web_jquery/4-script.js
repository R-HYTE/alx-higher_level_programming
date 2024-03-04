/* global $ */
// Ensure the DOM is fully loaded before executing the script
$(document).ready(function () {
  // Cache jQuery objects for better performance
  const $header = $('header');
  const $toggleHeader = $('#toggle_header');

  // Toggle class on <header> based on the click event of DIV#toggle_header
  $toggleHeader.on('click', function () {
    // Toggle between 'green' and 'red' classes
    $header.toggleClass('green red');
  });
});
