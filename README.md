# OnYourBike

## Description:

## Installation instructions:

### Application server

The Application Server is a Python package. It can be installed by logging onto your webserver and typing `pip install git+https://github.com/atreanor/OnYourBike`

#### EntryPoints:

*weather* - Executes the weather function in the core.py file's main function.

*bikes_dynammic* - Executes the bikes_dynamic function in the core.py file's main function

*bikes_flask* - Executes the bikes_flask function in the core.py file's main function.

#### Note

On a linux server, each entry point can be run as a background process by using the ampersand sign (&). The screen command can be used to create an environment that runs when the SSH connection to the server is terminated.

### Database Server

Create the tables below by executing the SQL create statements that are stored in this repository's docs/SQL folder:

*JCD_dynamic_data* - This is used for analytics purposes only. Contains historic JCdecaux bike data for all stations.

*JCD_flask* - Contains the current JCdecaux static and dynamic station information for each station

*OWM_current* - Contains weather data for Dublin


### OYB_WebServer

Clone the github repository by typing:
`git clone https://github.com/atreanor/OnYourBike.git`

If you are using Nginx or another webserver that isn't Flask's built-in development server:

Copy the *OYB_WebServer* directory into the webserver folder. For example in bash:
`cp -r /OYB_WebServer/ /home/www`

Open the Flask app directory (OnYourBike) and export the flask app run.py file:
`export FLASK_APP=run.py`

Start the webserver (Nginx using gunicorn):
`gunicorn --bind 0.0.0.0:8000 run:app`


