from typing import TypeVar

class Task:
	def __init__(self,**kwds):
		"""

    A class representing a task.
    
"""
		pass

	@property
	def applybuttonstate(self):
		pass
	@applybuttonstate.setter
	def applybuttonstate(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	def getID(self):
		"""
		Gets the entity ID.

        :return: Entity ID.
        :rtype: int
        
		"""
		pass

	def getPropertyDisplaytype(self,tag: str):
		"""
		
        Method to get the task property display type.

        :param tag: The tag of the property.
        :type tag: str
        
		"""
		pass

	def getPropertyEnabled(self,tag):
		"""
		
        Method to get the task property enabled state.

        :param tag: The tag of the property.
        :type tag: str
        
		"""
		pass

	def getPropertyFollowupdateCommand(self,tag: str):
		"""
		
        Method to get the task property *followupdatecommand* as a string.

        :param tag: The tag of the property.
        :type tag: str
        
		"""
		pass

	def getPropertyLabel(self,tag):
		"""
		
        Method to get the task property label.

        :param tag: The tag of the property.
        :type tag: str
        
		"""
		pass

	def getPropertySetCommand(self,tag: str):
		"""
		
        Method to get the task property *setcommand* as a string.

        :param tag: The tag of the property.
        :type tag: str
        
		"""
		pass

	def getPropertyValue(self,tag: str):
		"""
		
        Method to get the task property value.

        :param tag: The tag of the property.
        :type tag: str
        
		"""
		pass

	def getPropertyVisible(self,tag):
		"""
		
        Method to get the task property visible state.

        :param tag: The tag of the property.
        :type tag: str
        
		"""
		pass

	def getTMID(self):
		"""
		Gets the entity ID.

        :return: Entity ID.
        :rtype: int 
        
		"""
		pass

	def getType(self):
		"""
		Gets the entity type.

        :return: Entity type.
        :rtype: str 
        
		"""
		pass

	@property
	def help(self):
		pass
	@help.setter
	def help(self):
		pass

	@property
	def helpdocument(self):
		pass
	@helpdocument.setter
	def helpdocument(self):
		pass

	@property
	def image(self):
		pass
	@image.setter
	def image(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def nextbuttonstate(self):
		pass
	@nextbuttonstate.setter
	def nextbuttonstate(self):
		pass

	@property
	def node(self):
		pass
	@node.setter
	def node(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def postcommand(self):
		pass
	@postcommand.setter
	def postcommand(self):
		pass

	@property
	def precommand(self):
		pass
	@precommand.setter
	def precommand(self):
		pass

	@property
	def previousbuttonstate(self):
		pass
	@previousbuttonstate.setter
	def previousbuttonstate(self):
		pass

	def setPropertyDisplaytype(self,tag: str, value: str):
		"""
		
        Method to set the task property displaytype.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The *displaytype* of the task property as string.
        :type value: str
        
		"""
		pass

	def setPropertyEnabled(self,tag: str, value: bool):
		"""
		
        Method to set the task property enabled state.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The state to set the enabled state of the property to.
        :type value: bool
        
		"""
		pass

	def setPropertyFollowupdateCommand(self,tag: str, value: str):
		"""
		
        Method to set the task property *followupdatecommand*.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The *followupdatecommand* of the task property as string.
        :type value: str
        
		"""
		pass

	def setPropertyLabel(self,tag: str, value: str):
		"""
		
        Method to set the task property label.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The label of the task property.
        :type value: str
        
		"""
		pass

	def setPropertySetCommand(self,tag: str, value: str):
		"""
		
        Method to set the task property *setcommand*.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The *setcommand* of the task property as string.
        :type value: str
        
		"""
		pass

	def setPropertyValue(self,tag: str, value: str|int|float|bool):
		"""
		
        Method to set the task property value.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The tag of the property.
        :type value: Union[str, int, float, bool]
        
		"""
		pass

	def setPropertyVisible(self,tag: str, value: bool):
		"""
		
        Method to set the task property visible state.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The state to set the visible state of the property to.
        :type value: bool
        
		"""
		pass

	@property
	def status(self):
		pass
	@status.setter
	def status(self):
		pass

	@property
	def tag(self):
		pass
	@tag.setter
	def tag(self):
		pass

	@property
	def taskgroup(self):
		pass
	@taskgroup.setter
	def taskgroup(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def xml(self):
		pass
	@xml.setter
	def xml(self):
		pass

class TaskCategory:
	def __init__(self,tmtype: str="TaskCategory", **kwds):
		"""

    A class representing a task category.
    
"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def expand(self):
		pass
	@expand.setter
	def expand(self):
		pass

	def getID(self):
		"""
		Gets the entity ID.

        :return: Entity ID.
        :rtype: int
        
		"""
		pass

	def getTMID(self):
		"""
		Gets the entity ID.

        :return: Entity ID.
        :rtype: int 
        
		"""
		pass

	def getType(self):
		"""
		Gets the entity type.

        :return: Entity type.
        :rtype: str 
        
		"""
		pass

	@property
	def help(self):
		pass
	@help.setter
	def help(self):
		pass

	@property
	def helpdocument(self):
		pass
	@helpdocument.setter
	def helpdocument(self):
		pass

	@property
	def image(self):
		pass
	@image.setter
	def image(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def node(self):
		pass
	@node.setter
	def node(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def tag(self):
		pass
	@tag.setter
	def tag(self):
		pass

	@property
	def taskgroup(self):
		pass
	@taskgroup.setter
	def taskgroup(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

class attributes:
	pass

class entity:
	pass

def getTaskManager():
	"""

    Returns the Task Manager singleton object.
    
"""
	return Task()

class gui:
	pass

class model:
	pass

class tasks:
	pass

class utils:
	pass

