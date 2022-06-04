<h2>Getting started</h2>
<div>
    <h3>Dependencies</h3>
    <p>Check requirements.txt file for dependencies</p>
    <p>It is adviceable you setup a python virtual environment to run this project</p>
    <h3>Installing</h3>
    <ul>
        <li>Clone this repository to your local machine</li>
        <li>Navigate into the root directory of the repository</li>
        <li>Run command 'pip install virtualenv' (if you don't already have virtualenv installed)</li>
        <li>Run command 'virtualenv venv' to create your new environment (called 'venv' here)</li>
        <li>Run command 'source venv/bin/activate' to enter the virtual environment</li>
        <li>Run command 'pip install -r requirements.txt' to install all the dependencies</li>
    </ul>
    <h3>Setup environment</h3>
    <p>Run command 'python3 manage.py makemigrations' to setup the database</p>
    <p>Next run command 'python3 manage.py migrate</p>
    <p>Now that we have the database setup, lets run the server to listen for requests</p>
    <p>Run command 'python3 manage.py runserver'. You can specify a port number like so
    'python3 manage.py runserver [portnumber]' but by default, Django uses port 8000.</p>
</div>
<h2>Usage</h2>
    <p>There are 2 api routes in this project. The first '/task/new' is used to create a new task</p>
    <p>The second route '/task/all' is used to get all the tasks in the database</p>
    <p>To make a new task, use the cURL tool on your command line to make a post request.</p>
    <p>Example</p>
    <p>curl -X "POST" -d '{"name": "[task name]", "email": "[user email]", "description": "[Description of task]"}' 127.0.0.1:8000/task/new</p>
    <p>Make sure to change the port number if you are using a different port for the server</p>
    <br/>
    <p>To get all the tasks in the database, you can either use the browser on your local machine
    or the cURL tool on your command line.</p>
    <p>To use your browser, simply visit the url '127.0.0.1:8000/task/all'<p>
    <p>To use cURL</p>
    <p>curl 127.0.0.1:8000/task/all</p>
    <p>Again make sure to change the port number if you are using a different port for the server</p>