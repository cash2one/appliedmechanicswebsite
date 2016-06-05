# -*- coding: utf-8 -*-
from .. import BaseTestCase


class TestViewAdmin(BaseTestCase):

    def test_index(self):
        response = self.client.get('/admin/')
        assert b'Welcome to your new blueprint!' in response.data
