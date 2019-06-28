from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class db(db):
    def init(self):
        db = db()
        return db