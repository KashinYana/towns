# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from townInformation.models import TownInformation
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def search (request):
	if request.method == 'POST':
		prefix = request.POST.getlist('prefix')
		if len(prefix) > 0:
			prefix = prefix[0]
			data = TownInformation.objects.filter(name = prefix)
			if (len(data) > 0):
				data = data[0]
				return render_to_response('search.html', {'data': data, 'info' : 'info'})	
	return render_to_response('search.html')	

def add ():
	fin = open('list_towns_for_database.txt', 'r')
	for line in fin:
		line = line.strip()
		if len(line) > 0:
			townNew = TownInformation(name = line)
			townNew.save()
	fin.close()

@csrf_exempt 
def inputText (request):
	if request.is_ajax():
		data = request.POST['data']
		prefix = data			
		data2 = TownInformation.objects.filter(name__startswith = prefix)[:5]
		dataNames = []
		for town in data2:
			dataNames.append(town.name)
		response_data = {'data':dataNames}
		
		return HttpResponse(json.dumps(response_data), content_type="application/json")	
	response_data = {'data':'Error'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")	
	
	
