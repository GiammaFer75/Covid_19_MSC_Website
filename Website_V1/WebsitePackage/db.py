from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///Cov19_database.db', echo=False, 
						connect_args={'check_same_thread':False})
metadata_obj = MetaData()
Session = sessionmaker(bind=engine)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#flushing
