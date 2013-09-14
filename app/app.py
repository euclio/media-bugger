from flask import *

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
                'summary': 'This is a cool show'
            },{
                'name': 'The Big Bang Theory',
                'summary': 'This show is silly'
            },{
                'name': 'Test 1',
                'summary': 'Test'
            },{
                'name': 'Test 2',
                'summary': 'Test 2'
        }]
    #TODO swap-out
    
    #return recent_items(request.form['fb_id'])#, request.form['skip_index'])
    return recent_shows

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
