from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from .properties import SQLALCHEMY_DATABASE_URI, BIT_URI


def connection():
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    metadata = MetaData(bind=engine)
    tables = metadata.tables
    return session, engine, metadata, tables


def new_connection():
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    return engine, Session()


def connection(url):
    engine = create_engine(url, echo=False)
    Session = sessionmaker(bind=engine)
    return engine, Session()
