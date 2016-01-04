from pyramid.view import view_config
import pyramid.httpexceptions as exc
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from lib.asin_preparator import AsinController


class AsinFormSchema(Schema):

    src_asin = validators.UnicodeString()
    src_site = validators.UnicodeString()
    dst_site = validators.UnicodeString()


class AsinViews(object):

    AMAZON_SITES = ('UK', 'DE', 'FR', 'IT', 'ES')

    def __init__(self, request):
        self.request = request
        self.form = Form(self.request, schema=AsinFormSchema())

    @view_config(route_name='home',
                 renderer='templates/index.mak'
                 )
    def find(self):
        if self.request.POST:
            if not self.form.validate():
                raise exc.HTTPBadRequest
            data = self.form.data
            if data['src_site'] == data['dst_site']:
                self.request.session.flash(
                    "Destination site has to be differnet than source site.")
                raise exc.HTTPSeeOther('/')
            asins = AsinController(data['src_asin'])
            asin_list = asins.get_asins_from_request()
            if not asins.validate_list_length():
                self.request.session.flash(
                    "Please do not enter more than  %s ASINs at a time"
                    % asins.ASIN_LIST_LIMIT)
                raise exc.HTTPSeeOther('/')
        results = self.request.db.find_by_asin_list_and_sites(
            asin_list, data['src_site'], data['dst_site'])

        return {'form': FormRenderer(self.form),
                'qresults': results,
                'amazon_sites': self.AMAZON_SITES,
                'src_site': data['src_site'],
                'dst_site': data['dst_site']
                }
