'use strict'

function search() {
	let term = document.getElementById("searchBox").value;
	let type = document.getElementById("typeSelector").value;
	document.location.href = 'http://127.0.0.1:8000/browse_page.html?term=' + term + '&searchType=' + type;
}

function init() {
	let searchButton = document.getElementById("searchButton");
	searchButton.addEventListener("click", search);

	let inputSearch = document.getElementById("searchBox");
	inputSearch.addEventListener("keyup", function(e) {
		if (e.key === "Enter") {
			search();
		}
	});
}

init();