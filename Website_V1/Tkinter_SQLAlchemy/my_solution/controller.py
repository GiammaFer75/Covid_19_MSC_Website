from tkinter import Tk

from views.main_window import MainWindow
from models import Projects, Omics
from db import Session, engine

# When do I construct a Session, when do I commit it, and when do I close it?
#   1 - As a general rule, keep the lifecycle of the session separate and external 
#		from functions and objects that access and/or manipulate database data. 
#		This will greatly help with achieving a predictable and consistent transactional scope.
#   2 - Make sure you have a clear notion of where transactions begin and end, 
#		and keep transactions short, meaning, they end at the series of a sequence of operations, 
#		instead of being held open indefinitely.
#
# In my project Session() is in db module
session = Session()

class Controller:
	def __init__(self, model=None, view=None):
		self.model=model 
		self.view=view

	def count_records(self):
		number_of_records = session.query(Projects).count()
		return number_of_records

	def all_projects(self): 
		'''
		Queries as Python Code with SQLAlchemy's Expression Language
		https://hackersandslackers.com/database-queries-sqlalchemy-orm/
		'''
		return session.query(Projects)

	def search(self):
		'''
		The searching operation should works in all cases where not all fields are filled.
		In particular when only one is provided.
		For this reason the dictionary with the field values that come from the form,
		must be iterate searching for non-empty fields.
		This for loop creates the filter string used to query the dataabase.
		Because this string will be a command it must be executed bu the exec(). 
		In this way it is possible to create dynamic queryes (flexible as you like)
		'''
		# search_result = {
		# 		"project_id" : 'None',
		# 		"project_name" : 'None',
		# 		"project_description" : 'None'
		# }
		project_table=session.query(Projects) # Generate query object for the table

		search_project = self.view.get_data()
		print('\n',search_project,'\n')
		filter_str = ''
		for key,value in search_project.items():
			if (value != "") or (value==0):
				filter_str += f'Projects.{key}==\'{value}\','
		filter_str=filter_str[:-1] # remove the last comma
		print(filter_str)
		
		command_str=f'project_table.filter({filter_str})'#.first()
		print(command_str)
		if (filter_str != ''):  # At least one field in the form must provide some data
			search_result=eval(command_str)
		# Print in console for debug
		for row in search_result.all():
			print(row.project_id, row.project_name, row.project_description)
		return search_result


	def save(self):
		new_proj_form = self.view.get_data()
		new_project = self.model(
								 project_name = new_proj_form['project_name'],
								 project_description = new_proj_form['project_description'])
		session.add(new_project)
		session.commit()

	def delete(self):
		project_table=session.query(Projects) # Generate query object for the table
		del_proj_form = self.view.get_data()
		#delete_project = project_table.delete().where(project_id = del_proj_form['project_id'])
		print(del_proj_form['project_id'])
		delete_project = project_table.filter(Projects.project_id==del_proj_form['project_id']).delete()
		session.commit()


def main():
	root = Tk()
	controller = Controller()
	view = MainWindow(controller=controller)
	model_project = Projects
	controller.model = model_project
	controller.view = view
	# view.pack()
	view.grid(row=2, column=0)
	root.mainloop()

if __name__ == "__main__":
	main()