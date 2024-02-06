from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List:
    '''
    this function will return te list of requiremnts

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name= 'ML_1',
    version='0.0.1',
    author='Neel',
    author_email='neeljshani@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)