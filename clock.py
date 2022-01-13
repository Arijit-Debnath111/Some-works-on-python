#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *


# In[3]:


from tkinter.ttk import *


# In[4]:


from time import strftime


# In[8]:


root=Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label=Label(root,font=("ds-digital",80),background="black",foreground="cyan")
label.pack(anchor='center')
time()

mainloop()


# In[ ]:




