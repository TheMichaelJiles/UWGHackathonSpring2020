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
		let title = document.getElementById("title").value.replace(/ /g, "_");
		let author = document.getElementById("author").value.replace(/ /g, "_");
		let subject = document.getElementById("subject").value.replace(/ /g, "_");
		let summary = document.getElementById("summary").value.replace(/ /g, "_");
		let theLink = document.getElementById("link").value.replace(/ /g, "_");
		let courseid = document.getElementById("courseid").value.replace(/ /g, "_");
		let tag = document.getElementById("tag").value.replace(/ /g, "_");
		
		let url = "http://127.0.0.1:8000/add?title=" + title + "&author=" + author + "&subject=" + subject + "&summary=" + summary + "&link=" + theLink + "&courseid=" + courseid + "&tag=" + tag;
		httpGetAsync(url, function(response) {
			setTimeout(() => window.close(), 250);
		});
	});
}

function init() {
	setButtonListener();
}

init();