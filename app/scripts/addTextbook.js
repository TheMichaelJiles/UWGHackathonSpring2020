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

function setButtonListener() {
	let button = document.getElementById("submitButton");
	button.addEventListener("click", function() {
		let title = document.getElementById("title").value;
		let author = document.getElementById("author").value;
		let subject = document.getElementById("subject").value;
		let summary = document.getElementById("summary").value;
		let theLink = document.getElementById("link").value;
		
		let url = "http://127.0.0.1:8000/add?title=" + title + "&author=" + author + "&subject=" + subject + "&summary=" + summary + "&link=" + theLink;
		httpGetAsync(url, function(response) {
			console.log(response);
		});
	});
}

function init() {
	setButtonListener();
}

init();