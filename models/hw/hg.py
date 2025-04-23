from typing import TypeVar
class hw_module:
	class window:
		class Window:
			pass
	class page:
		class Page:
			pass
	class color:
		class Color:
			pass
	class font:
		class Font:
			pass
	class hg:
		class table:
			class Table:
				pass
class tuple:
	pass
class dict:
	pass
class Any:
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

    Class representing the CreateCurvesByFile.Provides the user to select single file or multiple files with intersecting data and plot the data from all files simultaneously in the current HyperGraph session.
    For the Multiple Files, Intersecting data refers to files that contain the same type, request, and component information.
    The constructor raises an exception if the creation of CreateCurvesByFile object fails.
    
    :param kwargs: Attributes of the CreateCurvesByFile object.
    :type kwargs: dict

    
"""
		pass

	@property
	def chartType(self):
		pass
	@chartType.setter
	def chartType(self):
		pass

	@property
	def curveOptions(self):
		pass
	@curveOptions.setter
	def curveOptions(self):
		pass

	@property
	def curveOptionsEnabled(self):
		pass
	@curveOptionsEnabled.setter
	def curveOptionsEnabled(self):
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

class CreateCurvesBySubcase:
	def __init__(self,**kwargs):
		"""

    Class representing the CreateCurvesBySubcase. Provides the user to select multiple subcases with intersecting data and plot the data from all subcases simultaneously in the current HyperGraph session.
    The constructor raises an exception if the creation of CreateCurvesBySubcase object fails.
    
    :param kwargs: Attributes of the CreateCurvesBySubcase object.
    :type kwargs: dict

    
"""
		pass

	@property
	def chartType(self):
		pass
	@chartType.setter
	def chartType(self):
		pass

	@property
	def curveOptions(self):
		pass
	@curveOptions.setter
	def curveOptions(self):
		pass

	@property
	def curveOptionsEnabled(self):
		pass
	@curveOptionsEnabled.setter
	def curveOptionsEnabled(self):
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
        
        | - If the subcaseSet is null or empty.
        | - If the yDataType or yRequest or yComponent is null or empty.
        | - If the yRequestFilter and yRequest gives empty requests list.
        | - If the yComponentFilter and yComponent gives empty component list.
        
        
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the CreateCurvesBySubcase attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def subcaseSet(self):
		pass
	@subcaseSet.setter
	def subcaseSet(self):
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

class CreateCurvesOptions:
	def __init__(self,name: str, **kwargs):
		"""

    Class representing the CreateCurvesOptions. Provides the user to create different configurations of the curves options for ploting.
    The curve options include the page, header, footer, horizontal axis, vertical axis, legend and curve properties.
    
    :param kwargs: Attributes of the CreateCurvesOptions object.
    :type kwargs: dict
    
