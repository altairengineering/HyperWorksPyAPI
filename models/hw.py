from typing import TypeVar
class Any:
	pass
class hw_module:
	class page:
		class Page:
			pass
		class window:
			class Window:
				pass

class AnimationTool:
	def __init__(self,page=None, **kwargs):
		"""

    Class representing the Animation Tool. Provides user with tools to control the animation and its parameters.
    
    :param page: Page the Animation Tool will be linked to. Default is active page.
    :type page: Union[Page, int, str]

    :param kwargs: Attributes of the Animation Tool object.
    :type kwargs: dict

    
"""
		pass

	@property
	def currentFrame(self):
		pass
	@currentFrame.setter
	def currentFrame(self):
		pass

	@property
	def currentTime(self):
		pass
	@currentTime.setter
	def currentTime(self):
		pass

	@property
	def endFrame(self):
		pass
	@endFrame.setter
	def endFrame(self):
		pass

	@property
	def endTime(self):
		pass
	@endTime.setter
	def endTime(self):
		pass

	def isAnimating(self):
		"""
		
        Method to check if page is animating.
        
        :return: Returns True if page is animating.
        :rtype: bool
        
		"""
		pass

	def next(self):
		"""
		Method to set the next frame of the animation.
		"""
		pass

	@property
	def numberOfFrames(self):
		pass
	@numberOfFrames.setter
	def numberOfFrames(self):
		pass

	@property
	def numberOfSteps(self):
		pass
	@numberOfSteps.setter
	def numberOfSteps(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def previous(self):
		"""
		Method to set the previous frame of the animation.
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the animation tool attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	def start(self,num_cycles="0"):
		"""
		Method to start the animation.
		"""
		pass

	@property
	def startFrame(self):
		pass
	@startFrame.setter
	def startFrame(self):
		pass

	@property
	def startTime(self):
		pass
	@startTime.setter
	def startTime(self):
		pass

	def stop(self):
		"""
		Method to stop the animation.
		"""
		pass

class Any:
	def __init__(self,*args, **kwds):
		"""
Internal indicator of special typing constructs.
    See _doc instance attribute for specific docs.
    
"""
		pass

class CaptureImageTool:
	def __init__(self,*args, **kwargs):
		"""

    Class representing the Capture Image Tool. Provides user with tools to define and capture screenshots.
    
    :param kwargs: Attributes of the Capture Image Tool object.
    :type kwargs: dict

    
"""
		pass

	@property
	def area(self):
		pass
	@area.setter
	def area(self):
		pass

	def capture(self):
		"""
		Method to capture the image and save it as a file. If the file name is not specified, the name will be set to *untitled*
        followed by an incremental value (e.g. *untitled1.jpg*).
		"""
		pass

	@property
	def compression(self):
		pass
	@compression.setter
	def compression(self):
		pass

	@property
	def dimension(self):
		pass
	@dimension.setter
	def dimension(self):
		pass

	@property
	def file(self):
		pass
	@file.setter
	def file(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the CaptureImageTool attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Color:
	def __init__(self,rgb=(0, 0, 0),hex: str="#000000", bgr=(0, 0, 0)):
		"""

    Class representing colors in various formats (**RGB**, **BGR**, and **Hex**). A Color object can be referenced to define an entity color.
    
"""
		pass

	@property
	def bgr(self):
		pass
	@bgr.setter
	def bgr(self):
		pass

	@property
	def hex(self):
		pass
	@hex.setter
	def hex(self):
		pass

	@property
	def postIndex(self):
		pass
	@postIndex.setter
	def postIndex(self):
		pass

	@property
	def preIndex(self):
		pass
	@preIndex.setter
	def preIndex(self):
		pass

	@property
	def rgb(self):
		pass
	@rgb.setter
	def rgb(self):
		pass

class ComplexPlotWindow:
	def __init__(self):
		"""

    Class representing a ComplexPlot Window. Gets a ComplexPlot Window for the given page.
    
"""
		pass

	@property
	def axisGradient(self):
		pass
	@axisGradient.setter
	def axisGradient(self):
		pass

	@property
	def axisMode(self):
		pass
	@axisMode.setter
	def axisMode(self):
		pass

	@property
	def axisProportion(self):
		pass
	@axisProportion.setter
	def axisProportion(self):
		pass

	@property
	def backgroundColor(self):
		pass
	@backgroundColor.setter
	def backgroundColor(self):
		pass

	@property
	def cursorAlwaysVisible(self):
		pass
	@cursorAlwaysVisible.setter
	def cursorAlwaysVisible(self):
		pass

	def delete(self,entity, objOrId):
		"""
		
        Method to delete an entity.
        
        :param entity: Entity class.
        :type entity: class
        :param objOrId: Entity object, entity ID, list of entity objects, list of entity IDs, or **all**.
        :type objOrId: Union[Entity, int, list, str]
        
		"""
		pass

	def draw(self):
		"""
		Method to draw the window.
		"""
		pass

	def erase(self):
		"""
		Method to erase window content.
		"""
		pass

	def fit(self,x=True, y=True):
		"""
		
        Method to adjust the view to fit the curves in the plot window.
        
        :param x: If True, the curves will be fitted along *x* axis.
        :type x: bool
        :param y: If True, the curves will be fitted along *y* axis.
        :type y: bool
        
		"""
		pass

	@property
	def graphicsHeight(self):
		pass
	@graphicsHeight.setter
	def graphicsHeight(self):
		pass

	@property
	def graphicsWidth(self):
		pass
	@graphicsWidth.setter
	def graphicsWidth(self):
		pass

	@property
	def gridLineColor(self):
		pass
	@gridLineColor.setter
	def gridLineColor(self):
		pass

	@property
	def gridLineTransparency(self):
		pass
	@gridLineTransparency.setter
	def gridLineTransparency(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	@property
	def lock(self):
		pass
	@lock.setter
	def lock(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def phaseConstrain(self):
		pass
	@phaseConstrain.setter
	def phaseConstrain(self):
		pass

	@property
	def publishFormat(self):
		pass
	@publishFormat.setter
	def publishFormat(self):
		pass

	@property
	def publishWindow(self):
		pass
	@publishWindow.setter
	def publishWindow(self):
		pass

	def recalculate(self):
		"""
		Method to recalculate the curves in the window.
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	@property
	def swapAxis(self):
		pass
	@swapAxis.setter
	def swapAxis(self):
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	def update(self):
		"""
		Method to recalculate the curves, fit the curves along both *x* and *y* axis, and redraw the window.
		"""
		pass

	@property
	def zeroLineColor(self):
		pass
	@zeroLineColor.setter
	def zeroLineColor(self):
		pass

class Font:
	def __init__(self,*args, **kwargs):
		"""

    Class representing a font specified by the family, size, and style configuration.

    :param kwargs: The attributes of the Font.
    :type kwargs: dict

    
"""
		pass

	@property
	def family(self):
		pass
	@family.setter
	def family(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		 
        Set the attributes of the Font object.

        :param kwargs: The attributes of the Font.
        :type kwargs: dict
        
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def style(self):
		pass
	@style.setter
	def style(self):
		pass

class HyperGraph3DWindow:
	def __init__(self,page=None, window=None, id=None):
		pass

	def draw(self):
		"""
		Method to draw the window.
		"""
		pass

	def erase(self):
		"""
		Method to erase window content.
		"""
		pass

	@property
	def graphicsHeight(self):
		pass
	@graphicsHeight.setter
	def graphicsHeight(self):
		pass

	@property
	def graphicsWidth(self):
		pass
	@graphicsWidth.setter
	def graphicsWidth(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def publishFormat(self):
		pass
	@publishFormat.setter
	def publishFormat(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

class HyperGraphWindow:
	def __init__(self):
		"""

    Class representing a HyperGraph Window. Gets a HyperGraph Window for the given page.
    
"""
		pass

	@property
	def axisGradient(self):
		pass
	@axisGradient.setter
	def axisGradient(self):
		pass

	@property
	def backgroundColor(self):
		pass
	@backgroundColor.setter
	def backgroundColor(self):
		pass

	@property
	def cursorAlwaysVisible(self):
		pass
	@cursorAlwaysVisible.setter
	def cursorAlwaysVisible(self):
		pass

	def delete(self,entity, objOrId):
		"""
		
        Method to delete an entity.
        
        :param entity: Entity class.
        :type entity: class
        :param objOrId: Entity object, entity ID, list of entity objects, list of entity IDs, or **all**.
        :type objOrId: Union[Entity, int, list, str]
        
		"""
		pass

	def draw(self):
		"""
		Method to draw the window.
		"""
		pass

	def erase(self):
		"""
		Method to erase window content.
		"""
		pass

	def fit(self,x=True, y=True):
		"""
		
        Method to adjust the view to fit the curves in the plot window.
        
        :param x: If True, the curves will be fitted along *x* axis.
        :type x: bool
        :param y: If True, the curves will be fitted along *y* axis.
        :type y: bool
        
		"""
		pass

	@property
	def graphicsHeight(self):
		pass
	@graphicsHeight.setter
	def graphicsHeight(self):
		pass

	@property
	def graphicsWidth(self):
		pass
	@graphicsWidth.setter
	def graphicsWidth(self):
		pass

	@property
	def gridLineColor(self):
		pass
	@gridLineColor.setter
	def gridLineColor(self):
		pass

	@property
	def gridLineTransparency(self):
		pass
	@gridLineTransparency.setter
	def gridLineTransparency(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	@property
	def lock(self):
		pass
	@lock.setter
	def lock(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def publishFormat(self):
		pass
	@publishFormat.setter
	def publishFormat(self):
		pass

	@property
	def publishWindow(self):
		pass
	@publishWindow.setter
	def publishWindow(self):
		pass

	def recalculate(self):
		"""
		Method to recalculate the curves in the window.
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	def update(self):
		"""
		Method to recalculate the curves, fit the curves along both *x* and *y* axis, and redraw the window.
		"""
		pass

	@property
	def zeroLineColor(self):
		pass
	@zeroLineColor.setter
	def zeroLineColor(self):
		pass

class HyperMeshWindow:
	def __init__(self,page=None, window=None, id=None):
		pass

	def draw(self):
		"""
		Method to draw the window.
		"""
		pass

	def erase(self):
		"""
		Method to erase window content.
		"""
		pass

	@property
	def graphicsHeight(self):
		pass
	@graphicsHeight.setter
	def graphicsHeight(self):
		pass

	@property
	def graphicsWidth(self):
		pass
	@graphicsWidth.setter
	def graphicsWidth(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def publishFormat(self):
		pass
	@publishFormat.setter
	def publishFormat(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

class HyperViewWindow:
	def __init__(self):
		pass

	def addModelAndResult(self,model=None, result=None, overlay=False, template="none"):
		"""
		
        Method to load model and result.

        :param model: Model file name.
        :type model: str
        :param result: Result file name.
        :type result: str
        :param overlay: If True, overlays the model.
        :type overlay: bool
        :param template: Template used to load model and result.
        :type template: str
        
		"""
		pass

	def addResult(self,resFiles, replace=False):
		"""
		
        Method to add results.
        
        :param resFiles: Result file name.
        :type resFiles: Union[str, list]
        :param replace: If True, replaces the currently loaded result file.
        :type replace: bool
        
		"""
		pass

	def delete(self,entity, objOrId):
		"""
		
        Method to delete an entity.
        
        :param entity: Entity class.
        :type entity: class
        :param objOrId: Entity object, entity ID, list of entity objects, list of entity IDs, or **all**.
        :type objOrId: Union[Entity, int, list, str]
        
		"""
		pass

	def draw(self):
		"""
		Method to draw the window.
		"""
		pass

	def erase(self):
		"""
		Method to erase window content.
		"""
		pass

	def fit(self,mode: str =" model"):
		"""
		
        Method to adjust the view to fit the objects in the modeling window.
        
        :param mode: Mode of the fit operation. Valid values are **model** (default), **selected**, and **allframes**.
        :type mode: str
        
		"""
		pass

	def getActiveModel(self):
		"""
		
        Method to get the active model object.

        :return: Model object.
        :rtype: Model
        
		"""
		pass

	def getModel(self,id: int):
		"""
		Method to get the model object.
        
        :param id: The ID of the model.
        :type id: int
        :return: Model object.
        :rtype: Model
        
		"""
		pass

	def getModels(self):
		"""
		
        Method to get the model object list.

        :return: Model object list.
        :rtype: list
        
		"""
		pass

	def getResultDefinitionList(self,type: str):
		"""
		Method to get the ResultDefinition object list.
        
        :param type: Type of ResultDefinition (**scalar**, **vector**, or **tensor**)
        :type type: int
        :return: Model object.
        :rtype: Model
        
		"""
		pass

	@property
	def graphicsHeight(self):
		pass
	@graphicsHeight.setter
	def graphicsHeight(self):
		pass

	@property
	def graphicsWidth(self):
		pass
	@graphicsWidth.setter
	def graphicsWidth(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def publishFormat(self):
		pass
	@publishFormat.setter
	def publishFormat(self):
		pass

	@property
	def sectionFeatureLines(self):
		pass
	@sectionFeatureLines.setter
	def sectionFeatureLines(self):
		pass

	@property
	def sectionTransparency(self):
		pass
	@sectionTransparency.setter
	def sectionTransparency(self):
		pass

	def setActiveModel(self,id: int):
		"""
		Method to set the active model and returns model object.
        
        :param id: The ID of the model.
        :type id: int
        :return: Model object.
        :rtype: Model
        
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	def update(self):
		"""
		Method to fit the model and draw the window.
		"""
		pass

class ImageDimension:
	def __init__(self,value, names=None, module=None, qualname=None, type=None, start=1):
		"""
An enumeration.
"""
		pass

class ImageType:
	def __init__(self,value, names=None, module=None, qualname=None, type=None, start=1):
		"""
An enumeration.
"""
		pass

class Page:
	def __init__(self,layout="0",title: str="Untitled", _obj=None, _id="0"):
		"""

    Class representing a page of the application.
    The constructor raises an exception if not pointed to a valid page.
    
    :param layout: The page layout.
    :type layout: int

    :param title: The page title.
    :type title: str
    
"""
		pass

	def draw(self,updateInterface: bool = False):
		"""
		
        Method to draw the page.
        
        :param bool updateInterface: If True, the graphics are updated.
        
		"""
		pass

	def getAverageAnimationFramerate(self):
		"""
		
        Method to get the average animation frame rate.
        
        :return: Animation frame rate.
        :rtype: int
        
		"""
		pass

	def getNumberOfWindows(self):
		"""
		
        Method to get the number of windows on a page.
        
        :return: Number of windows on a page.
        :rtype: int
        
		"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isAnimating(self):
		"""
		
        Method to check if page is animating.
        
        :return: Returns True if page is animating.
        :rtype: bool
        
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the page attributes.
        
        :param dict kwargs: attributes
        
		"""
		pass

	def startAnimation(self,num_cycles="0"):
		"""
		
        Method to start the animation.
        
        :param int num_cycles: Number of animation cycles defining how many times animation will be repeated (default 0).
        
		"""
		pass

	def stopAnimation(self):
		"""
		Method to stop the animation.
		"""
		pass

	@property
	def title(self):
		pass
	@title.setter
	def title(self):
		pass

	@property
	def titleAsDisplayed(self):
		pass
	@titleAsDisplayed.setter
	def titleAsDisplayed(self):
		pass

class Session:
	def __init__(self):
		"""

    A singleton class representing the Session. 
    All session level attributes and methods are defined in this class.
    
"""
		pass

	def close(self):
		"""
		Method to close the session.
		"""
		pass

	def delete(self,entity, objOrid):
		"""
		Method to delete an entity.
        
        :param entity: Entity to be deleted. Currently only supported for Page class.
        :type entity: Page

        :param objOrid: ID, title, Page object or list of IDs, titles or Page objects.
        :type objOrid: Union[int, str, Page, list]
  
        
		"""
		pass

	def get(self,tag, id: Any = None, label: str = None, title: str = None, page: int|hw_module.page.Page = None, window: int|hw_module.window.Window = None, model=None, curve: Any = None, reference: str = None, labelAsDisplayed: str = None, name: str = None, curveLabelAsDisplayed: str = None, curveLabel: str = None, operation: str = None):
		"""
		
        Method to get an entity object of class Page, Window, Model, Result, ResultDefinitionScalar, ResultDefinitionVector, ResultDefinitionTensor, ResultDefinitionIso, ResultDisplayIso, LegendScalar, LegendTensor, LegendVector,
        Note, CurveXY, DatumHorizontal, DatumVertical, AxisHorizontal, AxisVertical, Header, Footer, MathXY,SectionCutPlanar,SectionCutSpherical.
        
        :param tag: The class of the entity to get.
        :type tag: class

        :param id: id of the entity.
        :type id: int

        :param label: label of the entity.
        :type label: str

        :param title: title of the entity
        :type title: str

        :param page: Page of the entity specified as either a Page object or ID. Default is active page.
        :type page: Union[Page, int]

        :param window: Window of the entity specified as either a Window object or ID. Default is active window.
        :type window: Union[Window, int]

        :param model: Model specified either as a Model object or ID.
        :type model: Union[Model, int]

        
		"""
		pass

	def getMultiCoreMode(self):
		"""
		Method to get the MultiCore mode. Applicable for HyperView client. 
        
        :return: Returns True if MultiCore profile is loaded.
        :rtype: bool   
        
		"""
		pass

	def getPages(self):
		"""
		Method to get the pages.

        :return: List of Page class objects.
        :rtype: list    
        
		"""
		pass

	def getWindows(self,page: Any = None):
		"""
		Method to get the windows in specified page.

        :param page: Page for the windows. Default is active page.
        :type page: Union[Page, int, str]

        :return: List of windows in given page.
        :rtype: list    
        
		"""
		pass

	def load(self,filename, append=True):
		"""
		Method to load the session.

        :param filename: Session file name.
        :type filename: str

        :param append: If True, appends the given file to the existing session. Default is True.
        :type append: bool    
        
		"""
		pass

	def new(self):
		"""
		Method to create a new session.
		"""
		pass

	def save(self,filename=None):
		"""
		Method to save the session.

        :param filename: Session file name. If filename is not specified, it will save the session as *Untitled.mvw*.
        :type filename: str
  
        
		"""
		pass

	def setActive(self,tag, id: Any = None, title: str = None, page: int|hw_module.page.Page = None, window: int|hw_module.window.Window = None, model=None):
		"""
		Method to set the active entity like Page, Window, or Model.

        :param tag: Entity to be set as active. Applicable for Page, Window or Model.
        :type tag: Page, Window or Model

        :param id: ID of the entity.
        :type id: int

        :param title: Title of the entity. Applicable for Page and Model.
        :type title: str

        :param page: Page of the entity specified as either a Page object or ID. Default is active page.
        :type page: Union[Page, int]

        :param window: Window of the entity specified as either a Window object or ID. Default is active window.
        :type window: Union[Window, int]

        :param model: Model specified either as a Model object or ID.
        :type model: Union[Model, int]

        
		"""
		pass

class Tclinter:
	"""

  implements:

    tcl    - class to talk back into Hyperworks tcl
             implements an eval and an exec method

    Widget - make a Hyperworks tcl widget work with Tkinter

"""
	pass

class Union:
	def __init__(self,*args, **kwds):
		"""
Internal indicator of special typing constructs.
    See _doc instance attribute for specific docs.
    
"""
		pass

class Window:
	def __init__(self,page=None, window=None, id=None):
		"""

    Class representing a Window. Get a Window for the given page.
    The constructor raises an exception if not pointed to a valid window.
    
    :param page: The page of the window.
    :type page: Union[int, Page, str]

    :param window: The specific window.
    :type window: Union[int, Window]

    :param id: ID of the window
    :type id: int
    
"""
		pass

	def draw(self):
		"""
		Method to draw the window.
		"""
		pass

	def erase(self):
		"""
		Method to erase window content.
		"""
		pass

	@property
	def graphicsHeight(self):
		pass
	@graphicsHeight.setter
	def graphicsHeight(self):
		pass

	@property
	def graphicsWidth(self):
		pass
	@graphicsWidth.setter
	def graphicsWidth(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def publishFormat(self):
		pass
	@publishFormat.setter
	def publishFormat(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

class XYPlotWindow:
	def __init__(self):
		"""

    Class representing a XYPlot Window. Gets a XYPlot Window for the given page.
    
"""
		pass

	@property
	def axisGradient(self):
		pass
	@axisGradient.setter
	def axisGradient(self):
		pass

	@property
	def backgroundColor(self):
		pass
	@backgroundColor.setter
	def backgroundColor(self):
		pass

	@property
	def cursorAlwaysVisible(self):
		pass
	@cursorAlwaysVisible.setter
	def cursorAlwaysVisible(self):
		pass

	@property
	def cursorCurveColor(self):
		pass
	@cursorCurveColor.setter
	def cursorCurveColor(self):
		pass

	@property
	def cursorCurveStyle(self):
		pass
	@cursorCurveStyle.setter
	def cursorCurveStyle(self):
		pass

	@property
	def cursorDisplay(self):
		pass
	@cursorDisplay.setter
	def cursorDisplay(self):
		pass

	@property
	def cursorThickness(self):
		pass
	@cursorThickness.setter
	def cursorThickness(self):
		pass

	def delete(self,entity, objOrId):
		"""
		
        Method to delete an entity.
        
        :param entity: Entity class.
        :type entity: class
        :param objOrId: Entity object, entity ID, list of entity objects, list of entity IDs, or **all**.
        :type objOrId: Union[Entity, int, list, str]
        
		"""
		pass

	def draw(self):
		"""
		Method to draw the window.
		"""
		pass

	def erase(self):
		"""
		Method to erase window content.
		"""
		pass

	def fit(self,x=True, y=True):
		"""
		
        Method to adjust the view to fit the curves in the plot window.
        
        :param x: If True, the curves will be fitted along *x* axis.
        :type x: bool
        :param y: If True, the curves will be fitted along *y* axis.
        :type y: bool
        
		"""
		pass

	@property
	def graphicsHeight(self):
		pass
	@graphicsHeight.setter
	def graphicsHeight(self):
		pass

	@property
	def graphicsWidth(self):
		pass
	@graphicsWidth.setter
	def graphicsWidth(self):
		pass

	@property
	def gridLineColor(self):
		pass
	@gridLineColor.setter
	def gridLineColor(self):
		pass

	@property
	def gridLineTransparency(self):
		pass
	@gridLineTransparency.setter
	def gridLineTransparency(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def invalidPointMode(self):
		pass
	@invalidPointMode.setter
	def invalidPointMode(self):
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	@property
	def lock(self):
		pass
	@lock.setter
	def lock(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def publishFormat(self):
		pass
	@publishFormat.setter
	def publishFormat(self):
		pass

	@property
	def publishWindow(self):
		pass
	@publishWindow.setter
	def publishWindow(self):
		pass

	def recalculate(self):
		"""
		Method to recalculate the curves in the window.
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	@property
	def uniformAspectRatio(self):
		pass
	@uniformAspectRatio.setter
	def uniformAspectRatio(self):
		pass

	def update(self):
		"""
		Method to recalculate the curves, fit the curves along both *x* and *y* axis, and redraw the window.
		"""
		pass

	@property
	def zeroLineColor(self):
		pass
	@zeroLineColor.setter
	def zeroLineColor(self):
		pass

class animation:
	pass

class capturetool:
	pass

class color:
	pass

class common:
	pass

class enum:
	pass

def evalHWC(command_or_file: str):
	"""

    Evaluates a HWC based expression. Alternatively, if supplied a path to a HWC command file,
    it executes the command file.
    
"""
	pass

def evalTcl(command: str):
	"""

    Evaluates a Tcl based expression.   
    
"""
	pass

class font:
	pass

class hwi:
	pass

class hwiimport:
	def __init__(self):
		pass

	def runningInHyperworks(self):
		pass

class hwtypes:
	pass

class mdi:
	pass

class os:
	"""
OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).

"""
	pass

class pag:
	pass

class page:
	pass

class pathlib:
	pass

class re:
	"""
Support for regular expressions (RE).

This module provides regular expression matching operations similar to
those found in Perl.  It supports both 8-bit and Unicode strings; both
the pattern and the strings being processed can contain null bytes and
characters outside the US ASCII range.

Regular expressions can contain both special and ordinary characters.
Most ordinary characters, like "A", "a", or "0", are the simplest
regular expressions; they simply match themselves.  You can
concatenate ordinary characters, so last matches the string 'last'.

The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?aiLmsux) The letters set the corresponding flags defined below.
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.

The special sequences consist of "\\" and a character from the list
below.  If the ordinary character is not on the list, then the
resulting RE will match the second character.
    \number  Matches the contents of the group of the same number.
    \A       Matches only at the start of the string.
    \Z       Matches only at the end of the string.
    \b       Matches the empty string, but only at the start or end of a word.
    \B       Matches the empty string, but not at the start or end of a word.
    \d       Matches any decimal digit; equivalent to the set [0-9] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode digits.
    \D       Matches any non-digit character; equivalent to [^\d].
    \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode whitespace characters.
    \S       Matches any non-whitespace character; equivalent to [^\s].
    \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
             in bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the
             range of Unicode alphanumeric characters (letters plus digits
             plus underscore).
             With LOCALE, it will match the set [0-9_] plus characters defined
             as letters for the current locale.
    \W       Matches the complement of \w.
    \\       Matches a literal backslash.

This module exports the following functions:
    match     Match a regular expression pattern to the beginning of a string.
    fullmatch Match a regular expression pattern to all of a string.
    search    Search a string for the presence of a pattern.
    sub       Substitute occurrences of a pattern found in a string.
    subn      Same as sub, but also return the number of substitutions made.
    split     Split a string by the occurrences of a pattern.
    findall   Find all occurrences of a pattern in a string.
    finditer  Return an iterator yielding a Match object for each match.
    compile   Compile a pattern into a Pattern object.
    purge     Clear the regular expression cache.
    escape    Backslash all non-alphanumerics in a string.

Each function other than purge and escape can take an optional 'flags' argument
consisting of one or more of the following module constants, joined by "|".
A, L, and U are mutually exclusive.
    A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                   match the corresponding ASCII character categories
                   (rather than the whole Unicode categories, which is the
                   default).
                   For bytes patterns, this flag is the only available
                   behaviour and needn't be specified.
    I  IGNORECASE  Perform case-insensitive matching.
    L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
    M  MULTILINE   "^" matches the beginning of lines (after a newline)
                   as well as the string.
                   "$" matches the end of lines (before a newline) as well
                   as the end of the string.
    S  DOTALL      "." matches any character at all, including the newline.
    X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    U  UNICODE     For compatibility only. Ignored for string patterns (it
                   is the default), and forbidden for bytes patterns.

This module also defines an exception 'error'.


"""
	pass

class sess:
	pass

class session:
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

class utils:
	pass

class win:
	pass

class window:
	pass

