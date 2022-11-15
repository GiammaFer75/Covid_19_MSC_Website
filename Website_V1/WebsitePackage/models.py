from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from WebsitePackage.db import Base, engine, Session, metadata_obj




# ********************************************************** #
# ****************** FIRST VERSION ************************* #
# ********************************************************** #


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


# ********************************************************** #
# ****************** SECOND VERSION ************************ #
# ********************************************************** #


sample_sampleTypes  = Table("sample_sampletypes",
							Base.metadata,
							Column("sample_id",      ForeignKey("samples.sample_id"), primary_key=True),
							Column("sample_type_id", ForeignKey("sample_types.sample_type_id"), primary_key=True)
							)

sample_analysisType = Table("sample_analysistypes",
							Base.metadata,
							Column("sample_id",        ForeignKey("samples.sample_id"), primary_key=True),
							Column("analysis_type_id", ForeignKey("analysis_types.analysis_type_id"), primary_key=True)
							)


class Subjects_Groups(Base):
	__tablename__ = "subjects_groups"

	subjects_group_id 	= Column(String, primary_key=True)
	site_id  			= Column(Integer, ForeignKey("sites.site_id"))

	# RELATIONSHIP --- Subjects_Group
	sites 				= relationship("Sites",    back_populates="subjects_groups")
	subjects         	= relationship("Subjects", back_populates="subjects_groups")

class Subjects(Base):
	__tablename__ = "subjects"

	subject_id   		= Column(String, primary_key=True)
	subject_group_id	= Column(String, ForeignKey("subjects_groups.subjects_group_id"))

	# RELATIONSHIP --- Subjects
	subjects_groups		= relationship("Subjects_Groups", back_populates="subjects")
	samples   			= relationship("Samples",         back_populates="subjects")

class Samples(Base):
	__tablename__ = "samples"

	sample_id 			= Column(Integer, autoincrement=True, primary_key=True)
	subject_id 			= Column(String,  ForeignKey("subjects.subject_id"))
	event_id 			= Column(Integer, ForeignKey("events.event_id"))
	site_id 			= Column(Integer, ForeignKey("sites.site_id"))

	sample_types        = relationship("Sample_Types", secondary=sample_sampleTypes, 
									   back_populates="samples")
	analysis_types      = relationship("Analysis_Types", secondary=sample_analysisType,
		                               back_populates="samples")

	# RELATIONSHIP --- Samples
	subjects 			= relationship("Subjects", back_populates="samples")
	events				= relationship("Events",   back_populates="samples")
	sites    			= relationship("Sites",    back_populates="samples")


class Sites(Base):
	__tablename__ = "sites"

	site_id 			= Column(Integer, autoincrement=True, primary_key=True)
	site_name 			= Column(String)

	# RELATIONSHIP --- Sites
	subjects_groups		= relationship("Subjects_Groups", back_populates="sites")
	samples   			= relationship("Samples",         back_populates="sites")

class Events(Base):
	__tablename__ = "events"

	event_id			= Column(Integer, autoincrement=True, primary_key=True)
	event_name			= Column(String)

	# RELATIONSHIP --- Events
	samples   			= relationship("Samples",         back_populates="events")
	#subjects_groups   	= relationship("Subjects_Groups", back_populates="events")


class Sample_Types(Base):
	__tablename__ = "sample_types"

	sample_type_id 		= Column(Integer, autoincrement=True, primary_key=True)
	sample_type_name 	= Column(String)

	# RELATIONSHIP --- Sample_Types
	samples 			= relationship("Samples", secondary=sample_sampleTypes,
										back_populates="sample_types")

class Analysis_Types(Base):
	__tablename__ = "analysis_types"
	
	analysis_type_id	= Column(Integer, autoincrement=True, primary_key=True)
	analysis_type_name	= Column(String)

	samples        		= relationship("Samples", secondary=sample_analysisType,
										back_populates="analysis_types")



# always initialise with create_all
Base.metadata.create_all(engine)

# Git branching
# https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging