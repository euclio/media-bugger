import pymongo import MongoClient

class db_interface:
  def __init__(self):
    self.client = MongoClient('localhost',27017)
    self.db = self.client.MBuggerDB
  def getShow(self,Title):
