# import pymongo
from pymongo import MongoClient


class MongoSessionFactory(object):

    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    def create_session_callable(self):
        try:
            session = MongoClient(self.mongo_uri)
            print 'connected!'
        except Exception as e:
            print "exception: ", type(e), e
        return session['wi-amazon']

