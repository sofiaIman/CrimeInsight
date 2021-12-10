from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import matplotlib
matplotlib.use('Agg')
import numpy as np
from django.views.generic import TemplateView
import pandas as pd
import os
import seaborn as sns
from app.models import sf_crimes
import plotly
import plotly.offline as opy
import plotly.graph_objs as go
import pickle


# Create your views here.

from django import forms
from django.utils import timezone
from app.forms import caw

from app.forms import sf




def sss(request):
 
    if request.method == "POST":
        form = sf(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            day = request.POST.get('Day')
            place = request.POST.get('location')
            filename = 'prediction.sav'
            module_dir = os.path.dirname(__file__)
            file_path = os.path.join(module_dir, filename)
            model = pickle.load(open(file_path, 'rb'))
            p = [0] * 17
            if day == 'Friday':
              p[0]= 1
            if day == 'Monday':
              p[1]= 1
            if day == 'Saturday':
              p[2]= 1
            if day == 'Sunday':
              p[3]= 1
            if day == 'Thursday':
              p[4]= 1
            if day == 'Tuesday':
              p[5]= 1
            if day == 'Wednesday':
              p[6]= 1
            if place == 'BAYVIEW':
              p[7] = 1
            if place == 'CENTRAL':
              p[8] = 1
            if place == 'INGLESIDE':
              p[9] = 1
            if place == 'MISSION':
              p[10] = 1
            if place == 'NORTHERN':
              p[11] = 1
            if place == 'PARK':
              p[12] = 1
            if place == 'RICHMOND':
              p[13] = 1
            if place == 'SOUTHERN':
              p[14] = 1
            if place == 'TARAVAL':
              p[15] = 1
            if place == 'TENDERLOIN':
              p[16] = 1
            array = model.predict_proba(p)
            crimes = ['ARSON', 'ASSAULT', 'BAD CHECKS', 'BRIBERY', 'BURGLARY',
            'DISORDERLY CONDUCT', 'DRIVING UNDER THE INFLUENCE',
            'DRUG/NARCOTIC', 'DRUNKENNESS', 'EMBEZZLEMENT', 'EXTORTION',
            'FAMILY OFFENSES', 'FORGERY/COUNTERFEITING', 'FRAUD', 'GAMBLING',
            'KIDNAPPING', 'LARCENY/THEFT', 'LIQUOR LAWS', 'LOITERING',
            'MISSING PERSON', 'NON-CRIMINAL', 'OTHER OFFENSES',
            'PORNOGRAPHY/OBSCENE MAT', 'PROSTITUTION', 'RECOVERED VEHICLE',
            'ROBBERY', 'RUNAWAY', 'SECONDARY CODES', 'SEX OFFENSES FORCIBLE',
            'SEX OFFENSES NON FORCIBLE', 'STOLEN PROPERTY', 'SUICIDE',
            'SUSPICIOUS OCC', 'TREA', 'TRESPASS', 'VANDALISM', 'VEHICLE THEFT',
            'WARRANTS', 'WEAPON LAWS']


            thevalues = {
            'day': day,
            'location': place,
            'array':array,
            'crimes':crimes,
            'crimes00':crimes[0],
            'crimes01':crimes[1],
            'crimes02':crimes[2],
            'crimes03':crimes[3],
            'crimes04':crimes[4],
            'crimes05':crimes[5],
            'crimes06':crimes[6],
            'crimes07':crimes[7],
            'crimes08':crimes[8],
            'crimes09':crimes[9],
            'crimes10':crimes[10],
            'crimes11':crimes[11],
            'crimes12':crimes[12],
            'crimes13':crimes[13],
            'crimes14':crimes[14],
            'crimes15':crimes[15],
            'crimes16':crimes[16],
            'crimes17':crimes[17],
            'crimes18':crimes[18],
            'crimes19':crimes[19],
            'crimes20':crimes[20],
            'crimes21':crimes[21],
            'crimes22':crimes[22],
            'crimes23':crimes[23],
            'crimes24':crimes[24],
            'crimes25':crimes[25],
            'crimes26':crimes[26],
            'crimes27':crimes[27],
            'crimes28':crimes[28],
            'crimes29':crimes[29],
            'crimes30':crimes[30],
            'crimes31':crimes[31],
            'crimes32':crimes[32],
            'crimes33':crimes[33],
            'crimes34':crimes[34],
            'crimes35':crimes[35],
            'crimes36':crimes[36],
            'crimes37':crimes[37],
            'crimes38':crimes[38],

            'array00' :array[0][0] * 100,
            'array01' :array[0][1] * 100,
            'array02' :array[0][2] * 100,
            'array03' :array[0][3] * 100,
            'array04' :array[0][4] * 100,
            'array05' :array[0][5] * 100,
            'array06' :array[0][6] * 100,
            'array07' :array[0][7] * 100,
            'array08' :array[0][8] * 100,
            'array09' :array[0][9] * 100,
            'array10' :array[0][10] * 100,
            'array11' :array[0][11] * 100,
            'array12' :array[0][12] * 100,
            'array13' :array[0][13] * 100,
            'array14' :array[0][14] * 100,
            'array15' :array[0][15] * 100,
            'array16' :array[0][16] * 100,
            'array17' :array[0][17] * 100,
            'array18' :array[0][18] * 100,
            'array19' :array[0][19] * 100,
            'array20' :array[0][20] * 100,
            'array21' :array[0][21] * 100,
            'array22' :array[0][22] * 100,
            'array23' :array[0][23] * 100,
            'array24' :array[0][24] * 100,
            'array25' :array[0][25] * 100,
            'array26' :array[0][26] * 100,
            'array27' :array[0][27] * 100,
            'array28' :array[0][28] * 100,
            'array29' :array[0][29] * 100,
            'array30' :array[0][30] * 100,
            'array31' :array[0][31] * 100,
            'array32' :array[0][32] * 100,
            'array33' :array[0][33] * 100,
            'array34' :array[0][34] * 100,
            'array35' :array[0][35] * 100,
            'array36' :array[0][36] * 100,
            'array37' :array[0][37] * 100,
            'array38' :array[0][38] * 100,





            
                      }


            template = loader.get_template('ML/ml.html')
            return HttpResponse(template.render(thevalues, request))


 
    else:
 
        form = sf()
 
        return render(request, "sf.html", {'form': form})


def add(request):
 
    if request.method == "POST":
        form = caw(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            template = loader.get_template('index.html')
            return HttpResponse(template.render())

        else:
          template = loader.get_template('wrong/wrong-caw.html')
          return HttpResponse(template.render())


 
    else:
 
        form = caw()
 
        return render(request, "caw.html", {'form': form})





@csrf_exempt
def login(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        name = request.POST.get('name')
        passwd = request.POST.get('passwd')


        #adding the values in a context variable 
        context = {
            'name': name,
            'passwd': passwd
        }
        user = authenticate(username=name, password=passwd)
        if user is not None:
            template = loader.get_template('index.html')
            return HttpResponse(template.render())

        else:
          template = loader.get_template('portfolio-page.html')
        #returing the template 
        return HttpResponse(template.render(context, request))
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('login.html')
        return HttpResponse(template.render())


def redi(request):
    return redirect('/login')



def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index#')
        else:
            template = loader.get_template('wrong/wrong-register.html')
            return HttpResponse(template.render())

    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'reg.html', args)

def page1(request):
    template = loader.get_template('pages/page1.html')
    return HttpResponse(template.render())



def wrtstate(request):
	template = loader.get_template('womenn.html')
	return HttpResponse(template.render())



from fusioncharts import FusionCharts
def chart2003(request):
    year = '2003'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2003):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2003, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2003.html', {'output': column2D.render()}, {'year':year}) 



def chart2004(request):
    year = '2004'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2004):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2004, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2004.html', {'output': column2D.render()}, {'year':year}) 




