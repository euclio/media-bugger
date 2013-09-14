import pymongo import MongoClient

class db_interface:
  def __init__(self,ClientName)
    #Creates a Collection for Client also create a interface to db.
    
    
    
    #Show
  def get_media(self, Title)
    #get a media from the media collection.
  def add_media(self, Title, Summ, Type, Links = [])
    #add a media to the media collection.
  def add_link_media(self, Title, Links)
    #add link to the media.  This is mainly for non TV shows items such as books and movies.
  def seen_media(self, Title) 
    #Edit the user's seend media and update the time.
    
    
    #Episode Only for TV Shows
  def get_episode(self,Title)
    #get the episode
  def add_episode(self,Title, Summ, Season, Number, Links = [])
    #return bool
  def add_link_episode(self, Title)
    #add link to the episode.
    

