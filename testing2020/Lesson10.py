from pywebcopy import save_webpage
kwargs = {'project_name': 'LibraryLesson10'}
save_webpage(
    url='https://180atlas.com/index.html',
    project_folder='path/to/downloads',
    **kwargs
)