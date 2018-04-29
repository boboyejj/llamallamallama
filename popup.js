// listen for message
/*chrome.runtime.onMessage.addListener(function(message, sender) {
	console.log(message.name);
});*/

chrome.storage.local.get(['name'], function(result) {
	console.log(result.name);
});


/*
document.getElementsByClassName('card-title')[0].innerText = name;*/