from pyramid.view import view_config
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

class AsinSchema(Schema):
    asin = validators.UnicodeString()

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def home(request):
    form = Form(request, schema=AsinSchema())
    return {'form':FormRenderer(form)}
    #return {'project': 'title-asins'}

@view_config(route_name='asin',
             renderer='templates/temp1.pt',
             #request_method='POST'
             )
def asin(request):
    form = Form(request, schema=AsinSchema())
    asin = request.db['item_translations'].find_one()
    return {'asin':asin}

    # if not form.validate:
    #     raise exc.HTTPBadRequest


    # l = Lunch(
    #     submitter=request.POST.get('submitter', 'nobody'),
    #     food=request.POST.get('food', 'nothing'),
    # )

    # with transaction.manager:
    #     DBSession.add(l)

    # raise exc.HTTPSeeOther('/')

#     @view_config(route_name='dashboard',
#              renderer="myapp:templates/dashboard.pt")
# def dashboard(request):
#     vendors = request.db['vendors'].find()
#     return {'vendors':vendors}

@view_config(route_name='find',
             renderer='templates/temp1.pt',
             #request_method='POST'
             )
def find(request):
    asin = request.matchdict['asin']
    src_site = request.matchdict['src_site']
    dst_site = request.matchdict['dst_site']
    
    query = request.db['item_translations'].find_one(
            {
                'src_asin': unicode(asin),
                'src_site': unicode(src_site),
                'dst_site': unicode(dst_site)
            })
    return {'asin':query['src_asin'], 
            'src_site':query['src_site'], 
            'dst_site':query['dst_site'],
            'translation':query['attributes.Title.translation'],
            'query':query
            }

