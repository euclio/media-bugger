from pymongo import MongoClient
import time, datetime, pymongo
from collections import defaultdict

#Creates a Collection for Client also create a interface to db.
DATABASE = MongoClient('localhost', 27017)["MBuggerDB"]
watched = DATABASE['watched']
tv_shows = DATABASE['tv_shows']

def error():
    return {"ERROR": True}

def seen_media(self, user_id, media_type, title, time):
    # Edit the user's seen media and update the time.
    # TODO Currently, the interface doesn't detect the title and attempt to 
    # update it, but instead just inerst a whole new item.
    target = media.find_all({"title": title})
    if target == None: # TODO In this case, we probably want to query IMDB and add it to the 
        # table, asynchronously
        return {"ERROR":True,"Cause":"Seen Media does not exist."}
    user = users.find_one({'user_id': user_id})
    user['media']['shows'][title][season][episode]['watched'] = True
    user['media']
    users.update(user)
    self.user_data.insert({"CollectionName":"media","MediaID":target["_id"],"TimeStamp":datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),"_time":time.time()})

def mark_seen_episode(self, user_id, title, season, episode):
    tv_spec = {
            'title': title,
            'season': season,
            'episode': episode,
            }
    media_id = tv_shows.find_one(title_spec)['_id']

    if media_id is None:
        # TODO we should query IMDB to get real info
        media_id = tv.shows.insert(tv_spec)

    watched.update(
            {'user_id': user_id, 'media_id': media_id},
            {'date': datetime.utcnow}, upsert=True)

def recent_shows(self, user_id,starting_index=0):
    recent_shows = (
            watched.find({'user_id': user_id, 'type': 'tv'})
            .sort('date')
            .skip(starting_index)
            .limit(40))
    return recent_shows

def recent_items(self, user_id,starting_index=0):
    recent_media = (  
            watched.find({'user_id': user_id})
            .sort('date')
            .skip(starting_index)
            .limit(40))
    return recent_media

def store_user(user_id, first_name, last_name, middle_name, friends):
    users.insert({
        '_id': user_id,
        'first_name': first_name,
        'middle_name': middle_name,
        'last_name': last_name,
        'friends': friends})

def get_user(user_id):
    return users.find_one({'_id': user_id})

#Media
def get_media(self, Title):
    #get a media from the media collection.
    ans = self.media.find_one({"Title":Title})
    if ans == None:
        return {"ERROR": True, "Cause": "Given Media Not Found: " + Title}
    return ans

def add_media(self, Title, Summ, Type, Links = []):
    #add a media to the media collection.
    self.media.insert({"Title":Title,"Summ":Summ,"Type":Type,"Links":Links})

def add_link_media(self, Title, Links):
    #add link to the media.  This is mainly for non TV shows items such as books and movies.
    target = self.media.find_one({"Title":Title})
    if target == None:
        return {"ERROR": True, "Cuase": "Given Media Not Found: " + Title}
    target["Links"] += Links
    self.media.update({'_id':target['_id']},target)

#Episode Only for TV Shows
def get_episode(self,Title, Show, Season, Number):
    #get the episdoe
    ans = self.db[Show + "_"+Season].find_one({"Title":Title})
    if ans == None:
        return {"ERROR": True, "Cause": "Given Episode Not Found: " + Title}

def add_episode(self,Title, Show, Summ, Season, Number, Links = []):
    #Automatically inserts TV_Episodes as Type
    self.db[Show+"_"+Season].insert({"Title":Title,"Summ":Summ,"Type":"TV Episode","Links":Links,"Show":Show,"Season": Season})
    #return bool

def add_link_episode(self, Title, Show, Season, Number):
    #add link to the episode.
    target = self.db[Show+"_"+Season].find_one({"Title":Title})
    if target == None:
        return {"ERROR": True, "Cuase": "Given TV Epispode Not Found: " + Title}
    target["Links"] += Links
    self.media.update({'_id':target['_id']},target)
