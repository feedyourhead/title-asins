from pyramid.view import view_config
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
#from pyramid.response import Response

class AsinSchema(Schema):
    asin = validators.UnicodeString()
    src_site = validators.UnicodeString()
    dst_site = validators.UnicodeString()


class AsinViews:
    def __init__(self, request):
        self.request = request

    #move to models   
    def query(self, asin, src_site, dst_site):
        query = self.request.db['item_translations'].find_one(
                {
                    'src_asin': unicode(asin),
                    'src_site': unicode(src_site),
                    'dst_site': unicode(dst_site)
                })
        results = {'asin':query['src_asin'], 
                'src_site':query['src_site'], 
                'dst_site':query['dst_site'],
                'translation':query['attributes']['Title']['translation'],
                'query':query
                }
        return results

    @view_config(route_name='home', renderer='templates/mytemplate.pt')
    def home(self):
        form = Form(self.request, schema=AsinSchema())
        return {'form':FormRenderer(form)}
        #return {'project': 'title-asins'}

    @view_config(route_name='result',
                 renderer='templates/temp1.pt',
                 #request_method='POST'
                 )
    def result(self):
        #name = self.request.params.get('name', 'No Name Provided')
        asin = self.request.params.get('asin')
        src_site = self.request.params.get('src_site')
        dst_site = self.request.params.get('dst_site')

        return self.query(asin, src_site, dst_site)

        #form = Form(request, schema=AsinSchema())
        #asin = request.db['item_translations'].find_one()
        #return {'asin':asin}

        # if not form.validate:
        #     raise exc.HTTPBadRequest


        # l = Lunch(
        #     submitter=request.POST.get('submitter', 'nobody'),
        #     food=request.POST.get('food', 'nothing'),
        # )

        # with transaction.manager:
        #     DBSession.add(l)

        # raise exc.HTTPSeeOther('/')



    @view_config(route_name='find',
                 renderer='templates/temp1.pt',
                 #request_method='POST'
                 )
    def find(self):
        asin = self.request.matchdict['asin']
        src_site = self.request.matchdict['src_site']
        dst_site = self.request.matchdict['dst_site']
           
        return self.query(asin, src_site, dst_site)



