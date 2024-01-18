from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT='-e .'

'''def get_requirements(file_path:str)->List[str]:
     requirements=[]
     with open(file_path) as f:
          requirements=f.readlines()
          requirements=[req.replace("\n"," ")for req in requirements]
          
          if HYPEN_E_DOT in requirements:
               requirements.remove(HYPEN_E_DOT)
     return requirements'''


with open('README.md','r',encoding='utf-8') as f:
     long_description=f.read()
     
     
__version__="0.0.4"
REPO_NAME="pypi_project"
PKG_NAME="databaseautomation"
AUTHOR_USER_NAME="vikalp026var"
AUTHOR_EMAIL="vikalp026varshney@gmail.com"

setup(
     name=PKG_NAME,
     version=__version__,
     author=AUTHOR_USER_NAME,
     author_email=AUTHOR_EMAIL,
     description='A python package for connecting with  database.',
     long_description=long_description,
     long_description_content="text/markdown",
     url=f"https://github.com/{AUTHOR_USER_NAME}/pypi_project.git"
     project_urls={
          "Bug Traker":f"https://github.com/{AUTHOR_USER_NAME}/pypi_project/issues",
     },
     package_dir={"":"src"},
     packages=find_packages(where="src"),
          
     
)
