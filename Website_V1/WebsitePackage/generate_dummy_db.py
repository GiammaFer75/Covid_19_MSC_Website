from db import Session
from models import SubjectGroup


def main():
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

    print('Database RESET')

if __name__ == '__main__':
    main()