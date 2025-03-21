from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import drop_database, create_database, database_exists

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from tests import Potato, PotatoType, Carrot, CarrotCreate, CustomPotato, CarrotUpdate, PAGINATION_SIZE

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


def _setup_base_app():
    if database_exists(SQLALCHEMY_DATABASE_URL):
        drop_database(SQLALCHEMY_DATABASE_URL)

    create_database(SQLALCHEMY_DATABASE_URL)

    app = FastAPI()

    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    def session():
        session = SessionLocal()
        try:
            yield session
            session.commit()
        finally:
            session.close()

    return app, engine, Base, session


def sqlalchemy_implementation():
    app, engine, Base, session = _setup_base_app()

    class PotatoModel(Base):
        __tablename__ = 'potatoes'
        id = Column(Integer, primary_key=True, index=True)
        thickness = Column(Float)
        mass = Column(Float)
        color = Column(String)
        type = Column(String)

    class CarrotModel(Base):
        __tablename__ = 'carrots'
        id = Column(Integer, primary_key=True, index=True)
        length = Column(Float)
        color = Column(String)

    Base.metadata.create_all(bind=engine)
    app.include_router(SQLAlchemyCRUDRouter(schema=Potato, db_model=PotatoModel, db=session, prefix='potato', paginate=PAGINATION_SIZE))
    app.include_router(SQLAlchemyCRUDRouter(
        schema=Carrot,
        db_model=CarrotModel,
        db=session,
        create_schema=CarrotCreate,
        update_schema=CarrotUpdate,
        prefix='carrot'
    ))

    return app


# noinspection DuplicatedCode
def sqlalchemy_implementation_custom_ids():
    app, engine, Base, session = _setup_base_app()

    class PotatoModel(Base):
        __tablename__ = 'potatoes'
        potato_id = Column(Integer, primary_key=True, index=True)
        thickness = Column(Float)
        mass = Column(Float)
        color = Column(String)
        type = Column(String)

    Base.metadata.create_all(bind=engine)
    app.include_router(SQLAlchemyCRUDRouter(schema=CustomPotato, db_model=PotatoModel, db=session))

    return app


def sqlalchemy_implementation_string_pk():
    app, engine, Base, session = _setup_base_app()

    class PotatoTypeModel(Base):
        __tablename__ = 'potato_type'
        name = Column(String, primary_key=True, index=True)
        origin = Column(String)

    Base.metadata.create_all(bind=engine)
    app.include_router(SQLAlchemyCRUDRouter(schema=PotatoType, create_schema=PotatoType, db_model=PotatoTypeModel, db=session, prefix='potato_type'))

    return app
