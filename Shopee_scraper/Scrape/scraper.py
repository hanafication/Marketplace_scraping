from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

class listingsScrape:
    main_information = {'kategori' : {'tag' : 'a', 'class' : '._3YDLCj', 'get' : 'href', 'order' : 2},
                        'nama_produk' : {'tag' : 'div', 'class' : '.attM6y'},
                        'deskripsi_produk' : {'tag' : 'div', 'class' : '._3yZnxJ'}}

    varian_information = {'nama_variasi1' : {'tag' : 'label', 'class' : '._2IW_UG', 'order' : 0},
                           'varian_variasi1' : {'tag' : 'div', 'class' : '_2oeDUI', 'order' : 0},
                           'foto_variasi1' : {'tag' : 'div', 'class' : '._3Q7kBy._2GchKS', 'get' : 'style', 'order' : 0},
                           'nama_variasi2' : {'tag' : 'div', 'class' : '_2IW_UG', 'order' : 1},
                           'varian_variasi2' : {'tag' : 'div', 'class' : 'flex.items.center._2oeDUI', 'order' : 1},
                           'harga' : {'tag' : 'div', 'class' : '._3e_UQT'},
                           'stok' : {'tag' : 'div', 'class' : '.flex.items.center._90fTvx'}}

    def __init__(self,  resp):
        #self.url = url
        self.resp = resp

    def element_scrape(self):
        '''
        Test for single product
        '''
        soup = BeautifulSoup(self.resp, 'html.parser')
        #soup = soup.prettify()
        print(soup)
        #product_detail = list()
        product_dict = dict()
        for info in listingsScrape.LISTING_INFORMATION:
            try:
                if 'class' in listingsScrape.LISTING_INFORMATION[info]:
                    element = soup.find_all(listingsScrape.LISTING_INFORMATION[info], listingsScrape.LISTING_INFORMATION[info]['class'])
                    print(element)
                else:
                    element = soup.find_all(listingsScrape.LISTING_INFORMATION[info]['tag'])
                    print(element)
                # Order
                orders = listingsScrape.LISTING_INFORMATION[info].get('order', 0)
                elements = element[orders]

                # Values
                if 'get' in listingsScrape.LISTING_INFORMATION[info]:
                    output = elements.get_attribute(listingsScrape.LISTING_INFORMATION[info]['get'])
                    print(output)
                else:
                    output = elements.get_text()
                    print(output)
                product_dict[info] = output

            except:
                print('Error in list : ' + info)
                product_dict[info] = 'empty'
            #product_detail.append(product_dict)

        return product_dict

    def selenium_scrape(self):
        '''
        Using selenium instead of bs4
        '''
        driver = self.resp
        #driver.get(self.url)
        table = listingsScrape.main_information
        #time.sleep(10)
        for detail in table:
            orders = table[detail].get('order', 0)
            if 'class' and 'get' in table[detail]:
                explore = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, table[detail]['class'])))
                print(explore[orders].get_attribute(table[detail]['get']))

                #print(explore[orders].get_attribute(table[detail]['get']))
            else:
                #'class' in table:
                try:
                    explore = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, table[detail]['class'])))
                    print(explore[orders].text)
                except:
                    print('error 2')
                #print(explore[orders].text)












    def to_df(self, input_list):
        dataframe = pd.DataFrame.from_records(input_list)
        return dataframe












