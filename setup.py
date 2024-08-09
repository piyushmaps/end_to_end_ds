from setuptools import find_packages, setup
from typing import  List



def get_requirements(file_path:str)->List[str]: #this function is returning list of string
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.read()
        requirements=[req.replace("\n","") for req in requirements]
        return requirements
   
setup(
    name="end_to_end_ds",
    version="0.0.1",
    author="Piyush thakur",
    author_email="piyushthakur3613@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)