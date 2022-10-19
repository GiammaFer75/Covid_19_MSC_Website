# In order to use the Flask instance you have to import it from the script where it has been created
from WebsitePackage import Cov19_msc 
from WebsitePackage import db
from WebsitePackage.db import Base, Session, engine, metadata_obj
from WebsitePackage.models import SubjectGroup
from flask import Flask, render_template, url_for, request
import os, sqlalchemy
from sqlalchemy import delete

from WebsitePackage import controller

session = Session()

@Cov19_msc.route("/")
@Cov19_msc.route("/Home")
def home_page():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  subject_group_table = session.query(SubjectGroup)

  print('Current number of records - ',session.query(SubjectGroup).count())

  df = controller.return_SubjectGroup_table()

  return render_template("Home.html", 
                         logo_image = logo_filename, 
                         subject_group_table=df) #subject_group_table.all()



@Cov19_msc.route("/page1")
def page1():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  subject_group_table = controller.return_SubjectGroup_table()
  return render_template("page1.html", 
                         logo_image = logo_filename,
                         subject_group_table=subject_group_table)



# ******************************************************************************************** #
#                                       UTILITY PAGES                                          #  
# ******************************************************************************************** #

@Cov19_msc.route("/New_Record", methods=['GET', 'POST'])
def New_Record():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  if request.method == 'POST':
    description = request.form.get('description')
    repositories = request.form.get('repositories')

    # print('\n*******************************\n',description)
    # print(repositories,'\n*******************************\n')

    subj_group_table = SubjectGroup 
    new_group = subj_group_table(description=description, repositories=repositories)
    session.add(new_group)
    session.commit()
  return render_template("NewRecord.html",
                         logo_image = logo_filename)

@Cov19_msc.route("/Delete_Record", methods=['GET', 'POST'])
def Delete_Record():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  if request.method == 'POST':
    group_id = request.form.get('group_id')
    description = request.form.get('description')
    repositories = request.form.get('repositories')

    # print('\n*******************************\n',group_id,'\n',description)
    # print(repositories,'\n*******************************\n')

  return render_template("DeleteRecord.html",
                         logo_image = logo_filename)


@Cov19_msc.route("/Create_Dummy_Database")
def Create_DD():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  #metadata_obj.create_all(engine)
  list_id = session.query(SubjectGroup.group_id)
  for g_id in list_id.all():
    print(g_id[0])
    session.query(SubjectGroup).filter(SubjectGroup.group_id == g_id[0]).delete(synchronize_session=False)
    session.commit()

  # Dummy table
  subject_group_table = [{'group_id': '001', 'description': 'Hospitalized subjects', 'rep':['p','m','z']},
        {'group_id': '002', 'description': 'Young students'       , 'rep':['p','z']},
        {'group_id': '003', 'description': 'Female from Wales'    , 'rep':['p','m','z']},
        {'group_id': '004', 'description': 'Male from London'     , 'rep':['p','m']},
        {'group_id': '005', 'description': 'Scottish healthcare personnel', 'rep':['m']},
        {'group_id': '006', 'description': 'Commonwealth research', 'rep':['p']}]
  

  descript_vect = ['Male London', 'Female Surrey', 'Health Workers', 'Elder subjects', 
                   'Liverpool group', 'Subjects over 80', 'Male Surrey', 'Health Workers 40'
  ]
  repos_vect = ['PRIDE,MetaboLight', 'ZENODO', 'PRIDE,ZENODO','PRIDE,MetaboLight,ZENODO',
                'PRIDE, ZENODO', 'MetaboLight,ZENODO', 'PRIDE,MetaboLight,ZENODO', 'PRIDE,MetaboLight,ZENODO'
  ]

  subj_group_table = SubjectGroup 
  for ind, desc in enumerate(descript_vect):
      new_group = subj_group_table(description=desc, repositories=repos_vect[ind]) # It is a class of type SubjectGroup with the attributes
      session.add(new_group)
      session.commit()

  print(session.query(SubjectGroup).count())
  return render_template("Create_DD.html",
                         logo_image = logo_filename)

# @Cov19_msc.context_processor
# def utility_functions():
#     def print_in_console(message):
#         print (str(message))

#     return dict(mdebug=print_in_console)