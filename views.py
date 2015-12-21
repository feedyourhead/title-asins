from pyramid.view import view_config
import pyramid.httpexceptions as exc
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from model import ItemTranslation
from lib.asin_preparator import AsinController


class AsinFormSchema(Schema):

    src_asin = validators.UnicodeString()
    src_site = validators.UnicodeString()
    dst_site = validators.UnicodeString()


class AsinViews:

    AMAZON_SITES = ('UK', 'DE', 'FR', 'IT', 'ES')

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',
                 renderer='templates/index.mak'
                 )
    def find_mako(self):
        form = Form(self.request, schema=AsinFormSchema())
        src_site = self.request.params.get('src_site')
        dst_site = self.request.params.get('dst_site')
        asins = self.request.params.get('src_asin')
        if not form.validate:
            raise exc.HTTPBadRequest
        if src_site != None and src_site == dst_site:
            self.request.session.flash(
                "Destination site has to be differnet than source site.")
            raise exc.HTTPSeeOther('/')
            # return redirect('/')
        asin_list = []
        print 'im here'
        if asins:
            asins = AsinController(asins)
            asin_list = asins.get_asins_from_request()
            # asin_list = AsinController(asins).get_asins_from_request()
            if not asins.validate_list_length():
                self.request.session.flash(
                    "Please do not enter more than  %s ASINs at a time" % asins.ASIN_LIST_LIMIT)
                raise exc.HTTPSeeOther('/')
        results = []
        for asin in asin_list:
            try:
                item_trans = ItemTranslation.find_one_by_asin_and_sites(
                    asin,
                    src_site,
                    dst_site
                )
                item_trans = {
                    'src_asin': item_trans['src_asin'],
                    'translation': item_trans['attributes']['Title']['translation'],
                    'original': item_trans['attributes']['Title']['original']
                }
                results.append(item_trans)
            except:
                results.append(
                    {'src_asin': asin,
                     'translation': 'not found',
                     'original': 'not found'
                     })

        return {'form': FormRenderer(form),
                'qresults': results,
                'amazon_sites': self.AMAZON_SITES,
                'src_site': src_site,
                'dst_site': dst_site
                }
