from pyramid.view import view_config
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from model import ItemTranslation
from lib.asin_preparator import AsinController


class AsinViews:

    AMAZON_SITES = ('UK', 'DE', 'FR', 'IT', 'ES')  

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',
                 renderer='templates/index.mak'
                 )
    def find_mako(self):
        form = Form(self.request, schema=ItemTranslation())
        asins = self.request.params.get('src_asin')
        src_site = self.request.params.get('src_site')
        dst_site = self.request.params.get('dst_site')
        asin_list = []
        if asins:
            asin_list = AsinController(asins).validate_asin_list_length()
        results = []

        for asin in asin_list:
            try:
                item_trans = ItemTranslation().find_one_by_asin_and_sites(asin, src_site, dst_site)
                results.append(item_trans)
            except:
                results.append(
                    {'src_asin':asin, 
                    'translation':'not found',
                    'original':'not found', 
                    'query':'not found'
                    })

        return {'form':FormRenderer(form),
                'qresults':results ,
                'amazon_sites':self.AMAZON_SITES,
                'src_site':src_site,
                'dst_site':dst_site
                }







