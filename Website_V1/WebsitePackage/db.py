from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.exc import OperationalError, StatementError
from sqlalchemy.orm.query import Query as _Query
from time import sleep

class RetryingQuery(_Query):
    __max_retry_count__ = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        attempts = 0
        while True:
            attempts += 1
            try:
                return super().__iter__()
            except OperationalError as ex:
                if "server closed the connection unexpectedly" not in str(ex):
                    raise
                if attempts <= self.__max_retry_count__:
                    sleep_for = 2 ** (attempts - 1)
                    logging.error(
                        "/!\ Database connection error: retrying Strategy => sleeping for {}s"
                    " and will retry (attempt #{} of {}) \n Detailed query impacted: {}".format(
                        sleep_for, attempts, self.__max_retry_count__, ex)
                )
                    sleep(sleep_for)
                    continue
                else:
                    raise
            except StatementError as ex:
                if "reconnect until invalid transaction is rolled back" not in str(ex):
                    raise
                self.session.rollback()



Base = declarative_base()


                       # ********* LOCAL DB ********* #
                       #------------------------------#
engine = create_engine('sqlite:///Cov19_database.db', echo=False, 
						connect_args={'check_same_thread':False})
Session = sessionmaker(bind=engine)

                    # ********* LOCAL DB POSTGRE********* #
                    #-------------------------------------#
engine = create_engine('postgresql+psycopg2://postgres:123@localhost/test_database', echo=False)
Session = sessionmaker(bind=engine)

                      # ********* EXTERNAL DB ********* #
                      #---------------------------------#
# engine = create_engine('postgresql://Covid19MSC:v2_3wK5L_S9wisniwuVBYbsP2jWusbBT@db.bit.io/Covid19MSC/Covid19MSC',
# 	                   pool_size=30,
#                        max_overflow=10,
#                        pool_recycle=300,
#                        pool_pre_ping=True,
#                        pool_use_lifo=True)
    					
# Session = sessionmaker(bind=engine, query_cls=RetryingQuery)
# REFERENCES
# https://stackoverflow.com/questions/65657767/psycopg2-operationalerror-ssl-syscall-error-eof-detected-on-flask-sqlaclemy-ce

# How to fix "OperationalError: (psycopg2.OperationalError) server closed the connection unexpectedly"
# https://stackoverflow.com/questions/55457069/how-to-fix-operationalerror-psycopg2-operationalerror-server-closed-the-conn

metadata_obj = MetaData()


# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#flushing
