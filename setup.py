from setuptools import setup , find_packages

with open("requirements.txt") as f:
   requirements = f.read().splitlines()


setup(
     name='MLOPS_PROJECT-1',
     version = "0.1",
     author = "Mikdat",
     packages = find_packages(),
     install_requires = requirements,   
 

)   

"""pip install -e .   automaticly detect setup.py and run"""