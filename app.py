from flask import *

import json
import os

import db_interface as db

app = Flask(__name__)
app.debug = True

@app.route('/user/<int:user_id>', methods=['GET'])
def user_page(user_id):
    if request.methods == 'GET':
        user = db.get_user(user_id)
        recent_shows = db.recent_shows(user_id)
        return render_template('user.html', user=user, 
                recent_shows=recent_shows)

@app.route('/media', methods=['POST'])
def mark_media_watched():
    print request.form
    user_id = int(request.form['fb_id'])
    media_type = request.form['type']
    showTitle = request.form['title']
    if media_type == 'tv':
        season = int(request.form['season'])
        episode = int(request.form['episode'])
        db.mark_seen_episode(user_id, showTitle, season, episode)
    else:
        #TODO add other media.
        raise ValueError

def recent_shows():
    recent_shows = [{
                'name': 'King of the Hill',
                'summary': 'King of the Hill is an American adult animated sitcom created by Mike Judge and Greg Daniels that ran from January 12, 1997, to May 6, 2010, on Fox.',
                'imageUrl': 'http://abortionsforall.files.wordpress.com/2011/08/hillposter.jpg',
                'epSum': 'Hank discovers that his mother plans on marrying a man that he hasn\'t been introduced to plus hank finds out that she is going to move into a recreational vehicle.',
                'lastSeason': 14,
                'lastEp': 1
            },{
                'name': 'The Big Bang Theory',
                'summary': 'The Big Bang Theory is an American sitcom created by Chuck Lorre and Bill Prady, both of whom serve as executive producers on the show along with Steven Molaro. All three also serve as head writers. It premiered on CBS on September 24, 2007.',
                'imageUrl': 'http://vishalgoel38.files.wordpress.com/2013/05/tv-the-big-bang-theory34.jpg',
                'epSum': 'Sheldon gets excited when he learns that his favorite TV science personality, Professor Proton, is able to be booked for private parties.',
                'lastSeason': 6,
                'lastEp': 22
            },{
                'name': 'Friends',
                'summary': 'Friends is an American sitcom created by David Crane and Marta Kauffman, which aired on NBC from September 22, 1994 to May 6, 2004. The series revolves around a group of friends in the New York City borough of Manhattan.',
                'imageUrl': 'http://bilmoore.com/wp-content/uploads/2012/01/friends-tv-show-wallpapers-1280x1024.jpg',
                'epSum': 'Chandler gets calls from an intriguing woman (Jade) looking for someone named Bob. On the phone, he pretends to be Bob and arranges to meet her, so he can console her when "Bob" stands her up. Their relationship seems to be going very well, until she calls "Bob" back and complains of Chandler\'s sexual inadequacies. Chandler plans a big birthday hoopla for Ross, but the expense involved touches a nerve with Phoebe, Joey, and Rachel, who don\'t make as much money as the others. Monica, Chandler, and Ross celebrate his birthday by attending Hootie and the Blowfish in concert; they end up partying backstage afterwards with the band. Monica gets a new position as Head Lunch Chef, also in charge of purchasing, who has her own little desk (when Roland\'s not there), and a beeper. However, she is soon fired for accepting a gift from the restaurant\'s new meat supplier.',
                'lastSeason': 2,
                'lastEp': 5
            },{
                'name': 'Game of Thrones',
                'summary': 'Game of Thrones is an American fantasy drama television series created for HBO by David Benioff and D. B. Weiss.',
                'imageUrl': 'http://fansided.com/wp-content/blogs.dir/229/files/2013/05/got8.jpg',
                'epSum': '"The Old Gods and the New" is the sixth episode of the second season of Game of Thrones. It is the sixteenth episode of the series overall. It premiered on May 6, 2012. It was written by co-executive producer Vanessa Taylor and directed by David Nutter.',
                'lastSeason': 2,
                'lastEp': 6
        }]
    #TODO swap-out
    #return recent_items(request.form['fb_id'])#, request.form['skip_index'])
    return recent_shows

@app.route('/friends', methods=['POST'])
def registered_friends():
    user_id = request.form['fb_id']
    friends = request.form['friends']
    registered_friends = db.get_registered_friends(user_id)
    return json.dumps({'friends': regeistered_friends})

@app.route('/login', methods=['POST'])
def login():
    # TODO There is no way that this is secure #HackathonSwag
    db.store_user(
        user_id = request.form['fb_id'],
        first_name = request.form['first_name'],
        middle_name = request.form['middle_name'],
        last_name = request.form['last_name'],
        friends = request.form['friends'])

@app.route('/')
def show_index():
    return render_template('user.html', recent_shows=recent_shows())

if __name__ == '__main__':
    app.run()
