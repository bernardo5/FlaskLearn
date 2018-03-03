#initial setup

#1. sudo apt-get install python-virtualenv
#2. virtualenv <name>
#3. source <name>/bin/activate   --> to deactivate just type "deactivate"
#4. pip install Flask

#to run the flask app:
#1. export FLASK_APP=<name>.py
#2. flask run


#Flask Context Variables
#-current_app --> Application context --> app instance for the active application
#-g --> Application context --> object that the app can use for temporary storage during the handling of a request. Is reset at each request
#-request --> request context --> the request object which encapsulates the contents of a http request sent by the client
#-session --> request context --> the user session, a dictionary that the application can use to store values that are remembered betwen requests


#hooks supported by flask --> implemented as decorators
# before_first_request --> Register a function to run before each request
# before_request --> register a function to run before each request
# after_request --> register a function to run after each request, if no unhandled exceptions occurred
# teardown_request --> register a function to run after each request, even if unhandled exceptions ocurred

from flask import Flask, request, make_response, redirect, abort

app=Flask(__name__) #needs to be right after import

@app.route('/')
def index():
	user_agent=request.headers.get('User-Agent')
	return '<h1>Hello World</h1> <p>Oh...and your browser is %s</p>' % user_agent

#dynamic display
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello %s!</h1>' % name

#sets a different status code than the 200 one assumed by default
@app.route('/error/')
def error():
	return '<h1>Bad Request</h1>', 400

#sets a cookie
@app.route('/cookie/')
def setCookie():
	response=make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response

#redirects to a different web page
@app.route('/redirect')
def redirectPage():
	return redirect('http://www.google.pt')
	
#abort function example
def load_user(id):
	return null
@app.route('/abort/<id>')
def abortExample():
	user=load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name


if __name__=='__main__':
	app.run(debug=True)