"""
		pass

	@property
	def curveEndIndex(self):
		pass
	@curveEndIndex.setter
	def curveEndIndex(self):
		pass

	@property
	def curveIndexIncrement(self):
		pass
	@curveIndexIncrement.setter
	def curveIndexIncrement(self):
		pass

	@property
	def curveLabel(self):
		pass
	@curveLabel.setter
	def curveLabel(self):
		pass

	@property
	def curveLabelPrefix(self):
		pass
	@curveLabelPrefix.setter
	def curveLabelPrefix(self):
		pass

	@property
	def curveLabelScheme(self):
		pass
	@curveLabelScheme.setter
	def curveLabelScheme(self):
		pass

	@property
	def curveLabelSuffix(self):
		pass
	@curveLabelSuffix.setter
	def curveLabelSuffix(self):
		pass

	@property
	def curveLineColor(self):
		pass
	@curveLineColor.setter
	def curveLineColor(self):
		pass

	@property
	def curveLineColorScheme(self):
		pass
	@curveLineColorScheme.setter
	def curveLineColorScheme(self):
		pass

	@property
	def curveLineStyle(self):
		pass
	@curveLineStyle.setter
	def curveLineStyle(self):
		pass

	@property
	def curveLineStyleScheme(self):
		pass
	@curveLineStyleScheme.setter
	def curveLineStyleScheme(self):
		pass

	@property
	def curveLineThickness(self):
		pass
	@curveLineThickness.setter
	def curveLineThickness(self):
		pass

	@property
	def curveLineThicknessScheme(self):
		pass
	@curveLineThicknessScheme.setter
	def curveLineThicknessScheme(self):
		pass

	@property
	def curveShowLabel(self):
		pass
	@curveShowLabel.setter
	def curveShowLabel(self):
		pass

	@property
	def curveShowLabelPrefix(self):
		pass
	@curveShowLabelPrefix.setter
	def curveShowLabelPrefix(self):
		pass

	@property
	def curveShowLabelSuffix(self):
		pass
	@curveShowLabelSuffix.setter
	def curveShowLabelSuffix(self):
		pass

	@property
	def curveStartIndex(self):
		pass
	@curveStartIndex.setter
	def curveStartIndex(self):
		pass

	@property
	def curveSymbolColor(self):
		pass
	@curveSymbolColor.setter
	def curveSymbolColor(self):
		pass

	@property
	def curveSymbolFrequency(self):
		pass
	@curveSymbolFrequency.setter
	def curveSymbolFrequency(self):
		pass

	@property
	def curveSymbolScheme(self):
		pass
	@curveSymbolScheme.setter
	def curveSymbolScheme(self):
		pass

	@property
	def curveSymbolStyle(self):
		pass
	@curveSymbolStyle.setter
	def curveSymbolStyle(self):
		pass

	@property
	def curveUseMath(self):
		pass
	@curveUseMath.setter
	def curveUseMath(self):
		pass

	@property
	def curveXexpression(self):
		pass
	@curveXexpression.setter
	def curveXexpression(self):
		pass

	@property
	def curveXoffset(self):
		pass
	@curveXoffset.setter
	def curveXoffset(self):
		pass

	@property
	def curveXscale(self):
		pass
	@curveXscale.setter
	def curveXscale(self):
		pass

	@property
	def curveYexpression(self):
		pass
	@curveYexpression.setter
	def curveYexpression(self):
		pass

	@property
	def curveYoffset(self):
		pass
	@curveYoffset.setter
	def curveYoffset(self):
		pass

	@property
	def curveYscale(self):
		pass
	@curveYscale.setter
	def curveYscale(self):
		pass

	@property
	def footerAlignment(self):
		pass
	@footerAlignment.setter
	def footerAlignment(self):
		pass

	@property
	def footerLabelScheme(self):
		pass
	@footerLabelScheme.setter
	def footerLabelScheme(self):
		pass

	@property
	def footerPrimaryFont(self):
		pass
	@footerPrimaryFont.setter
	def footerPrimaryFont(self):
		pass

	@property
	def footerPrimaryFontSize(self):
		pass
	@footerPrimaryFontSize.setter
	def footerPrimaryFontSize(self):
		pass

	@property
	def footerText(self):
		pass
	@footerText.setter
	def footerText(self):
		pass

	@property
	def footerVisibility(self):
		pass
	@footerVisibility.setter
	def footerVisibility(self):
		pass

	@property
	def headerAlignment(self):
		pass
	@headerAlignment.setter
	def headerAlignment(self):
		pass

	@property
	def headerLabelScheme(self):
		pass
	@headerLabelScheme.setter
	def headerLabelScheme(self):
		pass

	@property
	def headerPrimaryFont(self):
		pass
	@headerPrimaryFont.setter
	def headerPrimaryFont(self):
		pass

	@property
	def headerPrimaryFontSize(self):
		pass
	@headerPrimaryFontSize.setter
	def headerPrimaryFontSize(self):
		pass

	@property
	def headerText(self):
		pass
	@headerText.setter
	def headerText(self):
		pass

	@property
	def headerVisibility(self):
		pass
	@headerVisibility.setter
	def headerVisibility(self):
		pass

	@property
	def horizontalAxisFont(self):
		pass
	@horizontalAxisFont.setter
	def horizontalAxisFont(self):
		pass

	@property
	def horizontalAxisFontSize(self):
		pass
	@horizontalAxisFontSize.setter
	def horizontalAxisFontSize(self):
		pass

	@property
	def horizontalAxisReference(self):
		pass
	@horizontalAxisReference.setter
	def horizontalAxisReference(self):
		pass

	@property
	def horizontalAxisScaleType(self):
		pass
	@horizontalAxisScaleType.setter
	def horizontalAxisScaleType(self):
		pass

	@property
	def horizontalAxisText(self):
		pass
	@horizontalAxisText.setter
	def horizontalAxisText(self):
		pass

	@property
	def horizontalAxisWeighting(self):
		pass
	@horizontalAxisWeighting.setter
	def horizontalAxisWeighting(self):
		pass

	@property
	def legendFont(self):
		pass
	@legendFont.setter
	def legendFont(self):
		pass

	@property
	def legendFontSize(self):
		pass
	@legendFontSize.setter
	def legendFontSize(self):
		pass

	@property
	def legendPlacement(self):
		pass
	@legendPlacement.setter
	def legendPlacement(self):
		pass

	@property
	def legendVisibility(self):
		pass
	@legendVisibility.setter
	def legendVisibility(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def pageFont(self):
		pass
	@pageFont.setter
	def pageFont(self):
		pass

	@property
	def pageFontSize(self):
		pass
	@pageFontSize.setter
	def pageFontSize(self):
		pass

	@property
	def pagePublishTitle(self):
		pass
	@pagePublishTitle.setter
	def pagePublishTitle(self):
		pass

	@property
	def pageTitle(self):
		pass
	@pageTitle.setter
	def pageTitle(self):
		pass

	@property
	def pageTitleScheme(self):
		pass
	@pageTitleScheme.setter
	def pageTitleScheme(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the CreateCurvesOptions attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def verticalAxisFont(self):
		pass
	@verticalAxisFont.setter
	def verticalAxisFont(self):
		pass

	@property
	def verticalAxisFontSize(self):
		pass
	@verticalAxisFontSize.setter
	def verticalAxisFontSize(self):
		pass

	@property
	def verticalAxisReference(self):
		pass
	@verticalAxisReference.setter
	def verticalAxisReference(self):
		pass

	@property
	def verticalAxisScaleType(self):
		pass
	@verticalAxisScaleType.setter
	def verticalAxisScaleType(self):
		pass

	@property
	def verticalAxisText(self):
		pass
	@verticalAxisText.setter
	def verticalAxisText(self):
		pass

	@property
	def verticalAxisWeighting(self):
		pass
	@verticalAxisWeighting.setter
	def verticalAxisWeighting(self):
		pass

class CurveBar:
	def __init__(self,window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", id_type: str = None, **kwargs):
		"""

    A class representing a Curve in Bar Chart. Creates a CurveBar for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph Bar Plot window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]

    
"""
		pass

	@property
	def barViewStyle(self):
		pass
	@barViewStyle.setter
	def barViewStyle(self):
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

class CurvePolar:
	def __init__(self,mode:str=" pm", window: int|hw_module.window.Window = None, page: int|str|hw_module.page.Page = None, id: int|str =" 0", id_type: str = None, **kwargs):
		"""

    A class representing a Curve in Polar Chart. Creates a CurvePolar for the given window and page.
    Raises an Exception if those parameters do not point to a valid HyperGraph Polar Plot window.
    
    :param window: The window of the curve.
    :type window: Union[int, Window]

    :param page: The page of the curve.
    :type page: Union[int, Page]
    
"""
		pass

	def getXYvalues(self):
		"""
		
        Method to get the x and y values of the polar curve.

        :getter: Returns x and y values of the polar curve.
        :type: numpy array
        
		"""
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
	def mode(self):
		pass
	@mode.setter
	def mode(self):
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

	def getComponents(self,datatype: str, includeTime: bool = True, format: str =" xy"):
		"""
		
        Method to get the list of all components for a given datatype.
        
        :getter: Gets the list of all components for a given datatype.
        :type: list

        :param datatype: The name of the data type that is being queried. Components vary by data type. For a list of datatype names, use the method getDataTypes.
        :type datatype: str
        :param includeTime: A param that determines if Time is to be included as a dataType. Defaults to True.
        :type includeTime: bool
        :param format: The chart type for which the components are queried. Options are 'xy', 'complex', 'polar'.
        :type format: str
        
		"""
		pass

	def getComponentsPerRequest(self,datatype: str, request: str, includeTime: bool = True, format: str =" xy"):
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
        :param format: The chart type for which the compoenents are queried.
        :type format: str
        
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
	def __init__(self,file: str,dataType:str=" ", requests: str|list =" []", components: str|list =" []", includeTime: str = True, **kwargs):
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

	@property
	def format(self):
		pass
	@format.setter
	def format(self):
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

    Class representing the MultipleFiles. Provides the user to select multiple files with intersecting data (for example, multiple runs of a test) and create a FileSet in the current HyperGraph session.
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

class MultipleSubcases:
	def __init__(self,**kwargs):
		"""

    Class representing the MultipleSubcases. Provides the user to select multiple subcases with intersecting data (for example, multiple subcases in a simulation file) and create a SubcaseSet in the current HyperGraph session.
    Intersecting data refers to subcases that contain the same type, request, and component information.
    The constructor raises an exception if the creation of MultipleSubcases fails.
    
    :param kwargs: Attributes of the MultipleSubcases object.
    :type kwargs: dict

    
