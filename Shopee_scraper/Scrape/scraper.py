from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

class listingsScrape:
    LISTING_INFORMATION = {'kategori' : {'tag' : 'a', 'class' : '_3YDLCj', 'get' : 'style'},
                           'nama_produk' : {'tag' : 'div', 'class' : 'attM6y'},
                           'deskripsi_produk' : {'tag' : 'div', 'class' : '_3yZnxJ'},
                           'nama_variasi1' : {'tag' : 'label', 'class' : '_2IW_UG', 'order' : 0},
                           'varian_variasi1' : {'tag' : 'div', 'class' : 'flex items-center _2oeDUI', 'order' : 0},
                           'foto_variasi1' : {'tag' : 'div', 'class' : '_3Q7kBy _2GchKS', 'get' : 'style'},
                           'nama_variasi2' : {'tag' : 'div', 'class' : '_2IW_UG', 'order' : 1},
                           'varian_variasi2' : {'tag' : 'div', 'class' : 'flex items-center _2oeDUI', 'order' : 1},
                           'harga' : {'tag' : 'div', 'class' : '_3e_UQT'},
                           'stok' : {'tag' : 'div', 'class' : 'flex items-center _90fTvx'}}

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver

    def element_scrape(self):
        '''
        Test for single product
        '''
        soup = BeautifulSoup(requests.get(self.url).content, 'html_parser')
        product_detail = list()

        for info in listingsScrape.LISTING_INFORMATION:
            try:
                if 'class' in listingsScrape[info]:
                    element = soup.find_all(listingsScrape.LISTING_INFORMATION[info], listingsScrape.LISTING_INFORMATION[info]['class'])
                else:
                    element = soup.find_all(listingsScrape.LISTING_INFORMATION[info]['tag'])

                if len(element) > 1:
                    for sub in element:
                        sub_element =




        # Order
        orders = listingsScrape.LISTING_INFORMATION[info].get('order', 0)
        elements = element[orders]



