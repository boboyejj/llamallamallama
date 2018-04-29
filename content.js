var productName = document.getElementsByClassName('productName')[0].innerText;

chrome.storage.local.set({'name': productName}, function() {

});


/*chrome.runtime.sendMessage({
	name: "hello"
});*/