"""
		pass

	@property
	def attach(self):
		pass
	@attach.setter
	def attach(self):
		pass

	def createSubcaseSet(self):
		"""
		
        Method to create the Subcase set from the file.
        The method raises an error message for the following cases:
        
        | - If the subcase set name is empty.
        | - If the file path for the subcase set is not specified.
        | - If the file does not exist.
        | - If the subcase list is empty.
        
        :getter: Gets the information for the SubcaseSet created.
        :type: dict
        
		"""
		pass

	@property
	def file(self):
		pass
	@file.setter
	def file(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set the MultipleSubcases attributes.
        
        :param kwargs: Attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def subcaseList(self):
		pass
	@subcaseList.setter
	def subcaseList(self):
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
	def notePosition(self):
		pass
	@notePosition.setter
	def notePosition(self):
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

class Table:
	def __init__(self,page: int|str|hw_module.page.Page = None, window: int|hw_module.window.Window = None):
		"""

    A class representing Table client.
    
    :param page: Page of the Table, default is the active page.
    :type page: Union[Page, int, str]

    :param window: Window of the Table,default is the active window.
    :type window: Union[Window, int]
    
"""
		pass

	def addOverlayArea(self):
		"""
		
        Method to add the overlay area. It returls the newly added TableOverlay object.
        
        :return: Returns the recently added TableOverlay object.
        :type: TableOverlay
        
		"""
		pass

	def addRule(self):
		"""
		
        Method to add rule to the table.
        :return:TableRule object recently added.
        :rettype:TableRule
        
		"""
		pass

	def checkCellEmpty(self,cells: str|list):
		"""
		
        Method to check if a cell is empty.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :return: {(1,2'True',4,5):"False"} or  {'b1':'True','e4':"False"}
        :rtype: dict
        
		"""
		pass

	def clearCellProperties(self,cells: str|list):
		"""
		
        Method to clear the cell properties.
        
        :param cellnames: "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames: Union[str,list]
        
		"""
		pass

	def deleteCellContent(self,cells: str|list):
		"""
		
        Method to delete the cell content. Clears only the cell data.
         
        :param cellnames: eg. "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames: Union[str,list]
        
		"""
		pass

	def deleteColumn(self,column: str|int, ndelete=1):
		"""
		
        Method to delete column.
        
        :param column: column name eg. 'd' or column index  eg. 4
        :type column: Union[str,int]
        :param ndelete: number of columns to be added. Default is 1.
        :type ndelete: int
        
		"""
		pass

	def deleteOverlayArea(self,overlayId):
		"""
		
        Method to delete the TableOverlay having overlayId.
        
        :param overlayAreaId: TableOverlay id
        :type overlayAreaId: int
        
		"""
		pass

	def deleteRow(self,row: str|int, ndelete=1):
		"""
		
        Method to delete row.
        
        :param row: column name eg. '4' or column index index eg. 4
        :type row: Union[str,int]
        :param ndelete: number of rows to be deleted. Default is 1.
        :type ndelete: int
        
		"""
		pass

	def deleteRule(self,ruleId):
		"""
		
        Method to delete rule using the ruleId.
        
        :param ruleId: Rule id
        :type ruleId: int
        
		"""
		pass

	def exportCSV(self,filepath, ignoreWarning=True):
		"""
		
        Method to export csv file.
        
        :param filepath: valid filepath
        :type filepath: str
        :param ignoreWarning: To set/unset the batchMode. If True batchmode is False otherwise True.
        :type ignoreWarning: bool
        
		"""
		pass

	def getAutofitColumnWidth(self,columnName):
		"""
		
        Method to get the column width flag of a column
         
        :param columnName: Single column eg. 'a'
        :return: True or False
        :rtype: bool
        
		"""
		pass

	def getCellAlignmentHorizontal(self,cell):
		"""
		
        Method to get horizontal alignment of the cell content.
        
        :param cellname: cellname eg. 'a1' , 'b2' etc.
        :type cellname: str
        
        :return: 'left', 'center' or 'right' or blank.
        :rtype: str
        
		"""
		pass

	def getCellAlignmentVertical(self,cell):
		"""
		
        Method to get vertical alignment of the cell content.
        
        :param cellname: cellname  eg. 'a1' , 'b2' etc.
        :type cellname: str
        
        :return: 'top', 'middle' or 'bottom' or blank.
        :rtype: str
        
		"""
		pass

	def getCellBackgroundColor(self,cellname):
		"""
		
        Method to get cell background color.
        
        :param cellname: Name of the cell.eg.'a1','b2' etc.
        :type cellname: str
        :return: Returns the background color
        :rtype: Color
        
		"""
		pass

	def getCellData(self,cells: str|list):
		"""
		
        Method to get data celldata.It returns the evaluated value in case cell is holding the expressions, e.g. =2+2 will return 4.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :return: cell data directory eg.{'a1':100,'b1':'abc'} etc.
        :rtype: dict
        
		"""
		pass

	def getCellDataByIndex(self,arg1: int|list, arg2: int = None):
		"""
		       
        Method to get cell data by index. It is a generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 1. arg1 is a list of tuples of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param arg1: arg1 is cell row inddex or list of tuples.
        :type arg1: Union[int,list]
        :param arg2: arg2 is colindx or arg2 is None.
        :type arg2: int or None
        :return: cell data directory.eg.{(1,2'4',4,5):"Altair Engineering"}
        :rtype: dict
        
		"""
		pass

	def getCellExpression(self,cells: str|list):
		"""
		
        Method to get data cell expression. Contrayt to the getCellData() method this api returns the expression the cell is holding.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        
        :return: cell data directory eg.{'a1':100,'b1':'abc'} etc.
        :rtype: dict
        
		"""
		pass

	def getCellExpressionByIndex(self,arg1: int|list, arg2: int = None):
		"""
		
        Method to get cell expressions by index. It is a generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 1. arg1 is a list of tuples of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param arg1: arg1 is cell row inddex or list of tuples.
        :type arg1: Union[int,list]
        :param arg2: arg2 is colindx or arg2 is None.
        :type arg2: int or None
        :return: cell data directory.eg.{(1,2'="a1'",4,5):"=2*2"}
        :rtype: dict
        
		"""
		pass

	def getCellFont(self,cellname):
		"""
		
         Method to get cell font.
         
        :param cellname: Name of the cell.
        :type cellname: str
        :return: Returns the font applied to the cells.
        :rtype: Font
        
		"""
		pass

	def getCellListHavingData(self):
		"""
		
        Method to get the dirty rows and columns having data. It returns the name of the dirty cells inside a list eg. ['a1','b2','c3','d4'].
        
        :return: cellnames inside a list
        :rtype: list[str]
        
		"""
		pass

	def getCellListHavingProperty(self):
		"""
		
        Method to get the dirty rows and columns having property like background color, text color ,font ,alignment etc. It returns the name of the dirty cells inside a list eg. ['a1','b2','c3','d4']
        
        :return: cellnames inside a list
        :rtype: list[str]
        
		"""
		pass

	def getCellListPublishProperty(self):
		"""
		
        Method to get the dirty rows and columns details. It returns the name of the dirty cells inside a list, eg. ['a1','b2','c3','d4']
        
        :return: Publishable cellnames inside a list
        :rtype: list[str]
        
		"""
		pass

	def getCellTextColor(self,cellname):
		"""
		
        Method to get cell text color.
        
        :param cellname: Name of the cell, eg.'a1', 'b2' etc.
        :type cellname: str
        :return: Returns the text color
        :rtype: Color
        
		"""
		pass

	def getData(self,*args):
		"""
		
        Method to get cell data. It is generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 2 and arg1 is a list and arg2 is a string. arg1 is row or column index list. arg2 is the orientation 'row' or 'col'. An example is arg1=['1','2','3:5'] and arg2='row' 
        - **Case 3** - Number of arguments = 1. arg is a list of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param args: One or two arguments
        :return: cell data directory, eg. {(1,2'4',4,5):"Altair Engineering"}
        :rtype: dict
        
		"""
		pass

	def getExpandedCellList(self,cells: str|list):
		"""
		
        Method to get the list of cells within a given range.
        
        :param cellrange: ['a1','b1','c1','d1:e2']
        
        :return: Returns the string of cells within a range separated by space.Returns "a1 b1 c1 d1:e2" i.e it doesn't expand the d1:e2.
        :type: string
        
		"""
		pass

	def getExpression(self,*args):
		"""
		
        Method to get cell expression. It is generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 2 and arg1 is a list and arg2 is a string. arg1 is row or column index list. arg2 is the orientation 'row' or 'col'. An example is arg1=['1','2','3:5'] and arg2='row' 
        - **Case 3** - Number of arguments = 1. arg is a list of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param args: One or two arguments
        :return: cell data directory, eg. {(1,2'="2+2'",4,5):"=a1"}
        :rtype: dict       
        
		"""
		pass

	def getFilledLowerRightCell(self):
		"""
		
        Method to get the top bottom right cellname of a dirty table.
        
        :return: cellname eg. 'e4','g11' etc.
        :rtype: str
        
		"""
		pass

	def getFilledTableDetails(self):
		"""
		
        Method to get the dirty row and column details in verbose. The format it returns is as follows: [number_of_dirty_rows,number_of_dirty_columns, row_start_index, row_end_index, col_start_indx,col_end_indx, start_col_name, start_row_indx, end_col_name, end_row_indx]. An example of the returned list is eg. [4,3,1,5,2,5,B,1,E,5]
        
        :return: list of dirty rows and dirty columns 
        :rtype: list[int,str]
        
		"""
		pass

	def getFilledTableSize(self):
		"""
		
        Method to get the number of dirty rows and columns of a table.
        
        :return: list dirty rows and dirty columns.eg. [3 4]
        :rtype: list[int]
        
		"""
		pass

	def getFilledUpperLeftCell(self):
		"""
		
        Method to get the top left cellname of a dirty table.
        
        :return: cellname eg. 'd1','c2' etc
        :rtype: str
        
		"""
		pass

	def getFullyExpandedCellList(self,cells: str|list):
		"""
		
        Method to get the list of cells within a given range.
        
        :param cellrange: ['a1','b1','c1','d1:e2']
        
        :return: Returns the string of cells within a range separated by space.Returns "a1 b1 c1 d1 e1 d2 e2" i.e it does expand the d1:e2 tp d1,e1,d2,e2
        :type: string
        
		"""
		pass

	def getOverlay(self,id: int):
		"""
		
        Method to get the overlay area having id.
        
        :param id: TableOverlay id.
        :type id: int
        :return: Returns the TableOverlay object having id.
        :rtype: TableOverlay
        
		"""
		pass

	def getOverlayIds(self):
		"""
		
        Method to get the list of overlay ids applied in the table.
        
        :return: list of overlay ids.
        :rtype: list[int]
        
		"""
		pass

	def getOverlayList(self):
		"""
		
        Method to get the list of TableOverlay objects applied in the table.
        
        :return: list of TableOverlay objects..
        :rtype: list[TableOverlay]
        
		"""
		pass

	def getOverlayType(self):
		"""
		
        Method to get the overlay mode of the active table. The value is either "appendAsRows","appendAsColumns","insertAsRows" or "insertAsColumns"
        
        :return: Returns one of the overlay mode.
        :rtype: str
        
		"""
		pass

	def getOverlayTypeTypes(self):
		"""
		
        Method to get the overlay types. The value either "appendAsRows","appendAsColumns","insertAsRows" or "insertAsColumns"'
        
        :return: Returns one of the overlay mode.
        :rtype: str
        
		"""
		pass

	def getRule(self,id: int):
		"""
		
        Method to get a rule by id.
        
        :param id: Rule id
        :type id: int
        :return: TableRule object with the given id
        :rtype: TableRule
        
		"""
		pass

	def getRuleIds(self):
		"""
		
        Method to get the list of rule ids applied in the table.
        
        :return: list of rule ids.
        :rtype: list[int]
        
		"""
		pass

	def getRuleList(self):
		"""
		
        Method to get the list of TableRule objects applied in the table.
        
        :return: list of TableRule object.
        :rtype: list[TableRule]
        
		"""
		pass

	@property
	def headerVisibility(self):
		pass
	@headerVisibility.setter
	def headerVisibility(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def importCSV(self,filepath, delimiter: str="",):
		"""
		
        Method to import csv.
        
        :param filepath: valid filepath
        :type filepath: str
        :param delimiter: To set the delimiter. Default is comma ','
        :type delimiter: str
        
		"""
		pass

	def insertColumnAfter(self,column: str|int, nadd=1):
		"""
		
        Method to insert columns after a column.
        
        :param column: columnname eg. 'd' or column index eg. 4
        :type column: Union[str,int]
        :param nadd: number of columns to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def insertColumnBefore(self,column: str|int, nadd=1):
		"""
		
        Method to insert columns before a column.
        
        :param column: columnname eg. 'd' or column index eg. 4
        :type column: Union[str,int]
        :param nadd: number of columns to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def insertRowAbove(self,row: str|int, nadd=1):
		"""
		
        Method to insert rows above a row.
        
        :param row: rowname eg. '2' or rowi index eg.2
        :type row: Union[str,int]
        :param nadd: number of rows to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def insertRowBelow(self,row: str|int, nadd=1):
		"""
		
        Method to insert rows below a row.
        
        :param row: rowname eg. '2' or row index eg.2
        :type row: Union[str,int]
        :param nadd: number of rows to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def mergeCells(self,cellRange: str, rowSpan: int = None, columnSpan: int = None):
		"""
		
        Method to merge cells.
        
        :param cellRange: Cell Range to be merged, eg. "a1:d4" or cellname.
        :type cellRange: str
        :param rowSpan: Cell to be spanned over number of rows. Valid only when the cellRange mentions cellName, otherwise None.
        :type rowSpan: int
        :param columnSpan: Cell to be spanned over number of columns. Valid only when the cellRange mentions cellName, otherwise None.
        :type columnSpan: int
        
		"""
		pass

	@property
	def numberOfColumns(self):
		pass
	@numberOfColumns.setter
	def numberOfColumns(self):
		pass

	@property
	def numberOfRows(self):
		pass
	@numberOfRows.setter
	def numberOfRows(self):
		pass

	def overlayAreaExists(self,overlayAreaId: int):
		"""
		
        Method to check if the TableOverlay having overlayAreaId exists.
        :param overlayAreaId:TableOverlay id
        :type overlayAreaId:int
        :return:Returs True of False depending on the existence of the overlayAreaId.
        :rettype:bool
        
		"""
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def refresh(self):
		"""
		
        Method to refresh the Table. All expressions will be evaluated and dependent formatting will be executed.
        
		"""
		pass

	def ruleExists(self,rulId: int):
		"""
		
        Method to check if the rule having id exists.
        
        :param rulId: Rule id
        :type rulId: int
        :return: Returns True of False depending on the existence of the rulId.
        :rtype: bool
        
		"""
		pass

	def setAutofitColumnWidth(self,columns: str|list, flag):
		"""
		
         Method to adjust the columnwidth as per the data in the cell.It will fit its width as per the content as per the widest column.
         
        :param columns: "a:d" or ['a','c','d','e:g']
        :param flag: True or False
        
		"""
		pass

	def setCellAlignmentHorizontal(self,cells: str|list, alignment):
		"""
		
        Method to set horizontal alignment of the cell content.
        
        :param cellnames: "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames:  Union[str,list]
        
        :param alignment: 'left', 'center' or 'right'.
        :type alignment: string
        
		"""
		pass

	def setCellAlignmentVertical(self,cells: str|list, alignment):
		"""
		
        Method to set vertical alignment of the cell content.
        
        :param cellnames: "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames: Union[str,list]
        
        :param alignment: 'top', 'middle' or 'bottom'.
        :type alignment: string
        
		"""
		pass

	def setCellBackgroundColor(self,cells: str|list, color: str|hw_module.color.Color|tuple):
		"""
		
        Method to set the background color of cells. The format can be a sting, rgb, hex or a Color object, like e.g. "233 45 66", '#E92D42' or (233,45,66)
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :param color: Color applied to cell background.
        :type color: Union[str,Color,tuple]             
        
		"""
		pass

	def setCellData(self,cellinfo: dict|str, cellvalue=None):
		"""
		
        Method to set data to cell. This can be either cell reference and vaue like eg. TableWin.setCellData('a1','<cellValue>') or a dictionary like TableWin.setCellData({'a1':'100','b1':100,'c1':'=a1','d1':'=a1+b1'})   
        
        :param cellinfo: Eiter a single cell reference or a dictionary
        :type cellinfo: Union[dict,str]
        :param cellvalue: valid only when cell info is of type str, eg. 'a1'. Default  is None
        :type cellvalue: None, Str, Int or Double
        
		"""
		pass

	def setCellFont(self,cells: str|list, font: hw_module.font.Font):
		"""
		
        Method to set font to cell.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :param font: Font to be applied to cell.
        :type font: Font object
        
		"""
		pass

	def setCellTextColor(self,cells: str|list, color: str|hw_module.color.Color|tuple):
		"""
		
        Method to set textcolor color to cells. The format can be a sting, rgb, hex or a Color object, like e.g. "233 45 66", '#E92D42' or (233,45,66)
         
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :param color: Color applied as background to cell.
        :type color: Union[str,Color,tuple]
        
		"""
		pass

	def setOverlayType(self,overlayType):
		"""
		
        Method to set the overlay mode to the table. The value is one of from "appendAsRows", "appendAsColumns", "insertAsRows" or "insertAsColumns"
        
        :param overlayType: overlay type to be set.
        :type overlayType: str
        
		"""
		pass

	def unMergeCells(self,cellname):
		"""
		
        Method to unmerge cells..
        :param cellname:cell to be unmerged.
        :type cellname:str
        
		"""
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class TableOverlay:
	def __init__(self,page: int|str|hw_module.page.Page = None, window: int|hw_module.window.Window = None, table: hw_module.hg.table.Table = None, id: int =" 0"):
		"""

    A class representing TableOverlay.
    
    :param page: Page of the Table, default is the active page.
    :type page: Union[Page, int, str]

    :param window: Window of the Table, default is the active window.
    :type window: Union[Window, int]

    :param table: Table. Default None
    :type table: Table or None

    :param id: Table id.Default is 0.
    :type id: int
    
    :param kwargs: To set the other attributes of TableOverlay class.
    :type kwargs: dict

    
"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def range(self):
		pass
	@range.setter
	def range(self):
		pass

	@property
	def table(self):
		pass
	@table.setter
	def table(self):
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class TableRule:
	def __init__(self,page: int|str|hw_module.page.Page = None, window: int|hw_module.window.Window = None, table: hw_module.hg.table.Table = None, id: int =" 0"):
		"""

    A class representing TableRule.
    
    :param page: Page of the TableRule. Default is the active page.
    :type page: Union[Page, int, str]

    :param window: Window of the TableRule. Default is the active window.
    :type window: Union[Window, int]

    :param table: Table of the TableRule. Default is None
    :type table: Table or None

    :param id: TableRule id. Default is 0.
    :type id: int
    
    :param kwargs: To set the other attributes of TableRule class.
    :type kwargs: dict

    
"""
		pass

	@property
	def backgroundColor(self):
		pass
	@backgroundColor.setter
	def backgroundColor(self):
		pass

	@property
	def cellList(self):
		pass
	@cellList.setter
	def cellList(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def operator(self):
		pass
	@operator.setter
	def operator(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def ruleId(self):
		pass
	@ruleId.setter
	def ruleId(self):
		pass

	@property
	def table(self):
		pass
	@table.setter
	def table(self):
		pass

	@property
	def textColor(self):
		pass
	@textColor.setter
	def textColor(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class TableViewWindow:
	def __init__(self,*args, **kwargs):
		"""

    A class representing TableViewWindow.
    
    :param page: Page of the Table, default is the active page.
    :type page: Union[Page, int, str]

    :param window: Window of the Table,default is the active window.
    :type window: Union[Window, int]
    
"""
		pass

	def addOverlayArea(self):
		"""
		
        Method to add the overlay area.It returns the newly added TableOverlay object.
        
        :return: Recently added TableOverlay object.
        :rtype: TableOverlay
        
		"""
		pass

	def checkCellEmpty(self,cells: str|list):
		"""
		
        Method to check if a cell is empty.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :return: {(1,2'True',4,5):"False"} or  {'b1':'True','e4':"False"}
        :rtype: dict
        
		"""
		pass

	def clearCellProperties(self,cells: str|list):
		"""
		
        Method to clear the cell properties.
        
        :param cellnames: "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames: Union[str,list]
        
		"""
		pass

	def delete(self,tag, objsOrIds: Any):
		"""
		
        Method to delete TableRule or TableOverlay based on the type of object tag.
        
        :param tag: either TableRule or TableOverlay class. (tag.__name__ is used internally) 
        :type tag: TableRule of TableOverlay class.
        :param objsOrIds: Deletes the TableRule or TableOverlay object based on the class used in tag parameter.
        :type objsOrIds: Either list[int] or list[TableRule] or list[TableOverlay] or 'all'
        
		"""
		pass

	def deleteCellContent(self,cells: str|list):
		"""
		
        Method to delete the cell content. Clears only the cell data.
         
        :param cellnames: eg. "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames: Union[str,list]
        
		"""
		pass

	def deleteColumn(self,column: str|int, ndelete=1):
		"""
		
        Method to delete column.
        
        :param column: column name eg. 'd' or column index  eg. 4
        :type column: Union[str,int]
        :param ndelete: number of columns to be added. Default is 1
        :type ndelete: int
        
		"""
		pass

	def deleteOverlayArea(self,overlayId):
		"""
		
        Method to delete the TableOverlay having overlayId.
        
        :param overlayAreaId: TableOverlay id
        :type overlayAreaId: int
        
		"""
		pass

	def deleteRow(self,row: str|int, ndelete=1):
		"""
		
        Method to delete row.
        
        :param row: column name eg. '4' or column index index eg. 4
        :type row: Union[str,int]
        :param ndelete: Number of rows to be deleted. Default is 1.
        :type ndelete: int
        
		"""
		pass

	def deleteRule(self,ruleId):
		"""
		
        Method to delete rule using the ruleId.
        
        :param ruleId: Rule id
        :type ruleId: int
        
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

	def exportCSV(self,filepath, ignoreWarning=True):
		"""
		
        Method to export csv file.
        
        :param filepath: valid filepath
        :type filepath: str
        :param ignoreWarning: To set/unset the batchMode.
        :type ignoreWarning: bool
        
		"""
		pass

	def getAutofitColumnWidth(self,columnName):
		"""
		
        Method to get the columnwidth flag of a column.
         
        :param columnName: Single column eg. 'a'
        :return: Status of the autofit for the specified column.
        :rtype: bool
        
		"""
		pass

	def getCellAlignmentHorizontal(self,cellname):
		"""
		
        Method to get horizontal alignment of the cell content.
        
        :param cellname: cellname eg. 'a1' , 'b2' etc.
        :type cellname: str
        
        :return: 'left', 'center', 'right', or blank
        :rtype: str
        
		"""
		pass

	def getCellAlignmentVertical(self,cellname):
		"""
		
        Method to get vertical alignment of the cell content.
        
        :param cellname: cellname  eg. 'a1' , 'b2' etc.
        :type cellname: str
        
        :return: 'top', 'middle', 'bottom', or blank
        :rtype: str
        
		"""
		pass

	def getCellBackgroundColor(self,cellname):
		"""
		
        Method to get cell background color.
        
        :param cellname: Name of the cell.eg.'a1','b2' etc.
        :type cellname: str
        :return: Returns the background color
        :rtype: Color
        
		"""
		pass

	def getCellData(self,cells: str|list):
		"""
		
        Method to get data celldata. It returns the evaluated value in case cell is holding the expressions, e.g. *=2+2* will return 4.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :return: cell data directory eg.{'a1':100,'b1':'abc'} etc.
        :rtype: dict
        
		"""
		pass

	def getCellDataByIndex(self,arg1: int|list, arg2: int = None):
		"""
		
        Method to get cell data by index. It is a generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 1. arg1 is a list of tuples of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param arg1: arg1 is cell row inddex or list of tuples.
        :type arg1: Union[int,list]
        :param arg2: arg2 is colindx or arg2 is None.
        :type arg2: int or None
        :return: cell data directory.eg.{(1,2'4',4,5):"Altair Engineering"}
        :rtype: dict
        
		"""
		pass

	def getCellExpression(self,cells: str|list):
		"""
		
        Method to get data cell expression. Contrayt to the getCellData() method this api returns the expression the cell is holding.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        
        :return: cell data directory eg.{'a1':100,'b1':'abc'} etc.
        :rtype: dict
        
		"""
		pass

	def getCellExpressionByIndex(self,arg1: int|list, arg2: int = None):
		"""
		
        Method to get cell expressions by index. It is a generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 1. arg1 is a list of tuples of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param arg1: arg1 is cell row inddex or list of tuples.
        :type arg1: Union[int,list]
        :param arg2: arg2 is colindx or arg2 is None.
        :type arg2: int or None
        :return: cell data directory.eg.{(1,2'="a1'",4,5):"=2*2"}
        :rtype: dict
        
		"""
		pass

	def getCellFont(self,cellname):
		"""
		
         Method to get cell font.
         
        :param cellname: Name of the cell.
        :type cellname: str
        :return: Returns the font applied to the cells.
        :rtype: Font
        
		"""
		pass

	def getCellListHavingData(self):
		"""
		
        Method to get the dirty rows and columns having data. It returns the name of the dirty cells inside a list eg. ['a1','b2','c3','d4'].
        
        :return: cellnames inside a list
        :rtype: list[str]
        
		"""
		pass

	def getCellListHavingProperty(self):
		"""
		
        Method to get the dirty rows and columns having property like background color, text color ,font ,alignment etc. It returns the name of the dirty cells inside a list eg. ['a1','b2','c3','d4']
        
        :return: cellnames inside a list
        :rtype: list[str]
        
		"""
		pass

	def getCellListPublishProperty(self):
		"""
		
        Method to get the dirty rows and columns details. It returns the name of the dirty cells inside a list, eg. ['a1','b2','c3','d4']
        
        :return: Publishable cellnames inside a list
        :rtype: list[str]
        
		"""
		pass

	def getCellTextColor(self,cellname):
		"""
		
        Method to get cell text color.
        
        :param cellname: Name of the cell, eg.'a1', 'b2' etc.
        :type cellname: str
        :return: Returns the text color
        :rtype: Color
        
		"""
		pass

	def getData(self,*args, **kwargs):
		"""
		
        Method to get cell data. It is generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 2 and arg1 is a list and arg2 is string. arg1 is row or column index list. arg2 is the orientation 'row' or 'col'. An example is arg1=['1','2','3:5'] and arg2='row' 
        - **Case 3** - Number of arguments = 1. arg is a list of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param args: One or two arguments
        :return: cell data directory, eg. {(1,2'4',4,5):"Altair Engineering"}
        :rtype: dict
        
		"""
		pass

	def getDisplayOptionList(self):
		"""
		
        Method to get the list of post display options.
        
        :return: Returns the list of post display options.
        :rtype: list
        
		"""
		pass

	def getExpression(self,*args, **kwargs):
		"""
		
        Method to get cell expression. It is generic method as it accepts the arguments in different formats. 
        
        - **Case 1** - Number of arguments = 2 and arg1 and arg2 are both integers. These are the indexes of the cell. Convinient to use inside an index-based loop. 
        - **Case 2** - Number of arguments = 2 and arg1 is a list and arg2 is a string. arg1 is row or column index list. arg2 is the orientation 'row' or 'col'. An example is arg1=['1','2','3:5'] and arg2='row' 
        - **Case 3** - Number of arguments = 1. arg is a list of cell index pairs. An example is arg=[(1,2),(4,5)]
        
        :param args: One or two arguments
        :return: cell data directory, eg. {(1,2'="2+2'",4,5):"=a1"}
        :rtype: dict     
        
		"""
		pass

	def getFilledLowerRightCell(self):
		"""
		
        Method to get the top bottom right cellname of a dirty table.
        
        :return: cellname eg. 'e4','g11' etc.
        :rtype: str
        
		"""
		pass

	def getFilledTableDetails(self):
		"""
		
        Method to get the dirty row and column details in verbose. The format it returns is as follows: [number_of_dirty_rows,number_of_dirty_columns, row_start_index, row_end_index, col_start_indx,col_end_indx, start_col_name, start_row_indx, end_col_name, end_row_indx]. An example of the returned list is eg. [4,3,1,5,2,5,B,1,E,5]
        
        :return: list of dirty rows and dirty columns 
        :rtype: list[int,str]
        
		"""
		pass

	def getFilledTableSize(self):
		"""
		
        Method to get the number of dirty rows and columns of a table.
        
        :return: list dirty rows and dirty columns.eg. [3 4]
        :rtype: list[int]
        
		"""
		pass

	def getFilledUpperLeftCell(self):
		"""
		
        Method to get the top left cellname of a dirty table.
        
        :return: cellname eg. 'd1','c2' etc
        :rtype: str
        
		"""
		pass

	def getOverlay(self,id: int):
		"""
		
        Method to get the overlay area having id.
        
        :param id: TableOverlay id.
        :type id: int
        :return: Returns the TableOverlay object having id.
        :rtype: TableOverlay
        
		"""
		pass

	def getOverlayIds(self):
		"""
		
        Method to get the list of overlay ids applied in the table.
        
        :return: list of overlay ids.
        :rtype: list[int]
        
		"""
		pass

	def getOverlayList(self):
		"""
		
        Method to get the list of TableOverlay objects applied in the table.
        
        :return: list of TableOverlay objects..
        :rtype: list[TableOverlay]
        
		"""
		pass

	def getOverlayType(self):
		"""
		
        Method to get the overlay mode of the active table. The value is either "appendAsRows","appendAsColumns","insertAsRows" or "insertAsColumns"
        
        :return: Returns one of the overlay mode.
        :rtype: str
        
		"""
		pass

	def getOverlayTypeTypes(self):
		"""
		
        Method to get the overlay types. The value either "appendAsRows","appendAsColumns","insertAsRows" or "insertAsColumns"'
        
        :return: Returns one of the overlay mode.
        :rtype: str
        
		"""
		pass

	def getRule(self,id: int):
		"""
		
        Method to get a rule by id.
        
        :param id: Rule id
        :type id: int
        :return: TableRule object with the given id
        :rtype: TableRule
        
		"""
		pass

	def getRuleIds(self):
		"""
		
        Method to get the list of rule ids applied in the table.
        
        :return: list of rule ids.
        :rtype: list[int]
        
		"""
		pass

	def getRuleList(self):
		"""
		
        Method to get the list of TableRule objects applied in the table.
        
        :return: list of TableRule object.
        :rtype: list[TableRule]
        
		"""
		pass

	def getStatusDisplay(self,option:str=""):
		"""
		Method to get the display option setting.

        :param option: Available options are **tracing**, **tracking**, **contour**, **iso value**, **tensor**, **vector**, **legend**, **section cut**, **measure**, **notes**, **axisymmetry**, and **perspective**.
        :type option: str

        :return: Status of display option.
        :rtype: bool 
        
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
	def headerVisibility(self):
		pass
	@headerVisibility.setter
	def headerVisibility(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def importCSV(self,filepath, delimiter: str="",):
		"""
		
        Method to import csv.
        
        :param filepath: valid filepath
        :type filepath: str
        :param delimiter: To set the delimiter. Default is comma ','.
        :type delimiter: str
        
		"""
		pass

	def insertColumnAfter(self,column: str|int, nadd=1):
		"""
		
        Method to insert columns after a column.
        
        :param column: column name eg. 'd' or column index eg. 4
        :type column: Union[str,int]
        :param nadd: number of columns to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def insertColumnBefore(self,column: str|int, nadd=1):
		"""
		
        Method to insert columns before a column.
        
        :param column: column name eg. 'd' or column index eg. 4
        :type column: Union[str,int]
        :param nadd: number of columns to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def insertRowAbove(self,row: str|int, nadd=1):
		"""
		
        Method to insert rows above a row.
        
        :param row: rowname eg. '2' or rowi index eg.2
        :type row: Union[str,int]
        :param nadd: number of rows to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def insertRowBelow(self,row: str|int, nadd=1):
		"""
		
        Method to insert rows below a row.
        
        :param row: rowname eg. '2' or row index eg.2
        :type row: Union[str,int]
        :param nadd: number of rows to be added. Default is 1
        :type nadd: int
        
		"""
		pass

	def isEmpty(self):
		"""
		
        Method to check if window is empty.
        
        :return: Returns True if window is empty.
        :rtype: bool
        
		"""
		pass

	def mergeCells(self,cellRange: str, rowSpan: int = None, columnSpan: int = None):
		"""
		
        Method to merge cells.
        
        :param cellRange: Cell Range to be merged, eg. "a1:d4" or cellname.
        :type cellRange: str
        :param rowSpan: Cell to be spanned over number of rows. Valid only when the cellRange mentions cellName, otherwise None.
        :type rowSpan: int
        :param columnSpan: Cell to be spanned over number of columns. Valid only when the cellRange mentions cellName, otherwise None.
        :type columnSpan: int
        
		"""
		pass

	@property
	def numberOfColumns(self):
		pass
	@numberOfColumns.setter
	def numberOfColumns(self):
		pass

	@property
	def numberOfRows(self):
		pass
	@numberOfRows.setter
	def numberOfRows(self):
		pass

	def overlayAreaExists(self,overlayAreaId: int):
		"""
		
        Method to check if the TableOverlay having overlayAreaId exists.
        
        :param overlayAreaId: TableOverlay id
        :type overlayAreaId: int
        :return: Returs True of False depending on the existence of the overlayAreaId.
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

	def refresh(self):
		"""
		
        Method to refresh the Table. All expressions will be evaluated and dependent formatting will be executed.
        
		"""
		pass

	def ruleExists(self,rulId: int):
		"""
		
        Method to check if the rule having id exists.
        
        :param rulId: Rule id
        :type rulId: int
        :return: Returns True of False depending on the existence of the rulId.
        :rtype: bool
        
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set window attributes.
        
        :param kwargs: Attributes
        :param type: dict
        
		"""
		pass

	def setAutofitColumnWidth(self,columns: str|list, flag):
		"""
		
        Method to adjust the columnwidth dependent on the data in the cell. It will fit its width as per the content of the widest cell in the column.
        
        :param columns: "a:d" or ['a','c','d','e:g']
        :type columns: Union[str,list]
        :param flag: Flag to activate or deactivate the autofit for the specified column.
        :type flag: bool
        
		"""
		pass

	def setCellAlignmentHorizontal(self,cells: str|list, alignment):
		"""
		
        Method to set horizontal alignment of the cell content.
        
        :param cellnames: "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames:  Union[str,list]
        
        :param alignment: 'left', 'center', or 'right'
        :type alignment: string
        
		"""
		pass

	def setCellAlignmentVertical(self,cells: str|list, alignment):
		"""
		
        Method to set vertical alignment of the cell content.
        
        :param cellnames: "a1:d3" or [''a1','b1','c1:d4']
        :type cellnames: Union[str,list]
        
        :param alignment: 'top', 'middle', or 'bottom'
        :type alignment: string
        
		"""
		pass

	def setCellBackgroundColor(self,cells: str|list, color: str|hw_module.color.Color|tuple):
		"""
		
        Method to set the background color of cells. The format can be a sting, rgb, hex or a Color object, like e.g. "233 45 66", '#E92D42' or (233,45,66)
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :param color: Color applied to cell background.
        :type color: Union[str,Color,tuple]        
        
		"""
		pass

	def setCellData(self,cellinfo: dict|str, cellvalue=None):
		"""
		
        Method to set data to cell. This can be either cell reference and vaue like eg. TableWin.setCellData('a1','<cellValue>') or a dictionary like TableWin.setCellData({'a1':'100','b1':100,'c1':'=a1','d1':'=a1+b1'})   
        
        :param cellinfo: Eiter a single cell reference or a dictionary
        :type cellinfo: Union[dict,str]
        :param cellvalue: valid only when cell info is of type str, eg. 'a1'. Default is None.
        :type cellvalue: None, str, int, or float
        
		"""
		pass

	def setCellFont(self,cells: str|list, font: hw_module.font.Font):
		"""
		
        Method to set font to cell.
        
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :param font: Font to be applied to cell.
        :type font: Font object
        
		"""
		pass

	def setCellTextColor(self,cells: str|list, color: str|hw_module.color.Color|tuple):
		"""
		
        Method to set textcolor color to cells. The format can be a sting, rgb, hex or a Color object, like e.g. "233 45 66", '#E92D42' or (233,45,66)
         
        :param cells: range or list eg. 'a1:b2' or ['a1','b1','d2:g2']
        :type cells: Union[str,list]
        :param color: Color applied as background to cell.
        :type color: Union[str,Color,tuple]
        
		"""
		pass

	def setOverlayType(self,overlayType):
		"""
		
        Method to set the overlay mode to the table. The value is one of from "appendAsRows", "appendAsColumns", "insertAsRows" or "insertAsColumns"
        
        :param overlayType: overlay type to be set.
        :type overlayType: str
        
		"""
		pass

	def setStatusDisplay(self,option:str="", status: bool = True):
		"""
		Method to set the display options.

        :param option: Available options are **tracing**, **tracking**, **contour**, **iso value**, **tensor**, **vector**, **legend**, **section cut**, **measure**, **notes**, **axisymmetry**, and **perspective**.
        :type option: str

        :param status: Status of display option.
        :type status: bool 
        
		"""
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	def unMergeCells(self,cellname):
		"""
		
        Method to unmerge cells.
        :param cellname: Cell to be unmerged.
        :type cellname: str
        
		"""
		pass

class axis:
	pass

class core:
	pass

class createcurvesOptions:
	pass

class createcurvesbyFile:
	pass

class createcurvesbySubcase:
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

class multiplesubcases:
	pass

class note:
	pass

class table:
	pass

class tableoverlay:
	pass

class tablerule:
	pass

class title:
	pass

