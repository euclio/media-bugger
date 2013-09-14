from flask import *

import json

import db_interface

app = Flask(__name__)

@app.route('/user/<int:user_id>')
def front_page_json(user_id):
    front_page = {}
    front_page['recent_shows'] = db_interface.get_recent_shows(user_id)
    return json.dumps(front_page)

@app.route('/media', methods=['POST'])
def mark_media_watched():
    media_type = request.form['type']
    title = request.form['title']
    if media_type == 'tv':
        season = int(request.form['season'])
        episode = int(request.form['episode'])
        db_interface.mark_tv_watched(title, season, episode)

if __name__ == '__main__':
    app.run()
