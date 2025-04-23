from typing import TypeVar

class gui:
	"""

  Client independent GUI code
  
  Framework - create new clients or add new profiles to existing clients
  Ribbon    - add a new ribbon page to an existing profile
  Widgets   - standard GUI controls
  Dialogs   - Dialog boxes
  Tree      - Hierachical list 
  Actions   - GUI commands including SpriteActions

"""
	pass

class hwui:
	pass

class pauseprocess:
	def __init__(self,message,pos: str="<hwui.uiPoint; proxy of <Swig Object of type uiPoint * at 0x00000196DCE61690> >",title: str="SimLab",Button1: str="OK",Button2: str="Cancel"):
		"""
This function is used for to pause the script and user can interact the user interface to do manual operations.

  
"""
		pass

	@property
	def status(self):
		pass
	@status.setter
	def status(self):
		pass

def popupmsg(msg):
	pass

class tk:
	"""
Wrapper functions for Tcl/Tk.

Tkinter provides classes which allow the display, positioning and
control of widgets. Toplevel widgets are Tk and Toplevel. Other
widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
LabelFrame and PanedWindow.

Properties of the widgets are specified with keyword arguments.
Keyword arguments have the same name as the corresponding resource
under Tk.

Widgets are positioned with one of the geometry managers Place, Pack
or Grid. These managers can be called with methods place, pack, grid
available in every Widget.

Actions are bound to events by resources (e.g. keyword argument
command) or with the method bind.

Example (Hello, World):
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()

"""
	pass

class ttk:
	"""
Ttk wrapper.

This module provides classes to allow using Tk themed widget set.

Ttk is based on a revised and enhanced version of
TIP #48 (http://tip.tcl.tk/48) specified style engine.

Its basic idea is to separate, to the extent possible, the code
implementing a widget's behavior from the code implementing its
appearance. Widget class bindings are primarily responsible for
maintaining the widget state and invoking callbacks, all aspects
of the widgets appearance lies at Themes.

"""
	pass

