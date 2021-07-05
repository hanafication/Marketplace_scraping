import os
from Shopee_scraper.initialize_scraper import engine
from multiprocessing import Pool
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import time, datetime
import pandas as pd

def get_urls_by_category(resp):
    ''''
    Getting all urls by category
    '''
    driver = resp

    # Locating all url to be processed
    try:
        scrape = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.row.shopee-search-item-result__items')))
    except:
        scrape = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1-gCzV')))

    sub_class = scrape.find_elements_by_xpath('//a[@data-sqe="link"]')
    # Adding url into list of urls
    urls = list()
    for i in sub_class:
        url = r'{}'.format(i.get_attribute('href'))
        urls.append(url)

    return urls

def shopee_scrape(total_product, resp):
    '''
    iterating base on total product
    '''
    target_product = list()
    driver = resp
    while True:
        urls = get_urls_by_category(resp = driver)
        for i in urls:
            target_product.append(i)

        if len(target_product) < total_product:
            scrape = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.shopee-icon-button.shopee-icon-button--right')))
            scrape.click()
        else:
            break

    return target_product[:total_product]


class listingsScrape():
    # Unused element: 'kategori' : {'tag' : 'a', 'class' : '._3YDLCj', 'get' : 'href', 'order' : 2}

    main_information = {'nama_produk' : {'tag' : 'div', 'class' : '.attM6y'},
                        'deskripsi_produk' : {'tag' : 'div', 'class' : '._3yZnxJ'},
                        'foto_sampul': {'tag' : 'div', 'class' : '._3Q7kBy._2GchKS', 'get' : 'style', 'order' : 0}}

    varian_name = {'nama_variasi1' : {'tag' : 'label', 'class' : '._2IW_UG', 'order' : 0},
                   'nama_variasi2' : {'tag' : 'div', 'class' : '._2IW_UG', 'order' : -2}}

    varian_information = {'varian_variasi1' : {'tag' : 'div', 'class' : '._2oeDUI', 'order' : 0},
                          'foto_variasi1' : {'tag' : 'div', 'class' : '._3Q7kBy._2GchKS', 'get' : 'style', 'order' : 0},
                          'varian_variasi2' : {'tag' : 'div', 'class' : 'flex.items.center._2oeDUI', 'order' : 1},
                          'harga' : {'tag' : 'div', 'class' : '._3e_UQT'},
                          'stok' : {'tag' : 'div', 'class' : '.flex.items-center._90fTvx'}}



    def __init__(self, resp):
        self.resp = resp

    def main_information_scrape(self):
        '''
        Using selenium instead of bs4
        '''
        driver = self.resp

        table = listingsScrape.main_information
        main_dict = dict()

        for detail in table:
            orders = table[detail].get('order', 0)
            if 'class' and 'get' in table[detail]:
                try:
                    explore = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, table[detail]['class'])))
                    main_dict[detail] = explore[orders].get_attribute(table[detail]['get'])
                except:
                    main_dict[detail] = ''
                #print(explore[orders].get_attribute(table[detail]['get']))
            else:
                #'class' in table:
                try:
                    explore = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, table[detail]['class'])))
                    main_dict[detail] = explore[orders].text
                except:
                    main_dict[detail] = ''

        return main_dict

    def varian_scrape(self):

        driver = self.resp
        table = listingsScrape.varian_name
        varian = WebDriverWait(driver, 20).until((EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.flex._3AHLrn._2XdAdB'))))
        varian_dict = dict()
        vars = varian[0].find_elements_by_css_selector('._2IW_UG')

        # Loop varian name
        for detail in table:
            if len(vars)  > 2:
                if detail == 'nama_variasi1':
                    varian_dict[detail] = vars[0].text
                else:
                    varian_dict[detail] = vars[1].text
            elif len(vars) == 2:
                if detail == 'nama_variasi1':
                    varian_dict[detail] = vars[0].text
                else:
                    varian_dict[detail] = ''
            else:
                varian_dict[detail] = ''


        # Loop for varian values
        subvar_list = list()
        try:
            main_vars = varian[0].find_elements_by_css_selector('.flex .items-center ._2oeDUI')
            list_var1 = main_vars[0].find_elements_by_css_selector('*')
        except:
            dict_var1 = dict()
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
            foto_varian = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
                (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS'))))
            harga = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '._3e_UQT')))
            stok_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.flex.items-center._90fTvx')))
            stok = stok_element[0].find_element_by_css_selector('.flex.items-center')

            dict_var1['varian_variasi1'] = ''
            dict_var1['foto_varian1'] = foto_varian.get_attribute('style')
            dict_var1['varian_variasi2'] = ''
            dict_var1['harga'] = harga[0].text
            dict_var1['stok'] = stok.text
            # Append dict to list
            subvar_list.append(dict_var1)

            #print(len(subvar_list))
            return subvar_list, varian_dict

        for var1 in list_var1:
            if varian_dict['nama_variasi1'] != '' and varian_dict['nama_variasi2'] != '':
                sub_vars = varian[0].find_elements_by_css_selector('.flex .items-center ._2oeDUI')
                list_var2 = sub_vars[1].find_elements_by_css_selector('*')
                if var1.get_attribute('class') == 'product-variation':
                    for var2 in list_var2:
                        dict_var1 = dict()
                        dict_var1['varian_variasi1'] = var1.text
                        var1.click()

                        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
