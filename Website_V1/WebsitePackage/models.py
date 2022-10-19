from sqlalchemy import Column, String, Integer
from WebsitePackage.db import Base, engine, Session, metadata_obj
#


class SubjectGroup(Base):
	__tablename__ = "subject_group"

	group_id     = Column(Integer, autoincrement=True, primary_key=True)
	description  = Column(String)
	repositories = Column(String)

	def __repr__(self):
		return f"{group_id}"

# always initialise with create_all
Base.metadata.create_all(engine)
