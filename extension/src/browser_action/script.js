var getTVString = function() {
    var domain;
    chrome.tabs.getSelected(null, function(tab) {
        domain = tab.url.split('.')[1];
    });
    console.log(domain);
    
    var tvName;

    if (domain == 'youtube') {
        tvName = $('title').text;
        console.log("On youtube");
    } else if (domain == 'free-tv-video-online') {
        tvName = document.querySelectorAll('td div h1')[0].innerText;
        console.log("On project free tv");
    }
    return tvName != undefined ? tvName : 'Unable to parse TV show name';
};

var parseTVNameParts = function(tvString) {
    var showName;
    var curSeason;
    var curEpisode;

    return { showName : tvString, 
             season : 4,
             curEpisode : 2 };
};

$(document).ready(function() {
    var tvString = getTVString();
    var tvParts = parseTVNameParts();
    $('#video-name').text(tvParts.showName);
});
