# In order to use the Flask instance you have to import it from the script where it has been created
from WebsitePackage import Cov19_msc 
from WebsitePackage import db
from WebsitePackage.db import Base, Session, engine, metadata_obj
from WebsitePackage.models import Subjects_Groups, Subjects, Samples, Sample_Types, Analysis_Types
from WebsitePackage import controller

from flask import Flask, render_template, url_for, request
import os, sqlalchemy
from sqlalchemy import delete
import json

import pandas as pd



subjects_groups_names, sample_types_names, analysis_types_names = controller.initialise_tables()
session = Session()
number_of_sg       = session.query(Subjects_Groups).count()
number_of_samples  = session.query(Samples).count()
number_of_subjects = session.query(Subjects).count()
session.close()

sample_types_table = Sample_Types

@Cov19_msc.route("/")
@Cov19_msc.route("/Home", methods=['GET', 'POST'])
def home_page():
  
  searching_criteria = {}

  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  
  if request.method == "POST":

    searching_criteria['form_subjects_group'] = request.form.get("subjects_group")
    searching_criteria['form_subject']        = request.form.get("subject")
    searching_criteria['form_event']          = request.form.get("event")
    searching_criteria['form_site']           = request.form.get("site")
    searching_criteria['form_sample_type']    = request.form.get("sample_type")
    searching_criteria['form_analysis_type']  = request.form.get("analysis_type")

    print(searching_criteria)
    

    # print(f"""
    #       Subjects Group : {form_subjects_group}
    #       Subject        : {form_subject}
    #       Event          : {form_event}
    #       Site           : {form_site}
    #       Sample Type    : {form_sample_type}
    #       Analysis       : {form_analysis}

    #        """)
    print('Current number of subjects groups - ', number_of_sg) 
    print('Current number of subjects        - ', number_of_subjects)
    print('Current number of samples         - ', number_of_samples)
    try:
      df = controller.dynamic_query(searching_criteria)
      print(df)
    except:
      print('Dynamic query FAILED')
      # df = controller.return_SubjectGroup_table()
      # print(df)
  
  if request.method == "GET":  
    print('A GET REQUEST AS BEEN ISSUED FOR THE HOME PAGE')
  
  df = controller.return_SubjectGroup_table()
  print(df)  
    # try:
    #   controller.test_query()
    # except:
    #   print('test_query FAILED')

  #if request.method == "POST":

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

@Cov19_msc.route("/Search", methods=['GET', 'POST'])
def Search():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')

  # session = Session()
  # sample_types_table = session.query(Sample_Types)                # Fetch SAMPLE TYPES items
  # sample_types_items = [item.sample_type_name for item in sample_types_table.all()]
  # analysis_types_table = session.query(Analysis_Types)
  # analysis_types_items = [item.analysis_type_name for item in analysis_types_table.all()]
  # session.close()
  
  if request.method == "POST":
    try:
      form_data = json.loads(request.data)
      for key, item in form_data.items():
        print('FORM DATA')
        print(key, item)
    except:
      # MESSAGE ????????
      pass
  
  return render_template("Search.html",
                         logo_image = logo_filename,
                         sample_types_names = sample_types_names,
                         analysis_types_names=analysis_types_names)



@Cov19_msc.route("/New_Record", methods=['GET', 'POST'])
def New_Record():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')

  if request.method == 'POST':
    #try:
      print('JQuery DATA')
      form_data = json.loads(request.data)
      print('form_data - ', form_data)
      for key, item in form_data.items():
         print(key, item)
      try:
        controller.test_input(form_data)
      except Exception as err_msg_input:
        print(f'test_input FAILED - {err_msg_input}')

    # except Exception as err_msg:
    #   print(f'JQuery FAILED - {err_msg}')


      
  #if request.method == 'GET':  
    # print('from NEW RECORD page - ', request.form.get('subjects_group'))
    # print('from NEW RECORD page - ', request.form.get('subject_id'))

    # controller.test_input(form_data)
    
  return render_template("NewRecord.html",
                         logo_image = logo_filename, 
                         subjects_groups_names = subjects_groups_names,
                         analysis_types_names=analysis_types_names)



@Cov19_msc.route("/Delete_Record", methods=['GET', 'POST'])
def Delete_Record():
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  if request.method == "POST":
      try:
        form_data = json.loads(request.data)
        for key, item in form_data.items():
          print('FORM DATA')
          print(key, item)
      except:
        # MESSAGE ????????
        pass
    # print('\n*******************************\n',group_id,'\n',description)
    # print(repositories,'\n*******************************\n')

  return render_template("DeleteRecord.html",
                         logo_image = logo_filename,
                         sample_types_names = sample_types_names,
                         analysis_types_names = analysis_types_names)


@Cov19_msc.route("/Create_Dummy_Database")
def Create_DD():
  '''
  Create the dummy database from the scratch
  '''
  logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
  from WebsitePackage import generate_dummy_db, FAST_generate_dummy_db 
  generate_dummy_db.main()
  #FAST_generate_dummy_db
  return render_template("Create_DD.html",
                         logo_image = logo_filename)
