from datetime import date
from hashlib import md5
from flask import Flask, abort, render_template, redirect, url_for, flash, request,current_app, session
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy, pagination
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from typing import List
import hashlib
import smtplib
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

#global variables 
completed_tasks=[]


# Create a new Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "secret")
ckeditor = CKEditor(app)
Bootstrap5(app)

#initializing the login manager
login_manager = LoginManager()
login_manager.init_app(app)

#loading the user
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

#creating a declarative base
class Base(DeclarativeBase):
    pass

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#create a user table in the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    #creating a relationship between the user and the todo_list
    todo_list = db.relationship('ToDoList', back_populates='user')


# Create a task table in the database
class ToDoList(db.Model):
    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True)#primary key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#foreign key
    name = db.Column(db.String(250), nullable=False)
    #creating a relationship between the tasks and the task_list
    todo_task = db.relationship('TasksList', back_populates='todo_list')
    #creating a relationship between the user and the todo_list
    user = db.relationship('User', back_populates='todo_list')


# Create a new table TaskList in the database
class TasksList(db.Model):
    __tablename__ = 'tasks_list'
    id = db.Column(db.Integer, primary_key=True)#primary key
    todo_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))#foreign key
    #creating a relationship between the tasks and the task_list
    todo_list = db.relationship('ToDoList', back_populates='todo_task')
    title = db.Column(db.String(250), nullable=False)#title of the task
    date = db.Column(db.String(250), nullable=False) #due date of the task
    is_completed = db.Column(db.Boolean, nullable=False) #status of the task

#initialize the database
with app.app_context():
    db.create_all()


# #login manager
# login_manager = LoginManager()
# login_manager.init_app(app)

# #loading the user
# @login_manager.user_loader
# def load_user(user_id):
#     return db.get_or_404(User, user_id)


#login form 
class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Login')

#creating a ToDoList form for the task table
class CreateToDoList(FlaskForm):
    name = StringField(label='To-Do List Name', validators=[DataRequired()], render_kw={"placeholder": "To-Do List Name"})
    submit = SubmitField(label='Add ToDoList')

# Update ToDoList form
class UpdateToDoListForm(CreateToDoList):
    submit = SubmitField(label='Update ToDoList')

