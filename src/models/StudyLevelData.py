"""
This module contains a auxiliar dictionary for StudyLevel class
and it's attibutes as salary_impact_rate, employment_rate, unupdate_rate
"""

STUDY_LEVELS = {
    'elementary':{
        'salary_impact_rate': 0.0,
        'employment_rate': 0.01,
        'obsolescence_rate': 0.1,
    },
    'high_school':{
        'salary_impact_rate': 0.2,
        'employment_rate': 0.1,
        'obsolescence_rate': 0.05,
    },
    'college':{
        'salary_impact_rate': 0.5,
        'employment_rate': 0.3,
        'obsolescence_rate': 0.03,
    },
    'graduate_school':{
        'salary_impact_rate': 0.7,
        'employment_rate': 0.5,
        'obsolescence_rate': 0.01,
    },
}
