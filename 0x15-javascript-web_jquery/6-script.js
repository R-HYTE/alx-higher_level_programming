/* global $ */
// Ensure the DOM is fully loaded before executing the script
$(document).ready(function () {
  // Select the DIV#update_header element using jQuery
  const $updateHeader = $('#update_header');
  const $header = $('header');

  // Add click event to DIV#update_header
  $updateHeader.on('click', function () {
    // Update the text of the <header> element to 'New Header!!!'
    $header.text('New Header!!!');
  });
});
