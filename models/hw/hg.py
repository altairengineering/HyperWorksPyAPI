from typing import TypeVar
class hw_module:
	class window:
		class Window:
			pass
		class page:
			class Page:
				pass

class AxisHorizontal:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", **kwargs):
		"""

    A class representing a AxisHorizontal in XY Chart. Creates a Horizontal Axis for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class AxisVertical:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", **kwargs):
		"""

    A class representing a AxisVertical in XY Chart. Creates a Vertical Axis for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class CreateCurvesByFile:
	def __init__(self,**kwargs):
		"""

    Class representing the CreateCurvesByFile.Provides the user to single file or multiple files with intersecting data and plot the data from all files simultaneously in the current HyperGraph session.
    For the Multiple Files, Intersecting data refers to files that contain the same type, request, and component information.
    The constructor raises an exception if the creation of CreateCurvesByFile object fails.
    
    :param kwargs: Attributes of the CreateCurvesByFile object.
    :type kwargs: dict

    
"""
		pass

	@property
	def file(self):
		pass
	@file.setter
	def file(self):
		pass

	@property
	def layoutOrganisation(self):
		pass
	@layoutOrganisation.setter
	def layoutOrganisation(self):
		pass

	@property
	def layoutType(self):
		pass
	@layoutType.setter
	def layoutType(self):
		pass

	def run(self):
		"""
		
        Method to plot the curves based on the information specifed.
        The method raises an error message for the following cases:
        
        | - If the file is not empty.
        | - If the subcase is null or empty.
        | - If the yDataType or yRequest or yComponent is null or empty.
        | - If the yRequestFilter and yRequest gives empty requests list.
        | - If the yComponentFilter and yComponent gives empty component list.
        
        
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the CreateCurvesByFile attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def subcase(self):
		pass
	@subcase.setter
	def subcase(self):
		pass

	@property
	def xComponent(self):
		pass
	@xComponent.setter
	def xComponent(self):
		pass

	@property
	def xComponentMatchY(self):
		pass
	@xComponentMatchY.setter
	def xComponentMatchY(self):
		pass

	@property
	def xDataType(self):
		pass
	@xDataType.setter
	def xDataType(self):
		pass

	@property
	def xRequest(self):
		pass
	@xRequest.setter
	def xRequest(self):
		pass

	@property
	def xRequestMatchY(self):
		pass
	@xRequestMatchY.setter
	def xRequestMatchY(self):
		pass

	@property
	def yComponent(self):
		pass
	@yComponent.setter
	def yComponent(self):
		pass

	@property
	def yComponentFilter(self):
		pass
	@yComponentFilter.setter
	def yComponentFilter(self):
		pass

	@property
	def yComponentSorting(self):
		pass
	@yComponentSorting.setter
	def yComponentSorting(self):
		pass

	@property
	def yDataType(self):
		pass
	@yDataType.setter
	def yDataType(self):
		pass

	@property
	def yRequest(self):
		pass
	@yRequest.setter
	def yRequest(self):
		pass

	@property
	def yRequestFilter(self):
		pass
	@yRequestFilter.setter
	def yRequestFilter(self):
		pass

	@property
	def yRequestSorting(self):
		pass
	@yRequestSorting.setter
	def yRequestSorting(self):
		pass

class CurveComplex:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", id_type: str = None, **kwargs):
		"""

    A class representing a Curve in Complex Chart.Create a CurveComplex for the given window and page.
    Raises a Exception parmater doesn't points to a valid Hypergraph Plot window
    
    :param window: The window of the curve.
    :type window: (Union[int, Window])

    :param page: The page of the curve.
    :type page: (Union[int, Page])

    
