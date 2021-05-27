#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from elasticsearch import Elasticsearch
from elasticsearch import helpers

def get_key(val,dic):
	for key, value in dic.items():
		if val ==value:
			return key
			
def hfilter(s):
	return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

def make_index(es, index_name):
	if es.indices.exists(index=index_name):
		es.indices.delete(index=index_name)
	print(es.indices.create(index=index_name))

es_host="127.0.0.1"
es_port="9200"

if __name__ == '__main__':
	
	es=Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)

	es.info()	
	index_name = 'goods'
	make_index(es, index_name)
	
	req = requests.get('https://en.wikipedia.org/wiki/Web_crawler')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	lists = soup.find_all('div',class_='mw-parser-output')
	
#	text1 = "".join(text for text in lists.find_all(text=True) if text.parent.name !="span")
#	content=soup.get_text('\n',strip=True)
#	print(content)
	text=[]
	for list1 in lists:
	#	if list1.parent.name != "article":
		Tex=list1.text.replace("\n","")
		text.extend(Tex.split())
#		print(Tex.split())
		
	line1=[]
	for i in text:
		line1.extend(i.split())
#	print(line1)
	p={}	
	for i in line1:
		if i in p:
			p[i] += 1
		else:
			p[i] = 1
	print(p)
	j=0
	for i in line1:
		temp=(list)(p.values())
#	print(temp)
	temp.sort()
	temp.reverse()
	es.index(index=index_name, doc_type='string', body=p)
	es.indices.refresh(index=index_name)
#	print(temp)
#	for i in range(3):
#		print(str(get_key(temp[i],p).ljust(10)),str(temp[i]).rjust(10))	
		
		
