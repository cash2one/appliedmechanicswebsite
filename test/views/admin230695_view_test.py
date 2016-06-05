# -*- coding: utf-8 -*-
from .. import BaseTestCase


class TestViewAdmin230695(BaseTestCase):

    def test_index(self):
        response = self.client.get('/admin230695/')
        assert b'Welcome to your new blueprint!' in response.data
