from django.test import LiveServerTestCase
from selenium import webdriver
from ...forms import LocationEntryForm

path_to_chromedriver = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_chromedriver)

class FrontendTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = driver

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_selects(self):
        self.selenium.get(self.live_server_url + '')
        main_select = self.selenium.find_elements_by_tag_name('select')
        self.assertEqual(len(main_select), 2)

    def test_button(self):
        self.selenium.get(self.live_server_url + '')
        main_button = self.selenium.find_elements_by_tag_name('button')
        self.assertEqual(len(main_button), 1)

    def test_input(self):
        self.selenium.get(self.live_server_url + '')
        main_input = self.selenium.find_elements_by_tag_name('input')
        self.assertEqual(len(main_input), 1)

    def test_analysis_selects(self):
        self.selenium.get(self.live_server_url + '/analysis/')
        analysis_select = self.selenium.find_elements_by_tag_name('select')
        self.assertEqual(len(analysis_select), 2)

    def test_analysis_button(self):
        self.selenium.get(self.live_server_url + '/analysis/')
        analisis_button = self.selenium.find_elements_by_tag_name('button')
        self.assertEqual(len(analisis_button), 1)

    def test_analysis_input(self):
        self.selenium.get(self.live_server_url + '/analysis/')
        analisis_input = self.selenium.find_elements_by_tag_name('input')
        self.assertEqual(len(analisis_input), 2)

    def test_classification_button(self):
        self.selenium.get(self.live_server_url + '/classification/')
        classification_button = self.selenium.find_elements_by_tag_name('button')
        self.assertEqual(len(classification_button), 1)

    def testdata_input(self):
        self.selenium.get(self.live_server_url + '/data')
        main_input = self.selenium.find_elements_by_tag_name('input')
        self.assertEqual(len(main_input), 5)

    def test_data_selects(self):
        self.selenium.get(self.live_server_url + '/data')
        data_select = self.selenium.find_elements_by_tag_name('select')
        self.assertEqual(len(data_select), 3)

    def test_data_button(self):
        self.selenium.get(self.live_server_url + '/data')
        data_button = self.selenium.find_elements_by_tag_name('button')
        self.assertEqual(len(data_button), 2)

