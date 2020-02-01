'use strict'

function httpGetAsync(url, callback) {
	let xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() {
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			callback(xmlHttp.responseText);
		}
	}
	xmlHttp.open("GET", url, true);
	xmlHttp.send(null);
}

function showTerm(response) {
    let span = document.getElementById("searchTerm");
    console.log("Term Response: " + response);
}

function showResponse(response) {
    let resultsList = document.getElementById("searchResults");
    console.log("Results Response: " + response);
}

function init() {
    let termUrl = 'http://127.0.0.1:8000/getSearchTerm?';
    httpGetAsync(termUrl, function(response) {
        showTerm(response);
    });

    let searchUrl = 'http://127.0.0.1:8000/getSearchResults?';
    httpGetAsync(searchUrl, function(response) {
        showResponse(response);
    });
}

init();