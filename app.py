from flask import Flask, render_template, redirect, request
from models.task import Task


# Init the Flask app
app = Flask(__name__)

# Set the app secret
app.config['SECRET_KEY'] = 'gu26LFcF87LJEehmlJX69bHQA2zGubR4JM9xLB9NrdmOBpYqYYNYdb9uvnkVG7cz'

# Set debug to true
app.config['DEBUG'] = True


# Set the api for POST and GET
@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'POST':
		task_description = request.form['description']
		task = Task(description=task_description)
		try:
			Task.add(task)
			return redirect('/')
		except:
			return 'There was an issue adding your task'
	else:
		tasks = Task.findAll()
		return render_template('index.html', tasks=tasks)


# Set the api for UPDATE
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
	if request.method == 'POST':
		task = Task(description=task_description)
		try:
			description = request.form['description']
			Task.update(id, task)
			return redirect('/')
		except:
			return 'There was an issue deleting your task'
	else:
		return render_teamplte('update.html', task=task_to_update)


# Set the api for DELETE
@app.route('/delete/<int:id>')
def delete(id):
	try:
		Task.delete(id)
		return redirect('/')
	except:
		return 'There was an issue deleting your task'


if __name__ == '__main__':
	# Use http://localhost
	# Use port :5000
	# Activate debug
	# Disable thread (to solve problem with sqlalchemy)
	app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)

