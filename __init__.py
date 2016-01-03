from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from db import MongoSessionFactory
from model import ItemTranslationFinder

__author__ = "Daniel Wykretowicz"


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    cookie_session_factory = SignedCookieSessionFactory('wiverysecretcookie')
    config.set_session_factory(cookie_session_factory)
    config.include('pyramid_mako')
    dbsession_factory = MongoSessionFactory(settings['mongo_uri'])
    dbsession = dbsession_factory.create_session_callable()
    config.registry.db = dbsession
    item_translation_finder = ItemTranslationFinder(dbsession)
    config.add_request_method(
        item_translation_finder.request_property, 'db', reify=True)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
