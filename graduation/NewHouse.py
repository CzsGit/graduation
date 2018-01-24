from bs4 import BeautifulSoup
import requests
import pymongo
import time

client = pymongo.MongoClient('localhost' , 27017)
HousePrice = client['HousePrice']
new_house_price = HousePrice['new_house_price']

def get_all_links_from():
    for num in range(1, 50):
        get_item_info(num)

def get_item_info(pages):

    url_link = 'http://langfang.ganji.com/fang12/o{}/'.format(str(pages))
    i=5
    for a in range(40):
        try:
            wb_data = requests.get(url_link)
            soup = BeautifulSoup(wb_data.text, 'lxml')
            price = soup.select('span.price-unit')[i].text.split('元')[0]
            date=time.strftime('%Y-%m-%d', time.localtime(time.time()))

            new_house_price.insert_one({'price': price,'time':date})
            i=i+1
            print(price+'元/平米')
        except:
            pass


if __name__=='__main__':
    get_all_links_from()