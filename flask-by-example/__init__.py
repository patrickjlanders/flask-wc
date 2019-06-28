import os
from flask_migrate import Migrate
from .app import create_app
from .model.models import db


migrate = Migrate(app, db)

app = create_app(os.environ['APP_SETTINGS'] or 'default')
migrate = Migrate(app, db)


