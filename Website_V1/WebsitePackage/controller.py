# from db import Base, Session
from WebsitePackage.db import Base, Session
#from WebsitePackage.models import SubjectGroup
from WebsitePackage.models import Subjects_Groups, Subjects, Samples, Sites, Events, Sample_Types, Analysis_Types, sample_sampleTypes, sample_analysisType
import pandas as pd

# session = Session()

def initialise_tables():
  """
  This function fetches the table data that must fitted into the dropdown menues and return them 
  """
  session = Session()
  subjects_groups_table = session.query(Subjects_Groups)                                   # Fetch UBJECTS GROUPS records
  subjects_groups_items = [item.subjects_group_id for item in subjects_groups_table.all()]
  sample_types_table = session.query(Sample_Types)                                         # Fetch SAMPLE TYPES records
  sample_types_items = [item.sample_type_name for item in sample_types_table.all()]
  analysis_types_table = session.query(Analysis_Types)                                     # Fetch ANALYSIS TYPES records 
  analysis_types_items = [item.analysis_type_name for item in analysis_types_table.all()]
  session.close()
  return subjects_groups_items, sample_types_items, analysis_types_items

def test_input(form_data):
  session = Session()
  if 'group_id' in form_data:
    print(form_data['group_id'])
    try:
      new_group_inst = Subjects_Groups
      new_group = new_group_inst(subjects_group_id=form_data['group_id'],
                                 site_id = 1)
      session.add(new_group)
      session.commit()
      #session.close()
    except:
      print('Commit was wrong')
      raise

  if 'subject_id' in form_data:
    print(form_data['subject_id'])
    try:  
      new_subject_inst = Subjects
      new_subject = new_subject_inst(subject_id=form_data['subject_id'],
                                     subjects_group_id = 1)
      session.add(new_subject)
      session.commit()
    except:
      print('Commit was wrong')
      raise
  
  session.close()
  


def test_query():
  #try:
    #query = session.query(Subjects).join(Subjects.subjects_groups).filter(Subjects_Groups.subjects_group_id == 'MSC-G-1' ) ###OK
  #  try:
      # How to filter by multiple criteria in Flask SQLAlchemy?
      # https://stackoverflow.com/questions/46141867/how-to-filter-by-multiple-criteria-in-flask-sqlalchemy
    
    session = Session()

    s_group = ''
    subject = 'MSC-210'

    query_cmd = 'session.query('

    tables_lst = []  
    if s_group: tables_lst.append('Subjects')
    if subject: tables_lst.append('Subjects, Samples') 
    tables_lst = set(tables_lst)
    print(tables_lst)

    for table in tables_lst:
      query_cmd += f'{table}, '
    query_cmd = query_cmd[:-2] + ')' # remove the exceding ',' and add ')'


    
    print(query_cmd)  

    

    if s_group: query_cmd += f''
    if subject: query_cmd += f''
    #query = session.query(Subjects).join(Samples).filter(Subjects.subject_id == 'MSC-92').all() #, 
    
    try:
      query=session.query(Subjects, Samples).filter(Subjects.subject_id == 'MSC-202').filter(Samples.subject_id==Subjects.subject_id) ### OK
      query=session.query(Subjects, Samples).join(Samples.sample_types).filter(Subjects.subject_id == 'MSC-202') \
                                                                       .filter(Samples.subject_id==Subjects.subject_id) \
                                                                       .filter(Sample_Types.sample_type_id == 3) ### OK
    except:
      print('QUERY FAILED')

    tab_tuple=query.first()
    tabs_columns_lst = []
    for tab in tab_tuple:
      tabs_columns_lst.append(tab.__table__.columns.keys())
    print('tabs_columns_lst',tabs_columns_lst)

    for i, tc in enumerate(tabs_columns_lst):
      print(f'Columns TABLE {i}')
      print(tc)

    for tab_tuple in query.all():
        for i, tab in enumerate(tab_tuple):
          for col in tabs_columns_lst[i]:
            exec(f'print(tab.{col}, end=\'\t\')')
          if i==1: 
            for i in tab.sample_types:
              print(i.sample_type_id,' - ', i.sample_type_name)
          #if i==1: print(tab.sample_types.sample_type_id)
          #if i==1: print(tab.sample_types)#.sample_type_id, ' - ', tab.sample_types.sample_type_name)
          #if i==1: [print(x) for x in tab.sample_types]
        print('\n------------------')

    session.close()
          
  #  except:
  #    print('|||| Complex query doesn\'t pass ||||')
    #query = session.query(Samples).join(Samples.subjects).filter(Subjects.subject_id == 'MSC-155' )###OK
    #query_columns = query.statement.columns.keys() # https://stackoverflow.com/questions/6455560/how-to-get-column-names-from-sqlalchemy-result-declarative-syntax
    #print(query_columns)

    # for samp in query.all():
    #   #print(samp)
    #   print('--------------')
    #   for column in query_columns:
    #     print('\t',column, end='\r')
    #     cmd_str=f'print(samp.{column})'
    #     exec(cmd_str)
      #print(samp.subject_id,' - ',samp.subjects.subject_id)
      #print(samp.sample_id,' - ',samp.subjects.subjects_group_id)
  #except:
  #  print(' --- SOMETHING WRONG ---')


