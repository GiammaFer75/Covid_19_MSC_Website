from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base() # sqlalchemy class for basic tabl

class SubjectGroup(Base): # inerhit the basic structure for sqlalchemy table
	__tablename__ = 'subject_group'
	project_id = Column(Integer, autoincrement=True, primary_key = True)
	description = Column(String(250))
	repositories = Column(String(250))

engine = create_engine("sqlite:///:memory:", echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Generate dummy db
descript_vect = ['Male London', 'Female Surrey', 'Health Workers', 'Elder subjects']
repos_vect = ['PRIDE,MetaboLight', 'ZENODO', 'PRIDE,ZENODO','PRIDE,MetaboLight,ZENODO']
for ind, desc in enumerate(descript_vect):
    new_group = SubjectGroup(description=desc, repositories=repos_vect[ind])
    session.add(new_group)
    session.commit()

# Generate a query object
group = session.query(SubjectGroup)

print('\n Database content')
for i in group:
    print(i.project_id, 
          i.description,
          i.repositories)
print('''
	---------------
	QUERIES SESSION
	---------------''')

# Query the query object
group_1 = group.filter(SubjectGroup.project_id==1).first()
print(group_1.project_id, 
      group_1.description,
      group_1.repositories) 
print('\n')
group_1 = group.filter(SubjectGroup.description=='Health Workers').first()
print(group_1.project_id, 
      group_1.description,
      group_1.repositories)
print('\n')
group_1 = group.filter(SubjectGroup.repositories=='PRIDE,MetaboLight,ZENODO').first()
print(group_1.project_id, 
      group_1.description,
      group_1.repositories)
print('\n')

print('''
      --------------------
      MORE COMPLEX QUERIES
      --------------------''')      


# The field values arrive from the main window form like 
# new_proj_form = self.view.get_data()

new_proj_form = {
      'description' : "Wrongkey", # Female Surrey
      'repositories' : ""
}

filter_str = ""
for key,value in new_proj_form.items():
      if (value != "") or (value==0):
            filter_str += f'SubjectGroup.{key}==\'{value}\','
filter_str=filter_str[:-1] # remove the last comma
command_str=f'group_1=group.filter({filter_str}).first()'
print('\n')
print(command_str)
exec(command_str)
print(group_1.project_id, 
      group_1.description,
      group_1.repositories)
print('\n')


