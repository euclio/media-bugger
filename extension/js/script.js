var getTVString = function() {
    var domain = document.URL.split('.')[1];
    var tvName = 'Unparsable';

    if (domain == 'youtube') {
        tvName = document.title;
    } else if (domain == 'free-tv-video-online') {
        tvName = document.querySelectorAll("td div h1")[0].innerText;
    } 

    return tvName;
};

var parseTVNameParts = function(tvString) {
    var showName;
    var curSeason;
    var curEpisode;

    return { showName : tvString, 
             season : 4,
             curEpisode : 2 };
};

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        console.log('hey');
        var tvString = getTVString();
        console.log(tvString);
        sendResponse({method:'getTV', tvShow: tvString});
    }
);
