#!/usr/bin/env python
# coding: utf-8

# #### with the help of setup.py we will be able to use this ML project as packages and it will the be used to installed for different models

# In[33]:


from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    """
    this function takes file_path as string ,the file will contain list of 
    packages as per our requirements and return the list of requirements line
    by line
    
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements     

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Shivam',
    author_email = 'shekharshivam333@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)






