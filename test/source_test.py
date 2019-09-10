from .app import models
import unittest as unit

class TestArticle(unit.TestCase):
    def setUp(self):
        self.new_source = models.NewsSource('abc-news','ABC NEWS','https/abc-news&q=boom','Your up to date news','general','en','us')

    def test_init(self):
        self.assertTrue(isinstance(self.new_source,models.NewsSource))
