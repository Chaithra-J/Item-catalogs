Item Catalog Project
Project Overview
This application provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit, and delete their own items.

Features
Proper authentication and authorisation check.
Full CRUD support using SQLAlchemy and Flask.
JSON endpoints.
Implements oAuth using Google Sign-in API.
Project Structure
.
├── app.py
├── client_secrets.json
├── database_setup.py
├── fake_db_populator.py
├── itemcatalog.db
├── LICENSE
├── README.md
├── static
│   └── style.css
└── templates
    ├── delete_category.html
    ├── delete.html
    ├── edit_category.html
    ├── index.html
    ├── items.html
    ├── layout.html
    ├── login.html
    ├── new-category.html
    ├── new-item-2.html
    ├── new-item.html
    ├── update-item.html
    └── view-item.html
Steps to run this project
Download and install Vagrant.

Download and install VirtualBox.

Clone or download the Vagrant VM configuration file from here.

Open the above directory and navigate to the vagrant/ sub-directory.

Open terminal, and type

vagrant up
This will cause Vagrant to download the Ubuntu operating system and install it. This may take quite a while depending on how fast your Internet connection is.

After the above command succeeds, connect to the newly created VM by typing the following command:

vagrant ssh
Type cd /vagrant/ to navigate to the shared repository.

Download or clone this repository, and navigate to it.

Install or upgrade Flask:

sudo python3 -m pip install --upgrade flask
Run the following command to set up the database:

python3 database_setup.py
Run the following command to insert dummy values. If you don't run this, the application will not run.

python3 fake_db_populator.py
Run this application:

python3 app.py
Open http://localhost:5000/ in your favourite Web browser, and enjoy.

Debugging
In case the app doesn't run, make sure to confirm the following points:

You have run python3 fake_db_populator.py before running the application. This is an essential step.
The latest version of Flask 1.x is installed.
The latest version of Python 3.6.x is installed. In the vagrant machine, you may find Python 3.5.x installed by default. To install Python 3.6.x, follow this answer. To invoke Python 3.6, type python3.6 instead of python3.
Known Issue
This app might show an empty username if you sign in with a custom-domain-based Google account. For instance, if you use a Google account johndoe@company.com, this app might show an empty username. So, make sure to use an email with gmail.com domain only for best experience.

Help and Support
In case you run into any trouble, create an issue on GitHub. I will make sure to look into it as soon as possible.# item-catalog
