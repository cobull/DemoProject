##Description
This project demos a Django app connected to a MySQL backend. Specifically, this project includes a login page, a home page, and a "drill-down" page. Once a user logs in via the login page, the user will be redirected to the home page where the data from the MySQL database will be displayed in a table. The user can then click on a row of the table to "drill-down" on that specific data point. The process of "drilling-down" redirects to different page. The user has the option to log out after they are logged in by clicking the log out button.

##Dependencies
Python 3.12.6
Django 5.2
MySQL 8.0.41

##Important Notes
The "settings.py" file has been modified from the working version to not include any sensitive credentials. Specifically, SECRET_KEY, and DATABASES have been modified.

