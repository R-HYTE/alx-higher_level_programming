/* global $ */
// Ensure the DOM is fully loaded before executing the script
$(document).ready(function () {
  // Select the DIV#add_item and UL.my_list elements using jQuery
  const $addItem = $('#add_item');
  const $myList = $('ul.my_list');

  // Add click event to DIV#add_item
  $addItem.on('click', function () {
    // Create a new <li> element with the text 'Item'
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to UL.my_list
    $myList.append(newItem);
  });
});
