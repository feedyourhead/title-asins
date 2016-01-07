from pyramid.view import view_config
import pyramid.httpexceptions as exc
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from title_asins.lib.list_preparator import ListPreparator
from title_asins.schemas.asin_form import AsinFormSchema


class BaseView(object):

    def __init__(self, request):
        self.request = request
        self.form = Form(self.request, schema=AsinFormSchema())

    def _redirect(self, url):
        return exc.HTTPFound(url)

    def _see_other(self, url):
        return exc.HTTPSeeOther(url)

    def _no_content(self):
        return exc.HTTPNoContent()

    def _flash_msg(self, msg):
        return self.request.session.flash(msg)

    def _bad_request(self):
        return exc.HTTPBadRequest


class AsinView(BaseView):

    AMAZON_SITES = ('UK', 'DE', 'FR', 'IT', 'ES')
    LIST_LIMIT = 10

    @view_config(route_name='home',
                 renderer='title_asins:templates/index.mak'
                 )
    def find(self):
        results = {"translations": [], "errors": []}
        data = {'src_site': None, 'dst_site': None}
        if self.request.POST:
            if not self.form.validate():
                raise self._bad_request()
            data = self.form.data
            self.validate_sites(data['src_site'], data['dst_site'])

            asin_list = ListPreparator.convert_string_to_list(
                data['src_asin'])

            self.validate_list_length(asin_list, self.LIST_LIMIT)
            # if not ListPreparator.validate_list_length(
            #         asin_list, self.LIST_LIMIT):
            #     self._flash_msg(
            #         "Please do not enter more than  %s ASINs at a time"
            #         % self.LIST_LIMIT)
            #     raise self._redirect('/')
            results = self.request.db.find_by_asin_list_and_sites(
                asin_list, data['src_site'], data['dst_site'])
            for error in results["errors"]:
                self._flash_msg(error)

        return {'form': FormRenderer(self.form),
                'qresults': results,
                'amazon_sites': self.AMAZON_SITES,
                'src_site': data['src_site'],
                'dst_site': data['dst_site']
                }

    def validate_sites(self, src_site, dst_site):
        if src_site == dst_site:
            self._flash_msg(
                "Destination site has to be differnet than source site.")
            raise self._redirect('/')

    def validate_list_length(self, asin_list, list_limit=10):
        if len(asin_list) >= list_limit:
            self._flash_msg(
                "Please do not enter more than  %s ASINs at a time."
                % list_limit)
            raise self._redirect('/')
