from initialize_scraper.engine import engine
from Scrape.scraper import shopee_scrape, multiprocess
import time

if __name__ == '__main__':
    total_product = int(input('Jumlah produk yang ingin discrape: '))
    start_time = time.time()
    driver = engine()
    driver.get('https://shopee.co.id/search?keyword=tas')
    tests = shopee_scrape(total_product=total_product, resp=driver)
    driver.close()
    print(tests)
    multiprocess(tests)
    print('Selesai Memproses Semua URL selama {} detik.'.format((time.time() - start_time)))
    time.sleep(1.5)





#result = scraping.combine()

#test_df = scraping.to_df(test_list)
#test_df
