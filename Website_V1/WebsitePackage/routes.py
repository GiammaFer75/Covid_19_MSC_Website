# In order to use the Flask instance you have to import it from the script where it has been created
from WebsitePackage import Cov19_msc 
from WebsitePackage import db
from WebsitePackage.db import Base, Session, engine, metadata_obj
from WebsitePackage.models import Subjects_Groups
from flask import Flask, render_template, url_for, request
import os, sqlalchemy
import json
from sqlalchemy import delete

from WebsitePackage import controller

session = Session()


@Cov19_msc.route("/")
@Cov19_msc.route("/Home")
def home_page():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  print('Current number of records - ',session.query(Subjects_Groups).count())
  
  df = controller.return_SubjectGroup_table()
  return render_template("Home.html", 
                         logo_image = logo_filename, 
                         subject_group_table=df) #subject_group_table.all()
  # return render_template("Home.html", 
  #                         logo_image = logo_filename)


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

@Cov19_msc.route("/Search", methods=['GET', 'POST'])
def Search():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')

  if request.method == "POST":

    if request.data != '':
      form_data = json.loads(request.data)
      print(form_data["sample_type"])
    print(request.data)

    form_subjects_group = request.form.get("subjects_group")
    form_subject        = request.form.get("subject")
    form_event          = request.form.get("event")
    form_site           = request.form.get("site")
    form_sample_type    = request.form.get("sample_type")
    form_analysis       = request.form.get("analysis")

    print(f"""
          Subjects Group : {form_subjects_group}
          Subject        : {form_subject}
          Event          : {form_event}
          Site           : {form_site}
          Sample Type    : {form_sample_type}
          Analysis       : {form_analysis}

           """)
  return render_template("Search.html",
                         logo_image = logo_filename)

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
  '''
  Create the dummy database from the scratch
  '''
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  from WebsitePackage import generate_dummy_db 
  generate_dummy_db.main()
  return render_template("Create_DD.html",
                         logo_image = logo_filename)
