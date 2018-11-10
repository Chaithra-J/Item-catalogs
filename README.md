# Item Catalog Project
## Project Overview:
This application provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit, and delete their own items.

## Features:
* Proper authentication and authorisation check.
* Full CRUD support using SQLAlchemy and Flask.
* JSON endpoints.
* Implements oAuth using Google Sign-in API.

## Project Structure:

* app.py
* client_secrets.json
* database_setup.py
* catalog.py
* itemcatalog.db
* LICENSE
* README.md
* static
  * style.css
* templates
  * delete_category.html
  * delete.html
  * edit_category.html
  * index.html
  * items.html
  * layout.html
  * login.html
  * new-category.html
  * new-item-2.html
  * new-item.html
  * update-item.html
  * view-item.html

## Steps to run this project
1. Download and install Vagrant.

1. Download and install VirtualBox.

1. Clone or download the Vagrant VM configuration file from here.

1. Open the above directory and navigate to the vagrant/ sub-directory.

1. Open terminal, and type

```vagrant up```

This will cause Vagrant to download the Ubuntu operating system and install it. This may take quite a while depending on how fast your Internet connection is.

1. After the above command succeeds, connect to the newly created VM by typing the following command:

```vagrant ssh```

1. Type cd /vagrant/ to navigate to the shared repository.

1. Download or clone this repository, and navigate to it.

1. Install or upgrade Flask:

```sudo python -m pip install --upgrade flask```

1. Run the following command to set up the database:

```python database_setup.py```

1. Run the following command to insert dummy values. If you don't run this, the application will not run.

```python catalog.py```

1. Run this application:

```python app.py```

1. Open [http://localhost:5000/](http://localhost:5000/) in your favourite Web browser, and enjoy.

1. Debugging
In case the app doesn't run, make sure to confirm the following points:

* You have run python catalog.py before running the application. This is an essential step.
* The latest version of Flask 1.x is installed.
* The latest version of Python 3.6.x is installed. In the vagrant machine, you may find Python 3.5.x installed by default. 
* To invoke Python 3.6, type python3.6 instead of python3.
