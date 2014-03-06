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
		townName = request.POST.getlist('prefix')
		if len(townName) > 0:
			townName = townName[0].title()
			townData = TownInformation.objects.filter(name = townName)
			if len(townData) > 0:
				return render_to_response('search.html', {'prefix':townName, 'townData': townData[0]})
			else:
				return render_to_response('search.html', {'prefix':townName, 'error' : 'Такого города нет в нашей базе данных.'})	
	return render_to_response('search.html', {'prefix': ''})	

def fillTownData ():
	fin = open('list_towns_for_database.txt', 'r')
	TownInformation.objects.all().delete()
	for line in fin:
		line = line.strip()
		if len(line) > 0:
			townNew = TownInformation(name = line)
			townNew.save()
	fin.close()
	
@csrf_exempt 
def suggest (request):
	if request.is_ajax():
		data = request.POST['data']
		prefix = data.title()				
		choiceSet = TownInformation.objects.filter(name__startswith = prefix)[:5]
		townNames = []
		for town in choiceSet:
			townNames.append(town.name)
		response_data = {'choiceSet' : townNames}
		return HttpResponse(json.dumps(response_data), content_type="application/json")	
		
