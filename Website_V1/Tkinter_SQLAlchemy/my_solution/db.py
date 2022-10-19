from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#flushing
#
# When do I construct a Session, when do I commit it, and when do I close it?
# tl;dr;
#
#     As a general rule, keep the lifecycle of the session separate and external from functions 
#     and objects that access and/or manipulate database data. This will greatly help with achieving 
#     a predictable and consistent transactional scope.
#
#     Make sure you have a clear notion of where transactions begin and end, and keep transactions 
#     short, meaning, they end at the series of a sequence of operations, instead of being held open 
#     indefinitely.



