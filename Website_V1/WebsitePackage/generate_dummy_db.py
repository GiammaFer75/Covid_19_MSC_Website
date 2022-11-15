from WebsitePackage.db import Base, engine, Session
from WebsitePackage.models import SubjectGroup, Projects, Institutions, Sample_Processing, Protocols, Data_Processing, Repositories, Researchers
from WebsitePackage.models import Subjects_Groups, Subjects, Samples, Sites, Events, Sample_Types, Analysis_Types, sample_sampleTypes, sample_analysisType
import random
import copy

# RESET EVERYTHING
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

subjectgroup_description =['Male London', 'Female Surrey', 'Health Workers', 'Elder subjects', 
                           'Liverpool group', 'Subjects over 80', 'Male Surrey', 'Health Workers 40']

institution_names = ['University of Surrey', 'University of Sussex', 'University of Cambria', 'University of Sunderland', 'University of Suffolk', 
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




def db_V1():
    session = Session()
    subj_group_tab = SubjectGroup

    descript_vect = ['Male London', 'Female Surrey', 'Health Workers', 'Elder subjects', 
                     'Liverpool group', 'Subjects over 80', 'Male Surrey', 'Health Workers 40'
    ]
    repos_vect = ['PRIDE,MetaboLight', 'ZENODO', 'PRIDE,ZENODO','PRIDE,MetaboLight,ZENODO',
                  'PRIDE, ZENODO', 'MetaboLight,ZENODO', 'PRIDE,MetaboLight,ZENODO', 'PRIDE,MetaboLight,ZENODO'
    ]
    for ind, desc in enumerate(descript_vect):
        new_group = subj_group_tab(description=desc, repositories=repos_vect[ind])
        session.add(new_group)
        session.commit()




def db_V2(n_projects = 5):
    '''
    Generate a dummy database using the fisical model that is related only to the OMICS FEATURES
    '''
    session = Session()
    
    print('''
*********************
GENERATE FIXED TABLES
*********************
          ''')

    print(''' 
------------
Institutions
------------ 
          ''')
    institution_tab  = Institutions
    for ind, institution in enumerate(institution_names):
        new_institution = institution_tab(inst_name=institution, 
                                          address= 'Street of ' + institution + ' ' + institution[-1].upper() 
                                          + str(ind) + ' ' + institution[-4:-2].upper())
        session.add(new_institution)
        session.commit()

    inst_tab = session.query(Institutions)
    for i in inst_tab.all(): print(f'{i.institution_ID}\t-\t{i.inst_name}\t-\t{i.address}')


    print(''' 
-----------------
Sample_Processing
----------------- 
          ''')

    samp_process_tab = Sample_Processing
    for p_type in analysis_types_list:
        new_samp_process = samp_process_tab(processing_type=p_type)
        session.add(new_samp_process)
        session.commit()

    samp_process = session.query(Sample_Processing)
    for i in samp_process.all(): print(f'{i.processing_ID}\t-\t{i.processing_type}')


    print(''' 
--------
Protocol
-------- 
          ''')

    protocols_tab = Protocols
    for prot_type in protocol_type:
        new_protocol = protocols_tab(protocol_type=prot_type)
        session.add(new_protocol)
        session.commit()

    protocol = session.query(Protocols)
    for i in protocol.all(): print(f'{i.protocol_ID}\t-\t{i.protocol_type}')


    print(''' 
---------------
Data_processing
--------------- 
          ''')
    data_process_tab = Data_Processing
    for dapro_type in data_processing_type:
        new_data_process = data_process_tab(processing_type=dapro_type)
        session.add(new_data_process)
        session.commit()

    data_process = session.query(Data_Processing)
    for i in data_process.all(): print(f'{i.processing_ID}\t-\t{i.processing_type}')


    print(''' 
------------
Repositories
------------ 
          ''')
    repositories_tab = Repositories
    for repo in repository_name:
        new_repository = repositories_tab(name=repo)
        session.add(new_repository)
        session.commit()

    repositories = session.query(Repositories)
    for i in repositories.all(): print(f'{i.repository_ID}\t-\t{i.name}')


    print(''' 
-----------
Researchers
----------- 
          ''')
    researchers_tab  = Researchers
    for researcher in researcher_name:
        new_researcher = researchers_tab(name = researcher,
                                         institution_ID = 1)
        session.add(new_researcher)
        session.commit()

    researchers = session.query(Researchers)
    for i in researchers.all(): print(f'{i.researcher_ID}\t-\t{i.name}\t-\t{i.institution_ID}')


#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§


    print('''\n\n\n
++++++++++++++++++++++++
GENERATE VARIABLE TABLES
++++++++++++++++++++++++
          ''')

    print(''' 
------------
SubjectGroup
------------ 
          ''')
    n_groups = 10
    subj_group_tab = SubjectGroup
    
    # Prepare data for a new record
    description     = random_series(subjectgroup_descriptions, n_groups)
    group_size      = random.sample(range(50,400),n_groups)
    n_institutions   = session.query(Institutions).count()
    institution_ID  = random.sample(range(1,n_institutions),n_groups)

    for ind, sub_gro_desc in enumerate(description):
        new_subject_group = subj_group_tab(description    = sub_gro_desc,
                                           group_size     = group_size[ind],
                                           institution_ID = institution_ID[ind])
        session.add(new_subject_group)
        session.commit()

    subj_grou = session.query(SubjectGroup)
    
    for i in subj_grou.all():
        inst = session.query(Institutions).filter_by(institution_ID = i.institution_ID).one() 
        print(f'{i.group_id}\t-\t{i.description}\t-\t{i.group_size}\t-\t{inst.inst_name}')


    print(''' 
--------
Projects
-------- 
          ''')

    n_projects= 20
    def pl(l):
        print(f'\n{len(l)}')
        print(l)

    projects_tab   = Projects

    # Prepare data for a new record
    accession_code       = ["#MSC"+str(i) for i in range(n_projects)]
    pl(accession_code)
    project_title        = random_series(project_titles, n_projects)
    pl(project_title)
    researcher_ID        = random_series(researcher_name, n_projects)
    pl(researcher)
    institution_ID       = random_series(institution_names, n_projects)
    pl(institution_ID)
    sample_processing_ID = [select_samprocess(title) for title in project_title] #random_series(analysis_types_list, n_projects)
    pl(sample_processing_ID)
    protocol_ID          = [select_protocol(title) for title in project_title] #random_series(protocol_type, n_projects)
    pl(protocol_ID)
    data_processing_ID   = random_series(data_processing_type, n_projects)
    pl(data_processing_ID)
    repository_ID        = [select_repository(title) for title in project_title]
    pl(repository_ID)
    
    for ind in range(n_projects):
        #print(institution_ID[ind])
        #print('sample_processing_ID -',sample_processing_ID[ind])
        new_project = projects_tab(accession_code     = accession_code[ind], 
                                   group_ID           = 0,
                                   project_title      = project_title[ind],
                                   researcher         = session.query(Researchers)
                                                               .filter_by(name = researcher_ID[ind]).first()
                                                               .researcher_ID,
                                   institution_ID     = session.query(Institutions)
                                                               .filter_by(inst_name = institution_ID[ind]).first()
                                                               .institution_ID,
                                   processing_type_ID = session.query(Sample_Processing)
                                                               .filter_by(processing_ID = sample_processing_ID[ind]).first()
                                                               .processing_ID,
                                   protocol_ID        = session.query(Protocols)
                                                               .filter_by(protocol_ID = protocol_ID[ind]).first()
                                                               .protocol_ID,
                                   data_processing_ID = session.query(Data_Processing)
                                                               .filter_by(processing_type = data_processing_ID[ind]).first()
                                                               .processing_ID, 
                                   repository_ID      = session.query(Repositories) 
                                                               .filter_by(repository_ID = repository_ID[ind]).first()
                                                               .repository_ID
                                   )
        session.add(new_project)
        session.commit()

    project = session.query(Projects)
    inst = session.query(Institutions).filter_by(institution_ID = i.institution_ID).one()
    for i in project.all(): print(f'''
{i.accession_code}
    Subject Group Reference - {i.group_ID}
    Project Title           - {i.project_title}
    Researcher              - {[r.name for r in session.query(Researchers).filter_by(researcher_ID = i.researcher)]}
    Institution             - {session.query(Institutions).filter_by(institution_ID = i.institution_ID).first().inst_name}
    Sample Processing       - {session.query(Sample_Processing).filter_by(processing_ID = i.processing_type_ID).first().processing_type}                                
    Protocol                - {session.query(Protocols).filter_by(protocol_ID = i.protocol_ID).first().protocol_type}                                
    Data Processing         - {session.query(Data_Processing).filter_by(processing_ID = i.data_processing_ID).first().processing_type}                                
    Repository              - {session.query(Repositories).filter_by(repository_ID = i.repository_ID).first().name}                                      
                                    ''')



    print(''' 
^^^^^^^^^^^^^^^^^^^^^
POPULATE MANY-TO-MANY
^^^^^^^^^^^^^^^^^^^^^
          ''') 
    add_researcher = Researchers

    project_records = session.query(Projects)
    total_researchers_names = session.query(Researchers).count()
    for project in project_records.all():
        # Randomise how many researchers are involved in this project
        number_of_researchers = random.randint(1,total_researchers_names)
        for current_researcher in range(1,number_of_researchers+1):
            # Move to the current reasearcher record in the table Researchers
            researcher = session.query(Researchers).filter_by(researcher_ID=current_researcher).first()
            add_reseracher_record = add_researcher(researcher_ID  =researcher.researcher_ID,
                                                   name           =researcher.name,
                                                   institution_ID =researcher.institution_ID
                                                  )
            # Append the relationship
            project.researchers.append(researcher)
            session.commit()
        #print(project.researchers)




def db_V3(n_subj_group = 5, n_subjects = 30,
          sites_list = institution_names):
    """
    This database reflect the schema created on 14/11/2022
    """
    session = Session()

    events_list       = ["First Sample", "Second Sample", "Third Sample"]
    sample_types_list = ["serum", "sebum", "saliva"]
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


    print(''' 
---------------
Subjects_Groups
--------------- 
    ''')
    subj_group_inst = Subjects_Groups
    for project in range(1, n_subj_group):
        project_code = "MSC-G-" + str(project)
        new_subj_group = subj_group_inst(subjects_group_id=project_code,
                                         site_id          =0
                                         )
        session.add(new_subj_group)
        session.commit()

    subjects_groups = session.query(Subjects_Groups)
    for i in subjects_groups.all(): print(f'{i.subjects_group_id}\t-\t{i.site_id}')

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
                                    subject_group_id=random.choice(subjects_groups_list)
                                    )
        session.add(new_subject)
        session.commit()

    subjects = session.query(Subjects)
    for i in subjects.all(): print(f'{i.subject_id}\t-\t{i.subject_group_id}')

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
                  " - ",session.query(Subjects).filter_by(subject_id=sample.subject_id).first().subject_group_id,
                  " - ",sample.sample_id,
                  " - ",session.query(Events).filter_by(event_id=sample.event_id).first().event_name,
                  " - ",session.query(Sites).filter_by(site_id=sample.site_id).first().site_name,
                  " - "," | ".join(sample_types.sample_type_name for sample_types in sample.sample_types),
                  " - "," | ".join(analysis_types.analysis_type_name for analysis_types in sample.analysis_types)
                  )
#         print(f"""

# Sample - {i.sample_id}
#        Subject - {i.subject_id}
#        {i.event_id}\t-\t{i.site_id}
#        Sample type - {" | ".join(sample_types.sample_type_name for sample_types in sample.sample_types)}
#        Analysis type - {" | ".join(analys_types.analysis_type_name for analys_types in sample.analysis_types)}
#         """)


def main():

    db_V3()
    print('Database RESET')



if __name__ == '__main__':
    main()