var getTVShowName = function() {
    var domain = activeTab.url;
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

$(document).ready(function() {
    $('#video-name').text(getTVShowName());
});
