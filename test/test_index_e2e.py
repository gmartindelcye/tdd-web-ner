import unittest
from selenium import webdriver

class E2ETests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:5000')
        
    def tearDown(self):
        self.driver.quit()
        
        
    def test_browser_contain_app_name(self):
        self.assertIn('Named Entity', self.driver.title)