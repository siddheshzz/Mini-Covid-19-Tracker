import json
from collections import OrderedDict
import urllib.request
# Create your views here.

def index():

    # source = urllib.request.urlopen('https://api.covid19api.com/summary').read() 
    source = open("C:\\Users\\sidzo\\Desktop\\d.json",'r')     
        # converting JSON data to a dictionary 
    list_of_data = json.loads(source.read())
    # print(list_of_data.keys())
    country_list={}
    l=[]
    d ={}
    for i in range(len(list_of_data['Countries'])):
        a = {'id':list_of_data['Countries'][i]['CountryCode'],'value':list_of_data['Countries'][i]['TotalDeaths']}
        l.append(a)
    print(l)        
        # data for variable list_of_data 
    # for i in range(len(list_of_data['Countries'])):
    #     d[list_of_data['Countries'][i]['Country']] = list_of_data['Countries'][i]['TotalDeaths']
    # # print(d)
    # ds = {k: v for k, v in sorted(d.items(), reverse=True,key=lambda item: item[1])}
    # print(ds)
    data = { 
            "Globe": str('Global'),
            "newconfirmed": str(list_of_data['Global']['NewConfirmed']),
            "totalconfirmed": str(list_of_data['Global']['TotalConfirmed']), 
            "Newdeaths": str(list_of_data['Global']['NewDeaths']), 
            "Totaldeaths": str(list_of_data['Global']['TotalDeaths']), 
            "Newrecovered": str(list_of_data['Global']['NewRecovered']),
            "Totalrecovered": str(list_of_data['Global']['TotalRecovered']),
            # "image": str(list_of_data['weather'][0]['icon']),

    } 
    print(data) 
    return "Hellow there "
a = index()
print(a)