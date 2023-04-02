from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    This function will retrun the list of requirments
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]
        # The `-e .` notation in a **`requirements.txt`** file specifies a 
        # "editable" or "develop" mode install of the current package.
        # This is often used during development when you want to install a
        # package and make changes to it without having to reinstall it 
        # every time. While reading the file we need to remove the notation.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name='mlproject',
    version='0.0.0.1',
    author='James Alvin',
    author_email='jamesalvin49@gmail.com',
    packages=find_packages(),
    # Since there can be many more packages required, instead we will
    # create a function and pass requirement.txt
    # install_requires=[
    #     'numpy>=1.18.0',
    #     'pandas>=1.0.0',
    #     'matplotlib>=3.2.0'
    # ],
    install_requires = get_requirements('requirements.txt')
)
