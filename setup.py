from setuptools import setup,find_packages
from typing import List
#Variable declaration
PROJECT_NAME="House_Rent_Prediction"
VERSION="0.0.3"
AUTHOR="MANJUNATH"
DESCRIPTION="This is demo project"

REQUIREMENT_FILENAME="requirements.txt"


"""This function will return all the list of requirements mention in the requirements.txt file"""
def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILENAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


#Setup file
setup(name=PROJECT_NAME,
 version=VERSION,
 author=AUTHOR,
 description=DESCRIPTION,
 packages=find_packages(),
 install_requires=get_requirements_list()
 )

