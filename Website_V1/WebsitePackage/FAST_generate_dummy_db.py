from WebsitePackage.db import Base, engine, Session
from WebsitePackage.models import Subjects_Groups, Subjects, Samples, Sites, Events, Sample_Types, Analysis_Types, sample_sampleTypes, sample_analysisType
import random
import copy

# RESET EVERYTHING
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

subjectgroup_description =['Male London', 'Female Surrey', 'Health Workers', 'Elder subjects', 
                           'Liverpool group', 'Subjects over 80', 'Male Surrey', 'Health Workers 40']

sites_list = ['University of Surrey', 'University of Sussex', 'University of Cambria', 'University of Sunderland', 'University of Suffolk', 
              'University of Cambridge', 'University of Oxford', 'University of Edinburgh',
              'Queen Mary Hospital', 'Charing Cross Hospital', 'Chelsea and Westminster Hospital', 'Queen Charlotte''s and Chelsea Hospital', 
              'St Thomas'' Hospital', 'University College Hospital', 'University Hospital Wishaw']

analysis_types_list = ['SWATH Proteomic', 'Proteomic', 'Metabolomic', 'Lipodomic']

protocol_type = ['Metabolomic/Lipodomic-V0.4', 'Proteomic-V0.2', 'HDX-MS-2020']

data_processing_type = ['MetaboSoft', 'FindProt', 'LipoLevel']

repository_name = ['PRIDE', 'MetaboLight', 'ZENODO']

researcher_name = ['Mark Spence', 'Olive Yew', 'Aida Bugg', 'Peg Legge', 'Teri Dactyl', 'Allie Grater', 'Liz Erd', 
                    'Constance Norin', 'Minnie Ryder', 'Lynn O’Leeum', 'Ray O’Sun', 'Isabelle Ring']               


subjectgroup_descriptions = ['Male London', 'Female Surrey', 'Health Workers', 'Elder subjects', 
                             'Liverpool group', 'Subjects over 80', 'Male Surrey', 'Health Workers 40']


project_titles = ['Proteomics Investigation of protein RTD4654', 'Metabolomic Comparative Study', 'Lipodomics fingerprint of Covid19', 'Metabolomics Investigation',
                  'Cov19 Proteomic profile', 'Metabolomic Assessment for Covid19']






def random_series(randomizable_list, n):
    import random

    out_rand_list = []
    past = []              # The list for holding the previous random results
    for i in range(0,n):
        new_rand = True 
        if len(past) == len(randomizable_list): past = [] # When all the elements have been drew then restart the 'past' list
        while new_rand:
            rand_choice = random.choice(randomizable_list)
            if (rand_choice not in past):
                past.append(rand_choice)
                out_rand_list.append(rand_choice)
                # print(i,' - ',rand_choice)
                new_rand = False
    return out_rand_list

def select_repository(target_string):
    if 'proteomic'   in target_string.lower(): return 1
    if 'metabolomic' in target_string.lower(): return 2
    if 'lipodomic'   in target_string.lower(): return 3
    else: return 1

def select_protocol(target_string):
    if 'proteomic' in target_string.lower(): return 2
    if 'metabolomic' in target_string.lower(): return 1
    if 'lipodomic'   in target_string.lower(): return 3

def select_samprocess(target_string):
    if 'proteomic' in target_string.lower(): 
        choice=random.choice([1,2])
        return choice
    if 'metabolomic' in target_string.lower(): return 3
    if 'lipodomic'   in target_string.lower(): return 4




# ======================================================================================== #
#                                           V3
# ======================================================================================== #

n_subj_group = 10
n_subjects = 5


"""
This database reflect the schema created on 14/11/2022
"""
session = Session()

events_list       = ["First Sample", "Second Sample", "Third Sample"]
sample_types_list = ["Serum", "Sebum", "Saliva"]
sites_list        = ["Surrey", "ISARIC", "PHOSP"]


print(''' 
------
Events
------ 
''')
event_types_inst = Events
for event_type_name in events_list:
    new_event_type = event_types_inst(event_name=event_type_name)
    session.add(new_event_type)
    session.commit()

event_t = session.query(Events)
for i in event_t.all(): print(f'{i.event_id}\t-\t{i.event_name}')
session.close()

print(''' 
-----
Sites
----- 
''')
sites_inst = Sites
for site_name in sites_list:
    new_site = sites_inst(site_name=site_name)
    session.add(new_site)
    session.commit()

site_t = session.query(Sites)
for i in site_t.all(): print(f'{i.site_id}\t-\t{i.site_name}')
session.close()

print(''' 
------------
Sample_Types
------------ 
''')
sample_types_inst = Sample_Types
for sample_type_name in sample_types_list:
    new_sample_type = sample_types_inst(sample_type_name=sample_type_name)
    session.add(new_sample_type)
    session.commit()

sample_t = session.query(Sample_Types)
for i in sample_t.all(): print(f'{i.sample_type_id}\t-\t{i.sample_type_name}')
session.close()

