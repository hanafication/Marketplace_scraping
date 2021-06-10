from selenium import webdriver

def engine(url):
    ''''
    Initializing webdriver to get url
    '''
# Setting
    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument('--headless')
#    chrome_options.add_argument('--no-sandbox')
#    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('detach', True)
    # PC
    #driver = webdriver.Chrome('C:/Users/Rahadian/Documents/Python Scripts/chromedriver_win32/chromedriver.exe',
    #                          chrome_options=chrome_options)
    # Using laptop
    driver = webdriver.Chrome('/home/expiatio/Documents/chromedriver',
                              chrome_options=chrome_options)

    driver.get(url=url)
    return driver
