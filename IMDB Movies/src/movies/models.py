import os
from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
    Text,
    create_engine,
    select
)
from sqlalchemy.ext.declarative import declarative_base
from UriPostgres import PostgresURI

'''
Posible separación de responsabilidades de declaración de modelos y de inicio de la base de datos
'''

## -- Single Responsibility
# Separated the class UriPostgres.py from models

Base = declarative_base(
    metadata=MetaData(),
)


engine = create_engine(
    PostgresURI.get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)


class movies(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    create_time = Column(TIMESTAMP(timezone=True), index=True)


def start_mappers():
    Base.metadata.create_all(engine)




