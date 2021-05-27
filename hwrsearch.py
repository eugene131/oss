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
	return re.sub(u'[^a-zA-Z]+',' ',s)

def make_index(es, index_name):
	if es.indices.exists(index=index_name):
		es.indices.delete(index=index_name)
	print(es.indices.create(index=index_name))

es_host="127.0.0.1"
es_port="9200"
D = {}
if __name__ == '__main__':

	es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)
#	index_name = 'goods'
#	make_index(es, index_name)

	req = requests.get(u'https://en.wikipedia.org/wiki/Web_crawler')
	soup = BeautifulSoup(req.content, 'html.parser')
	lists = soup.find_all('div',class_='mw-parser-output')

#	text1 = "".join(text for text in lists.find_all(text=True) if text.parent.name !="span")
#	content=soup.get_text('\n',strip=True)
#	print(content)

#               수정한부분 
	p={}
	for list1 in lists:
		text = hfilter(list1.get_text())
		arr = text.split()
		print (arr)
		
		for i in arr:
			if i in p:
				p[i]+=1
			else:
				p[i]=1
		j=0
		for i in arr:
			temp=list(p.values())
	temp.sort()
	temp.reverse()
	for i in range(int(3)):
			print(str(get_key(temp[i],p).ljust(10)),str(temp[i]).rjust(10))
	j=0
#	print(temp)
	num=1
	for i,j in p.items():
		e={"word" : i, "num":j}
		es.index(index='good', doc_type='string',id=num, body=e)
		num+=1
	
	
	
	
	
	
	
	
	
