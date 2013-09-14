var getTVString = function(tab) {
    var domain = tab.url.split('.')[1];
    var tvName = 'Unable to parse TV show name';
    var ready = false;

    if (domain == 'youtube') {
        tvName = tab.title;
        ready = true;
    } else if (domain == 'free-tv-video-online') {
        chrome.tabs.executeScript(tab.id, 
                {code: 'var name=document.querySelectorAll("td div h1")[0].innerText; name'},
            function(name) {
                tvName = name; 
                console.log(tvName);
                ready = true;
            }
        );    
    } else {
        ready = true;
    }
    
    while (!ready) {};
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

$(document).ready(function() {
    chrome.tabs.query({active:true, currentWindow:true}, function(tabArray) {
        var tvString = getTVString(tabArray[0]);
        console.log(tvString);
        document.getElementById('video-name').innerHTML = tvString;
    });
});
