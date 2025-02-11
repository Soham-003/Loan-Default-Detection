from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e."

def get_requirements(file_path:str):
    requirements = []
    
    with open(file_path,'r') as file:
        
        requirements = file.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name = "Loan Default Prediction",
    version = "0.1",
    author = "Soham Khanna",
    author_email = "sohamsawankhanna@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)


