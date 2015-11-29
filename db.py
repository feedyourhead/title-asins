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
       
        db = pymongo.MongoClient('mongodb://dwykretowicz:PASSWORD@wi-amazon-mongo-2.db.devwebinterpret.com:27017/wi-amazon'
        )
        return db['wi-amazon']



mongosession = MongoConnection.dbsession()

# print mongosession['item_translations'].find_one()
