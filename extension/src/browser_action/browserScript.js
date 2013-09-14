chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
	chrome.tabs.sendMessage(tabs[0].id, {},
		function(response) {
		    if (response.method == "getTV") {
		    	if (response.tvShow) {
			   		$('#video-name').val(response.tvShow.tvName);
			   		$('#season').val(response.tvShow.season);
			   		$('#episode').val(response.tvShow.episode);
			   	} else {
			   		$('#video-name').val('Nothing');
			   	}
			} else {
				$('#video-name').val(Nothing);
			}
		}
	);
});