![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/logo.png?raw=true)
![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/home.png)
![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/config.png)
i![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/manual.png)
i![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/unit.jpeg)

To Install:
1. First make sure you are using pipenv.  Use "pipenv install" to install dependencies.
2. Some dependencies need to be installed locally outside of pipenv.  Make sure you have "RPi.GPIO installed" using "sudo apt-get install RPi.GPIO".
3. PIrigation uses SQLite.  After installing dependencies, navigate to root of flask project, then open a Python REPL. 
  Type in:  
    1. "from pirigation import db", 
    2. "db create_all()"
  This creates the database and database tables.
4. To run with flask, navigate to root of flask directory where "start.py" file is located.  Run python3.7 start.py 
4a. Need to upgrade to python 3.9.

ToDo:
Need to rewrite database tables to work with new weather methods.
Need to rewrite weather module. Currently it is broken as I am changing from darksky since Apple owns it now and wants to charge for its use.

Scrap the whole damn project!
[![GitHub license](https://img.shields.io/badge/Build-failing-red)](https://github.com/equineranch/desk_control)
