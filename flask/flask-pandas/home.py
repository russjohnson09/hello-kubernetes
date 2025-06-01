import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from werkzeug.security import check_password_hash, generate_password_hash

# from flaskr.db import get_db


bp = Blueprint('home', __name__, url_prefix='/')


#csv
#feather file
#parquet file

# @bp.route('/', methods=('GET'))
@bp.get('/')
def register():
    return render_template('index.html')


