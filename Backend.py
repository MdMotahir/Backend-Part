import json,requests,datetime

data_given = requests.get("https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences")

data=data_given.json()

paid_data=data['paid']


def date_converter(date):
    l1=['Jan,','Feb,','Mar,','Apr,','May,','Jun,','Jul,','Aug,','Sept,','Oct,','Nov,','Dec,']
    l2=['January,', 'February,', 'March,', 'April,', 'May,', 'June,', 'July,','August,', 'September,', 'October,', 'November,', 'December,']
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    dates=date.split()
    final_date=[]
    for i in dates:
        if i in l1:
            d=l1.index(i)
            final_date.append(d+1)
        else:
            if i in l2:
                d=l2.index(i)
                final_date.append(d+1)
            else:
                final_date.append(int(i))
    final_dates=datetime.datetime(int(final_date[-1]), int(final_date[1]),int(final_date[0]))
    date1=final_dates.strftime(f"%B {ordinal(int(final_date[0]))} %Y")
    return date1

contents=[]
for i in paid_data:
    # for k,v in i.items():         #its opional
    #     if not i[k]:
    #         i[k]=None
    content=f"{i['confName']}, {date_converter(i['confStartDate'])},{i['city']}, {i['state']}, {i['country']}, {i['entryType']}. {i['confUrl']}"
    contents.append(content)

# print(contents)
# for i in contents:
#     print(i)

exact_duplicate=set([x for x in contents if contents.count(x) > 1])
# print(exact_duplicate)


ids=[]
for i in paid_data:
    ids.append(i['confName'])       #here we do this according to name but if anyone want then he also use id, date, url etc

sementic_duplicates=set([x for x in ids if ids.count(x)>1])
print(sementic_duplicates)