// var getTVString = function() {
//     var domain = tab.url.split('.')[1];
//     var tvName = 'Unable to parse TV show name';

//     if (domain == 'youtube') {
//         tvName = tab.title;
//         ready = true;
//     } else if (domain == 'free-tv-video-online') {
//         var tvName = document.querySelectorAll("td div h1")[0].innerText;
//         console.log(tvName);
//     } 
// };

// var parseTVNameParts = function(tvString) {
//     var showName;
//     var curSeason;
//     var curEpisode;

//     return { showName : tvString, 
//              season : 4,
//              curEpisode : 2 };
// };

$(document).ready(function() {
    chrome.tabs.query({active:true, currentWindow:true}, function(tabArray) {
        // var tvString = getTVString(tabArray[0]);
        // console.log(tvString);
        document.getElementById('video-name').innerHTML = 'Nothing';
    });
    // document.getElementById('video-name').innerHTML = 'Nothing';                 
    // chrome.extension.sendRequest({message:'getTV', data: 'hi'}, function(response) {});
});

// $(document).ready(function() {
    // console.log('hello');
// });

