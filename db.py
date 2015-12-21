#from pyramid.config import Configurator
# from urlparse import urlparse
# from gridfs import GridFS
import pymongo


class MongoConnection(object):

    # @classmethod
    # def dbsession(cls, **settings):
    #     #config = Configurator(settings=settings)
    #     db_url = urlparse(settings['mongo_uri'])
    #     db = pymongo.MongoClient(
    #        host=db_url.hostname,
    #        port=db_url.port,
    #     )
       
    #     if db_url.username and db_url.password:
    #        db.authenticate(db_url.username, db_url.password)

    #     return db


    @classmethod
    def dbsession(cls):
        try:
            db = pymongo.MongoClient('mongodb_uri')
            print 'connected!'
        # except pymongo.errors.ConnectionFailure, e:
        except Exception as e:
            print "exception: ", type(e), e
        return db['wi-amazon']

mongosession = MongoConnection.dbsession()

# print mongosession['item_translations'].find_one()
