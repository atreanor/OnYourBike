# OnYourBike

## Description:

## Installation instructions:

### Application server

The Application Server is a Python package. It can be installed by logging onto your webserver and typing `pip install git+https://github.com/atreanor/OnYourBike`

#### EntryPoints:

*weather* - Executes the weather function in the core.py file's main function.

*bikes_dynammic* - Executes the bikes_dynamic function in the core.py file's main function

*bikes_flask* - Executes the bikes_flask function in the core.py file's main function.

### OYB_Database_Server

Create the following tables on your database server:

*JCD_dynamic_data* - Can be created by executing the JCD_dynamic_data.sql create statement

*JCD_flask* - Can be created by executing the JCD_flask.sql create statement

*OWM_current* - Can be created by executing the OWM_current.sql create statement

