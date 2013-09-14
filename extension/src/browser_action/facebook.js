if (localStorage.accessToken) {
    var graphUrl = "https://graph.facebook.com/me?" + localStorage.accessToken + "&callback=displayUser";
    console.log(graphUrl);

    function displayUser(user) {
        console.log(user);
    }
} 
