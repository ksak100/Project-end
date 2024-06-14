from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of required libraries
    '''
    hyphen_e="-e ."
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements


setup(
name = "Project end",
version="0.0.1",
author="kunal",
author_email="kunalsingh14091999@gmail.com",
packages=find_packages(),
install_requires = get_requirements("requirements.txt")

)