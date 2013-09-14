chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
	chrome.tabs.sendMessage(tabs[0].id, {},
		function(response) {
		    if (response.method == "getTV") {
		    	if (response.tvShow) {
			   		document.getElementById('video-name').innerHTML = response.tvShow;     
			   	} else {
			   		document.getElementById('video-name').innerHTML = 'Nothing';
			   	}
			} else {
				document.getElementById('video-name').innerHTML = 'Nothing';				 
			}
		}
	);
});