# FullMap Django Interview App

This is my simple Django app that uses:
[LeafLet](https://leafletjs.com) as map lib.
All of my past projects, i've been using GoogleMaps, at this project
i decided to use LeafLeft so study more about the API and to test the
performance.

[Bootstrap 4](https://getbootstrap.com) as css responsive lib.
[JQuery](https://jquery.com) as JS framework.
[SQLite](https://sqlite.org) as local database.
[Google Fusion](https://developers.google.com/fusiontables/) as external and integrated db tables.
[JQuery](https://jquery.com) as JS framework.
[DataTables](https://datatables.net/) as datatable component.


# Google Fusion Table URL

https://www.google.com/fusiontables/DataSource?docid=16IQoLcCIq_hJV35YFbN1cqTqV6yTtLe0aNOBEWCN

## Building

Setting up FullMap to work in you machine with Django is very easy. 
You need to create a python virtual machine using this commands: 

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally.


Developed by,

Victor Guimarães Silva.
victorgs301194@hotmail.com
