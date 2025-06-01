import functools

import pandas as pd
import base64
from io import BytesIO

from matplotlib.figure import Figure

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from werkzeug.security import check_password_hash, generate_password_hash

# from flaskr.db import get_db


bp = Blueprint('home', __name__, url_prefix='/')

df = pd.read_csv("https://raw.githubusercontent.com/AlexTheAnalyst/PandasYouTubeSeries/refs/heads/main/Ice%20Cream%20Ratings.csv")
df = df.set_index("Date")
#csv
#feather file
#parquet file

# @bp.route('/', methods=('GET'))
@bp.get('/')
def home():

    #starting a matplotlib GUI outside of the main thread will likely fail
    fig = df.plot(kind = 'line').get_figure()
    buf = BytesIO()
    fig.savefig(buf, format='png')
    # buf.seek(0)
    # buffer = b''.join(buf)
    # b2 = base64.b64encode(buffer)
    # sunalt2=b2.decode('utf-8')
    plot_data = base64.b64encode(buf.getbuffer()).decode("ascii")


    return render_template('index.html', plot_data=plot_data)


# https://matplotlib.org/stable/gallery/user_interfaces/web_application_server_sgskip.html
# https://stackoverflow.com/questions/20107414/passing-a-matplotlib-figure-to-html-flask
@bp.get('/test')
def test():
    # return 'hello'
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # data = '1'
    return f"<img src='data:image/png;base64,{data}'/>"
