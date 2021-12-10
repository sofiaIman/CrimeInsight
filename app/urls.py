from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.redi , name = 'redi'),
    url(r'^index', views.login , name = 'login'),
    url(r'^login/$', views.login , name = 'login'),
    url(r'^register', views.register , name = 'register'),
    url(r'^page1', views.page1 , name = 'page1'),
    url(r'^overyears', views.wrtstate , name = 'wrtstate'),
    
    url(r'^chart2003', views.chart2003 , name = 'chart2003'),
    url(r'^chart2004', views.chart2004 , name = 'chart2004'),
    
    url(r'^chart2005', views.chart2005 , name = 'chart2005'),
    url(r'^chart2006', views.chart2006 , name = 'chart2006'),
    url(r'^chart2007', views.chart2007 , name = 'chart2007'),
    url(r'^chart2008', views.chart2008 , name = 'chart2008'),
    url(r'^chart2009', views.chart2009 , name = 'chart2009'),
    url(r'^chart2010', views.chart2010 , name = 'chart2010'),
    url(r'^chart2011', views.chart2011 , name = 'chart2011'),
    url(r'^chart2012', views.chart2012 , name = 'chart2012'),
    url(r'^chart2013', views.chart2013 , name = 'chart2013'),
    url(r'^chart2014', views.chart2014 , name = 'chart2014'),
    url(r'^chart2015', views.chart2015 , name = 'chart2015'),
    url(r'^pie2001', views.pie2003 , name = 'pie2003'),
    url(r'^pie2002', views.pie2002 , name = 'ddds'),
    url(r'^pie2003', views.pie2003 , name = 'sdf'),
    url(r'^pie2004', views.pie2004 , name = 'mzzm'),
    url(r'^pie2005', views.pie2005 , name = 'amm'),
    url(r'^pie2006', views.pie2006 , name = 'mdmsd'),
    url(r'^pie2007', views.pie2007 , name = 'sms'),
    url(r'^pie2008', views.pie2008 , name = 'smsss'),
    url(r'^pie2009', views.pie2009 , name = 'lvl'),
    url(r'^pie2010', views.pie2010 , name = 'trr'),
    
    url(r'^formcrimesagaintswomen', views.add , name = 'add_model'),
    url(r'^sanfrancisco', views.sss , name = 'sanfrancisco'),












    












]
