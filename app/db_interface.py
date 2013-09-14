import pymongo import MongoClient

class db_interface:
  def error():
    return {"ERROR": True}
  def __init__(self,UserName):
    #Creates a Collection for Client also create a interface to db.
    self.db = MongoClient('localhost',27017)["MBuggerDB"]
    if UserName not in self.db.collections_names(include_system_collections=False):
      self.db.create_collection(UserName)
    self.user_data = self.db[UserName]
    if "media" not in self.db.collection_names(include_system_collections=False):
      self.db.create_collection("media")
    self.media = self.db["media"]
    
    
    
    #Media
  def get_media(self, Title):
    #get a media from the media collection.
    ans = self.media.find_one({"Title":Title})
    if ans == None:
      return {"ERROR": True, "Cause": "Given Media Not Found:" + Title}
    return ans
    
  def add_media(self, Title, Summ, Type, Links = [])
    #add a media to the media collection.
    self.media.insert({"Title":Title,"Summ":Summ,"Type":Type,"Links":Links})
    
  def add_link_media(self, Title, Links)
    #add link to the media.  This is mainly for non TV shows items such as books and movies.
    target = self.media.find_one("Title")
    if target == None:
      return {"ERROR": True, "Cuase": "Given Media Not Found:" + Title}
    target["Links"] += Links
    self.media.update({'_id':target['_id']},target)
    
  def seen_media(self, Title)
    #Edit the user's seen media and update the time.
    
    
    
    #Episode Only for TV Shows
  def get_episode(self,Title)
    #get the episode
  def add_episode(self,Title, Summ, Season, Number, Links = [])
    #return bool
  def add_link_episode(self, Title)
    #add link to the episode.
    

