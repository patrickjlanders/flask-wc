#!/bin/bash
##################################################################
# WRAPS flask CLI so that vars included
# obviously these can be sourced fro an .env
# that will happen later
##################################################################
export FLASK_APP="flask-by-example"
export APP_SETTINGS="config.DevelopmentConfig"
export FLASK_ENV="development"
export SQLALCHEMY_TRACK_MODIFICATIONS=FALSE
export DATABASE_URL="postgresql://localhost/wordcount_dev"
flask $@
