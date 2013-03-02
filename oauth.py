from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth


SECRET_KEY = 'development key'
DEBUG = True
GITHUB_APP_ID = '303807aa12145f8d6b73'
GITHUB_APP_SECRET = '288c5fb6d3eb689ee16f59473633c4d6adcd9bcd'

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

github = oauth.remote_app('github',
    base_url='https://github.com/login/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    consumer_key=GITHUB_APP_ID,
    consumer_secret=GITHUB_APP_SECRET,
    request_token_params={'scope': 'email,repo,user:follow'}
)

@app.route('/done')
def auth_over():
	#ret_string =  "Congrats. You are authorized. The oauth_token is %s. Check it out. "%(session['oauth_token'][0])
	return "Aen macha"

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return github.authorize(callback=url_for('github_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/login/authorized')
@github.authorized_handler
def github_authorized(resp):
	if resp is None:
		return 'Access denied: reason=%s error=%s' % (
		request.args.get('error_reason',None),
		request.args.get('error_description',None)
		)
	session['oauth_token'] = (resp.get('access_token',None), '')
	print session['oauth_token']

if __name__=='__main__':
	#app.run()
	app.run(host='0.0.0.0')
	    
