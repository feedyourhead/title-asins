# import unittest

from pyramid import testing
import pytest


class TestAsinView(object):

    # def setUp(self):
    #     self.config = testing.setUp()

    # def tearDown(self):
    #     testing.tearDown()

    @pytest.fixture
    def pyramid_req(self):
        return testing.DummyRequest()

    def test_find(self):
        from title_asins.views.views import AsinView
        inst = AsinView(self.pyramid_req)
        response = inst.find()
        assert response.status_code == 200


class TestBaseView(object):

    @pytest.fixture
    def pyramid_req(self):
        return testing.DummyRequest()

    def test_flash_msg(self):
        from title_asins.views.base import BaseView
        inst = BaseView(self.pyramid_req)
        flash = inst.session.flash('test')
        print flash
        assert flash == inst.session.flash('test')


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
