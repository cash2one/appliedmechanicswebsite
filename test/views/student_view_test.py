# -*- coding: utf-8 -*-
from .. import BaseTestCase


class TestViewStudent(BaseTestCase):

    def test_index(self):
        response = self.client.get('/student/')
        assert b'Welcome to your new blueprint!' in response.data
