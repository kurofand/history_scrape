# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from basescr import BaseScr

class Rakuten(BaseScr):
#	user=''
#	password=''
#	header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
#	log_url='https://grp01.id.rakuten.co.jp/rms/nid/logini'
#	scr_url='https://www.rakuten-card.co.jp/card/#lineupWrap'
#	page=0
#	requests_session=requests.Session()
#moved init part to parent

	def scrape(self):
		if(self.page==0):
			print('Page was not loaded, exiting...')
			return False
		payload={'u':self.user, 'p':self.password}
		data=self.page.text
		body=BeautifulSoup(data, 'lxml')
		form=body.find('form', {'id':'indexForm'})
		#device_fp=c1afcc0d948683834142a959ae9d8e0d
		#was copied from login page, cose device is not changing I guess that it will be not changing too
		hiddens=form.findChildren('input', {'type':'hidden'})
		if(hiddens):
			for hidden in hiddens:
				payload[hidden['name']]=hidden['value']

			self.page=self.requests_session.post('https://grp01.id.rakuten.co.jp/rms/nid/login?', data=payload, headers=self.header)

			for i in range(15):
				self.page=self.requests_session.get(self.scr_url, data={'tabNo':'%d'%i})
				data=self.page.text
				body=BeautifulSoup(data, 'lxml')
				div=body.find('div',{'id':'mainCol'}).find('p').text
				print('%i) %s'%(i, div))

			return True
		else:
			print('Hiddens was not found! Exiting...')
			return False
