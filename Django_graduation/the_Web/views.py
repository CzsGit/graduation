from django.shortcuts import render
from the_Web.models import new_house_price
from the_Web.models import old_house_price
from the_Web.models import rent_house_price
# Create your views here.

def index(request):
    rent_price = []
    old_price=[]
    new_price=[]
    rent_avg_price = []
    old_avg_price=[]
    new_avg_price=[]
    all_time=[]
    num_rent=0
    num_new=0
    num_old=0
    change_time = ''
    month=[]
    day=[]

    for i in rent_house_price.objects():
        if change_time == i.time:
            continue
        else:
            all_time.append(i.time)
            month.append(int(i.time.split('-',2)[1]))
            day.append(int(i.time.split('-',2)[2]))
            change_time = i.time
#租房
    while num_rent < len(all_time):
        for i in rent_house_price.objects(time=all_time[num_rent]):
            try:
                rent_price.append(int(i.price))
            except:
                pass
        rent_avg_price.append(int(sum(rent_price) / len(rent_price)))
        num_rent=num_rent+1
#二手房
    while num_old < len(all_time):
        for i in old_house_price.objects(time=all_time[num_old]):
            try:
                old_price.append(int(i.price))
            except:
                pass
        old_avg_price.append(int(sum(old_price) / len(old_price)))
        num_old=num_old+1

#新房 len(all_time)
    while num_new < len(all_time):
        for i in new_house_price.objects(time=all_time[num_new]):
            try:
                new_price.append(int(i.price))
            except:
                pass
        new_avg_price.append(int(sum(new_price) / len(new_price)))
        num_new=num_new+1
    #print(rent_avg_price[1])
    context = {
        'month':month,
        'day':day,
        'rent_avg_price':rent_avg_price,
        'old_avg_price':old_avg_price,
        'new_avg_price':new_avg_price
    }
    return render(request, 'index.html',context)