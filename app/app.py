from flask import *

import os

import db_interface

app = Flask(__name__)
app.debug = True

@app.route('/user/<int:user_id>', methods=['GET'])
def user_page(user_id):
    if request.methods == 'GET':
        user = db_interface.get_user(user_id)
        recent_shows = db_interface.recent_shows(user_id)
        return render_template('user.html', user=user, 
                recent_shows=recent_shows)

@app.route('/media', methods=['POST'])
def mark_media_watched():
    user_id = int(request.form['fb_id'])
    media_type = request.form['type']
    title = request.form['title']
    if media_type == 'tv':
        season = int(request.form['season'])
        episode = int(request.form['episode'])
        db_interface.mark_tv_watched(title, season, episode)

def recent_shows():
    recent_shows = [
            {
                'name': 'King of the Hill',
                'summary': 'This is a cool show'
            },
            {
                'name': 'The Big Bang Theory',
                'summary': 'This show is silly'
            },
            {
                'name': 'Test 1',
                'summary': 'Test'
            },
            {
                'name': 'Test 2',
                'summary': 'Test 2'
            }
        ]

    return recent_shows

@app.route('/login', methods=['POST'])
def login():
    # TODO There is no way that this is secure #HackathonSwag
    user_id = request.form['fb_id']
    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    db_interface.store_user(user_id, first_name, middle_name, friends)


@app.route('/')
def show_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
