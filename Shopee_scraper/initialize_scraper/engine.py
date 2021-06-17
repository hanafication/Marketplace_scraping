from selenium import webdriver

def engine(url):
    ''''
    Initializing webdriver to get url
    '''
# Setting
#    chrome_options = webdriver.ChromeOptions(
#    chrome_options.add_argument('--headless')
#    chrome_options.add_argument('--no-sandbox')
#    chrome_options.add_argument('--disable-dev-shm-usage')
#   chrome_options.add_experimental_option('detach', True)
    # PC
    #headers = {
    #    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #    'cookie': '_gcl_au=1.1.961206468.1594951946; _med=refer; _fbp=fb.2.1594951949275.1940955365; SPC_IA=-1; SPC_F=y1evilme0ImdfEmNWEc08bul3d8toc33; REC_T_ID=fab983c8-c7d2-11ea-a977-ccbbfe23657a; SPC_SI=uv1y64sfvhx3w6dir503ixw89ve2ixt4; _gid=GA1.3.413262278.1594951963; SPC_U=286107140; SPC_EC=GwoQmu7TiknULYXKODlEi5vEgjawyqNcpIWQjoxjQEW2yJ3H/jsB1Pw9iCgGRGYFfAkT/Ej00ruDcf7DHjg4eNGWbCG+0uXcKb7bqLDcn+A2hEl1XMtj1FCCIES7k17xoVdYW1tGg0qaXnSz0/Uf3iaEIIk7Q9rqsnT+COWVg8Y=; csrftoken=5MdKKnZH5boQXpaAza1kOVLRFBjx1eij; welcomePkgShown=true; _ga=GA1.1.1693450966.1594951955; _dc_gtm_UA-61904553-8=1; REC_MD_30_2002454304=1595153616; _ga_SW6D8G0HXK=GS1.1.1595152099.14.1.1595153019.0; REC_MD_41_1000044=1595153318_0_50_0_49; SPC_R_T_ID="Am9bCo3cc3Jno2mV5RDkLJIVsbIWEDTC6ezJknXdVVRfxlQRoGDcya57fIQsioFKZWhP8/9PAGhldR0L/efzcrKONe62GAzvsztkZHfAl0I="; SPC_T_IV="IETR5YkWloW3OcKf80c6RQ=="; SPC_R_T_IV="IETR5YkWloW3OcKf80c6RQ=="; SPC_T_ID="Am9bCo3cc3Jno2mV5RDkLJIVsbIWEDTC6ezJknXdVVRfxlQRoGDcya57fIQsioFKZWhP8/9PAGhldR0L/efzcrKONe62GAzvsztkZHfAl0I="'
    #}
    #driver = webdriver.Chrome(executable_path = 'C:/Users/Rahadian/Documents/Python Scripts/chromedriver_win32/chromedriver.exe',
    #                           chrome_options = chrome_options)
    try:
        driver = webdriver.Firefox(executable_path='C:/Users/Rahadian/Documents/Python Scripts/geckodriver-v0.29.1-win64/geckodriver.exe')
        driver.get(url=url)
        return driver
    except:

    # Using laptop
    #driver = webdriver.Chrome('/home/expiatio/Documents/chromedriver',
    #                          chrome_options=chrome_options)
        driver = webdriver.Firefox(executable_path='/home/expiatio/Documents/geckodriver')
        driver.get(url=url)
        return driver
    #response = driver.page_source
    #driver.implicitly_wait(30)
    #print(response)



