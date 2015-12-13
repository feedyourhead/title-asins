# -*- coding: utf-8 -*-

class AsinController(object):

    ASIN_LIST_LIMIT = 10
    
    def __init__(self, asins):
        self.asins = asins

    def _get_asins_from_request(self):
        asin_list = []
        for line in self.asins.splitlines():
            for asin in line.split(','):
                try:
                    asin_list.append(str(asin.strip()))
                except ValueError:
                    pass
        return list(set(asin_list))

    def validate_asin_list_length(self):
        asin_list = self._get_asins_from_request()
        if len(asin_list) > self.ASIN_LIST_LIMIT:
            return asin_list[:self.ASIN_LIST_LIMIT] #check in bulk requster
        else:
            return asin_list
