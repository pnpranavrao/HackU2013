import json
from github.githubapi import *

#What do I Need to do?

#* Authenticate the user
#* When given a file name(figure out how) in the argument, return the json.
#* When forks of a file are asked, list everything. 
#* Create a fork 
#* Given a fork and master, supply the diff properly. 
#* Some mechanism to show which lines were written by whom. 

###Later
#* Proper stats.

def get_contents(user='pnpranavrao',repo='HackU2013'):
	""" Default username is 'yahoohackathon', and default repo will be
	'testrepo' """
	gh = GitHub(username=user)
	query = gh.repos(user)(repo).readme
	result = query.get()
	
	return_dict = {}
	return_dict["user"] = user
	for k,v in result.iteritems():
		if k in ["name","content"]:
			return_dict[k] = v
	print json.dumps(return_dict)

if __name__=='__main__':
	get_contents()

