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
