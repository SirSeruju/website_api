import os
from sqlalchemy import Column, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
 
class Article(Base):
    __tablename__ = 'article'
    name = Column(Text(), primary_key=True, nullable=False)
    text = Column(Text())
 
engine = create_engine(os.environ["ENGINE_CONFIGURATION"])
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
