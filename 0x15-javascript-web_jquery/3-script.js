/* global $ */

// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Use jQuery to select the DIV#red_header element and attach a click event
  $('#red_header').click(function () {
    // Add the class "red" to the <header> element
    $('header').addClass('red');
  });
});