def dynamic_query(searching_criteria_dict):
  """
  This function receive as input a list searching criteria.
  Then create a query based on the searching criteria provided.
  """

  # Extract the searching criteria
  # The key names in the criteria_dict MUST be the id of the element set in the db model.
  # This because will be used for query directly the database.
  # For instance, if you use the site name you cannot query the Samples table
  # because in there the sites are recorded as ids from the Sites table 
  
  session = Session()

  criteria_dict = {}
  for criteria_key, criteria in searching_criteria_dict.items(): 
    if criteria_key == 'form_subjects_group': criteria_dict['subjects_group_id']  = criteria        # subjects_group_id
    if criteria_key == 'form_subject'       : criteria_dict['subject_id']         = criteria        # subject_id
    if criteria_key == 'form_event'         : 
      event_id = session.query(Events).filter_by(event_name = criteria).first().event_id
      criteria_dict['event_id'] = event_id                                                          # event_id
      #print(criteria_key, criteria, event_id)                                                          
    if criteria_key == 'form_site'          : 
      site_id = session.query(Sites).filter_by(site_name = criteria)
      criteria_dict['site_id'] = analysis_type_id                                                   # site_id
    if criteria_key == 'form_sample_type'   : 
      sample_type_id = session.query(Sample_Types).filter_by(sample_type_name = criteria)
      criteria_dict['sample_type_id'] = sample_type_id                                              # sample_type_id
    if criteria_key == 'form_analysis_type' : 
      analysis_type_id = session.query(Analysis_Types).filter_by(analysis_type_name = criteria)
      criteria_dict['analysis_type_id'] = criteria_key                                              # analysis_type_id


  # # Is there a dynamic query builder for Flask using Sqlalchemy? - BUT THIS IS ONLY FOR QUERY ONE TABLE. WHAT ABOUT MULTY TABLE QUEERING
  # # https://stackoverflow.com/questions/43926883/is-there-a-dynamic-query-builder-for-flask-using-sqlalchemy
  # criteria = {"site_id" : 1}
  # query = session.query(Samples).filter_by(**criteria)
  # for item in query:
  #   print(item.sample_id)

  session.close()
  for k, i in criteria_dict.items():#searching_criteria_dict.items():
    print(k,' - ',i)
  return i

def return_SubjectGroup_table():

  session = Session()

  subject_group_table = session.query(Subjects_Groups)
  table_to_df = pd.DataFrame()
  for sub_gro in subject_group_table.all(): 
    # # SITE
    # sg_site = session.query(Sites)            
    #                  .filter_by(site_id=sub_gro.site_id)
    #                  .first().site_name
    # Subset the subjects that belong to the current subjects group
    subjects_table = session.query(Subjects) \
                            .filter_by(subjects_group_id=sub_gro.subjects_group_id).all()  
                            
    for sub in subjects_table:
      # Subset the samples that belong to the current subject
      samples_table = session.query(Samples) \
                             .filter_by(subject_id=sub.subject_id).all()
      for samp in samples_table: 
        # EVENT
        event = session.query(Events) \
                       .filter_by(event_id=samp.event_id) \
                       .first().event_name         
        # SITE
        samp_site = session.query(Sites) \
                           .filter_by(site_id=samp.site_id) \
                           .first().site_name

        new_row = {'subjects_group_id': sub_gro.subjects_group_id, # SUBJECTS GROUP ID
                   'subject_id'       : sub.subject_id,            # SUBJECT ID 
                   'site'             : samp_site,
                   'event'            : event,
                   'sample_type'      : " | ".join(samp_types.sample_type_name for samp_types in samp.sample_types),
                   'analysis_type'    : " | ".join(analysis_types.analysis_type_name for analysis_types in samp.analysis_types)
                   }
        #print(new_row)
        table_to_df=table_to_df.append(new_row, ignore_index=True)
  #print('*************************************\n*************************************\n*************************************\n')
  #print(table_to_df)
  session.close()


  return table_to_df
