# -*- coding: utf-8 -*-

from hashlib import md5
# from portal.utils.db_helpers import mongosession
from datetime import datetime

# from base import WIDocument

# class ItemTranslationMongo(WIDocument):

#     __collection__ = 'item_translations'

#     structure = {
#         'src_asin': unicode,
#         'src_site': unicode,
#         'dst_site': unicode,
#         'when_created': datetime,
#         'title': basestring,
#         'bullet_points': [{
#             'original': unicode,
#             'translated': unicode,
#         }],
#         'attributes': dict,
#         'variations': dict,
#     }
#     required_fields = ['src_asin', 'src_site', 'dst_site']
#     default_values = {'when_created': datetime.utcnow, 'title': u''}

#     @classmethod
#     def create(cls, src_asin, src_site, dst_site):
#         item_translation = mongosession().ItemTranslationMongo()
#         item_translation['src_asin'] = unicode(src_asin)
#         item_translation['src_site'] = unicode(src_site)
#         item_translation['dst_site'] = unicode(dst_site)
#         return item_translation

#     @classmethod
#     def find_one_by_asin_and_sites(cls, src_asin, src_site, dst_site):
#         found = mongosession().ItemTranslationMongo.find_one(
#             {
#                 'src_asin': unicode(src_asin),
#                 'src_site': unicode(src_site),
#                 'dst_site': unicode(dst_site)
#             })
#         return found