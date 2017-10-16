/* global $ */

console.log('Hello World.');

var DATA_URL = './static/data/numbers.data';
var SERVER_URL = './';

/*
 * Example of making an AJAX request to get file in public/data golder
 */
$.get(DATA_URL, function(data) {
	console.log(data);
	var numbers = getNumbersFromData(data);
	for (var i = 0; i < numbers.length; i++) {
		console.log(numbers[i]);
	}
});

/*
 * Example of making an AJAX request to access server API created by backend engineer
 */
function getName(inputName) {
	$.get(SERVER_URL + '/reflect/' + inputName, function(data) {
		console.log(data);
		var result = document.createElement('span');
		result.innerText = data.name;
		result.id = 'result';
		var output = document.querySelector('#output');
		output.appendChild(result);
	});
}

/*
 * Parameters: text data with valid numbers separated by spaces on each line
 * Returns: a list of numbers
 */
function getNumbersFromData(data) {
	var numbers = [];
	var lines = data.split('\n');
	for (var l = 0; l < lines.length; l++) {
		var nums = lines[l].split(' ');
		for (var n = 0; n < nums.length; n++) {
			var value = parseFloat(nums[n]);
			numbers.push(value);
		}
	}
	return numbers;
}