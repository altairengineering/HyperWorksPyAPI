from typing import TypeVar

class HasMethodsToHide:
	pass

class ParameterManager:
	pass

class SwigPatches:
	"""

This module exists to work around swig bugs nobody has been able to figure out

"""
	pass

class Translate:
	pass

class Units:
	def __init__(self,system: str="SI", **aliases):
		"""
Utility class used to convert values from one set of units to another.
  
"""
		pass

	def changeUnitInUnitSystem(self,unitType, unitName, unitSystemName):
		"""
		Changes the name of the unit in use, for the 'unitType' in the unit system
    'unitSystemName'.

    Args:
      unitType (str): The unit type.
      unitName (str): The new unit name.
      unitSystemName (str): The system name.

    Returns:
      bool: True on success, False otherwise.
    
		"""
		pass

	def convert(self,value, units, formula, toBase):
		"""
		Converts the specified value to/from base units.

    Args:
      value (Union[float, list[float], str, list[str]]): The value to convert.
      units (str): The units to convert.
      formula (str): The string conversion expression: m, mm, in, etc.
      toBase (bool): Determines whether to convert to base units or not.

    Raises:
      ValueError: If units is invalid.

    Returns:
      float: The converted value.
    
		"""
		pass

	def createUnit(self,unitType, unitName, substitution_str, multiplier=1.0):
		"""
		Creates a new unit 'unitName' of type 'unitType'.
    
    For instance:
      createUnit('pressure', 'bar', 'kg, m, s', multiplier=1e5)

    Args:
        unitType (str): The new unit type.
        unitName (str): The new unit name.
        substitution_str (str): A string that must contain, a comma separated list
          of units which suffice to build the unitType.
        multiplier (float): The conversion factor to the corresponding
          unit in the model unit.

    Returns:
      bool: True on success, False otherwise.
    
		"""
		pass

	def createUnitSystem(self,newUnitSystemName, templateUnitSystemName="m Kg N Pa", unitsToChange=None):
		"""
		Creates a new Unit System by copying the units used in the templateUnitSystem
      and then replacing the units for the unit types defined in unitsToChange.

    Args:
      newUnitSystemName (str): The new unit system name.
      templateUnitSystemName (str): Template unit system to get units
        from and apply to new unit system. 
      unitsToChange (dict[str, str]): A dictionary with unitTypes as
        keys and units as values. 

    Returns:
      bool: True on success, False otherwise. 
    
		"""
		pass

	def deleteUnitSystem(self,unitSystemName):
		"""
		Deletes the unit system.

    Args:
      unitSystemName (str): The unit system to delete.

    Returns:
      bool: True on success, False otherwise.
    
		"""
		pass

	def extractValueAndUnit(self,string):
		"""
		Returns a double value and a unit expression from the specified string.

    Args:
      string (str): The string containing both the value and the unit.

    Raises:
      ValueError: If Units could not be split.

    Returns:
      tuple[float, str]: The double value and the unit expression as a string.
    
		"""
		pass

	def fromBase(self,value, units="length"):
		"""
		Converts the value from base units to the user specified unit.

    Args:
      value (Union[float, list[float], str, list[str]]): The value to convert.
      units (str): The units to convert.

    Returns:
      float: The converted value.
    
		"""
		pass

	def getAllUnits(self):
		"""
		Returns all the unit formulas for given unit system.
		"""
		pass

	def getConversionScaleFactor(self,sourceUnit, targetUnit, units):
		"""
		Returns the scale factor from source unit to target for the particular formula

    Args:
      sourceUnit (str): "m", "kg", "deg" ...
      targetUnit (str): "cm", "g", "rad" ...
      units (str): "length", "mass", "angle" ...

    Returns:
      float
    
		"""
		pass

	def getDefinedUnits(self,units="length"):
		"""
		Returns all the units defined for the particular formula

    Args:
      units (str): "length", "mass", "angle" ...

    Returns:
      list[str]
    
		"""
		pass

	def getFormattedString(self,value, units="length", format="modeling"):
		"""
		Converts the value from base units to user units and formats it into a
    string containing the value and unit: 5 -> '5 cm'.

    Args:
      value (float | list[float]): The float to display.
        An iterable is returned comma separated: [1, 2] -> '1 cm, 2 cm'.
      units (str): length, mass, ...
      format (str | list[float, float]):
        "modeling": User preference for values shown during model setup.
        "results": User preference for solver results.
        [width, precision]
        Python format string like "%g".

    Returns:
      str
    
		"""
		pass

	def getInternalName(self,units):
		"""
		Named used in c++
		"""
		pass

	def getPublicName(self,units):
		"""
		Named used in python
		"""
		pass

	def getSystemNames(self):
		"""
		Returns a list of names of the supported systems.
    
		"""
		pass

	def getUnit(self,units="length"):
		"""
		Returns the formula in the user unit system for the specified units.

    Args:
      units (str): The units to consider.

    Raises:
      ValueError: If units is invalid.

    Returns:
      str: The formula in the user unit system.
    
		"""
		pass

	def getUnitsDisplayName(self,units, withUnits=True):
		"""
		Converts units to a gui label.

    Args:
      units (str): The units.
      withUnits (bool): Determines whether to include units in the return value.

    Returns:
      str: The display name.
    
		"""
		pass

	def getUnitsFromDisplayName(self,name):
		"""
		Returns the units from the display name.
    
    This is the inverse of getUnitsDisplayName.
    
		"""
		pass

	def getUserUnit(self,units="length"):
		"""
		Returns the formula in the user unit system for the specified units.

    Args:
      units (str): The units to consider.

    Raises:
      ValueError: If units is invalid.

    Returns:
      str: The formula in the user unit system.
    
		"""
		pass

	def setSystem(self,system="SI"):
		"""
		Sets user specified system to system.
		"""
		pass

	@property
	def shortSystemName(self):
		pass
	@shortSystemName.setter
	def shortSystemName(self):
		pass

	@property
	def system(self):
		pass
	@system.setter
	def system(self):
		pass

	def toBase(self,value, units="length"):
		"""
		Converts the value from the user specified unit to base units

    Args:
      value (Union[float, list[float], str, list[str]]): The value to convert.
      units (str): The units to convert.

    Returns:
      float: The converted value.
    
		"""
		pass

