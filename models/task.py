from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from datetime import datetime
from config.db import Session 


Base = declarative_base()

class Task(Base):
	__tablename__ = 'tasks'
	id = Column(u'id', Integer(), primary_key=True, nullable=False)
	description = Column(u'description', String(length=256), primary_key=False, nullable=False)

	def __init__(self, description):
		self.description = description

	def __repr__(self):
		return "<Task(description='%s')>" % (self.description)

	def findAll():
		''' Find all tasks '''
		print(' ---- FIND ALL TASKS\n')
		session = Session()
		r = session.query(Task).all()
		session.close()
		return r

	def findById(id):
		''' Find task by id '''
		print(' ---- FIND TASKS BY ID ' + id + ' \n')
		session = Session()
		r = session.query(Task).filter(Task.id == id).first()
		session.close()
		return r

	def add(task):
		''' Add new task '''
		print(' ---- ADDING TASK\n\n')
		print(task)
		session = Session()
		session.add(task)
		session.commit()
		session.close()

	def update(id, task):
		''' Update existing task '''
		print(' ---- UPDATING TASK WITH ID ' + id + ' \n\n')
		print(task)
		pass

	def delete(id):
		''' Delete task '''
		print(' ---- DELETING TASK WITH ID ' + id + ' \n\n')
		pass

	def exists(description):
		''' Check if task with that descripton already exists '''
		print(' ---- CHECKING TASK WITH DESCRIPTION ' + description + ' \n\n')
		session = Session()
		r = session.query(exists().where(Task.description == description)).scalar()
		session.close()
		return r
