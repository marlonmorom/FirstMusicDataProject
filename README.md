# First Project from Udacity's Data Engineering Nanodegree

This project uses PostgreSQL database and the psycopg2 library in order to apply an ETL process using real data, namely, from the Million Song Dataset.

## Files Description

### create_tables.py

This code is used whenever we want to drop all the existing tables and create new ones, also setting up the sparkify database, which is our main database in this project.


### sql_queries.py

File containing all the creation, dropping and value's insertion set-up codes. It shows how the tables are going to be generate, their columns' names and types,
the codes from dropping each table, and how the data insertion proceeds in each one of these referred tables.

### etl.ipynb

Jupyter notebook file that has each step of the ETL process. You can use this file to ensure that each step is correct, before completing the etl.py code.

### etl.py

This file contains the code necessary to the ETL process.

### test.ipynb

As the name says, this file has the codes from testing your progress. Each code session test some part of your project, and you can use this file to assure that your code
is working in the intended way. 


### Observations

You have to configure before hand an PostgreSQL database, with the name of studentdb, with user student and password student. If you want to connect with your own user,
you will have to change the connection code with your credentials.<br>
And before running the ETL and test codes, it is good practice to run the create_tables.py file, in order to restart your tables.
By default, postgreSQL does not prevent that you add the same row twice or more times.

### Data Description

The data is stored in JSON files. We can split the files in two categories: song data and log data.

We have multiples folders for each category. In the song data folders, each subfolder represents one letter of the song data ID.<br>
In the log folder, each file contains an event that was generated using  an event simulator, based on the songs from the song data files.
