from app import app
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

class CommonConfig(object):
	VERSION = 'Version: WCG v2.0'
	FORECAST_TITLE = "AZCENTRAL FORECAST"
	THREEDAY_TITLE = "THREE-DAY FORECAST"
	WEATHERIMG = "azcentral"
	IMGDIR = "http://nocache.azcentral.com/imgs/staff-bios/staff-bio-"
	WEATHER_ICONS = "http://nocache.azcentral.com/weather/imgs/icons/"
	WEATHER_JSON = "http://www.azcentral.com/weather.json"
	WEATHER_URL = "http://weather.azcentral.com"
	ARTICLE_JSON = "http://www.azcentral.com/story/news/local/arizona/2015/01/16/phoenix-weather-weekend-forecast-sunny-warm-brk/21848897.json"
	ARTICLE_URL = "http://www.azcentral.com/story/news/local/arizona/2015/01/16/phoenix-weather-weekend-forecast-sunny-warm-brk/21848897/"
	FRONT_JSON = "http://www.azcentral.com/story/news/12-news/2015/01/18/12news-weather-forecast/21953337.json"
	FRONT_URL = "http://www.azcentral.com/story/news/12-news/2015/01/18/12news-weather-forecast/21953337/"
	AD_ALIAS = "weather/forecasts_newsletter"
	UPLOAD_FOLDER = "/mnt/writehere.azcentral.com/drupalfiles/persistent/weather-front/"
	DEBUG = False
	app.secret_key = '\xd1\xfc\x92f,\x9e\xfd\xfc\x06}\xe1\x97'
