from sqlalchemy import Column, String, Integer
from db import Base, engine, Session

class Projects(Base):
	__tablename__='projects'

	project_id = Column(Integer, autoincrement=True, primary_key=True)

	project_name = Column(String)
	project_description = Column(String)
	def __str__(self):
		return f"{self.project_id} - {self.project_name}"

class Omics(Base):
	__tablename__='omics'

	accession_code = Column(Integer, primary_key=True)

	project_id = Column(Integer) # *** HOW TO SET FOREING KEY ??? *** #
	omics_type = Column(String)
	repository_name = Column(String)

	def __str__(self):
		return f"{self.accession_code} - {self.project_id}"

Base.metadata.create_all(engine)