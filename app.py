#pythgon flask app

from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
@app.route('/')
def welcome():
	return render_template('index.html')

@app.route('/method',methods=['GET','POST'])
def method():
	if request.method=='POST':
		return "You are using a post method"
	else:
		return "You are using a Get Method"

app.run()