from setuptools import setup, find_packages
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirements(path)->List[str]:
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    
    return requirements
    
setup(
    name='ML-projects',
    version='1.0',
    author='Pranay',
    author_email='pranaynavoth.236@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)