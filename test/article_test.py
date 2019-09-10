from .app import models
import unittest as unit

class TestArticle(unit.TestCase):
    def setUp(self):
        self.new_article = models.NewsArticle('abc-news','Boom','This is a boom','https/abc-news&q=boom','https//lsdhaljh.png','12-02-2019','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    def test_init(self):
        self.assertTrue(isinstance(self.new_article,models.NewsArticle))
