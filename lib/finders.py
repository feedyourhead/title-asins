
class BaseFinder(object):

    def __init__(self, session):
        self.session = session

    def request_property(self, request):
        return self


class ItemTranslationFinder(BaseFinder):

    collection = 'item_translations'

    def find_one_by_asin_and_sites(self, src_asin, src_site, dst_site):
        collection = getattr(self.session, self.collection)
        return collection.find_one(
            {
                'src_asin': unicode(src_asin),
                'src_site': unicode(src_site),
                'dst_site': unicode(dst_site)
            })

    def find_by_asin_list_and_sites(self, asin_list, src_site, dst_site):
        results = {"translations": [], "errors": []}
        for asin in asin_list:
            try:
                item_trans = self.find_one_by_asin_and_sites(
                    asin,
                    src_site,
                    dst_site
                )
                if item_trans is not None:
                    results["translations"].append(item_trans)
                else:
                    results["errors"].append("Asin " + asin + " not found")
            except Exception as e:
                print "Exception: ", type(e), e
                results["errors"].append(
                    "Exception: " + " " + type(e) + " " + e)
        return results
