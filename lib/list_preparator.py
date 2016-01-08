# -*- coding: utf-8 -*-


class ListPreparator(object):

    def convert_string_to_list(self, value):
        a_list = []
        for line in value.splitlines():
            for item in line.split(','):
                try:
                    a_list.append(str(item.strip()))
                except ValueError:
                    pass
        return list(set(a_list))

#zainstancjonowac. jak nie ma initat to warto zainstancjonowac.
# wrzucic w katalog 'dependencies'
list_preparator = ListPreparator()
