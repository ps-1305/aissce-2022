# ==================================={login_screen.py}============================================
from tkinter import *
from tkinter import messagebox
import backend as bk
# INCREASING DPI
try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
except:
        pass

# FONT TUPLES: 
# 1) TYPE COURIER NEW, SIZE 12, WEIGHT BOLD
font = ('Courier New', 12, 'bold')
# 2) TYPE CONSOLAS, SIZE 16, WEIGHT BOLD, FORMATTING UNDERLINE  
font2 = ('Consolas', 16, 'bold','underline')


# ------------------------------------COMMANDS---------------------------------------------------

# LOGIN COMMAND (BUTTON b1 @ LINES 97-108)
# USE FUNCTION bk.login() WITH ALL THE PARAMETERS FROM THE ENTRIES
# IF bk.login() RETURNS True THEN DESTROY THE LOGIN WINDOW AND OPEN THE MAIN APP
# ELSE SHOW WARNING THAT THE USERNAME OR PASSWORD HAS A FAULT 
# THE COMMAND TAKES IN event AS A PARAMETER  BECAUSE THE <Return> KEY IS BINDED TO THE FUNCTION
def login_command(event=None):
    if bk.login(username.get(), password.get()):
        window.destroy()
        import app
    else:
        messagebox.showwarning(
            'Login error', 'The username or password is incorrect!'
        )

# ---------------------------------MAIN PROGRAM----------------------------------------------

window = Tk()
window.title('Alpha Healthcare Login')
window.configure(bg='teal')
window.resizable(False, False)
window.config(padx=10)
window.iconbitmap(r"photos/icon.ico")


# ===============================[IMAGES]========================================
img = PhotoImage(file='photos/main_logo.png')
img_button = Button(window, image=img)
img_button.grid(row=0,
                column=0,
                pady=5)

# ===============================[FRAMES]=======================================
mainFrame = Frame(window, bg='teal')
mainFrame.grid(row=1, column=0)

# ===============================[LABELS]=======================================

# THE MAIN DISPLAY LABEL
title2 = Label(mainFrame, text='Alpha healthcare\u2122 PORTAL', fg='yellow', bg='teal')
title2.grid(row=0, column=0, columnspan=2)
title2.configure(font=font2)

# USERNAME
l1 = Label(mainFrame, text='Username:', fg='white', bg='teal')
l1.grid(row=1, column=0)
l1.configure(font= font)

# PASSWORD
l2 = Label(mainFrame, text='Password:', fg='white', bg='teal')
l2.grid(row=2, column=0)
l2.configure(font=font)

# COPYRIGHT STATEMENT
l3 = Label(window, text='Copyright (c) Alpha Healthcare 2022', fg='white', bg='teal')
l3.grid(row=4, column=0, columnspan=2)
l3.configure(font=('Arial', 8))

# =================================[ENTRIES]======================================= 

# USERNAME
username = StringVar()
e1 = Entry(mainFrame, textvariable=username)
e1.grid(row=1, column=1)
e1.configure(font=font)

# PASSWORD
password = StringVar()
e2 = Entry(mainFrame, textvariable=password, show='●')
e2.grid(row=2,
        column=1)
e2.bind('<Return>', login_command)
e2.configure(font=font)

# ================================[BUTTONS]==========================================

# LOGIN BUTTON
b1 = Button(mainFrame,
            text='Login',
            bg='lime',
            command=login_command,
            activebackground='green',
            activeforeground='white')
b1.grid(row=3,
        column=0,
        columnspan=2,
        sticky=W + E,
        pady=5)
b1.configure(font=font)

# CLOSE BUTTON
b2 = Button(mainFrame,
            text='Close',
            bg='red',
            command=window.destroy)
b2.grid(row=4,
        column=0,
        columnspan=2,
        sticky=W + E,
        pady=10)
b2.configure(font=font)

window.mainloop()

# -------------------------------------------END---------------------------------------------
