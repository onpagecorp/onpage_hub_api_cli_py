from setuptools import setup

__author__ = 'Onset Technology'

setup(
    name='OnPage HUB API CLI',
    version='0.1.0.1',
    author='Onset Technology',
    author_email='support@onsettechnology.com',
    packages=[],
    scripts=[] ,
    url='http://www.onpage.com',
    license='LICENSE',
    description='CLI to send Page to OnPage Pager using OnPage HUB API',
    long_description=open('README').read(),
    install_requires=[
        "OnPage-HUB-API-Client >= 0.1.0",
        ],
)
