export FLASK_APP="flask-by-example"
export APP_SETTINGS="config.DevelopmentConfig"
export FLASK_ENV="development"
export DATABASE_URL="postgresql://localhost/wordcount_dev"
flask $1
