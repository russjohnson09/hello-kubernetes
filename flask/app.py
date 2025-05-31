from flask import Flask
from dotenv import load_dotenv

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