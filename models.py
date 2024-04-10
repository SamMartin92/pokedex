from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Trainer(Base):
    __tablename__ = "trainers"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"Trainer Name: {self.name}"

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
sesion = Session()

