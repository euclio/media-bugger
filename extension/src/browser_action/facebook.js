if (localStorage.accessToken) {
    var mainUrl = "https://graph.facebook.com/me?" + localStorage.accessToken;
    var friendsUrl = "https://graph.facebook.com/me/friends?" + localStorage.accessToken;
    console.log(mainUrl);
    console.log(friendsUrl);

    function processMain(data) {
        console.log(data);
    }

    function processFriends(data) {
        console.log(data);
    }

    $.get(mainUrl, {}, processMain);
    $.get(friendsUrl, {}, processFriends);
} 
