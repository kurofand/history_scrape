# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

class BaseScr:
	user=''
	password=''
	requests_session=requests.Session()
	log_url=''
	scr_url=''
	header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
	page=0

	def __init__(self, info):
		try:
			self.user=info['user']
			self.password=info['password']
			self.log_url=info['log_url']
			self.scr_url=info['scr_url']
		except:
			print('Some information was missed! Look 4 it, dude!')
			return False
		self.page=self.requests_session.get(self.log_url, headers=self.header)
