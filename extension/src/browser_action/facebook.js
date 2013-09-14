function clearLocalData() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('first_name');
    localStorage.removeItem('middle_name');
    localStorage.removeItem('last_name');
    localStorage.removeItem('fb_id');
    localStorage.removeItem('friends');
}

if (localStorage.accessToken) {
    var mainUrl = "https://graph.facebook.com/me?" + localStorage.accessToken;
    var friendsUrl = "https://graph.facebook.com/me/friends?" + localStorage.accessToken;

    function processMain(data) {
        localStorage.first_name = data.first_name;
        localStorage.middle_name = data.middle_name;
        localStorage.last_name = data.last_name;
        localStorage.fb_id = data.id;
        $('#intro').html('Hello, ' + localStorage.first_name + '!' +
            '<br /> <a id="logout" href="#">Logout</a>');
        $('#logout').click(function(e) {
            clearLocalData();
            location.reload();
        });
    }

    function processFriends(data) {
        var friendsArray = [];
        for (var i = 0; i < data.data.length; i++) {
            friendsArray.push(data.data[i].id);
        }
        localStorage.friends = JSON.stringify(friendsArray);
    }

    $.get(mainUrl, {}, processMain);
    $.get(friendsUrl, {}, processFriends);
} else {
    $('#fbconnect').click(function(e) {
        location.reload();
    });
}
