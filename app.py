#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import request
import es
import search_moviename

count=1
for i in range(10002,10005):
        total = search_moviename.integrate(str(i))
        es.inputmovie(total,count)
        count = count+1

def Movsearch(movname):
	D={}
	moviename = movname
	D = es.moviesearch(moviename)
	
	return D

app= Flask(__name__)

@app.route('/')
def index():
        return render_template('practice.html')
        
@app.route('/1',methods=['POST'])
def t1():
	if request.method=='POST':
		result = request.form['search']
		D=Movsearch(result)
		return render_template('page1.html',result=result,title=D[1].pop('title'),text=D[1].pop('texts'),name=D[1].pop('names')) 
		        
@app.route('/2',methods=['POST'])
def t2():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page2.html',result=result) 
		        
@app.route('/3',methods=['POST'])
def t3():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page3.html',result=result) 
		        
@app.route('/4',methods=['POST'])
def t4():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page4.html',result=result) 
		        
@app.route('/5',methods=['POST'])
def t5():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page5.html',result=result) 
		        
@app.route('/6',methods=['POST'])
def t6():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page6.html',result=result) 
		

if __name__ == '__main__':
	app.run(debug=True)	
