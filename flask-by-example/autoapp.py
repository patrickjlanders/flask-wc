import os
from app import create_app
app = create_app(config_filename=os.environ['APP_SETTINGS'])

