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

function showResponse(response) {
    let resultsList = document.getElementById("searchResults");
    let responseList = JSON.parse(response);
    for (const result of responseList) {
        let resultItem = `<span class="flexitem">
                            <h4 class="listItemHeader">${result['title'].split('_').join(' ')}</h4>
                            <h5>Author: ${result['author'].split('_').join(' ')}</h5>
                            <h5>Subject: ${result['subject'].split('_').join(' ')}</h5>
                            <h5>Course ID: ${result['courseid'].split('_').join(' ')}</h5>
                            <h5>Tag: ${result['tag'].split('_').join(' ')}</h5>
                            <h5>Summary: </h5>
                            <p>${result['summary'].split('_').join(' ')}</p>
                            <a href="${result['link']}" target="_blank">Read Textbook</a>
                         </span>`
        resultsList.innerHTML += resultItem;
    }
}

function init() {
    let windowUrl = document.location.href;
    let params = windowUrl.split('?')[1].split('&');
    let termQuery = params[0].split('=');
    let typeQuery = params[1].split('=');

    let term = termQuery[1];
    let type = typeQuery[1];

    let termSpan = document.getElementById("type");
    termSpan.innerHTML = type.charAt(0).toUpperCase() + type.slice(1);

    let searchSpan = document.getElementById("searchTerm");
    searchSpan.innerHTML = term;

    let searchUrl = 'http://127.0.0.1:8000/search?term=' + term + '&searchType=' + type;
    httpGetAsync(searchUrl, function(response) {
        showResponse(response);
    });
}

init();