from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# ********* LOCAL DB ********* #
engine = create_engine('sqlite:///Cov19_database.db', echo=False, 
						connect_args={'check_same_thread':False})

# ********* EXTERNAL DB ********* #
# engine = create_engine('postgresql://Covid19MSC:v2_3wK5L_S9wisniwuVBYbsP2jWusbBT@db.bit.io/Covid19MSC/Covid19MSC',
# 	                   pool_pre_ping=True)
# REFERENCES
# https://stackoverflow.com/questions/65657767/psycopg2-operationalerror-ssl-syscall-error-eof-detected-on-flask-sqlaclemy-ce

metadata_obj = MetaData()
Session = sessionmaker(bind=engine)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#flushing
