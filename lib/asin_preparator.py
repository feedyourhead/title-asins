# -*- coding: utf-8 -*-

AMAZON_SITES = ('UK', 'FR', 'DE', 'IT', 'ES')   

class AsinPreparator(object):

    @staticmethod
    def get_list_of_asins(asins):
        asin_list = asins.splitlines()
        return asin_list

    @staticmethod
    def validate_list_lenght(asin_list, max_lenght=10):
        if len(asin_list) > max_lenght:
            return asin_list[:max_lenght] #check in bulk requster
        else:
            return asin_list

    def main(self, asins):
        return self.validate_list_lenght(
                self.get_list_of_asins(asins)
                )
