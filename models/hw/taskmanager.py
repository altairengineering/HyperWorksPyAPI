from typing import TypeVar
class hw_module:
    class taskmanager:
        class tasks:
            class Task:
                pass
class type:
    pass

class Task:
    def __init__(self,**kwds):
        """

    A class representing a task.
    
"""
        pass

    @property
    def active(self):
        pass
    @active.setter
    def active(self):
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

    def getPropertyEnabled(self,tag: str):
        """
        
        Method to get the task property enabled state.

        :param tag: The tag of the property.
        :type tag: str
        
        """
        pass

    def getPropertyExpand(self,tag: str):
        pass

    def getPropertyFollowupdateCommand(self,tag: str):
        """
        
        Method to get the task property *followupdatecommand* as a string.

        :param tag: The tag of the property.
        :type tag: str
        
        """
        pass

    def getPropertyLabel(self,tag: str):
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

    def getPropertyVisible(self,tag: str):
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

    def setPropertyExpand(self,tag: str, value: bool):
        """
        
        Method to set the task property category expand state.

        :param tag: The tag of the property.
        :type tag: str

        :param value: The state to set the expand state of the property cateogry to.
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
    def active(self):
        pass
    @active.setter
    def active(self):
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
    return TaskManager()

class gui:
    pass

class model:
    pass

class tasks:
    pass

class utils:
    pass

class TaskManager:
    def __init__(self):
        pass

    def addOnCloseCommand(fullcommandasstring: str):
        """

            Method to add *onClose* commands.

            :param fullcommandasstring: *onClose* command as a string
            :type fullcommandasstring: str
            
    """
        pass

    def apply():
        """

            Method to execute current task and set the status icon according to
            return value of command. If successful (returns value 1), the Task Manager proceeds to next task.
            
    """
        pass

    def autoApply():
        """

            Method to run all tasks sequentially starting with the current task. All previously run tasks with successful status will be ignored.
            
    """
        pass

    def close():
        """

            Method to close the Task Manager and delete the content.
            
    """
        pass

    def closeProcess():
        """

            Method to delete current content.
            
    """
        pass

    def getCurrentTask():
        """

            Method that returns the current task or category.
            
    """
        pass

    def getOnCloseCommands():
        """

            Method that returns all added *onClose* commands as a list.
            
    """
        pass

    def getTask(tag: str = None):
        """

            Method that returns the task or category object.

            :param tag: The tag of the task or category. If set to None, the current task or category is returned.
            :type tag: str
            
    """
        pass

    def getTaskList():
        """

            Method that returns list of tasks, exluding the cateogries.
            
    """
        pass

    def getTaskUIDockable(value):
        """

            Method to get if the window containing the task properties is dockable or not.
            
    """
        pass

    def getTaskUIStayOpen():
        """

            Method to get if the window containing the task properties stays open when empty.
            
    """
        pass

    def goToNextTask():
        """

            Method to go to the next task.
            
    """
        pass

    def goToPreviousTask():
        """

            Method to go to the previous task.
            
    """
        pass

    def goToTask(task: str|hw_module.taskmanager.tasks.Task = None):
        """

            Method to go to a specific task.

            :param task: Task object or task tag representing the task to go to. If not specified or set to None, then all tasks are deselected.
            :type task: Union[str, Task]
            
    """
        pass

    def isProcessLoaded():
        """

            Method to check if a process is loaded.
            
    """
        pass

    def openProcess(filepath=None):
        """

            Method to open a Task Manager session file.

            :param filepath: The path to the Task Manager session file. If not specified, user will be prompted to select a file.
            :type filepath: str
            
    """
        pass

    def populate(taskmanagerfile: str = None):
        """

            Method to open the Task Manager (Tasks tab) and to load the content from the task manager file (optional).

            :param taskmanagerfile: The XML process template describing the Tasks.
            :type taskmanagerfile: str
            
    """
        pass

    def registerDisplaytype(displaytype: str, widgetclass: str|type):
        pass

    def saveProcess(filepath=None):
        """

            Method to save the current Task Manager progress.

            :param filepath: The file path of the Task Manager session file to save. If not specified, the user will be prompted to select a file.
            :type filepath: str
            
    """
        pass

    def setTaskUIDockable(value: bool):
        """

            Method to set if the window containing the task properties is dockable or not.

            :param value: Set True to make the window dockable, False otherwise.
            :type value: bool
            
    """
        pass

    def setTaskUIStayOpen(value: bool):
        """

            Method to set if the window containing the task properties stays open when empty.
            This option is usually used together with docked window.

            :param value: Set True to keep the window open, False otherwise.
            :type value: bool
            
    """
        pass

    def showHelp(task=None):
        """

            Method to show a task help document.

            :param task: The task object representing the task for which to show the help document.
            :type task: Task
            
    """
        pass

    @property
    def title(self):
        pass

    @title.setter
    def title(self):
        pass    

    @property
    def saveonclose(self):
        pass

    @saveonclose.setter
    def saveonclose(self):
        pass 

    def whichProcessIsLoaded():
        """

            Method to check which process is loaded.
            
    """
        pass

