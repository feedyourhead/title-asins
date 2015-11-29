from pyramid.view import view_config
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from model import ItemTranslation
#from pyramid.response import Response


class AsinViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/mytemplate.pt')
    def home(self):
        form = Form(self.request, schema=ItemTranslation())
        return {'form':FormRenderer(form)}

    @view_config(route_name='result',
                 renderer='templates/temp1.pt',
                 #request_method='POST'
                 )
    def result(self):
        asins = self.request.params.get('asin')
        src_site = self.request.params.get('src_site')
        dst_site = self.request.params.get('dst_site')

        #move to lib
        results = []
        asin_list = asins.splitlines()

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

        return {'results':results, 'src_site':src_site, 'dst_site':dst_site}

    @view_config(route_name='find',
                 renderer='templates/temp1.pt',
                 #request_method='POST'
                 )
    def find(self):
        asin = self.request.matchdict['asin']
        src_site = self.request.matchdict['src_site']
        dst_site = self.request.matchdict['dst_site']
        item_trans = ItemTranslation().find_one_by_asin_and_sites(asin, src_site, dst_site)
        return item_trans

