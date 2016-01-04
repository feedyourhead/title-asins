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


class BaseFinder(object):

    def __init__(self, session):
        self.session = session


class ItemTranslationFinder(BaseFinder):

    collection = 'item_translations'

    def request_property(self, request):
        return self

    def find_one_by_asin_and_sites(self, src_asin, src_site, dst_site):
        collection = getattr(self.session, self.collection)
        return collection.find_one(
            {
                'src_asin': unicode(src_asin),
                'src_site': unicode(src_site),
                'dst_site': unicode(dst_site)
            })

    def find_by_asin_list_and_sites(self, asin_list, src_site, dst_site):
        results = []
        for asin in asin_list:
            try:
                item_trans = self.find_one_by_asin_and_sites(
                    asin,
                    src_site,
                    dst_site
                )
                item_trans = {
                    'src_asin': item_trans['src_asin'],
                    'translation':
                        item_trans['attributes']['Title']['translation'],
                    'original': item_trans['attributes']['Title']['original']
                }
                results.append(item_trans)
            except:
                results.append(
                    {'src_asin': asin,
                     'translation': 'not found',
                     'original': 'not found'
                     })
        return results