#                        foto_varian = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
#                            (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS'))))
                        harga = WebDriverWait(driver, 20).until(
                            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '._3e_UQT')))
                        stok_element = WebDriverWait(driver, 20).until(
                            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.flex.items-center._90fTvx')))
                        stok = stok_element[0].find_element_by_css_selector('.flex.items-center')

                        dict_var1['foto_varian1'] = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
                    (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS')))).get_attribute('style')
                        if var2.get_attribute('class') == 'product-variation':
                            dict_var1['varian_variasi2'] = var2.text
                            var2.click()
                            dict_var1['harga'] = harga[0].text
                            dict_var1['stok'] = stok.text
                            # Unclick var2
                            unselect_var2 = sub_vars[1].find_elements_by_css_selector(
                                '.product-variation.product-variation--selected')
                            unselect_var2[0].click()
                        else:
                            dict_var1['varian_variasi2'] = var2.text
                            dict_var1['harga'] = harga[0].text
                            dict_var1['stok'] = 0
                        # Append dict to list
                        subvar_list.append(dict_var1)

                        # Unclick var1
                        unselect_var1 = main_vars[0].find_elements_by_css_selector('.product-variation.product-variation--selected')
                        unselect_var1[0].click()
                else:
                    dict_var1 = dict()
                    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
                    driver.implicitly_wait(3)
#                    foto_varian = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
#                        (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS'))))
                    harga = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '._3e_UQT')))
                    stok_element = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '.flex.items-center._90fTvx')))
                    stok = stok_element[0].find_element_by_css_selector('.flex.items-center')

                    dict_var1['varian_variasi1'] = var1.text
                    dict_var1['foto_varian1'] = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
                    (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS')))).get_attribute('style')
                    dict_var1['varian_variasi2'] = ''
                    dict_var1['harga'] = harga.text
                    dict_var1['stok'] = 0
                    # Append dict to list
                    subvar_list.append(dict_var1)
            elif varian_dict['nama_variasi1'] != '' and varian_dict['nama_variasi2'] == '':
                dict_var1 = dict()
                ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
                #foto_varian =
                harga = WebDriverWait(driver, 20).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '._3e_UQT')))
                stok_element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.flex.items-center._90fTvx')))
                stok = stok_element[0].find_element_by_css_selector('.flex.items-center')

                dict_var1['varian_variasi1'] = var1.text
                var1.click()
                dict_var1['foto_varian1'] = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
                    (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS')))).get_attribute('style')
                dict_var1['varian_variasi2'] = ''
                dict_var1['harga'] = harga[0].text
                dict_var1['stok'] = stok.text
                # Append
                subvar_list.append(dict_var1)
                # Unclick var1
                try:
                    unselect_var1 = main_vars[0].find_elements_by_css_selector(
                    '.product-variation.product-variation--selected')
                    unselect_var1[0].click()
                except:
                    continue
            else:
                dict_var1 = dict()
                ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
#                foto_varian = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
#                    (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS'))))
                harga = WebDriverWait(driver, 20).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '._3e_UQT')))
                stok_element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.flex.items-center._90fTvx')))
                stok = stok_element[0].find_element_by_css_selector('.flex.items-center')

                dict_var1['varian_variasi1'] = ''
                dict_var1['foto_varian1'] = WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(
                    (EC.presence_of_element_located((By.CSS_SELECTOR, '._3Q7kBy._2GchKS')))).get_attribute('style')
                dict_var1['varian_variasi2'] = ''
                dict_var1['harga'] = harga[0].text
                dict_var1['stok'] = stok.text
                # Append dict to list
                subvar_list.append(dict_var1)


        #print(len(subvar_list))
        return subvar_list, varian_dict

    def combine(self):
        ''''
        Combining all list
        '''
        product_list = list()
        subvar_list, varian_dict = self.varian_scrape()
#        print(subvar_list)
        main_dict = self.main_information_scrape()
#        print(main_dict)

        single_product_list = list()
        for i in subvar_list:
            comb = {**main_dict, **varian_dict, **i}
            single_product_list.append(comb)

        return single_product_list


def to_pandas_csv(urls):
    dataframe = pd.DataFrame()
    driver = engine()
    driver.get(urls)
    start_time = time.time()
    for i in listingsScrape(resp = driver).combine():
        df = pd.DataFrame.from_dict([i])
        dataframe = dataframe.append(df, ignore_index=True)
    driver.close()
    print('Selesai Memproses Produk selama {} detik.'.format((time.time() - start_time)))
    ts = time.time()
    return dataframe

 #       return dataframe.to_csv('test.csv', index = False, sep = ';')

def multiprocess(urls):
    n_pool = os.cpu_count() // 2

    with Pool(n_pool) as pool:
        result = pool.map(to_pandas_csv, urls)
        pool.close()
        pool.join()
    return result

def pandas_csv(dfs):
    df = pd.concat(dfs, ignore_index = True)
    path = 'C:/Users/Rahadian/PycharmProjects/Marketplace_scraping/Shopee_scraper/scrapped_dataset'
    timenow = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S_%f')
    return df.to_csv(os.path.join(path, timenow + '-' + '.csv'), index=False, sep=';')