class collections:
	pass

class enum:
	pass

class parameterManager:
	pass

class settings:
	"""
Settings are named values maintained across application runs.

   They are user settable via the PreferencesEditor from the File menu.

   Settings are stored hierarchically in sections.
   To set/get a setting you use a slash (/) seperated string.

   This module supports the use cases:
     get the current value of a setting
     set the value of a setting
     define settings for plugins

   To get a setting value use:
     from hwx.common.Setting import getSetting
     getSetting ("Unity/BaseProfile/Workspace/Workspace/Language")

   To set a value use:
     from hwx.common.Setting import setSetting
     setSetting ("Unity/BaseProfile/Workspace/Workspace/Language", "English")

     Only pre-defined settings can be set.
     This is due to the way the settings are defined at application start up
     The startup code only adds settings to the application setting that are
     found in the plugins xml files and are defined via the classes in this file
     This is desinged to clean up old setting definitions from tha application
     definitions

   To define settings for a plugin:
     This is designed to look/work like the c++ plugins settings from an xml
     file
     The defined settings are added to and saved with the application settings
     Each time the settings are defined they replace the previouse ones.
     BUT if the new settings contain a setting found in the old settings
     and the user had changed it, we use the changed setting

     To define plugin settings use the Plugin, TreeItem and Section classes
     See these class docs for forther information of the following example

     #- Example of defining settings for a plugin ----------------------------
     from hwx.common.Settings import Settings, Plugin, TreeItem, Section

     Colors = "Divergent (Red-Blue)", "Rainbow"

     Plugin ("HFA", displayName="Stamping", sections=(
        TreeItem ("Analysis", sections=(
           Section ("Analysis", settings=(
             ("Element size",    ("Coarse", "*Medium", "Fine")),
             ("Fill Hole",       False),
             ("Run history path", "", "ExistingDirEditorWidget"),
           )),
           Section ("Analysis Legend Colors", settings=(
             ("Thinning",     Colors),
             ("Formability",  Colors),
             ("Thickness",    Colors),
           )),
        )),
     ))
     #- end of example -------------------------------------------------------

"""
	pass

class sigslot:
	pass

class sys:
	"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
_enablelegacywindowsfsencoding -- [Windows only]
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setcheckinterval() -- control how often the interpreter checks for events
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function

"""
	pass

class virtualMethodDecorator:
	def __init__(self,default=None,exceptions: str="<class Exception>"):
		"""
Decorate overloaded virtual methods to handle Python Exceptions

     Python exceptions in virtual methods can cause application crashes
     because of invalid return value.
     This decorator wraps the method with a try/except and returns the
     specified default value.
  
"""
		pass

