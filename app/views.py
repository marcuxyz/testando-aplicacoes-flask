from flask import Blueprint

page = Blueprint('page', __name__)


@page.route('/')
def home():
    return 'Olá, mundo!'
