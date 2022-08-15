# Django CRUD lecture series

## Technologies used
<hr>


[Gitpod](https://www.gitpod.io) 
- IDE (Intigrated Development Environment)

[Github](https://www.github.com)
- remote repository hosting platform

[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) | [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) | [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) |  [python](https://www.python.org/) 

- Languages Used to make the site

[django](https://www.djangoproject.com/)  

- Framework used to make the site

[Bootsrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

- CSS library used for rapid development

[HTMX](https://htmx.org/docs/)

- Htmx is a library that allows you to access modern browser features directly from HTML, rather than using javascript.

## Setting up the project
<hr>

make sure [python](https://www.python.org/) is installed on your machine

[clone](https://docs.github.com/en/repositories/) the [project github repository](https://github.com/xiaoniuniu89/google-shopping-list)

It is reccomended to set up a virtual environment. [python venv](https://docs.python.org/3/library/venv.html)

- in the root folder you can use the command - "python3 -m venv venv " 
- to activate the virtual environment - "source venv/bin/activate" 

install the project dependencies - "pip3 install -r requirements.txt"

create environment variables
- in the root directory of the project (same place as manage.py) create a file called "env.py"
- add the following
    - import os
    - os.environ["SECRET_KEY"] = 'random_key' (pick a better secret than this)
    - os.environ["DEVELOPMENT"] = "DEVELOPMENT"

create a super user - "python3 manage.py createsuperuser"

start the development server - "python3 manage.py runserver"

You should now be up and running, you can log in with the superuser credentials you just created. 

