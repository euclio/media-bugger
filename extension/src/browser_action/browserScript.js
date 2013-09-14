$("#fb_id").attr('value', localStorage.fb_id);

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
	chrome.tabs.sendMessage(tabs[0].id, {},
		function(response) {
		    if (response.method == "getTV") {
		    	if (response.tvShow) {
			   		$('#title').val(response.tvShow.tvName);
			   		$('#season').val(response.tvShow.season);
			   		$('#episode').val(response.tvShow.episode);
			   	} else {
			   		$('#title').val('Nothing');
			   	}
			} else {
				$('#title').val(Nothing);
			}
		}
	);
});

function submitShow() {
	alert('hi');
	var tvData = { 
		fb_id: localStorage.fb_id,
		type: 'tv',
		title: $('#title').val(),
		season: $('#season').val(),
		episode: $('#episode').val()
	};
	$.post('http://google.com', tvData, function(data) { });
}
