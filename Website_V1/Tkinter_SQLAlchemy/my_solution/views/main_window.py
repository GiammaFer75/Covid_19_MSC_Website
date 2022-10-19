from tkinter import Tk, Frame, Entry, Text, END
from tkinter import ttk
from tkinter import font
from tkinter import StringVar


window = Tk()
window.title("Interface")
window.geometry('1100x600')
window.configure(background = "gray")


class MainWindow(Frame):
	def __init__(self, controller=None, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.controller = controller
		self.make_widgets()

		show_db=self.controller.all_projects()
		self.print_db_tab(show_db)


	def make_widgets(self):
		
		# Define general text size
		fontsize=15
		gfont = font.Font(size=fontsize)

		# Define widgets containers
		show_database = Frame(window, height=22, width=52)
		show_database.grid(row=0, column=0)
		interact_area = Frame(window, height=22, width=42)
		interact_area.grid(row=0, column=1, sticky='N')
		show_stat = Frame(window,height=22, width=20, bg='grey')
		show_stat.grid(row=0, column=2, sticky='N')


		# [[ interact_area CONAINER ]]

		# Input area LABELS
		self.group_id = ttk.Label(interact_area, text="Project_id", font=gfont)
		self.description = ttk.Label(interact_area, text="Description", font=gfont)
		self.repositories = ttk.Label(interact_area, text="Repositories", font=gfont)

		# Input area ENTRY
		self.group_id_entry = ttk.Entry(interact_area, font=gfont)
		self.description_entry = ttk.Entry(interact_area, font=gfont)
		self.repositories_entry = ttk.Entry(interact_area, font=gfont)

		#Create an instance of Style Object
		style = ttk.Style()
		#Configure the properties of the Buttons
		style.configure('TButton', font=(None, fontsize)) # 'TButton' is used for ttk.Button
		self.btn_Submit = ttk.Button(interact_area ,text="Submit", style='TButton', 
						      		 command=self.submit_new_record)
		self.btn_Search = ttk.Button(interact_area ,text="Search", style='TButton', 
						      		 command=self.search_record)
		self.btn_Cancel = ttk.Button(interact_area ,text="Delete", style='TButton', 
						      		 command=self.delete_record)
		self.btn_ShowProjects = ttk.Button(interact_area ,text="Projects", style='TButton', 
						      		 	   command=self.show_projects)

		# [[ show_database CONAINER ]]

		# Output area 
		self.outarea = Text(show_database, height=30, width=40, font=gfont)


		# [[ show_stat CONAINER ]]

		self.tot_proj_lab = ttk.Label(show_stat, text="Total Projects", font=gfont)
		self.tot = StringVar()
		self.tot.set('0')
		self.tot_proj_quant = ttk.Label(show_stat, textvariable=self.tot, font=gfont)

		# placing
		self.group_id.grid(row=0, column=0, sticky='W')
		self.description.grid(row=1, column=0, sticky='W')
		self.repositories.grid(row=2, column=0, sticky='W')

		self.group_id_entry.grid(row=0, column=1, sticky='W')    
		self.description_entry.grid(row=1, column=1, sticky='W')
		self.repositories_entry.grid(row=2, column=1, sticky='W')

		self.outarea.grid(row=4, column=1)

		self.btn_Submit.grid(row=3,column=0, padx=3, pady=3)
		self.btn_Search.grid(row=4,column=0, padx=3, pady=3)
		self.btn_Cancel.grid(row=5,column=0, padx=3, pady=3)
		self.btn_ShowProjects.grid(row=6,column=0, padx=3, pady=3)

		self.tot_proj_lab.grid(row=0,column=0, padx=3, pady=3)
		self.tot_proj_quant.grid(row=0,column=1, padx=3, pady=3)
	
	def update_stats(self):
		rows = self.controller.count_records()
		return rows	

	def show_projects(self):
		self.clear_text_area()
		project_tab = self.controller.all_projects() # This query returns all the records in the db
		self.print_db_tab(project_tab)
		self.tot.set(str(self.update_stats()))

	def print_db_tab(self, table):
		for row in table:
			row_fields = [str(row.project_id), row.project_name, row.project_description]
			row_str = " - ".join(row_fields) + "\n"
			self.outarea.insert(END, row_str)

	def clear_text_area(self):
		self.outarea.delete(1.0, END)

	def submit_new_record(self):
	    self.controller.save()
	    self.clear_text_area()
	    self.show_projects()
	    self.tot.set(str(self.update_stats()))
	    
	def search_record(self):
		self.clear_text_area()
		search_results = self.controller.search()
		self.print_db_tab(search_results.all())
		
	def delete_record(self):
		self.clear_text_area()
		self.controller.delete()
		project_tab = self.controller.all_projects() # This query returns all the records in the db
		self.print_db_tab(project_tab)
		self.tot.set(str(self.update_stats()))

	def get_data(self):
		form_fields_dict = {
				"project_id" : self.group_id_entry.get(),
				"project_name" : self.description_entry.get(),
				"project_description" : self.repositories_entry.get()
		}
		return form_fields_dict


def main():
	#root = Tk()
	window = MainWindow()
	window.pack()
	#root.mainloop()

if __name__ == "__main__":
	main()
