var getTVString = function() {
    var domain = document.URL.split('.')[1];
    var tvString = {};

    if (domain == 'youtube') {
        tvString.tvName = document.title;
    } else if (domain == 'free-tv-video-online') {
        var freeTvString = document.querySelectorAll("td div h1")[0].innerText;
        var tvNameMatcher = new RegExp('.* Season');
        var seasonMatcher = new RegExp('Season [0-9]+');
        var episodeMatcher = new RegExp('Episode [0-9]+');

        tvString.tvName = freeTvString.match(tvNameMatcher)[0].split(' Season')[0];
        tvString.season = freeTvString.match(seasonMatcher)[0].split('Season ')[1];
        tvString.episode = freeTvString.match(episodeMatcher)[0].split('Episode ')[1];
    } 

    return tvString;
};

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        var tvString = getTVString();
        sendResponse({method:'getTV', tvShow: tvString});
    }
);
