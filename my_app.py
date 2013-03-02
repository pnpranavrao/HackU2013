from flask import Flask,url_for,request
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
def get_contents():
	""" Default username is 'yahoohackathon', and default repo will be
	'testrepo' """
	user = request.args.get('user') or "yahoohackathon"
	repo = request.args.get('repo') or "testrepo"
	gh = GitHub(username=user)
	query = gh.repos(user)(repo).readme
	result = query.get()
	
	return_dict = {}
	return_dict["user"] = user
	for k,v in result.iteritems():
		if k in ["name","content"]:
			return_dict[k] = v
	return json.dumps(return_dict)
	
#@app.route('/comments')
#def put_comment(user='pnpranavrao',repo='kivycontest',password='studio15',sha_id='836b6a7aaa814eb89e96be65daf7817f23013810',message="Hello World"):
#        gh = GitHub(username=user,password=password)
#        query = gh.repos(user)(repo).commits(sha_id).comments
#        query.post(body=message)
#        return "Comment published" 

@app.route('/fork')	
def create_fork():
	#POST /repos/:owner/:repo/forks
	user = request.args.get('user') or "yahoohackathon"
	password = request.args.get('pw') or "123yahoo"
	
	repo = request.args.get('repo') or "kivycontest"
	owner = request.args.get('owner') or "pnpranavrao"
	
	gh = GitHub(username=user,password = password)
	query = gh.repos(owner)(repo).forks
	result = query.post()
	return json.dumps(result)
	
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    # show the post with the given id, the id is an integer
#	return 'Post %d' % post_id

if __name__=='__main__':
	app.debug = True
	#app.run()
	app.run(host='0.0.0.0')
	