"""
		pass

	def getXYvalues(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def mathRef(self):
		pass
	@mathRef.setter
	def mathRef(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

	@property
	def xValues(self):
		pass
	@xValues.setter
	def xValues(self):
		pass

	@property
	def y2Values(self):
		pass
	@y2Values.setter
	def y2Values(self):
		pass

	@property
	def yiValues(self):
		pass
	@yiValues.setter
	def yiValues(self):
		pass

	@property
	def ymValues(self):
		pass
	@ymValues.setter
	def ymValues(self):
		pass

	@property
	def ypValues(self):
		pass
	@ypValues.setter
	def ypValues(self):
		pass

	@property
	def yrValues(self):
		pass
	@yrValues.setter
	def yrValues(self):
		pass

class CurveXY:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", id_type: str = None, **kwargs):
		"""

    A class representing a Curve in XY Chart. Create a CurveXY for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph XY plot (Line Chart) window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def mathAdd(self,name, parameter="{}", **kwargs):
		"""
		
        Create new instance of stackmath operation and adds an operation to the curve.
        Raises an Exception parameter does not points to a valid stackmath operation.

        :param name: The name of the stackmath operation.
        :type name: str
        :param parameter: A dictionary containing parameters for the operation.
        :type parameter: dict
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :return: New instance of MathXY.
        :rtype: MathXY
        
		"""
		pass

	def mathCopy(self,*args):
		"""
		
        Returns the complete math stack of the curve and its attributes.

        :param args: The list of name/ID of the operation.
        :type name: list

        :return: Complete math stack of the curve and its attributes.
        :rtype: dict
        
		"""
		pass

	def mathCut(self,*args):
		"""
		
        Removes the stackmath operation from the stack and returns a dictionary of all removed operation with attributes.

        :param args: The list of name/ID of stackmath operation to be removed.
        :type name: list

        :return: Complete math stack of the curve and its attributes.
        :rtype: dict
        
		"""
		pass

	def mathDown(self,name):
		"""
		
        Move a stackmath operation one level down. 
        Raises an Exception parameter does not point to a valid stackmath operation.

        :param name: The name/ID of the operation.
        :type name: str or int
        
		"""
		pass

	def mathEdit(self,value, parameter="{}", **kwargs):
		"""
		
        Edit the attributes of a stackmath operation.
        Raises an Exception parameter does not point to a valid stackmath operation.

        :param value: The name/ID/MathXY object of the operation.
        :type name: str or int or MathXY
        :param parameter: A dictionary containing parameters for the operation.
        :type parameter: dict
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :return: None
        :rtype: None
        
		"""
		pass

	def mathGetParameters(self,name):
		"""
		
        Returns all the attributes of the stackmath operation.
        Raises an Exception parameter does not point to a valid stackmath operation.

        :param name: The name/ID of the operation.
        :type name: str or int

        :return: All the attributes of the stackmath operation.
        :rtype: dict
        
		"""
		pass

	def mathPaste(self,inputdict, after=-1):
		"""
		
        Creates stackmath operation from the math Dictionary and add it to the end of stack or after a ID.

        :param inputdict: The dict of stackmath operation and attributes.
        :type name: dict

        :param after: The name/ID of the operation after which we need to add the new inputdict.
        :type name: str or int
        
		"""
		pass

	@property
	def mathRef(self):
		pass
	@mathRef.setter
	def mathRef(self):
		pass

	def mathRemove(self,val: str|int):
		"""
		
        Removes a stackmath operation.
        Raises an Exception parameter does not point to a valid stackmath operation.

        :param val: The name/ID of the operation.
        :type name: str or int
        
		"""
		pass

	def mathRemoveAll(self):
		"""
		
        Removes all stackmath operation.
        
		"""
		pass

	def mathUp(self,name):
		"""
		
        Move a stackmath operation one level up.
        Raises an Exception parameter does not point to a valid stackmath operation.

        :param name: The name/ID of the operation.
        :type name: str or int
        
		"""
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

	@property
	def xValues(self):
		pass
	@xValues.setter
	def xValues(self):
		pass

	@property
	def xyValues(self):
		pass
	@xyValues.setter
	def xyValues(self):
		pass

	@property
	def yValues(self):
		pass
	@yValues.setter
	def yValues(self):
		pass