#task_list form
class CreateTaskListForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()], render_kw={"placeholder": "ToDoList Title"})
    date = StringField(label='Date', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD "})
    submit = SubmitField(label='Add ToDoList')

# update ToDoList form
class UpdateTaskListForm(CreateTaskListForm):
    submit = SubmitField(label='Update ToDoList')



# url for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == os.getenv('EMAIL') and password == os.getenv('PASSWORD'):
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')

    return render_template('index.html', form=form)

# methods for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == os.getenv('EMAIL') and password == os.getenv('PASSWORD'):
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')

    return render_template('login.html', form=form)


# method for manage_list in nav bar
@app.route('/todo_lists', methods=['GET', 'POST'])
def todo_lists():
    todo_lists = db.session.query(ToDoList).all()
    form = CreateToDoList()
    if form.validate_on_submit():
        new_todo_list = ToDoList(
            name=form.name.data
        )
        try:
            db.session.add(new_todo_list)
            db.session.commit()
            flash(f"{new_todo_list.name} To-Do List added successfully!", "success")
            #redirect to the new_task page
            return redirect(url_for('new_task', todo_id=new_todo_list.id))#redirect to the new_task page
        
        except Exception:
            flash("An error occurred while adding the To-Do List.", "danger")
            db.session.rollback()
            return redirect(url_for('index'))
        
    return render_template('todo_lists.html', todo_lists=todo_lists, form=form)


# method to add_new todo list
@app.route('/add_new_todo_list', methods=['GET', 'POST'])
def add_new_todo_list():
    form = CreateToDoList()
    if form.validate_on_submit():
        new_todo_list = ToDoList(
            name=form.name.data
        )
        try:
            db.session.add(new_todo_list)
            db.session.commit()
            flash(f"{new_todo_list.name} To-Do List added successfully!", "success")
            #redirect to the new_task page
            new_todo_list_id = new_todo_list.id
            return redirect(url_for('new_task', todo_id=new_todo_list_id))#redirect to the new_task page
        
        except Exception as e:
            flash("An error occurred while adding the To-Do List.", "danger")
            db.session.rollback()
            return redirect(url_for('index'))

    return render_template('new_todo_list.html', form=form)

#method to edit the todo list
@app.route('/edit_todo_list/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo_list(todo_id):
    todo_list = db.get_or_404(ToDoList, todo_id)
    form = UpdateToDoListForm(obj=todo_list)

    if form.validate_on_submit():
        todo_list.name = form.name.data
        try:
            db.session.commit()
            flash(f"{todo_list.name} To-Do List updated successfully!", "success")
            return redirect(url_for('todo_lists'))

        except Exception as e:
            flash("An error occurred while updating the To-Do List.", "danger")
            db.session.rollback()
            return redirect(url_for('todo_lists'))
        
    return render_template('edit_todo_list.html', form=form, todo_list=todo_list)    


#method to delete the todo list
@app.route("/delete_todo_list/<int:todo_id>", methods=['GET']) 
def delete_todo_list(todo_id):
    # Query the To-Do List
    # todo_list = db.session.query(ToDoList).filter_by(id=todo_id).first() # Get the To-Do List from the database
    todo_list = db.get_or_404(ToDoList, todo_id) # Get the To-Do List from the database
    # Check if the To-Do List exists
    if not todo_list:
        flash("To-Do List not found.", "danger")
        return redirect(url_for('todo_lists'))

    # Getting hold of task list
    tasks = db.session.query(TasksList).filter(TasksList.todo_id == todo_id).all()

    # Delete the To-Do List and its tasks
    try:
        # Check if the To-Do List has tasks
        if tasks:
            # Delete all tasks in the To-Do List
            for task in tasks:
                db.session.delete(task)
                db.session.commit()
        # Delete the To-Do List
        db.session.delete(todo_list)
        db.session.commit()
        # Flash a success message
        flash(f"{todo_list.name} To-Do List deleted successfully!", "success") # Flash a success message
        
    except Exception as e:
        flash("An error occurred  while deleting the To-Do List.", "danger")
        db.session.rollback()
    return redirect(url_for('todo_lists'))   # Redirect after deleting the To-Do List



# method to add new_task
@app.route('/new/<int:todo_id>', methods=['GET', 'POST'])
def new_task(todo_id):
    # Validate if the todo_id exists (Assume TodoList is another model representing the parent to-do list)
    todo_list = db.session.query(ToDoList).filter_by(id=todo_id).first()
    if not todo_list:
        abort(404, description="To-Do List not found.")

    # Initialize the form
    form = CreateTaskListForm()

    # Query all tasks for the To-Do List
    tasks = db.session.query(TasksList).filter(TasksList.todo_id == todo_id).all()

    # Separate completed and incomplete tasks
    completed_tasks = [task for task in tasks if task.is_completed]
    incomplete_tasks = [task for task in tasks if not task.is_completed]

    # Handle form submission
    if form.validate_on_submit():
        new_task = TasksList(
            todo_id=todo_id,
            title=form.title.data.strip(),
            date=form.date.data,
            is_completed=False
        )
        try:
            # Add and commit the new task
            db.session.add(new_task)
            db.session.commit()
            flash("Task added successfully!", "success")
            return redirect(url_for('new_task', todo_id=todo_id))
        except Exception as e:
            # Log error and rollback
            app.logger.error(f"Error adding task: {e}")
            db.session.rollback()
            flash("An error occurred while adding the task.", "danger")
            return redirect(url_for('new_task', todo_id=todo_id))

    # Render the template with all necessary data
    return render_template(
        'new_task.html',
        form=form,
        tasks=incomplete_tasks,
        completed_tasks=completed_tasks,
        todo_list=todo_list
    )



# url for editing the task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = db.get_or_404(TasksList, task_id) # Get the task from the database
    form = UpdateTaskListForm(obj=task) # Prefill the form with the task data

    if form.validate_on_submit():

        task.title = form.title.data
        task.date = form.date.data

        try:
            db.session.commit()
            flash("Task updated successfully!", "success")
            return redirect(url_for('new_task', todo_id=task.todo_id))

        except Exception as e:
            flash("An error occurred while updating the task.", "danger")
            db.session.rollback()
            return redirect(url_for('new_task', todo_id=task.todo_id))

        
    return render_template('edit_task.html', form=form, task=task)

# url for deleting the task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = db.get_or_404(TasksList, task_id)
    try:
        db.session.delete(task)
        db.session.commit()
        flash(f"{task.title} Task deleted successfully!", "success")
        return redirect(url_for('new_task', todo_id=task.todo_id))

    
    except Exception as e:
        flash("An error occurred while deleting the task.", "danger")
        db.session.rollback()
        return redirect(url_for('new_task', todo_id=task.todo_id))

    



# url for complete task
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = db.get_or_404(TasksList, task_id)
    task.is_completed = not task.is_completed

    try:
        db.session.commit()
        flash(f"Task {task.title} completed successfully!", "success")
        return redirect(url_for('new_task', todo_id=task.todo_id))

    except Exception as e:
        flash("An error occurred while updating the task status.", "danger")
        db.session.rollback()
        return redirect(url_for('new_task', todo_id=task.todo_id))

    
# url for clearing the completed tasks
@app.route('/clear_completed_tasks/<int:todo_id>', methods=['GET'])
def clear_completed_tasks(todo_id):
 
    try:
        db.session.query(TasksList).filter(TasksList.todo_id==todo_id,TasksList.is_completed == True).delete()
        db.session.commit()
        flash("Completed tasks cleared successfully!", "success")
    except Exception as e:
        flash("An error occurred while clearing completed tasks.", "danger")
        db.session.rollback()
        
    return redirect(url_for('new_task', todo_id=todo_id))  # Redirect after clearing


# initializing the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)