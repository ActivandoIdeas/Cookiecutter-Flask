from sqlalchemy import Column, Integer, String
from core.database import Base


class Migration(Base):
    __tablename__ = 'migrations'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    timestamp = Column(String(50), unique=True)

    def __init__(self, name=None, timestamp=None):
        self.name = name
        self.timestamp = timestamp

    def __repr__(self):
        return '<migrations %r>' % (self.name)
