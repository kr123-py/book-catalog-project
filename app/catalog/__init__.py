# app/catalog/__init__.py
from flask import render_template, Blueprint

main = Blueprint('main', __name__, template_folder='templates')

from  app.catalog.templates import routers
