# if you utilize putting code directly in  __init__ you do not need to keep referencing more dots
from flask import Blueprint

# Note - Blueprints assume separation of a site into
# apps or sections of a site int sections;
# here we name them logically and can decorate the routes accordingly

# if this gets to big it is worth putting the parts in their own packages (dir) which represent the logical parts


main = Blueprint('main',  __name__)


@main.route('/')
def hello():
    return "Hello World!"


@main.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


