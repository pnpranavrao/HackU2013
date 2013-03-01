from flask import Flask 
import json
from github.githubapi import *
from flask import render_template
app = Flask(__name__)

#What do I Need to do?

#* Authenticate the user
#* When given a file name(figure out how) in the argument, return the json.
#* When forks of a file are asked, list everything. 
#* Create a fork 
#* Given a fork and master, supply the diff properly. 
#* Some mechanism to show which lines were written by whom. 

###Later
#* Proper stats.

@app.route('/')
def index():
	return "Hello World"
	
@app.route('/get')
def get_contents(user='yahoohackathon',repo='testrepo'):
	""" Default username is 'yahoohackathon', and default repo will be
	'testrepo' """
	gh = GitHub(username=user, password='123yahoo')
	query = gh.repos(user)(repo).readme
	result = query.get()
	
	return_dict = {}
	return_dict["user"] = user
	for k,v in result.iteritems():
		if k in ["name","content"]:
			return_dict[k] = v
	return json.dumps(return_dict)

#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    # show the post with the given id, the id is an integer
#	return 'Post %d' % post_id

if __name__=='__main__':
	app.debug = True
	#app.run()
	app.run(host='0.0.0.0')
	

