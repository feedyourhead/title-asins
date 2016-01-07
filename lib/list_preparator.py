# -*- coding: utf-8 -*-


class ListPreparator(object):

    @staticmethod
    def convert_string_to_list(string):
        a_list = []
        for line in string.splitlines():
            for item in line.split(','):
                try:
                    a_list.append(str(item.strip()))
                except ValueError:
                    pass
        return list(set(a_list))
