#!/usr/bin/python3
#-*- coding: utf-8 -*-

import es

if __name__=='__main__':
	D={}
	moviename = input()
	D = es.moviesearch(moviename)
	print(D[1].pop('title'))          #제목
	print(D[1].pop('texts'))          #인덱스로 접근가능
	print(D[1].pop('names'))          

def Movsearch(movname):
	D={}
	moviename = movname
	D = es.moviesearch(moviename)
	print(D[1].pop('title'))          
	print(D[1].pop('texts'))          
	print(D[1].pop('names'))

	return D
		
	 

