# Flask Interview Test

This is a repo designed to test basic Flask knowledge for potential candidates.

## The Task
Candidates are asked to create an additional endpoint in order to display information about the interviews scheduled. A candidate should create the route, access the data from the SQLite database, and then render the page using a Jinja2 template.


## Files
app.py: contains the routes for the application. This should be modified for the test.\
config.py: configuration for the app and database\
data_setup.py: a helper file to set up dummy data\
model.py: contains the data model for the application\
templates: directory containing html templates to be rendered by the application

## Running Flask

Because we have set our app up as simply as possible, running the application is as easy as activating the virtual environment:
```shell script
venv\Scripts\activate
```

and then executing the flask run command:
```shell script
flask run
```

To ensure you aren't blocked by a port that is taken already, run with the -p command:
```shell script
flask run -p 5002
```