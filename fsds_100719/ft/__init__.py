"""A collection of submodules by online-ds-ft-100719.
Maintained by James Irving (GitHub: jirvingphd)
james.irving@flatironschool.com
"""
# from ..imports import *
def quick_ref(topic='student_resource_folder'):
    """Displays quick reference url links and info.
    Args:
        topic (str): selects which reference info to show.
            - `student_resource_folder` : data science gdrive url
            - `fsds` :documentaion url"""
            
    if 'student_resource_folder' in topic:
        print('Data Science Student Resources:')
        print('https://flatiron.online/StudentResourcesGdrive')
        
    if 'fsds' in topic:
        print('fsds_100719 Package Documentation:')
        
def placeholder():
    pass