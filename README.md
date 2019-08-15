![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/logo.png?raw=true)
![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/home.png)
![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/config.png)
i![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/manual.png)
i![image](https://github.com/equineranch/PIrigation/blob/master/pirigation/static/images/unit.jpeg)

To Install:
1. First make sure you are using pipenv.  Use "pipenv install" to install dependencies.
2. Some dependencies need to be installed locally outside of pipenv.  Make sure you have "RPi.GPIO installed" using "sudo apt-get install RPi.GPIO".
3. PIrigation uses SQLite.  After installing dependencies, navigate to root of flask project, then open a Python REPL. 
    Type in:  "from pirigation import db", then "db create_all()"
    This creates the database and database tables.
4. To run with flask, navigate to root of flask directory where "start.py" file is located.  Run python3.7 start.py

ToDo:
Need to rewrite database tables to work with new weather methods.
Need to rewrite weather module. Currently it is broken.
Need to rewrite entire app I am so pissed right now.