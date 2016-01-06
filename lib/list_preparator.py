# -*- coding: utf-8 -*-


class ListPreparator(object):

    # def __init__(self, asins):
    #     self.string = asins
    #     self.list = []
    @staticmethod
    def convert_string_to_list(string):
        alist = []
        for line in string.splitlines():
            for asin in line.split(','):
                try:
                    alist.append(str(asin.strip()))
                except ValueError:
                    pass
        return list(set(alist))

    @staticmethod
    def validate_list_length(alist, limit):
        if len(alist) <= limit:
            return True
        else:
            return False
