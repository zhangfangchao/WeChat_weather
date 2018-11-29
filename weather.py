#-*- coding: utf-8 -*
import requests
import json
from wxpy import *

bot = Bot()

def weather (city=''):
	city = input("请输入您的城市：")
	
	url = 'https://restapi.amap.com/v3/weather/weatherInfo?city={}&key=909d31dcff00cc9f216510cf2af9d86c'.format(city)
	
	response = requests.get(url=url).text
	b = json.loads(response)
	data = (b['lives'][0])
	city_name = data['province'] + data['city']
	weather_state = data['weather']
	temperature = data['temperature']
	
	print("您好！您当前城市为：{}，" "天气状况为：{}，"  "当前气温为：{}" .format(city_name,weather_state,temperature))
	
if __name__ == '__main__':
	weather()