class DataFile:
	def __init__(self,file: str):
		"""

    Class representing a DataFile. Provides methods to interact with the data contained within it.
    The constructor raises an exception if file name or path is not valid or doesn't exist.
    
    :param file: The file name or path for the data file.
    :type file: str

    
"""
		pass

	def getComponents(self,datatype: str, includeTime: bool = True):
		"""
		
        Method to get the list of all components for a given datatype.
        
        :getter: Gets the list of all components for a given datatype.
        :type: list

        :param datatype: The name of the data type that is being queried. Components vary by data type. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param includeTime: A param that determines if Time is to be included as a dataType. Defaults to True.
        :type includeTime: bool
        
		"""
		pass

	def getComponentsPerRequest(self,datatype: str, request: str, includeTime: bool = True):
		"""
		
        Method to get the list of all components for a given datatype and request. It differs from GetComponentList in that it filters out components that are marked by the reader as not containing data.
        
        :getter: Gets the list of all components for a given datatype and request.
        :type: list

        :param datatype: The name of the data type that is being queried. Components vary by datatype.For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request to be used as a filter. Components vary by request. For a list of request names, use the method getRequests.
        :type request: str
        :param includeTime: A param that determines if Time is to be included as a dataType. Defaults to True.
        :type includeTime: bool
        
		"""
		pass

	def getDataTypes(self,includeTime: bool = True):
		"""
		
        Method to get the list of all datatypes.
        
        :getter: Gets the list of all datatypes.
        :type: list

        :param includeTime: A param that determines if Time is to be included as a dataType. Defaults to True.
        :type includeTime: bool
        
		"""
		pass

	def getMetaDataLabel(self,datatype: str, request: str, component: str, metadata: str):
		"""
		
        Method to get the label of the  metadata item associated with a file channel.The channel is identified by the datatype, request, and component parameters. These strings are specific to the particular file.
        
        :getter: Gets the label of the  metadata item associated with a file channel.
        :type: str

        :param datatype: The name of the data type that is being queried to specify the channel. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request that is being queried to specify the channel. For a list of request names, use the method getRequests.
        :type request: str
        :param component: The name of the component that is being queried to specify the channel. For a list of component names, use the method getComponents.
        :type component: str
        :param metadata: The item of data to retrieve.
        :type metadata: str
        
		"""
		pass

	def getMetaDataList(self,datatype: str, request: str, component: str):
		"""
		
        Method to get the list of meta data items associated with a file channel.The channel is identified by the datatype, request, and component parameters. These strings are specific to the particular file.

        :getter: Gets the list of meta data items associated with a file channel.
        :type: list

        :param datatype: The name of the data type that is being queried to get the channel. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request that is being queried to get the channel. For a list of request names, use the method getRequests.
        :type request: str
        :param component: The name of the component that is being queried to get the channel. For a list of component names, use the method getComponents.
        :type component: str
        
		"""
		pass

	def getMetaDataType(self,datatype: str, request: str, component: str, metadata: str):
		"""
		
        Method to get the type of the metadata item associated with the file channel.The channel is identified by the datatype, request, and component parameters. These strings are specific to the particular file.
        
        :getter: Gets the type of the metadata item associated with the file channel.
        :type: str

        :param datatype: The name of the data type that is being queried to specify the channel. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request that is being queried to specify the channel. For a list of request names, use the method getRequests.
        :type request: str
        :param component: The name of the component that is being queried to specify the channel. For a list of component names, use the method getComponents.
        :type component: str
        :param metadata: The item of data to retrieve.
        :type metadata: str
        
		"""
		pass

	def getMetaDataValue(self,datatype: str, request: str, component: str, metadata: str):
		"""
		
        Method to get an item of meta data associated with a file channel.The channel is identified by the datatype, request, and component parameters. These strings are specific to the particular file.
        
        :getter: Gets an item of meta data associated with a file channel.
        :type: str

        :param datatype: The name of the data type that is being queried to specify the channel. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request that is being queried to specify the channel. For a list of request names, use the method getRequests.
        :type request: str
        :param component: The name of the component that is being queried to specify the channel. For a list of component names, use the method getComponents.
        :type component: str
        :param metadata: The item of data to retrieve.
        :type metadata: str
        
		"""
		pass

	def getRequests(self,datatype: str, includeTime: bool = True):
		"""
		
        Method to get the list of all requests for a given datatype.
        
        :getter: Gets the list of all requests for a given datatype.
        :type: list

        :param datatype: The name of the data type that is being queried. Requests vary by data type. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param includeTime: A param that determines if Time is to be included as a dataType. Defaults to True.
        :type includeTime: bool
        
		"""
		pass

	def getSubcaseIds(self):
		"""
		
        Method to get the list of the IDs of all subcases.
        
        :getter: Gets the list of the IDs of all subcases.
        :type: list
        
		"""
		pass

	def getSubcaseLabels(self):
		"""
		
        Method to get the list of the labels of all subcases.
        
        :getter: Gets the list of the labels of all subcases.
        :type: list
        
		"""
		pass

	def getTimeChannelComponent(self,datatype: str, request: str, component: str):
		"""
		
        Method to get the component name of the time channel associated with a specified data channel.
        
        :getter: Gets the component name of the time channel associated with a specified data channel.
        :type: str

        :param datatype: The name of the data type that is being queried to specify the data channel. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request that is being queried to specify the data channel. For a list of request names, use the method getRequests.
        :type request: str
        :param component: The name of the component that is being queried to specify the data channel. For a list of component names, use the method getComponents.
        :type component: str
        
		"""
		pass

	def getTimeChannelDataType(self,datatype: str, request: str, component: str):
		"""
		
        Method to get the datatype name of the time channel associated with a specified data channel. The data channel is specified by the datatype, request, and component parameters.
        
        :getter: Gets the datatype name of the time channel associated with a specified data channel.
        :type: str

        :param datatype: The name of the data type that is being queried to get the channel. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request that is being queried to get the channel. For a list of request names, use the method getRequests.
        :type request: str
        :param component: The name of the component that is being queried to get the channel. For a list of component names, use the method getComponents.
        :type component: str
        
		"""
		pass

	def getTimeChannelRequest(self,datatype: str, request: str, component: str):
		"""
		
        Method to get the request name of the time channel associated with a specified data channel.
        
        :getter: Gets the request name of the time channel associated with a specified data channel.
        :type: str

        :param datatype: The name of the data type that is being queried to specify the data channel. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param request: The name of the request that is being queried to specify the data channel. For a list of request names, use the method getRequests.
        :type request: str
        :param component: The name of the component that is being queried to specify the data channel. For a list of component names, use the method getComponents.
        :type component: str
        
		"""
		pass

	@property
	def readerVersion(self):
		pass
	@readerVersion.setter
	def readerVersion(self):
		pass

	@property
	def subcase(self):
		pass
	@subcase.setter
	def subcase(self):
		pass

