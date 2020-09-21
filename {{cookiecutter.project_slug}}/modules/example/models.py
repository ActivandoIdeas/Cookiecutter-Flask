from sqlalchemy import Column, Integer, String
from app.connection.db_instance import db


class Msg(db.Model):
    """Simple model example"""
    __tablename__ = 'msgs'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)

    def __init__(self, name=None, timestamp=None):
        self.name = name

    def __repr__(self):
        return '<msg %r>' % (self.name)
