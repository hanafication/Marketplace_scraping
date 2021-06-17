from initialize_scraper.engine import engine
from Scrape.scraper import listingsScrape,get_urls_by_category, shopee_scrape, multiprocess_pool
import pandas as pd
total_product = int(input('Jumlah produk yang ingin discrape: '))
driver = engine(url = 'https://shopee.co.id/Sepatu-Pria-cat.35')
tests = shopee_scrape(total_product=total_product, resp=driver)
test = multiprocess_pool(driver = driver, pools=tests)
print(test)



#result = scraping.combine()

#test_df = scraping.to_df(test_list)
#test_df
