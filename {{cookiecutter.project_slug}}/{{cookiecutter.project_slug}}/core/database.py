from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from {{ cookiecutter.project_slug }}.models import Base


def database_connect(database_url: str):
    return create_engine(database_url)


def create_session(engine):
    return sessionmaker(bind=engine)()


def create_tables(engine):
    Base.metadata.create_all(engine)


def drop_tables(engine):
    Base.metadata.drop_all(engine)
