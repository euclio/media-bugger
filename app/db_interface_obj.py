from pymongo import MongoClient
import time,datetime,pymongo

class db_interface:
  def error():
    return {"ERROR": True}
  def __init__(self,UserName):
    #Creates a Collection for Client also create a interface to db.
    self.db = MongoClient('localhost',27017)["MBuggerDB"]
    if UserName not in self.db.collection_names(include_system_collections=False):
      self.db.create_collection(UserName)
    self.user_data = self.db[UserName]
    self.user_data.create_index([("_time", pymongo.DESCENDING)])
    if "media" not in self.db.collection_names(include_system_collections=False):
      self.db.create_collection("media")
    self.media = self.db["media"]
#User's collection will be documents of {"CollectionName":_, "id":_id,"Time": timeStamp,"_time": time in miliseconds}    
    
    

    #User
  def seen_media(self, Title):
    #Edit the user's seen media and update the time.
    #TODO Currently, the interface doesn't detect the title and attempt to update it, but instead just inerst a whole new item.
    target = self.media.find_one({"Title":Title})
    if target == None:
        return {"ERROR":True,"Cause":"Seen Media does not exist."}
    self.user_data.insert({"CollectionName":"media","MediaID":target["_id"],"TimeStamp":datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),"_time":time.time()})

  def seen_episode(self,Show, Season,Episode):
    #Edit the user's seen media and update the time.
    target = self.db[Show + "_"+Season].find_one({"Title":Episode})
    if target == None:
        return {"ERROR":True,"Cause":"Seen Episode does not exist."}
    self.user_data.insert({"CollectionName":Show+"_"+Season,"EpisodeID":target["_id"],"TimeStamp":datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"),"_time":time.time()})
  def recent_items(self,starting_index=0):
    #Gives out the next 40 items after the starting index after sort.
    if self.user_data.count() <=0:
        return []
    ending_index = starting_index + 40
    if self.user_data.count() < ending_index:
        ending_index = self.user_data.count()-1
        if ending_index - 40 <0:
            starting_index=0
        else:
            starting_index = ending_index - 40
    returnList = [for entry in ]
    return list(self.user_data.find(sort=[("_time",-1)])[starting_index:ending_index])
    
    	




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
    return ans
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

