/* global $ */

var SERVER_URL = '.';
/*
 * Example of making an AJAX request to access server API created by backend engineer
 */
function getLocationImage(searchText) {
	$.get(SERVER_URL + '/location_image/' + searchText, function(data) {
		console.log(data);
		let image = document.getElementById('image');
		image.src = data;
	});
}