import urllib.robotparser as urobot
import requests

url = "http://www.taobao.com/"
rp = urobot.RobotFileParser()

rp.set_url(url + "/robots.txt")
rp.read()

user_agent = 'Baiduspider'

if rp.can_fetch(user_agent, "http://www.taobao.com/product/"):
    site = requests.get(url)
    print(site)
    print('seems good')
else:
    print("banned")