class DataFileQuery:
	def __init__(self,file: str,dataType: str=" ", requests: str|list =" []", components: str|list =" []", includeTime: str = True, **kwargs):
		"""

    Class representing a DataFileQuery for querying data from a file.
    The constructor raises an exception if file name or path is not valid or doesn't exist.
    
    :param file: The name or path for the data file.
    :type file: str
    :param dataType (Optional): The dataType selected for the data file query. Defaults to empty string.
    :type dataType: str
    :param requests (Optional): The requests selected for the data file query. Defaults to empty string or list.
    :type requests: Union[str, list]
    :param components (Optional): The components selected for the data file query. Defaults to empty string or list.
    :type components: Union[str, list]
    :param includeTime (Optional): A param that determines if Time is to be included as a dataType. Defaults to True.
    :type includeTime: bool

    
"""
		pass

	@property
	def components(self):
		pass
	@components.setter
	def components(self):
		pass

	@property
	def dataType(self):
		pass
	@dataType.setter
	def dataType(self):
		pass

	def getChannelInfo(self):
		"""
		
        Method to get the file channel information for the data file query.
        
        :getter: Gets the file channel information for the data file query.
        :type: dictionary

        
		"""
		pass

	@property
	def includeTime(self):
		pass
	@includeTime.setter
	def includeTime(self):
		pass

	@property
	def readerVersion(self):
		pass
	@readerVersion.setter
	def readerVersion(self):
		pass

	@property
	def requests(self):
		pass
	@requests.setter
	def requests(self):
		pass

	def run(self,outputType: str):
		"""
		
        Method to get the data vectors for the data file query.
        
        :getter: Gets the data vectors for the data file query.
        :type: numpy array or pandas dataframe

        :param outputType: The type of output type (numpy or pandas).
        :type outputType: str

        
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the data file query attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def sort(self):
		pass
	@sort.setter
	def sort(self):
		pass

	@property
	def subcase(self):
		pass
	@subcase.setter
	def subcase(self):
		pass

class DatumHorizontal:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", **kwargs):
		"""

    A class representing a DatumHorizontal in XY Chart. Creates a Horizontal Datum for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class DatumVertical:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", **kwargs):
		"""

    A class representing a DatumVertical in XY Chart. Creates a Vertical Datum for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class ExportCurves:
	def __init__(self,**kwargs):
		"""

    Class providing functionality to export plot data in several different formats.   
    
