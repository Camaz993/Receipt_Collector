# INFO310
## Receipt Collector

Alex, Caleb, Kurt, Mackenzie


## Architecture

Predominantly web based application which exposes a REST framework, based on the Django web framework and the Python programming language.

## Development Environment

This project requires a version of Python above 3.6. 

The python package manager Pip is required to download Django and other dependencies.

To keep project packages isolated, the project dependencies are kept in something called a virtual environment (virtualenv).

Installation instructions are different across operating systems, but in general, it's in this order:

* Install Python 3+
* Install pip
* From a command line, run `pip install virtualenv`. 
* Clone this repository in to an appropriate directory, then change in to this directory.
* Run the command `virtualenv venv`. This creates a virtual environment named `venv`. Note that this needs to create a Python 3 virtual environment - if you need to specify this, it'll be similar to `virtualenv -p /usr/bin/python3 venv`
* Activate the virtual environment. For a Windows environment, this will be running the command `venv\Scripts\activate.bat` within cmd.exe. For MacOS / Linux, this will be `source venv/bin/activate`
* Install requirements within this virtual environment. `pip install -r requirements.txt`

## Project Architecture

Django makes a distinction between a project (ie: this whole repository) and an app which implements certain functionality.

In this project, there are currently two apps - `framework` for the models and REST API, `frontend` for the user facing website.

```
core/               Common project files
    settings.py     Settings for the whole project (ie debug, database, static files, middleware)
    urls.py         URL routing for whole project (will point to urls.py in individual apps)
    wsgi.py         Used when starting project (web server gateway interface)
    
framework/          REST API
    migrations/     Database migrations (Generated code to convert the model's Python to SQL)
    models/         Models - can be compared to the data structure of objects, or database tables.
                    Each model will be in its own .py file, rather than one big models.py file.
                    Therefore, we will need to manually add new models to the __init__.py file
    admin.py        Connects models to Django's built in admin site (useful for development, less so for end product)
    apps.py         Name of app (imported in core/settings.py)
    tests.py        Test cases for app
    views.py        Each serialiser for the REST framework will be defined here.
    urls.py         Routing - make a link for each view to be accessed from
    
frontend/           Web (HTML/CSS) frontend
    [most of the structure is the same as above]
    templates/
        frontend/   HTML templates, filled with Django {% tags %} then rendered at load time
                        Note that this is in a named subdirectory - Django collates files across apps
                        such that this is required to avoid files conflicting
    models.py       Models specific to ONLY the web front end (most models will need to be imported from the framework)
    views.py        Pass in / process data before rendering a web page from a template
    
templates/          Common web files for the whole project
    css/            
    js/
    _layout.html    Partial templates to be included in other templates are prefixed with an underscore by convention 
                    [ie: _layout.html would be HTML header data and a common theme / header / footer]
                    
db.sqlite3          SQLite database - don't commit to repo, 
                    should be deprecated in favour of PostgreSQL in a later sprint
                    
manage.py           Run django commands with the script `python3 manage.py [command]`

README.md           This help file

requirements.txt    Project (python) dependencies, to be installed in a virtual environment with `pip3 install -r requirements.txt`
```