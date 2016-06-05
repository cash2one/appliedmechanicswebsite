"""import os
import os.path as op
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from wtforms import validators
import app
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters
from flask import Blueprint, render_template
from app.models import Alumni
from app.models import AlumniInfo
from app.models import Tree
from random import randint"""

"""from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext import wtf
from flask.ext.superadmin import Admin, model
from app import app
from app.models import User
from app.models import Post
from app.models import Tag

#app.config['SECRET_KEY'] = '123456790'

admin = Admin(app, 'Simple Models')

# Add views
admin.register(User)
admin.register(Tag)
admin.register(Post)"""

from flask import Blueprint, render_template
from app.models import Book

mod = Blueprint(
    'admin3', __name__, url_prefix='/admin3'
)

@mod.route('/')
def index():
    return render_template('admin/index.html')
