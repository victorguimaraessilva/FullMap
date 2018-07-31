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

https://fusiontables.google.com/embedviz?viz=GVIZ&t=TABLE&q=select+col0%2C+col1%2C+col2%2C+col3%2C+col4%2C+col5%2C+col6+from+1MMiXyaFVQJAdmLg7JDwzimeY817fFt05IfLGE3Em&containerId=googft-gviz-canvas

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