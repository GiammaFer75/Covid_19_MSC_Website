from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from WebsitePackage.db import Base, engine, Session, metadata_obj
#


class SubjectGroup(Base):
	__tablename__ = "subject_group"

	group_id        = Column(Integer, autoincrement=True, primary_key=True)
	description     = Column(String)
	group_size      = Column(Integer)
	institution_ID  = Column(Integer, ForeignKey("institutions.institution_ID"))

	# RELATIONSHIP --- SubjectGroup
	institutions = relationship("Institutions", back_populates="subjects_group") 
	projects     = relationship("Projects", back_populates="subjects_group")

Project_Research = Table("project_research",
						 Base.metadata,
						 Column("project_accession_code", ForeignKey("projects.accession_code"), primary_key=True),
						 Column("researcher_ID", ForeignKey("researchers.researcher_ID"), primary_key=True)
						)

class Projects(Base):
	__tablename__ = "projects"

	accession_code     = Column(String, primary_key=True)
	group_ID           = Column(Integer, ForeignKey("subject_group.group_id"))
	project_title      = Column(String)
	researcher         = Column(Integer, ForeignKey("researchers.researcher_ID"))
	institution_ID     = Column(Integer, ForeignKey('institutions.institution_ID'))
	processing_type_ID = Column(Integer, ForeignKey("sample_processing.processing_ID"))
	protocol_ID        = Column(Integer, ForeignKey("protocols.protocol_ID"))
	data_processing_ID = Column(Integer, ForeignKey("data_processing.processing_ID"))
	repository_ID      = Column(Integer, ForeignKey("repositories.repository_ID"))

	# RELATIONSHIP --- Projects
	subjects_group    = relationship("SubjectGroup", back_populates="projects" )
	institutions      = relationship("Institutions", back_populates="projects")
	sample_processing = relationship("Sample_Processing", back_populates="projects")
	protocols         = relationship("Protocols", back_populates="projects")
	data_processing   = relationship("Data_Processing", back_populates="projects") 
	repositories      = relationship("Repositories", back_populates="projects")
	#researchers       = relationship("Researchers", back_populates="projects")
	researchers       = relationship("Researchers", secondary=Project_Research, back_populates="projects")

class Institutions(Base):
	__tablename__ = "institutions"
	
	institution_ID = Column(Integer, autoincrement=True, primary_key=True)
	inst_name      = Column(String)
	address		   = Column(String)

	# RELATIONSHIP --- Institutions
	projects       = relationship("Projects", back_populates="institutions")
	subjects_group = relationship("SubjectGroup", back_populates="institutions" )


class Sample_Processing(Base):
	__tablename__ = "sample_processing"
	
	processing_ID   = Column(Integer, autoincrement=True, primary_key=True)
	processing_type = Column(String)
    
    # RELATIONSHIP --- Sample_Processing
	projects      = relationship("Projects", back_populates="sample_processing")

class Protocols(Base):
	__tablename__ = "protocols"
	
	protocol_ID   = Column(Integer, autoincrement=True, primary_key=True)
	protocol_type = Column(String)

	# RELATIONSHIP --- Protocols
	projects      = relationship("Projects", back_populates="protocols")
	
class Data_Processing(Base):
	__tablename__ = "data_processing"
	
	processing_ID   = Column(Integer, autoincrement=True, primary_key=True)
	processing_type = Column(String)

	# RELATIONSHIP --- Data_processing
	projects       = relationship("Projects", back_populates="data_processing")

class Repositories(Base):
	__tablename__ = "repositories"
	
	repository_ID = Column(Integer, autoincrement=True, primary_key=True)
	name          = Column(String)

	# RELATIONSHIP --- Repositories
	projects       = relationship("Projects", back_populates="repositories")

class Researchers(Base):
	__tablename__ = "researchers"

	researcher_ID  = Column(Integer, autoincrement=True, primary_key=True)
	name           = Column(String)
	institution_ID = Column(Integer)

	# RELATIONSHIP --- Researchers
	#projects       = relationship("Projects", back_populates="researchers")
	projects = relationship("Projects", secondary=Project_Research, back_populates="researchers")
# always initialise with create_all
Base.metadata.create_all(engine)

# Git branching
# https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging