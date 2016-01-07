import pyramid.httpexceptions as exc


class BaseView(object):

    def __init__(self, request):
        self.request = request

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
