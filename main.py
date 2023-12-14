import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector, IPTypes

# helper function to return SQLAlchemy connection pool
def init_connection_pool(connector: Connector) -> Engine:
    # Python Connector database connection function
    def getconn():
        conn = connector.connect(
            "stokminder-ch2-ps429:asia-southeast2:db-stokminder-dev", # Cloud SQL Instance Connection Name
            "mysql+mysqlconnector",
            user="root",
            password="",
            db="db-stokminder-dev",
            ip_type= IPTypes.PUBLIC  # IPTypes.PRIVATE for private IP
        )
        return conn

    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL , creator=getconn
    )
    return engine

# initialize Cloud SQL Python Connector
connector = Connector()

# create connection pool engine
engine = init_connection_pool(connector)

# create SQLAlchemy ORM session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()