from initialize_scraper.engine import engine
from Scrape.scraper import listingsScrape
import pandas as pd
driver = engine(url = 'https://shopee.co.id/Sepatu-Safety-Armour-Bisa-COD-Termurah-Original-i.215025773.4946811401')
scraping = listingsScrape(resp=driver)
#result = scraping.combine()
scraping.to_pandas_csv()
#test_df = scraping.to_df(test_list)
#test_df
