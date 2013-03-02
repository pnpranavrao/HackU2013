from flask import Flask,url_for,request,render_template,jsonify
from github.githubapi import *
import json
import requests as r

app = Flask(__name__)
#What do I Need to do?

#* Authenticate the user
#DONE

#* When given a file name(figure out how) in the argument, return the json.
#DONE

#* When forks of a file are asked, list everything. 
#DONE

#* Create a fork 
#DONE

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

@app.route('/createfork')       
def create_fork():
        #POST /repos/:owner/:repo/forks
        user = request.args.get('user') or "yahoohackathon"
        password = request.args.get('pw') or "123yahoo"
        
        repo = request.args.get('repo') or "kivycontest"
        owner = request.args.get('owner') or "pnpranavrao"
        
        gh = GitHub(username=user,password = password)
        query = gh.repos(owner)(repo).forks
        result = query.post()
        return jsonify(**result)
        

@app.route('/listforks')        
def list_forks():
        #GET /repos/:owner/:repo/forks
        user = request.args.get('user') or "yahoohackathon"
        #password = request.args.get('pw') or "123yahoo"
        
        repo = request.args.get('repo') or "requests"
        owner = request.args.get('owner') or "kennethreitz"
        
        gh = GitHub(username=user)
        query = gh.repos(owner)(repo).forks
        result = query.get(sort="watchers")
        
        final_list = {}
        i = 0
        for fork in result:
                if i > 5:
                        continue
                temp_dict = {}
                for k,v in fork.iteritems():
                        if k in ["name","watchers","owner"]:
                                if k=="owner":
                                        temp_dict['owner_name'] = v['login']
                                else:
                                        temp_dict[k] = v                                
                final_list[str(i)] = temp_dict
                i = i+1
        return jsonify(**final_list)

#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    # show the post with the given id, the id is an integer
#       return 'Post %d' % post_id

@app.route('/commit')
def commit():
    user = request.args.get('user') or "yahoohackathon"
    password = request.args.get('password') or "123yahoo"
    repo = request.args.get('repo') or "kivycontest"
    content = [{"path":"readme.md","mode":"100644","type":"blob","content":"I loooooooove you"}]
    
    gh = GitHub(username=user,password=password)
    
    q = gh.repos(user)(repo).git.refs.heads.master
    sha_id = q.get()
    sha_latest = sha_id['object']['sha']
    
    qr = gh.repos(user)(repo).git.commits(sha_latest)
    sha_tree_result = qr.get()
    base_tree_sha = sha_tree_result['tree']['sha']
    
    qu = gh.repos(user)(repo).git.trees
    sha_new_tree_result = qu.post(base_tree=base_tree_sha,tree=content)
    
    #return json.dumps(sha_new_tree_result)
    parents = [sha_latest]
    qu = gh.repos(user)(repo).git.commits
    res = qu.post(message = "com-message",parents=parents,tree=sha_new_tree_result['sha'])
    sha_new_commit = res['sha']
    #return json.dumps(sha_new_commit)
#    http_proxy  = "144.16.192.245:8080"
#    https_proxy = "144.16.192.245:8080"
#    proxyDict = {'http':http_proxy,'https':https_proxy}
#    payload = {'sha':sha_new_commit,'force': 'true'}
#5363ecb49ced8981cfdcf49efd5df159101e332a

#/repos/:owner/:repo/git/refs/:ref
#/repos/pnpranavrao/kivycontest/git/refs/master
#    temp_url = "https://api.github.com/repos/%s/%s/git/refs/master"%(user,repo)
#    req = r.patch(temp_url, params = payload, proxies=proxyDict, verify = True)
#    
    qu = gh.repos(user)(repo).git.refs('heads/master')
    res = qu.post(sha=sha_new_commit,force='true')
    return json.dumps(res)

if __name__=='__main__':
        app.debug = True
        #app.run()
        app.run(host='0.0.0.0')
        

