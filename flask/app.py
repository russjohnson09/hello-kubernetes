from flask import Flask
from dotenv import load_dotenv
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template


# https://github.com/theskumar/python-dotenv#readme
load_dotenv()  # take environment variables

app = Flask(__name__)


#As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app. See Command Line Interface for more details.


# flask --app app run
# flask run

# flask run --host=0.0.0.0

# flask run --debug
@app.route("/")
def hello_world():
    return "<p>Hello, World! test 564</p>"



# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"



@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

def show_the_login_form():
    return 'hello'

def do_the_login():
    return 'hello'

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()


#https://palletsprojects.com/projects/jinja/


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)



#https://flask.palletsprojects.com/en/stable/quickstart/#file-uploads




# Static Files
# Dynamic web applications also need static files. 
# That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, 
# but during development Flask can do that as well. 
# Just create a folder called static in your package or next to your module and it will be available at /static on the application.


# with app.test_request_context():
#     # print(url_for('index'))
#     print(url_for('login'))
#     # print(url_for('login', next='/'))
#     # print(url_for('profile', username='John Doe'))



