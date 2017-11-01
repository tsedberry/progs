# Django Migrations

There are a few different moving pieces:
 - models.py
 - the state of the database
 - the django_migrations table
 - the modules in the migrations/ directory

## Your models.py

Python code that describes what you want the schema for the tables in your database(s) to look like.

## Your Database

The actual schema of the tables in your database(s). Note that django migrations don't seem to care about the contents of the tables on your database, just the schema.

## Your django_migrations table

There is a very simple table in your database that keeps track of which migrations have been applied (with a timestamp). Specifically, each row describes a single migration (apparently just the filename) and when it was applied.

## Your migrations/ directory

Roughly speaking, each module in the migrations/ directory represents a single migration.

More specifically, each module contains instructions for making specific changes to your database.

Django can read the modules in the migrations directory to deduce what the schema of the tables in your database should look like, for any particular migration, by starting at the first module in the migrations/ directory and applying all subsequent modules leading up to the target migration.

## Make Migrations

When you run

```
>>> python3 manage.py makemigrations
```

Django looks at the django_migrations table to determine which migrations have been applied. Then it goes through the migrations/ directory and reads all of the modules listed in the django_migrations table to figure out what the schema of the tables in your database should look like. Django compares what the database should look like to what it actually looks like and creates a new module in the migrations/ directory that describes how to change the schema of the tables in your database so that they match.

## Select a Particular Migration

When you run

```
>>> python3 manage.py migrate [appname] [migration]
```

Django changes the schema of the tables in your database so that they match the state described at the specified migration. Note that this can results in entire tables being dropped. It also updates the django_migrations table, adding any applied migrations and removing any rolled back migrations.




# Example

Start a new django project:

```
$ django-admin startproject djsandbox
$ cd djsandbox
```

Run initial migrations:

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Show migrations:

```
$ python3 manage.py showmigrations
```

Create a new app (named app):

```
$ python3 manage.py startapp app
```

Add a new model to app/models.py:

```
class Author(models.Model):
    name = models.CharField(max_length=512)
```

Update database:

```
$ python3 manage.py makemigrations --name added_Author_model app
$ python3 manage.py migrate
```

Add Book model:
```
class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.ForeignKey(Author)
```

Update database:

```
$ python3 manage.py makemigrations --name added_Author_model app
$ python3 manage.py migrate
```

Populate the database using the django ORM:

```
$ python3 manage.py shell
>>> from app.models import Author, Book
>>> author = Author(name="JK Rowling")
>>> author.save()
>>> book = Book(title="Harry Potter",author=author)
>>> book.save()
```

Verify the existence of the Author and Book tables, and their contents, using sqlite3:

```
$ sqlite3 db.sqlite3
sqlite> .tables
app_author
app_book
...
django_migrations
...
sqlite> select * from app_author;
1|JK Rowling
sqlite> select * from django_migrations;
...
14|app|0001_initial|datetimestamp
17|app|0002_added_Book_model|datetimestamp
sqlite> .exit
```

Roll back the most recent migration:

```
$ python3 manage.py showmigrations app
app
 [X] 0001_initial
 [X] 0002_added_Book_model
$ python3 manage.py migrate app 0001_initial
```

Verify that the Book table has been removed from the database, and the 0002_added_Book_model row of the django_migrations table has been removed:
```
TODO
```
