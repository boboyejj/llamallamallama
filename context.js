//  popup function
function createPopUp() {


	document.title = "HELLO";
/*	// create link element
	var link = document.createElement('link');
	link.rel = 'stylesheet';
	link.href = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css';

	// create script elements
	var jquery = document.createElement('script');
	jquery.src = 'https://code.jquery.com/jquery-3.2.1.slim.min.js';

	var ajax = document.createElement('script');
	ajax.src = 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js';

	var bootstrap = document.createElement('script');
	bootstrap.src = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js';

	// add elements to head
	document.head.appendChild(link);
	document.head.appendChild(jquery);
	document.head.appendChild(ajax);
	document.head.appendChild(bootstrap);

	// create test button
	var button = document.createElement('button');
	button.innerHTML = 'hi';

	// add button to body
	document.body.appendChild(button);*/


	// create popup
/*	var popup = document.createElement('div');
	popup.innerHTML = '<div class="modal" tabindex="-1" role="dialog"><div class="modal-dialog" role="document"><div class="modal-content"><div class="modal-header"><h5 class="modal-title">Modal title</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><p>Modal body text goes here.</p></div><div class="modal-footer"><button type="button" class="btn btn-primary">Save changes</button><button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button></div></div></div></div>';

	document.body.appendChild(popup);*/

}

chrome.contextMenus.create({
	title: "Scraper",
	contexts: ["selection"],
	onclick: createPopUp
});