# -*- coding: utf-8 -*-
from datetime import datetime


class ItemTranslation(object):

    __collection__ = 'item_translations'

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
