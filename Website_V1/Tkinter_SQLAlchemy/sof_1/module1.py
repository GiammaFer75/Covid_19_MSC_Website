import tkinter as tk
import user

TITLE_FONT = ("Helvetica", 18, "bold")

class Authorzation(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Register):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location; 
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()

class Login(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller

        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="Title", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        #Create the Username field
        label_username = tk.Label(self, text="username")
        label_username.pack()
        self.username = tk.StringVar()
        tk.Entry(self, textvariable=self.username).pack()

        #Create the password field
        label_password = tk.Label(self, text="password")
        label_password.pack()
        self.password = tk.StringVar()
        tk.Entry(self, textvariable=self.password).pack()


        login_btn = tk.Button(self, text="Login", 
                            command=self._check_credentials)
        login_btn.pack(pady=5)

        reg_btn = tk.Button(self, text="Registration", 
                            command=lambda: controller.show_frame(Register))
        reg_btn.pack(pady=10)

    def _check_credentials(self):
        session_user = session.query(user.User)\
                                    .filter_by(
                                               username=self.username
                                            ).first() 
        if session_user:
            return session_user.check_pwd(), session_user
        else:
            print("Sorry we could not find your username")
            return False, None

        self.controller.show_frame(Login)

class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", 
                           command=lambda: controller.show_frame(Login))
        button.pack()