from pyramid.config import Configurator
# from urlparse import urlparse
import pymongo
from db import mongosession

from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = SignedCookieSessionFactory('wiverysecretcookie')
    config = Configurator(settings=settings)
    config.set_session_factory(my_session_factory)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # config.registry.db = pymongo.MongoClient(settings['mongo_uri'])
    # config.add_request_method(mongosession, 'db', reify=True)
    config.add_route('home', '/')
    # config.add_route('result', '/result')
    # config.add_route('home_mako', '/home')
    # config.add_route('result_mako', '/result_mako' )
    # config.add_route('find', '/{asin}/{src_site}/{dst_site}')
    config.scan()
    return config.make_wsgi_app()
