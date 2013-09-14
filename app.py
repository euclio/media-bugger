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
        db.mark_tv_watched(showTitle, season, episode)
    else:
        #TODO add other media.
        raise ValueError

def recent_shows():
    recent_shows = [{
                'name': 'King of the Hill',
                'summary': 'King of the Hill is an American adult animated sitcom created by Mike Judge and Greg Daniels that ran from January 12, 1997, to May 6, 2010, on Fox.',
                'imageUrl': 'http://abortionsforall.files.wordpress.com/2011/08/hillposter.jpg' 
            },{
                'name': 'The Big Bang Theory',
                'summary': 'The Big Bang Theory is an American sitcom created by Chuck Lorre and Bill Prady, both of whom serve as executive producers on the show along with Steven Molaro. All three also serve as head writers. It premiered on CBS on September 24, 2007.',
                'imageUrl': 'http://vishalgoel38.files.wordpress.com/2013/05/tv-the-big-bang-theory34.jpg' 
            },{
                'name': 'Friends',
                'summary': 'Friends is an American sitcom created by David Crane and Marta Kauffman, which aired on NBC from September 22, 1994 to May 6, 2004. The series revolves around a group of friends in the New York City borough of Manhattan.',
                'imageUrl': 'http://bilmoore.com/wp-content/uploads/2012/01/friends-tv-show-wallpapers-1280x1024.jpg'
            },{
                'name': 'Game of Thrones',
                'summary': 'Game of Thrones is an American fantasy drama television series created for HBO by David Benioff and D. B. Weiss.',
                'imageUrl': 'http://fansided.com/wp-content/blogs.dir/229/files/2013/05/got8.jpg'
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
