// if you checked "fancy-settings" in extensionizr.com, uncomment this lines

// var settings = new Store("settings", {
//     "sample_setting": "This is how you use Store.js to remember values"
// });


//example of using a message handler from the inject scripts
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
  	chrome.pageAction.show(sender.tab.id);
    sendResponse();
  });

// https://github.com/zuzara/facebook-connect-for-chrome-extension
var successURL = 'https://www.facebook.com/connect/login_success.html';
function onFacebookLogin() {
    chrome.tabs.getAllInWindow(null, function(tabs) {
        for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].url.indexOf(successURL) === 0) {
                var params = tabs[i].url.split('#')[1];
                access = params.split('&')[0]
                localStorage.accessToken = access;
                chrome.tabs.remove(tabs[i].id);
                alert(localStorage.accessToken);
                getLoginData();
                return;
            }
        }   
    }); 
}   
chrome.tabs.onUpdated.addListener(onFacebookLogin);
