

"""
Usage:
    python setup.py py2app
"""
#Exporting game to app on osx

from setuptools import setup

APP = ['main.py']
DATA_FILES = [('', ['assets']), ('', ['fx']), ('', ['music']), ('', ['screens']), ('', ['music']), ('', ['fonts'])]
OPTIONS = {'iconfile':'logo.icns',} # 'argv_emulation': False/True
setup(

    app = APP,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],
)