#!/usr/bin/env python

############################################################################################################|
###########################################_CREATED_BY_ccod_###########################################|
############################################################################################################|
###########################################_####Version_0.01####_###########################################|
############################################################################################################|

#Importing modules
from tkinter import *
from time import sleep
import os
from tkinter import messagebox
#;


#Begin class main
class PyBash:
     def __init__(self, master):
          self.master = master #Frame Main

          master.title("Pybash | Main windows")
          master.geometry("700x500+0+0")
          self.create_components(master)


     def create_components(self, master):

          #Main components
          self.FrameMain = Frame(self.master, height=500, width=700, relief="raise", bd=1)#Frame over the master
          self.FrameMain.pack(side=TOP, fill=Y)
          self.FrameMain.configure(background="#333")
          
          self.Frame_Right = Frame(self.master, height=500, width=200, relief="raise", bd=15)#Frame Right
          self.Frame_Right.place(x=500, y=0)
          self.Frame_Right.configure(background="#fff")
          #;



          
          #Secundary_components
          self.Label_Top_Welcome = Label(self.FrameMain, text="Welcome to PyBash 0.01 Created by Chameleon", width=50, height=3, font=('arial', 14, 'bold')) #label top
          self.Label_Top_Welcome.place(x=0, y=0)

          


          self.Label_lft = Label(self.FrameMain, text="ADD Repository", width=15, height=1, font=('arial', 11, 'bold'))
          self.Label_lft.place(x=10, y=90)

          self.button_system = Button(self.FrameMain, height=1, width=10, text="ADD", command=self.add_repository_funct)
          self.button_system.place(x=340, y=86)

          self.entr_repository = Entry(self.FrameMain)
          self.entr_repository.place(x=140, y=90)


          self.button_system_dUp = Button(self.Frame_Right, height=2, width=10, text="dist-upgrade")
          self.button_system_dUp.place(x=34, y=210)


          self.Label_lft = Label(self.FrameMain, text="Command", width=9, height=1, font=('arial', 11, 'bold'))
          self.Label_lft.place(x=415, y=290)

          self.entr_command = Entry(self.FrameMain, width=35)
          self.entr_command.place(x=125, y=290)

          self.button_system = Button(self.FrameMain, height=1, width=10, text="execute", command=self.add_command)
          self.button_system.place(x=10, y=285)
          #;
          

          

          #Components frame_right
          self.button_system_update = Button(self.Frame_Right, height=2, width=10, text="update", command=self.update)
          self.button_system_update.place(x=34, y=70)

          self.button_system_upgrade = Button(self.Frame_Right, height=2, width=10, text="upgrade",command=self.upgrade_dist)
          self.button_system_upgrade.place(x=34, y=140)


          self.button_system_dUp = Button(self.Frame_Right, height=2, width=10, text="dist-upgrade", command=self.upgrade_dist)
          self.button_system_dUp.place(x=34, y=210)

          self.button_system_exit = Button(self.Frame_Right, height=2, width=10, text="Exit", command=self.killer)
          self.button_system_exit.place(x=34, y=280)
          #;




#functions 


     def update(self):
          try:
               up_date = os.system("apt update")
               print("comand executed \n{}".format(up_date))
               messagebox.showinfo("System","Command executed")
          except Exception:
               messagebox.showerror('Erro', '{}'.format(Exception))
               print("Error... Cod: {}".format(Exception))

     def upgrade(self):
          try:
               up_grade = os.system("apt upgrade")
               print("comand executed \n{}".format(up_grade))
               messagebox.showinfo("System","Command executed")
          except Exception: 
               messagebox.showerror('Erro', '{}'.format(Exception))
               print("Error... Cod: {}".format(Exception))


     def upgrade_dist(self): 
          try:
               dist_up = os.system("apt dist-upgrade")
               print("comand executed \n{}".format(dist_up))
               messagebox.showinfo("System","Command executed")
          except Exception: 
               messagebox.showerror('Erro', '{}'.format(Exception))
               print("Error... Cod: {}".format(Exception))


     def add_repository_funct(self):
          try:
               self.repositor = str(self.entr_repository.get())
               os.system("sudo echo '\n#ADD By PyBash\n{}' >> /etc/apt/sources.list".format(self.repositor))
               messagebox.showinfo("System","Command executed")
          except Exception:
               messagebox.showerror('Erro', '{}'.format(Exception))
               print("Error... Cod: {}".format(Exception))


     def add_command(self):
          try:
               self.command = str(self.entr_command.get())
               os.system("{}".format(self.command))
               messagebox.showinfo("System","Command executed")
          except Exception:
               messagebox.showerror('Erro', '{}'.format(Exception))
               print("Error... Cod: {}".format(Exception))
          


     def killer(self):
          try:
               self.master.destroy()
          except Exception:
               messagebox.showerror('Erro', '{}'.format(Exception))
               print("Error... Cod: {}".format(Exception))



               


#End Class 
          








Root = Tk()
PyBash(Root)
Root.mainloop()
               
