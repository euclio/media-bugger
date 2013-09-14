function clearLocalData() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('first_name');
    localStorage.removeItem('middle_name');
    localStorage.removeItem('last_name');
    localStorage.removeItem('fb_id');
    localStorage.removeItem('friends');
}

function getUserPage() {
    chrome.tabs.getAllInWindow(null, function(tabs) {
        var found = false;
        for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].url.indexOf('/user/' + localStorage.fb_id) >= 0) {
                chrome.tabs.reload(tabs[i].id);
                found = true;
                return;
            }
        }
        if (!found) {
            window.open('/user/' + localStorage.fb_id);
        }
    });
}

function getLoginData() {
    console.log(localStorage);
    if (localStorage.accessToken !== undefined) {
        var justLoggedIn = localStorage.fb_id === undefined;

        var mainUrl = "https://graph.facebook.com/me?" + localStorage.accessToken;
        var friendsUrl = "https://graph.facebook.com/me/friends?" + localStorage.accessToken;

        function processFriends(data) {
            var friendsArray = [];
            for (var i = 0; i < data.data.length; i++) {
                friendsArray.push(data.data[i].id);
            }
            localStorage.friends = JSON.stringify(friendsArray);

            if (justLoggedIn) {
                // send data to server
                var postUrl = '/login';
                $.get(postUrl, {'first_name': localStorage.first_name, 'last_name': localStorage.last_name,
                                'middle_name': localStorage.middle_name, 'friends': localStorage.friends,
                                "fb_id": localStorage.fb_id},
                      function() {});
                // redirect to user page
                getUserPage();
            }
        }

        function processMain(data) {
            localStorage.first_name = data.first_name;
            localStorage.middle_name = data.middle_name;
            localStorage.last_name = data.last_name;
            localStorage.fb_id = data.id;
            updatePage();

            $.get(friendsUrl, {}, processFriends);
        }

        $.get(mainUrl, {}, processMain);
    }
}

// https://github.com/zuzara/facebook-connect-for-chrome-extension
var successURL = 'https://www.facebook.com/connect/login_success.html';
function onFacebookLogin() {
    if (localStorage.actionToken === undefined) {
        chrome.tabs.getAllInWindow(null, function(tabs) {
            for (var i = 0; i < tabs.length; i++) {
                if (tabs[i].url.indexOf(successURL) === 0) {
                    var params = tabs[i].url.split('#')[1];
                    access = params.split('&')[0]
                    if (localStorage.actionToken === undefined) {
                        localStorage.accessToken = access;
                        chrome.tabs.remove(tabs[i].id);
                        getLoginData();
                    }
                    return;
                }
            }   
        }); 
    }
}   
chrome.tabs.onUpdated.addListener(onFacebookLogin);

function updatePage() {
    if (localStorage.first_name !== undefined) {
        $('#intro').html('Hello, ' + localStorage.first_name + '!' +
            '<br /> <a id="userpage" href="#">User Page</a> | <a id="logout" href="#">Logout</a>');
        $('#logout').click(function(e) {
            clearLocalData();
            location.reload();
        }); 
        $('#userpage').click(function(e) {
            getUserPage();
        }); 
    }   
    $('#fbconnect').click(function(e) {
        location.reload();
    }); 
}

function getPictureUrl(fb_id) {
    if (localStorage.accessToken !== undefined) {
        return "https://graph.facebook.com/" + fb_id + "/picture?" + localStorage.accessToken;
    } else {
        return "";
    }
}
