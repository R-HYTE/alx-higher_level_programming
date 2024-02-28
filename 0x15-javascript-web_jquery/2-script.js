/* global $ */

// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Use jQuery to select the DIV#red_header element and attach a click event
  $('#red_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
