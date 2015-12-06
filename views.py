from pyramid.view import view_config
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from model import ItemTranslation
from lib.asin_preparator import AsinPreparator

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
        asins = self.request.params.get('src_asin')
        src_site = self.request.params.get('src_site')
        dst_site = self.request.params.get('dst_site')
        asin_list = AsinPreparator().main(asins)
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

    @view_config(route_name='result_mako',
                 renderer='templates/results.mak',
                 request_method='POST'
                 )
    def find_mako(self):
        item = ItemTranslation().find_one_by_asin_and_sites('B005OJW9RO', 'DE', 'UK')
        return {'item': item}

    @view_config(route_name='home_mako', renderer='templates/index.mak')
    def home_mako(self):
        form = Form(self.request, schema=ItemTranslation())
        return {'form':FormRenderer(form)}






