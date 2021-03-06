from app import app
import requests
import json
import re
import random
from collections import OrderedDict
from datetime import datetime


class Weather(object):

	@classmethod
	def getForecast(self):
	    article_json = app.config['ARTICLE_JSON']
	    data = requests.get(str(article_json))
	    if data.status_code == 200:
	    	self.rand = random.randint(100000,999999)
	        self.alias = app.config['AD_ALIAS']
	    	content = ''
	    	offset = 0
	    	self.json = json.loads(data.content)
	    	json_obj = self.json['article']['body']
	    	for cnt in range(0, len(json_obj)):
	    		if 'value' in json_obj[cnt] and offset <= 2:
	    			content += json_obj[cnt]['value'] + '  '
	    			offset += 1
	        cleanr =re.compile('<.*?>')
	        self.narrative = text_truncate(re.sub(cleanr,'', content))
	        return
	    else:
	        return False

	@classmethod
	def getFront(self):
	    article_json = app.config['FRONT_JSON']
	    data = requests.get(str(article_json))
	    if data.status_code == 200:
	    	content = ''
	    	self.json = json.loads(data.content)
	    	json_obj = self.json['article']['body']
	    	for cnt in range(0, len(json_obj)):
	    		if 'value' in json_obj[cnt] and cnt == 3:
	    			content = json_obj[cnt]['value']
	        cleanr =re.compile('<.*?>')
	        self.narrative = re.sub(cleanr,'', content)
	        return
	    else:
	        return False

	@classmethod
	def getCurrent(self):
		config_url = app.config['WEATHER_JSON']
		data = requests.get(str(config_url))
		if data.status_code == 200:
			self.threeday = OrderedDict()
			self.hilo = OrderedDict()
			self.weathericons = OrderedDict()
			self.json = json.loads(data.content)
			self.json_obj = self.json['primary_modules']
			self.getOneDay(self)
			self.getThreeDay(self)
			return
		else:
			return False

	@staticmethod
	def getOneDay(self):
		for cnt in range(0, len(self.json_obj)):
			if 'weather_seven_day' in self.json_obj[cnt]:
				self.hi_to_replace = self.json_obj[cnt]['weather_seven_day'][0]['tempFHi']
				self.lo_to_replace =  self.json_obj[cnt]['weather_seven_day'][0]['tempFLo']
				self.weather_icon = app.config['WEATHER_ICONS'] + str(self.json_obj[cnt]['weather_seven_day'][0]['dayTime']['weatherIcon']) + '.png'

	@staticmethod
	def getThreeDay(self):
		for cnt in range(0, len(self.json_obj)):
			if 'weather_seven_day' in self.json_obj[cnt]:
				for offset in range(1, 4):
					dayname = self.json_obj[cnt]['weather_seven_day'][offset]['dayCode']
					hi = self.json_obj[cnt]['weather_seven_day'][offset]['tempFHi']
					lo =  self.json_obj[cnt]['weather_seven_day'][offset]['tempFLo']
					weather_icon = app.config['WEATHER_ICONS'] + str(self.json_obj[cnt]['weather_seven_day'][offset]['dayTime']['weatherIcon']) + '.png'
					self.threeday['day' + str(offset)] = dayname[:3]
					self.hilo['day' + str(offset) + '_hi'] = hi
					self.hilo['day' + str(offset) + '_lo'] = lo
					self.weathericons['icon' + str(offset)] = weather_icon


@app.context_processor
def utility_processor():
    def date_now(format="%d.m.%Y %H:%M:%S"):
        return datetime.now().strftime(format)
    return dict(date_now=date_now)

@app.context_processor
def get_title():
    return dict(get_title=app.config['FORECAST_TITLE'])

@app.context_processor
def get_threeday():
    return dict(get_threeday=app.config['THREEDAY_TITLE'])

@app.context_processor
def article_url():
	return dict(article_url=app.config['ARTICLE_URL'])

@app.context_processor
def weather_url():
	return dict(weather_url=app.config['WEATHER_URL'])

@app.context_processor
def front_url():
	return dict(front_url=app.config['FRONT_URL'])

def text_truncate(content, length=120, suffix='...'):
	return content[:length].rsplit(' ', 1)[0]+suffix
