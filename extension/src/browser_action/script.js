var getTVShowName = function() {
    var domain = document.domain.split('.')[1];
    var tvName;
    if (domain == 'youtube') {
        tvName = $('title').text;
    } else if (domain == 'free-tv-video-online') {
        tvName = document.querySelectorAll('td div h1')[0].innerText;
    }
    return tvName == undefined ? tvName : 'Unable to parse TV show name';
};

$(document).ready() {
    $('#video-name').text(getTVShowName());
};