"""
		pass

	def export(self):
		"""
		
        Exports plot data.
        
		"""
		pass

	@property
	def exportAxisValues(self):
		pass
	@exportAxisValues.setter
	def exportAxisValues(self):
		pass

	@property
	def file(self):
		pass
	@file.setter
	def file(self):
		pass

	@property
	def format(self):
		pass
	@format.setter
	def format(self):
		pass

	@property
	def isoMmeDeleteExistingFiles(self):
		pass
	@isoMmeDeleteExistingFiles.setter
	def isoMmeDeleteExistingFiles(self):
		pass

	def isoMmeTrimCurveLabel(self,startCharacterId, endCharacterId):
		"""
		
        To enter a start and end point to remove data outside of the specified range.
        
		"""
		pass

	@property
	def range(self):
		pass
	@range.setter
	def range(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Set the attributes of the ExportCurves object.

        :param kwargs: Attributes of ExportCurves object to set.
        :type kwargs: dict
        :raises ValueError: If an invalid attribute is provided.
        
		"""
		pass

class Footer:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, **kwargs):
		"""

    A class representing a Footer in XY Chart. Returns a Footer for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class Header:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, **kwargs):
		"""

    A class representing a Header in XY Chart. Returns a Header for the given window and page.
    RRaises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class Legend:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, **kwargs):
		"""

    A class representing a Legend in XY Chart. Returns a Legend for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class MathXY:
	def __init__(self,curve, id: int = 1):
		"""

    Returns a stackmath operation object, defined by curve and ID.
    Raises an Exception if those parameters do not point to a valid curve in a HyperGraph XY plot (Line Chart) window.

    :param curve: The curve for the stackmath operation.
    :type curve: Union[int, CurveXY]

    :param id: The id of the stackmath operation.
    :type id: int
    
"""
		pass

	@property
	def curve(self):
		pass
	@curve.setter
	def curve(self):
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def operation(self):
		pass
	@operation.setter
	def operation(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Set the attributes of the stackmath object.

        :param kwargs: Attributes of stackmath object to set.
        :type kwargs: dict
        :raises ValueError: If an invalid attribute is provided.
        
		"""
		pass

class MultipleFiles:
	def __init__(self,**kwargs):
		"""

    Class representing the MultipleFiles.Provides the user to select multiple files with intersecting data (for example, multiple runs of a test) and create a FileSet in the current HyperGraph session.
    Intersecting data refers to files that contain the same type, request, and component information.
    The constructor raises an exception if the creation of MultipleFiles fails.
    
    :param kwargs: Attributes of the MultipleFiles object.
    :type kwargs: dict

    
"""
		pass

	def createFileSet(self):
		"""
		
        Method to create the File set from the Multiple Files.
        The method raises an error message for the following cases:
        
        | - If the directory path is not specified.
        | - If the directory path is not valid.
        | - If the fileList is empty.
        | - If the none of the files mentioned in the fileSet exists in the directory.
        | - If the creation of File Set failed.
        
        :getter: Gets the information for the FileSet created.
        :type: dict
        
		"""
		pass

	@property
	def curveAttributes(self):
		pass
	@curveAttributes.setter
	def curveAttributes(self):
		pass

	@property
	def directory(self):
		pass
	@directory.setter
	def directory(self):
		pass

	@property
	def fileList(self):
		pass
	@fileList.setter
	def fileList(self):
		pass

	@property
	def ignoreStringFirstAppearanceString(self):
		pass
	@ignoreStringFirstAppearanceString.setter
	def ignoreStringFirstAppearanceString(self):
		pass

	@property
	def ignoreStringFirstNcharacters(self):
		pass
	@ignoreStringFirstNcharacters.setter
	def ignoreStringFirstNcharacters(self):
		pass

	@property
	def ignoreStrings(self):
		pass
	@ignoreStrings.setter
	def ignoreStrings(self):
		pass

	@property
	def labelPrefixSuffix(self):
		pass
	@labelPrefixSuffix.setter
	def labelPrefixSuffix(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the MultipleFiles attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def typePrefixSuffix(self):
		pass
	@typePrefixSuffix.setter
	def typePrefixSuffix(self):
		pass

class Note:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", **kwargs):
		"""

    A class representing a Note in XY Chart. Creates a Note for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class axis:
	pass

class core:
	pass

class createcurvesbyFile:
	pass

class curve:
	pass

class datafile:
	pass

class datafilequery:
	pass

class datum:
	pass

class exportcurves:
	pass

class hwiimport:
	def __init__(self):
		pass

	def runningInHyperworks(self):
		pass

class legend:
	pass

class math:
	pass

class multiplefiles:
	pass

class note:
	pass

class title:
	pass

