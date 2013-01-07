from django.template import Context, loader
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from checkin.models import singleFlightRecord, currentData, client
import urllib2
import json

def haha(request):
    return render_to_response('checkin/haha.html')

def getFlightInfo(request):
    return render_to_response('checkin/getFlightInfo.html',{},context_instance=RequestContext(request))

def getJson(request,carrier,flight,year,month,day):
    base = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/'
    authen = '?appId=1dba8baa&appKey=7b67b6221ec79e57c480b749e7f552bc&utc=false'
    url = base+carrier+'/'+flight+'/dep/'+year+'/'+month+'/'+day+'/'+authen
    
    #url = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/CA/981/dep/2013/1/3?appId=1dba8baa&appKey=7b67b6221ec79e57c480b749e7f552bc&utc=false'

    response = urllib2.urlopen(url).read()
    data = json.loads(response)
    #return HttpResponse(url)
    Info = 'Please check your flight information: <br />'
    flightcarrier = 'Your flight number is : '+carrier+flight+' <br />'
    scheduletime = data['flightStatuses'][0]['operationalTimes']['publishedDeparture']['dateLocal']
    flightdate = 'Your flight date is : '+scheduletime+' <br />'
    depCity = data['appendix']['airports'][0]['city']
    arrCity = data['appendix']['airports'][1]['city']
    flightplace = 'Your journey will begin at '+depCity+' and end at '+arrCity+' <br />'
    flightInfo = Info+flightcarrier+flightdate+flightplace;
    
    p = singleFlightRecord(carrier=carrier, flight=flight, date=scheduletime, depCity=depCity, arrCity=arrCity);
    p.distance = 10000;
    p.shareCode = 0;
    p.clientsID = 1;
    p.save();
    
    current = currentData.objects.get(pk=1)
    #current.record.add(p);
    current.save();
    
    return HttpResponse(flightInfo);

def findmyfriend(request, carrier,flight):
    p=singleFlightRecord.objects.filter(carrier=carrier,flight=flight)
    Info = 'Your airhangout friends are: <br />'
    i=0;
    while i<p.count():
        Info = Info + str(p[i].carrier)+str(p[i].flight)+' '+str(p[i].clientsID) + '<br />'
        i = i+1
    print p.count()
    print p[0].carrier
    return HttpResponse(Info)






