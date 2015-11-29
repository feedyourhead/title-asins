# -*- coding: utf-8 -*-

from datetime import datetime
from db import mongosession
from formencode import Schema, validators


class ItemTranslation(Schema):

    __collection__ = 'item_translations'   
    
    src_asin = validators.UnicodeString()
    src_site = validators.UnicodeString()
    dst_site = validators.UnicodeString()

    structure = {
        'src_asin': unicode,
        'src_site': unicode,
        'dst_site': unicode,
        'when_created': datetime,
        'title': basestring,
        'bullet_points': [{
            'original': unicode,
            'translated': unicode,
        }],
        'attributes': dict,
        'variations': dict,
    }
    required_fields = ['src_asin', 'src_site', 'dst_site']
    default_values = {'when_created': datetime.utcnow, 'title': u''}

    @classmethod
    def find_one_by_asin_and_sites(cls, src_asin, src_site, dst_site):
        query = mongosession['item_translations'].find_one(
                {
                    'src_asin': unicode(src_asin),
                    'src_site': unicode(src_site),
                    'dst_site': unicode(dst_site)
                })
        results = {'src_asin':query['src_asin'], 
                'src_site':query['src_site'], 
                'dst_site':query['dst_site'],
                'translation':query['attributes']['Title']['translation'],
                'original':query['attributes']['Title']['original'], 
                'query':query
                }
        # print 'query from models', query
        return results

