from django.shortcuts import render
from django.http import HttpResponse
import json 
import urllib.request
import numpy as np

# Create your views here.

def index(request):

    source = urllib.request.urlopen('https://api.covid19api.com/summary').read()
    # source = open("C:\\Users\\sidzo\\Desktop\\d.json",'r') 
    variable = request.POST.get('variable')
    print(variable)

    
    l=[]
    h={}
    
        # converting JSON data to a dictionary 
    list_of_data = json.loads(source)
    # print(type(list_of_data))
    d_count=[]
    aname=[]
    cname=[]
    # print(list_of_data.keys())
    for i in range(len(list_of_data['Countries'])):
        d_count.append(list_of_data['Countries'][i]['TotalDeaths'])
        aname.append(list_of_data['Countries'][i]['TotalRecovered'])
        cname.append(list_of_data['Countries'][i]['CountryCode'])
    for i in range(len(list_of_data['Countries'])):
        a = [list_of_data['Countries'][i]['CountryCode'],list_of_data['Countries'][i]['TotalConfirmed']]
        l.append(a)
    l.insert(0,["Country","Cases"])
 
    data = { 
            "Globe": str('Global'),
            "newconfirmed": str(list_of_data['Global']['NewConfirmed']),
            "totalconfirmed": str("{:,}".format(list_of_data['Global']['TotalConfirmed'])), 
            "Newdeaths": str(list_of_data['Global']['NewDeaths']), 
            "Totaldeaths": str("{:,}".format(list_of_data['Global']['TotalDeaths'])), 
            "Newrecovered": str(list_of_data['Global']['NewRecovered']),
            "Totalrecovered": str("{:,}".format(list_of_data['Global']['TotalRecovered'])),
            "dataForheatMap":l,
            "d":l,
            "d_count":d_count[80:90],
            "aname":aname[80:90],
            "cname":cname[80:90],
            "min12":np.mean(d_count),
            "max12":np.mean(aname),
            "perD":str((list_of_data['Global']['TotalDeaths']/list_of_data['Global']['TotalConfirmed'])*100),
            "perR":str((list_of_data['Global']['TotalRecovered']/list_of_data['Global']['TotalConfirmed'])*100),
            "totalactive":str("{:,}".format(list_of_data['Global']['TotalConfirmed']-list_of_data['Global']['TotalDeaths']-list_of_data['Global']['TotalRecovered'])),
            "perA":str((list_of_data['Global']['TotalConfirmed']-list_of_data['Global']['TotalDeaths']-list_of_data['Global']['TotalRecovered'])/list_of_data['Global']['TotalConfirmed']*100),
           
            # "image": str(list_of_data['weather'][0]['icon']),

    } 
    return render(request, "covid19/world.html", data)

def index1(request):

    # source = urllib.request.urlopen('https://api.covid19api.com/summary').read() 
    source = open("C:\\Users\\sidzo\\Desktop\\d.json",'r')    
        # converting JSON data to a dictionary 
    list_of_data = json.loads(source.read())
    print(type(list_of_data))
    d_count=[]
    d={}
    aname=[]
    print(list_of_data.keys())
    for i in range(len(list_of_data['Countries'])):
        d_count.append(list_of_data['Countries'][i]['TotalDeaths'])
        aname.append(list_of_data['Countries'][i]['CountryCode'])
    for i in range(len(list_of_data['Countries'])):
        d[list_of_data['Countries'][i]['Country']] = list_of_data['Countries'][i]['TotalDeaths']
    ds = {k: v for k, v in sorted(d.items(), reverse=True,key=lambda item: item[1])}
    print(ds)
        # data for variable list_of_data 
    data = { 
            "Globe": str('Global'),
            "newconfirmed": str(list_of_data['Global']['NewConfirmed']),
            "totalconfirmed": str("{:,}".format(list_of_data['Global']['TotalConfirmed'])), 
            "Newdeaths": str(list_of_data['Global']['NewDeaths']), 
            "Totaldeaths": str(list_of_data['Global']['TotalDeaths']), 
            "Newrecovered": str(list_of_data['Global']['NewRecovered']),
            "Totalrecovered": str(list_of_data['Global']['TotalRecovered']),
            "d_count": list(ds.values())[0:10],
            "aname":list(ds.keys())[0:10],
            
            # "image": str(list_of_data['weather'][0]['icon']),

    } 
    print(data) 
    return render(request, "covid19/graph.html", data) 
