# from db import Base, Session
from WebsitePackage.db import Base, Session
from WebsitePackage.models import SubjectGroup

import pandas as pd

session = Session()

def return_SubjectGroup_table():
  subject_group_table = session.query(SubjectGroup)
  df = pd.DataFrame()
  for row in subject_group_table.all(): #
    new_row = {'group_id': row.group_id, 
               'description': row.description, 
               'repositories': row.repositories}
    #print(new_row)
    df=df.append(new_row, ignore_index=True)
    #print(df)
  return df
