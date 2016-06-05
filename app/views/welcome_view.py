# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

mod = Blueprint('welcome', __name__, url_prefix='/welcome')


@mod.route('/')
def index():
    return render_template('welcome/index.html')