def chart2005(request):
    year = '2005'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2005):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2005, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2005.html', {'output': column2D.render()}, {'year':year}) 


def chart2006(request):
    year = '2006'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2006):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2006, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2006.html', {'output': column2D.render()}, {'year':year}) 


def chart2007(request):
    year = '2007'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2007):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2007, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2007.html', {'output': column2D.render()}, {'year':year}) 


def chart2008(request):
    year = '2008'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2008):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2008, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2008.html', {'output': column2D.render()}, {'year':year}) 



def chart2009(request):
    year = '2009'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2009):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2009, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2009.html', {'output': column2D.render()}, {'year':year}) 


def chart2010(request):
    year = '2010'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2010):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2010, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2010.html', {'output': column2D.render()}, {'year':year}) 

def chart2011(request):
    year = '2011'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2011):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2011, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2011.html', {'output': column2D.render()}, {'year':year}) 

def chart2012(request):
    year = '2012'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2012):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2012, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2012.html', {'output': column2D.render()}, {'year':year}) 

def chart2013(request):
    year = '2013'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2013):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2013, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2013.html', {'output': column2D.render()}, {'year':year}) 

def chart2014(request):
    year = '2014'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2014):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2014, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2014.html', {'output': column2D.render()}, {'year':year}) 

def chart2015(request):
    year = '2015'
    dataSource = {}
    dataSource['chart'] = { 
         "caption": "Click on each State for single Analysis",
            "xAxisName": "Name of the State",
            "yAxisName": "Number of Reported crimes",
            "theme": "ocean",
            "paletteColors" : "#0075c2",
            "bgColor" : "#ffffff",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor" : "#999999",
            "showValues" : "0",
            "divlineColor" : "#999999",
            "divLineIsDashed" : "1",
            "showAlternateHGridColor" : "0"

        }
    
    dataSource['data'] = []
    dataSource['linkeddata'] = []

    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in sf_crimes.objects.all().filter(Year = 2015):
      data = {}
      data['label'] = key.Area_Name
      data['value'] = key.Total
      data['link'] = 'newchart-json-'+ key.Area_Name
      dataSource['data'].append(data)
      # Create the linkData for cities drilldown    
      linkData = {}
      # Inititate the linkData for cities drilldown
      linkData['id'] = key.Area_Name
      linkedchart = {}
     

      # Convert the data in the `City` model into a format that can be consumed by FusionCharts.     
      linkedchart['data'] = []
      # Filtering the data base on the Country Code
      for key in sf_crimes.objects.all().filter(Year = 2015, Area_Name=key.Area_Name):
        arrDara = {}
        
        arrDara['value'] = key.Total
        linkedchart['data'].append(arrDara)

      linkData['linkedchart'] = linkedchart
      dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "1200", "600", "chart-1", "json", dataSource)
    return render(request, 'women/2015.html', {'output': column2D.render()}, {'year':year}) 




