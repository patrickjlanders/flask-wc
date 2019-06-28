import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


#config = os.environ['APP_SETTINGS']
# ESSENTIAL
# this is use of factory function
# register blueprints here
def create_app(test_config=None):

    print("inside create app")
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config.Config')
    print(app.config['SECRET_KEY'])
    print(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])

    db = SQLAlchemy(app)
    db.init_app(app)

    # note this conditional import - only called if the app created
    from .views import main
    app.register_blueprint(main)

    # TODO - invesigate how instance folders work
    # ensure the instance folder exists
    # try:
    #     print("instance path " + app.instance_path)
    #     os.makedirs(app.instance_path)

    #except OSError:
    #    pass

    return app


if __name__ == '__main__':
    create_app(config)

