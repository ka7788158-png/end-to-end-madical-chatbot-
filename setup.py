from setuptools import find_packages, setup

setup(
    name = 'Generative AI Project',
    version = '0.0.0',
    author = 'Kavya Agrawal',
    author_email = 'ka7788158@gmail.com',
    packages = find_packages(), # try to find __init__.py
    install_requires = []
)

# before doing this , if u try to write piplist on terminal u will find nothing 
# but after this 
# Generative AI Project will be there 

## Purpose
# Makes your project installable
# Organizes your project as a proper package
# Helps in production-level deployment