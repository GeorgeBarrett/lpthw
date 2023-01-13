try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'example of a project skeleton',
    'author': 'george',
    'URL': '(the URL)',
    'download_url': '(the download URL)',
    'author email': 'georgeaustinbarrett@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['project'],
    'scripts': [],
    'name': 'project'
}

setup(**config)