from initialize_scraper.engine import engine
from Scrape.scraper import listingsScrape
driver = engine(url = 'https://shopee.co.id/Sepatu-Slip-On-Pria-Virale-Sepatu-Selop-Pria-Casual-BG-01-i.12345956.2429787872')
scraping = listingsScrape(resp=driver)
test_list = scraping.selenium_scrape()
#print(test_list)

#test_df = scraping.to_df(test_list)
#test_df
