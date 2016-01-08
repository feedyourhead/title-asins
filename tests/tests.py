# import unittest

from pyramid import testing
import pytest


class TestListPreparator(object):

    PARAM_RESULT = [
        ('ASIN', ['ASIN']),
        ('ASIN\nASIN2', ['ASIN', 'ASIN2']),
        ('ASIN, ASIN2', ['ASIN', 'ASIN2'])
    ]

    @pytest.mark.parametrize(
        "input,expected",
        PARAM_RESULT
    )
    def test_convert_string_to_list(self, input, expected):
        from title_asins.lib.list_preparator import ListPreparator
        converter = ListPreparator.convert_string_to_list(input)
        assert converter == list(set(expected))


class TestAsinView(object):

    # def setUp(self):
    #     self.config = testing.setUp()

    # def tearDown(self):
    #     testing.tearDown()

    @pytest.fixture
    def pyramid_req(self):
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        return request

    def test_find(self, pyramid_req):
        # from title_asins.views.views import AsinView
        # inst = AsinView(self.pyramid_req)
        # # response = inst.find()
        # assert inst.status_code == 200

        from title_asins.views.views import AsinView
        inst = AsinView(pyramid_req)
        print dir(inst.request)
        assert inst.request.response.status_code == 200
        assert inst.request.POST == {}


# class TestBaseView(object):

#     @pytest.fixture
#     def pyramid_req(self):
#         return testing.DummyRequest()

#     def test_flash_msg(self):
#         from title_asins.views.base import BaseView
#         inst = BaseView(self.pyramid_req)
#         flash = inst.session.flash('test')
#         print flash
#         assert flash == inst.session.flash('test')

