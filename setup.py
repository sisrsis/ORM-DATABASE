from setuptools import setup ,find_packages


setup(
   name='orm_database',
   version='0.3.7',
   description='This module is written to launch your programs with any database you want in the shortest time ',
   license="MIT",
   author='SISRSIS',
   author_email='virussisrsis@gmail.com',
   url="https://github.com/sisrsis/orm-database",
   packages=find_packages(),  #same as name
   install_requires=['asyncpg','motor','mariadb'], #external packages as dependencies

)
