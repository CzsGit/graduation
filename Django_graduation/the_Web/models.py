from django.db import models
from mongoengine import *
# from mongoengine import connect
# connect('HousePrice', host='127.0.0.1', port=27017)

# Create your models here.
class old_house_price(Document):
    meta = {'collection': 'old_house_price'}
    price = StringField()
    time = StringField()


class new_house_price(Document):
    meta = {'collection': 'new_house_price'}
    price = StringField()
    time = StringField()

class rent_house_price(Document):
    meta = {'collection': 'rent_house_price'}
    price = StringField()
    time = StringField()

# for i in rent_house_price.objects(time='2017-05-12'):
#     print(i.price)
#ArtiInfo.objects.average(time='2017-05-12')
# all_time=[]
# change_time=''
# for i in rent_house_price.objects():
#     if change_time==i.time:
#         continue
#     else:
#         all_time.append(i.time.split('-',1)[1])
#         change_time=i.time
#
#
#     print(all_time)