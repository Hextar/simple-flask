from sqlalchemy import *
from datetime import datetime
from config.db import *


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
		return {}

	def findById(id):
		''' Find task by id '''
		print(' ---- FIND TASKS BY ID ' + id + ' \n')
		return {}

	def add(task):
		''' Add new task '''
		print(' ---- ADDING TASK\n\n')
		return {}

	def update(id, task):
		''' Update existing task '''
		print(' ---- UPDATING TASK WITH ID ' + id + ' \n\n')
		return {}

	def delete(id):
		''' Delete task '''
		print(' ---- DELETING TASK WITH ID ' + id + ' \n\n')
		return {}

	def exists(description):
		''' Check if task with that descripton already exists '''
		print(' ---- CHECKING TASK WITH DESCRIPTION ' + description + ' \n\n')
		return {}
