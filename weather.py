#-*- coding: utf-8 -*
import requests
import json
from wxpy import *
import schedule
import time

bot = Bot(cache_path=True)
#二维码登录微信网页端，开启缓存功能
friend = bot.friends().search(u'fermin')[0]
group = bot.groups().search(u'阿尔法小队')[0]
#好友的微信昵称，或者你存取的备注
city = friend.city



def weather():
	#返回城市+天气状态+气温

	url = 'https://restapi.amap.com/v3/weather/weatherInfo?city={}&key=909d31dcff00cc9f216510cf2af9d86c'.format(city)
	response = requests.get(url=url).text
	b = json.loads(response)
	data = (b['lives'][0])
	city_name = data['province'] + data['city']
	weather_state = data['weather']
	temperature = data['temperature']
	massage = ("您好！您当前城市为：{}，" "天气状况为：{}，"  "当前气温为：{}" .format(city_name,weather_state,temperature))
	return massage


def send_message():
	# 给单个好友发送消息-----------------
	# massage = weather(city)
	contentes = weather()
	# friend = bot.friends().search(u'fermin')[0]
	# city = friend.city
	friend.send(contentes)
	group.send(contentes)
	print("发送成功")
	
schedule.every().day.at("17:38").do(send_message)

while True:
	schedule.run_pending()
	time.sleep(1)
bot.join()


# if __name__ == "__main__":
#
# 	send_message()
#
# 	bot.join()
