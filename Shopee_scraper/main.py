from initialize_scraper.engine import engine
from Scrape.scraper import listingsScrape
driver = engine(url = 'https://shopee.co.id/Sepatu-WAKAI-kasual-slip-on-pria-wanita-GRADE-ORI-i.5518748.1830499251')
scraping = listingsScrape(resp=driver)
test_list = scraping.varian_scrape()
#print(test_list)

#test_df = scraping.to_df(test_list)
#test_df