def pie2003(request):
        data = pd.read_csv('sf_analysis.csv')
        var1 = 2003
        df = data[(data['Year'] == 2003)]
        top = [sum(df['Arson']),
         sum(df['Assault']),
         sum(df['Bad_Checks']),
         sum(df['Bribery']),
         sum(df['Bulgary']),
         sum(df['Disorderly_Conduct']),
         sum(df['Drug']),
         sum(df['Drunkedness']),
         sum(df['Embezzlement']),
         sum(df['Extortion']),
         sum(df['Family_Offenses']),
         sum(df['Forgery']),
         sum(df['Fraud']),
         sum(df['Gambling']),
         sum(df['Kidnapping']),
         sum(df['Theft']),
         sum(df['Liquor_Laws']),
         sum(df['Loitering']),
         sum(df['Missing_Person']),
         sum(df['NonCriminal']),
         sum(df['Other_Offenses']),
         sum(df['Porn']),
         sum(df['Prostitution']),
         sum(df['Recovered_Vehicle']),
         sum(df['Robbery']),
         sum(df['Runaway']),
         sum(df['Secondary_Code']),
         sum(df['Trea']),
         sum(df['Tresspass']),
         sum(df['Vandalism']),
         sum(df['Vehicle_Theft']),
         sum(df['Warrants']),
         sum(df['Weapon_Law'])

              ]
        value = ['Arson','Assault','Bad_Checks','Bribery','Bulgary','Disorderly_Conduct','Drug','Drunkedness','Embezzlement','Extortion','Family_Offenses','Forgery','Fraud','Gambling','Kidnapping','Theft','Liquor_Laws','Loitering','Missing_Person','NonCriminal','Other_Offenses','Porn','Prostitution','Recovered_Vehicle','Robbery','Runaway','Secondary_Code','Trea','Tresspass','Vandalism','Vehicle_Theft','Warrants','Weapon_Law']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the Crime Type distribution",
            "subCaption": "Crimes in the city",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})



