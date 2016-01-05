from pymongo import MongoClient


class MongoSessionFactory(object):

    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    def create_session_callable(self):
        try:
            client = MongoClient(self.mongo_uri)
            session = client['wi-amazon']
        except Exception as e:
            print "exception: ", type(e), e
        return session
