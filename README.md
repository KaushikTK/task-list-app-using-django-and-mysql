# task-list-app-using-django
 A simple task list app using django for understand the django framework.

 NOTE: This uses *mysql* as the database for storing the tasks.

 Setting up the virtual python environment:

 1. open command prompt in the root director of this folder
 2. run `py -m venv env`
 3. cd into env/Scripts and run `activate` and `cd..` back to the root directory of this folder
 4. run `pip install -r req.txt`

 Setting up mysql:
 
 You can import the todo_list.mysql file and start using it. Else, create a table with 2 columns with names `id` of int type and `task` of varchar(100) type with `id` being the primary key.

 Running the app:

 1. open command prompt inside the todoApp folder
 2. Make sure to change the credentials to mysql in views.py file and settings.py file and start your mysql server.
 2. run `py manage.py runserver`
 3. go to `localhost:8000` in your browser