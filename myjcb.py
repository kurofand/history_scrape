#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from basescr import BaseScr
import requests
import random
class Myjcb(BaseScr):
	def scrape(self):
		if(self.page==0):
			print('Page was not loaded, exiting...')
			return False
		payload={'userId':self.user, 'password':self.password}
		data=self.page.text
		body=BeautifulSoup(data, 'lxml')
		form=body.find('form', {'name':'loginForm'})
		if(form):
			hiddens=form.findChildren('input', {'type':'hidden'})
			if(hiddens):
				for hidden in hiddens:
					try:
						payload[hidden['name']]=hidden['value']
					except:
						print(hidden['name'])
				payload['devicePrint']='version%3D3%2E4%2E1%2E0%5F1%26pm%5Ffpua%3Dmozilla%2F5%2E0%20%28x11%3B%20linux%20x86%5F64%3B%20rv%3A45%2E0%29%20gecko%2F20100101%20firefox%2F45%2E0%7C5%2E0%20%28X11%29%7CLinux%20x86%5F64%26pm%5Ffpsc%3D24%7C1824%7C984%7C948%26pm%5Ffpsw%3D%26pm%5Ffptz%3D9%26pm%5Ffpln%3Dlang%3Den%2DUS%7Csyslang%3D%7Cuserlang%3D%26pm%5Ffpjv%3D0%26pm%5Ffpco%3D1%26pm%5Ffpasw%3D%26pm%5Ffpan%3DNetscape%26pm%5Ffpacn%3DMozilla%26pm%5Ffpol%3Dtrue%26pm%5Ffposp%3D%26pm%5Ffpup%3D%26pm%5Ffpsaw%3D1824%26pm%5Ffpspd%3D24%26pm%5Ffpsbd%3D%26pm%5Ffpsdx%3D%26pm%5Ffpsdy%3D%26pm%5Ffpslx%3D%26pm%5Ffpsly%3D%26pm%5Ffpsfse%3D%26pm%5Ffpsui%3D%26pm%5Fos%3DLinux%26pm%5Fbrmjv%3D45%26pm%5Fbr%3DFirefox%26pm%5Finpt%3D%26pm%5Fexpt%3D'

				payload['login.y']=str(random.randint(1,50))
				payload['login.x']=str(random.randint(1,230))
#				print(payload)
				self.page=self.requests_session.post('https://my.jcb.co.jp/iss-pc/member/user_manage/Login', data=payload, headers=self.header)
				print(self.page)
#				self.page.encoding=self.page.apparent_encoding
#				print(self.page.text.encode('raw-unicode-escape').decode('shift-jis'))
				self.page=self.requests_session.get(self.scr_url, headers=self.header)
				#self.page.encoding=self.page.apparent_encoding
				self.page.encoding=self.page.apparent_encoding;
				print(self.page.text)

				return True
			else:
				print('Hiddens were not found, exiting...')
				return False
		else:
			print('Form was not found, exiting...')
			return False