def pie2002(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2002
        df = data[(data['Year'] == 2002)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})



def pie2004(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2004
        df = data[(data['Year'] == 2004)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})

def pie2005(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2005
        df = data[(data['Year'] == 2005)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})

def pie2006(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2006
        df = data[(data['Year'] == 2006)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})
def pie2007(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2007
        df = data[(data['Year'] == 2007)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})
def pie2008(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2008
        df = data[(data['Year'] == 2008)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})
def pie2009(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2009
        df = data[(data['Year'] == 2009)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})
def pie2010(request):
        data = pd.read_csv('20_Victims_of_rape.csv')
        var1 = 2010
        df = data[(data['Year'] == 2010)]
        top = [sum(df['Victims_Above_50_Yrs']),
         sum(df['Victims_Between_10to14_Yrs']),
         sum(df['Victims_Between_14to18_Yrs']),
         sum(df['Victims_Between_18to30_Yrs']),
         sum(df['Victims_Between_30to50_Yrs']),
         sum(df['Victims_Upto_10_Yrs'])
              ]
        value = ['Victims_Above_50_Yrs','Victims_Between_10-14_Yrs','Victims_Between_14-18_Yrs','Victims_Between_18-30_Yrs','Victims_Between_30-50_Yrs','Victims_Upto_10_Yrs']
        dataSource = {}
        dataSource['chart'] = { 
        "caption": "Analysis of the victims age distribution",
            "subCaption": "Crimes Against women",
            "theme": "zune"
        }

        dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
        for key in range(0,6):
            data = {}
            data['label'] = value[key]
            data['value'] = float(top[key])
            dataSource['data'].append(data)

      
        # returning complete JavaScript and HTML code, wwohich is used to generate chart in the browsers. 
        pie3d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-1", "json",dataSource) 

        return  render(request, 'women/pie2001.html', {'output' : pie3d.render(), 'var1':var1})



def sanfrancisco(request):
  filename = 'prediction.sav'
  module_dir = os.path.dirname(__file__)
  file_path = os.path.join(module_dir, filename)
  model = pickle.load(open(file_path, 'rb'))
  p = [0] * 17
  day = 'Sunday'
  place = 'BAYVIEW'
  if day == 'Friday':
      p[0]= 1
  if day == 'Monday':
      p[1]= 1
  if day == 'Saturday':
      p[2]= 1
  if day == 'Sunday':
      p[3]= 1
  if day == 'Thursday':
      p[4]= 1
  if day == 'Tuesday':
     p[5]= 1
  if day == 'Wednesday':
      p[6]= 1
  if place == 'BAYVIEW':
      p[7] = 1
  if place == 'CENTRAL':
      p[8] = 1
  if place == 'INGLESIDE':
      p[9] = 1
  if place == 'MISSION':
      p[10] = 1
  if place == 'NORTHERN':
      p[11] = 1
  if place == 'PARK':
      p[12] = 1
  if place == 'RICHMOND':
      p[13] = 1
  if place == 'SOUTHERN':
      p[14] = 1
  if place == 'TARAVAL':
      p[15] = 1
  if place == 'TENDERLOIN':
      p[16] = 1
  array = model.predict_proba(p)
  print ("Probability of Arson: ",(array[0][0])* 100, "%")
  return HttpResponse(array[0][0]*100)