print(''' 
--------------
Analysis_Types
-------------- 
''')
analysis_types_inst = Analysis_Types
for analysis_type_name in analysis_types_list:
    new_analysis_type = analysis_types_inst(analysis_type_name=analysis_type_name)
    session.add(new_analysis_type)
    session.commit()

analysis_t = session.query(Analysis_Types)
for i in analysis_t.all(): print(f'{i.analysis_type_id}\t-\t{i.analysis_type_name}')
session.close()

print(''' 
---------------
Subjects_Groups
--------------- 
''')
subj_group_inst = Subjects_Groups
for project in range(1, n_subj_group):
    project_code = "MSC-G-" + str(project)
    new_subj_group = subj_group_inst(subjects_group_id=project_code,
                                     site_id          =1
                                     )
    session.add(new_subj_group)
    session.commit()

subjects_groups = session.query(Subjects_Groups)
for i in subjects_groups.all(): print(f'{i.subjects_group_id}\t-\t{i.site_id}')
session.close()

print(''' 
--------
Subjects
-------- 
''')
subjects_inst = Subjects
subj_id = random.sample(range(1, 500), n_subjects) # The subjects id list must be assigned below to the samples generation
subjects_groups = session.query(Subjects_Groups)
subjects_groups_list = [sbj_g.subjects_group_id for sbj_g in subjects_groups.all()]
for subject in subj_id:
    new_subject = subjects_inst(subject_id="MSC-" + str(subject),
                                subjects_group_id=random.choice(subjects_groups_list)
                                )
    session.add(new_subject)
    session.commit()

subjects = session.query(Subjects)
for i in subjects.all(): print(f'{i.subject_id}\t-\t{i.subjects_group_id}')
session.close()

print(''' 
--------
Samples
-------- 
''')
samples_inst = Samples
subj_id = session.query(Subjects)
subj_id_list = [s_id.subject_id for s_id in subj_id.all()]

for subject in subj_id_list:
    number_of_samples = random.randint(1,3)         # How many samples for this subject
    site = random.randint(1,len(sites_list))                # The site for all the sample is defined before the generation of the random samples
    for event_number in range(1,number_of_samples): # The event First - Second - Third sample are defined before the sample type and analysis

        type_of_samples   = random.sample(sample_types_list, number_of_samples) # Which type of samples for this subject 
        #print(type_of_samples)
        for sample_type in type_of_samples:
            number_of_analysis  = random.randint(1,3)           
            types_of_analysis   = random.sample(analysis_types_list, number_of_analysis)
            #types_of_analysis   =random_series(analysis_types_list, number_of_analysis)
            #print(types_of_analysis)
            for analysis_name in types_of_analysis:
                sample_type_record   = session.query(Sample_Types).filter_by(sample_type_name=sample_type).first()
                analysis_type_record = session.query(Analysis_Types).filter_by(analysis_type_name=analysis_name).first()
                
                # Add the new sample
                new_sample = samples_inst(subject_id=subject,
                                          event_id=event_number,
                                          site_id=site
                                          )
                session.add(new_sample)
                session.commit()
                sample_id=session.query(Samples).count() # Fetch the id of the LAST SAMPLE recorded

                
                # https://stackoverflow.com/questions/21667215/populating-a-sqlalchemy-many-to-many-relationship-using-ids-instead-of-objects
                # Connect the sample with the sample type
                session.execute(sample_sampleTypes.insert()
                       .values([(sample_id, sample_type_record.sample_type_id)]))
                # Connect the sample with the analysis type
                session.execute(sample_analysisType.insert()
                       .values([(sample_id, analysis_type_record.analysis_type_id)]))
                
                #print(f'{subject} - {sample_id} - {sample_type} - {analysis_name}')


samples = session.query(Samples)
for i in samples.all():
    # Query a many to many
    # https://stackoverflow.com/questions/12593421/sqlalchemy-and-flask-how-to-query-many-to-many-relationship 
    #print(f'{i.sample_id}\t-\t{i.subject_id}\n{i.event_id}\t-\t{i.site_id}')

    samples = session.query(Samples).filter_by(sample_id=i.sample_id).all()

    for sample in samples:
        # subjects   = sesion.query(Subjects).filter_by(subject_id=sample.subject_id).first()
        # subj_group = session.query

        print(sample.subject_id,
              " - ",session.query(Subjects).filter_by(subject_id=sample.subject_id).first().subjects_group_id,
              " - ",sample.sample_id,
              " - ",session.query(Events).filter_by(event_id=sample.event_id).first().event_name,
              " - ",session.query(Sites).filter_by(site_id=sample.site_id).first().site_name,
              " - "," | ".join(sample_types.sample_type_name for sample_types in sample.sample_types),
              " - "," | ".join(analysis_types.analysis_type_name for analysis_types in sample.analysis_types)
              )
session.close()


# def main():

#     db_V3()
#     print('Database RESET')



# if __name__ == '__main__':
#     main()