# -*- coding: utf-8 -*-


class AsinController(object):
    
    ASIN_LIST_LIMIT = 10

    def __init__(self, asins):
        self.asins = asins
        self.asin_list = []

    def get_asins_from_request(self):
        for line in self.asins.splitlines():
            for asin in line.split(','):
                try:
                    self.asin_list.append(str(asin.strip()))
                except ValueError:
                    pass
        return list(set(self.asin_list))

    def validate_list_length(self):
        if len(self.asin_list) <= self.ASIN_LIST_LIMIT:
            return True
        else:
            return False
