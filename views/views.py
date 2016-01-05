from pyramid.view import view_config
import pyramid.httpexceptions as exc
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from title_asins.lib.asin_preparator import AsinController
from title_asins.schemas.asin_form import AsinFormSchema


class BaseView(object):

    def __init__(self, request):
        self.request = request
        self.form = Form(self.request, schema=AsinFormSchema())

    def _make_error(self, status_code, exception):
        self.request.response.status_code = status_code
        message = exception.args and exception.args[0]
        return {'status': 'error', 'message': message}

    def _redirect(self, url):
        return exc.HTTPFound(url)

    def _see_other(self, url):
        return exc.HTTPSeeOther(url)

    def _no_content(self):
        return exc.HTTPNoContent()

    def _flash_msg(self, msg):
        return self.request.session.flash(msg)


class AsinView(BaseView):

    AMAZON_SITES = ('UK', 'DE', 'FR', 'IT', 'ES')

    @view_config(route_name='home',
                 renderer='title_asins/templates/index.mak'
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
