from pyramid.config import Configurator

try:
    # for python 2
    from urlparse import urlparse
except ImportError:
    # for python 3
    from urllib.parse import urlparse

from gridfs import GridFS
import pymongo

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    #move this chunk to db.py
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.MongoClient(
       host=db_url.hostname,
       port=db_url.port,
    )

    def add_db(request):
       db = config.registry.db[db_url.path[1:]]
       if db_url.username and db_url.password:
           db.authenticate(db_url.username, db_url.password)
       return db

    def add_fs(request):
       return GridFS(request.db)

    config.add_request_method(add_db, 'db', reify=True)
    config.add_request_method(add_fs, 'fs', reify=True)
    config.add_route('home', '/')
    config.add_route('result', '/result')
    config.add_route('find', '/{asin}/{src_site}/{dst_site}')
    config.scan()
    return config.make_wsgi_app()
