HackU2013
=========

Our entry for Yahoo's HackU competition. More details later.

* Install flask (pip install flask)
* Run my_app.py (python my_app.py)

Now the server is running on your external facing ip. 
Get your IP address and with port 5000, you can hit the server. 

* query it with something like "http://127.0.0.1:5000/get" to get a json payload with the agreed upon format {"content":"dfsf","user":"pranav","name":"README.md"}

### Notes 

* "content" above will be base 64 encoded. 
* I am using a test github account and repo.

### Experimental 

* The oauth.py file is a separate app which tests oauth capability. 
* OAuth is critical, so please go through the guide on github.
* Currently I am utilizing a flask extention to handle oauth - e.g https://github.com/mitsuhiko/flask-oauth/blob/master/example/facebook.py
* Now it seems like doing directly without the extension is better. 

