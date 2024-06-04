from typing import TypeVar
class hw_module:
	class hv:
		class model:
			class Model:
				pass
		class filter:
			class Filter:
				pass
		class resultdefinition:
			class ResultDefinition:
				pass
			class ResultPlotType:
				pass
		class entity:
			class Node:
				pass
		class legend:
			class ResultPlotType:
				pass
	class window:
		class Window:
			pass
	class page:
		class Page:
			pass
class Any:
	pass
class range:
	pass
class tuple:
	pass

class ABC:
	def __init__(self):
		"""
Helper class that provides a standard way to create an ABC using
    inheritance.
    
"""
		pass

class Any:
	def __init__(self,*args, **kwds):
		"""
Internal indicator of special typing constructs.
    See _doc instance attribute for specific docs.
    
"""
		pass

class Collection:
	def __init__(self,type: str = None, model: hw_module.hv.model.Model = None, populate: bool = True):
		"""

    A class representing Collection (Selection set) of entities.
    
    :param type: Entity type. Entity can be of Part, Node, or Element.
    :type type: Union[str, Entity]

    :param model: Model in which collection is present. Default is the active model.
    :type model: Union[Model, int, str]

    :param populate: Populate all entity in collection. Default is True.
    :type populate: bool

    
"""
		pass

	def addByAdjacent(self,repeat=1, visible: bool = True):
		"""
		Method to add entities to a collection by its adjacent.

        :param visible: All or displayed entities. Default is True (displayed).
        :type visible: bool

        
		"""
		pass

	def addByAttached(self,visible: bool = True):
		"""
		Method to add entities to a collection by attached.

        :param visible: All or displayed entities. Default is True (displayed).
        :type visible: bool

        
		"""
		pass

	def addByComponentName(self,cname: list|str):
		"""
		Method to add entities to a collection by part name.

        :param cname: Part name or part name list
        :type cname: Union[str, list]

        
		"""
		pass

	def addByConfig(self,config, visible: bool = True):
		"""
		Method to add entities to a collection by configuration option.

        :param config: Configuration of the entity.
        :type config: Union[str,list of str]

        :param visible: All or displayed entities. Default is True (displayed).
        :type visible: bool

        
		"""
		pass

	def addByDimension(self,dimension: list|int, visible: bool = True):
		"""
		Method to add entities to a collection by dimensions.

        :param dimension: Dimension of the entity. Dimension can be **0**, **1**, **2** or **3**.
        :type dimension: Union[int, list]

        :param visible: All or displayed entities. Default is True (displayed).
        :param type: bool

        
		"""
		pass

	def addByFace(self,visible: bool = True):
		"""
		Method to add entities to a collection by face. This is applicable for Node and Element.

        :param visible: All or displayed entities. Default is True (displayed).
        :type visible: bool

        
		"""
		pass

	def addByFilter(self,filter: list|hw_module.hv.filter.Filter):
		"""
		Method to add entities to the collection by the filter. Filter can be an instance of FilterByScalar, FilterBySphere, or FilterByPlane.

       :param filter: Filter object or list of filter objects.
       :type filter: Union[Filter, List of Filters]
       
		"""
		pass

	def addByID(self,type: str, idstr: list|str, visible: bool = True, pool: str = None):
		"""
		Method to add entities to a collection by id option.

        :param type: Entity type. Entity can be of type Part, Node, or Element.
        :type type: Union[str, Entity]

        :param idstr: ID, list of IDs or ID in string range format.
        :type idstr: Union[int, str, list]

        :param visible: All or displayed entities. Default is True (displayed).
        :param type: bool

        :param pool: The specific pool, default is None.
        :type pool: str

        
		"""
		pass

	def addDisplayed(self):
		"""
		Method to add displayed entities to a collection.
		"""
		pass

	def clear(self):
		pass

	@property
	def entityType(self):
		pass
	@entityType.setter
	def entityType(self):
		pass

	def getEntities(self,pool: str = None):
		"""
		Method to get the entity list from a collection.

        :param pool: The specific pool, default is None.
        :type pool: list of entities

        
		"""
		pass

	def getIds(self,pool: str = None):
		"""
		Method to get the list of entity ids from collection.

        :param pool: The specific pool, default is None.
        :type pool: list of int

        
		"""
		pass

	def getPools(self):
		"""
		Method to get the pool list of the entity.
		"""
		pass

	def getSize(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	def reverse(self,visible: bool = True):
		"""
		Method to reverse the entity selection of the collection. Default is True.

        :param visible: All or displayed entities.
        :param type: bool
        
		"""
		pass

	def subtractByComponentName(self,cname: list|str):
		"""
		Method to subtract entities from a collection by part name.

        :param cname: Part name or part name list
        :type cname: Union[str, list]

        
		"""
		pass

	def subtractByConfig(self,config, visible: bool = True):
		"""
		Method to subtract entities from a collection by configuration option.

        :param config: Configuration of the entity
        :type config: Union[str,list of str]

        :param visible: All or displayed entities. Default is True (displayed).
        :type visible: bool

        
		"""
		pass

	def subtractByDimension(self,dimension: list|int, visible: bool = True):
		"""
		Method to subtract entities from a collection by dimensions.

        :param dimension: Dimension of the entity. Dimension can be **0**, **1**, **2** or **3**.
        :type dimension: Union[int, list]

        :param visible: All or displayed entities. Default is True (displayed).
        :param type: bool

        
		"""
		pass

	def subtractByFilter(self,filter: list|hw_module.hv.filter.Filter):
		"""
		Method to subtract entities from a collection by filter. Filter can be instance of FilterByScalar, FilterBySphere, or FilterByPlane.

       :param filter: Filter object or list of filter objects.
       :type filter: Union[Filter, List of Filters]
       
		"""
		pass

	def subtractByID(self,type: str, idstr: list|str, visible: bool = True, pool: str = None):
		"""
		Method to subtract entities from a collection by id option.
        
        :param type: Entity type. Entity can be of type Part, Node, or Element.
        :type type: Union[str, Entity]

        :param idstr: ID, list of IDs or ID in string range format.
        :type idstr: Union[int, str, list]

        :param visible: All or displayed entities. Default is True (displayed).
        :param type: bool

        :param pool: The specific pool. Default is None.
        :type pool: str

        
		"""
		pass

	def subtractDisplayed(self):
		"""
		Method to subtract displayed entities from a collection.
		"""
		pass

class Element:
	def __init__(self,id, pool=None, model: hw_module.hv.model.Model = None):
		"""

    A class representing the element entity type. Get an Element for the given model.
    Raises an Exception parameter if it does not point to a valid Element.
    
    :param id: ID of the Element.
    :type id: int

    :param pool: The specific pool, default is None.
    :type pool: str

    :param model: The specific model, default is the active model.
    :type model: Union[int, str, Model]
    
"""
		pass

	@property
	def centroid(self):
		pass
	@centroid.setter
	def centroid(self):
		pass

	@property
	def config(self):
		pass
	@config.setter
	def config(self):
		pass

	@property
	def connectivity(self):
		pass
	@connectivity.setter
	def connectivity(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def normal(self):
		pass
	@normal.setter
	def normal(self):
		pass

	@property
	def part(self):
		pass
	@part.setter
	def part(self):
		pass

	@property
	def partId(self):
		pass
	@partId.setter
	def partId(self):
		pass

	@property
	def pool(self):
		pass
	@pool.setter
	def pool(self):
		pass

class Entity:
	def __init__(self):
		"""

    A abstract base class for entity like PartAssembly, PartSet, Part, Element, Node.
    Since it is an abstract class we can not create instance of it, but we can create
    instance of its child classes.
    
"""
		pass

class ExportModelH3D:
	def __init__(self,page=None, window=None,file: str="", **kwargs):
		"""

    A class representing exporting the model in H3D format.
    
    :param page: Page of the model, default is the active page.
    :type page: Union[Page, int, str]

    :param window: Window of the model,default is the active window.
    :type window: Union[Window, int]

    :param file: H3D file name that you want to export. No default value.
    :type file: str

    :param kwargs: Param to set other attributes of ExportModelH3D class.
    :type kwargs: dict

    
"""
		pass

	@property
	def allModels(self):
		pass
	@allModels.setter
	def allModels(self):
		pass

	@property
	def animation(self):
		pass
	@animation.setter
	def animation(self):
		pass

	@property
	def compressOutput(self):
		pass
	@compressOutput.setter
	def compressOutput(self):
		pass

	@property
	def compressionLoss(self):
		pass
	@compressionLoss.setter
	def compressionLoss(self):
		pass

	@property
	def entityAttributes(self):
		pass
	@entityAttributes.setter
	def entityAttributes(self):
		pass

	def export(self):
		"""
		Method to export the model. If the file name is not specified, the name will be set to *untitled*
        followed by an incremental value (e.g. *untitled1.jpg*).
        
        
		"""
		pass

	@property
	def file(self):
		pass
	@file.setter
	def file(self):
		pass

	@property
	def html(self):
		pass
	@html.setter
	def html(self):
		pass

	@property
	def includeMaskedElements(self):
		pass
	@includeMaskedElements.setter
	def includeMaskedElements(self):
		pass

	@property
	def includeSets(self):
		pass
	@includeSets.setter
	def includeSets(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def previewImage(self):
		pass
	@previewImage.setter
	def previewImage(self):
		pass

	@property
	def results(self):
		pass
	@results.setter
	def results(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the ExportModelH3D attributes.
		"""
		pass

	@property
	def viewAttributes(self):
		pass
	@viewAttributes.setter
	def viewAttributes(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class FilterByPlane:
	def __init__(self,normal: str='y', base=0, width=0.1):
		"""

    A class representing the Filter by plane option for displayed entities, which can be used in the addByFilter method of a collection.
    
    :param normal: Normal of the plane. Default is **y**. Other available options are **x**, **z**, **normaltoscreen**.
    :type normal: str

    :param base: Base node id for creating the plane. Default is 0.
    :type base: int

    :param width: width or tolerance for creating the plane. Default is 0.1.
    :type width: Union[int, float]
    
"""
		pass

	@property
	def base(self):
		pass
	@base.setter
	def base(self):
		pass

	@property
	def normal(self):
		pass
	@normal.setter
	def normal(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class FilterByScalar:
	def __init__(self,operator: str ="==", value: int|float = None):
		"""

    A class representing the Filter by scalar option for displayed entities, which can be used in the *addByFilter* method of a collection.
    
    :param operator: Rule string, default is **==**. Other available options are **value**, **percent**, **topn**, **bottomn**, **noresult**, **>**, **<**, **<=**, **>=**.
    :type operator: str

    :param value: Model in which collection is present. Default is active model.
    :type value: Union[int, float]
    
"""
		pass

	@property
	def operator(self):
		pass
	@operator.setter
	def operator(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

class FilterBySphere:
	def __init__(self,x: int|float =" 0", y: int|float =" 0", z: int|float =" 0", radius: int|float = 1):
		"""

    A class representing the Filter by sphere option for displayed entities, which can be used in the addByFilter method of a collection.
    
    :param x: x value of the sphere center. Default is 0.
    :type x: Union[int, float]

    :param y: y value of the sphere center. Default is 0.
    :type y: Union[int, float]

    :param z: z value of the sphere center. Default is 0.
    :type z: Union[int, float]

    :param radius: radius for creating the sphere. Default is 1.
    :type radius: Union[int, float]
    
"""
		pass

	@property
	def radius(self):
		pass
	@radius.setter
	def radius(self):
		pass

	@property
	def x(self):
		pass
	@x.setter
	def x(self):
		pass

	@property
	def y(self):
		pass
	@y.setter
	def y(self):
		pass

	@property
	def z(self):
		pass
	@z.setter
	def z(self):
		pass

class LegendScalar:
	def __init__(self,resType: hw_module.hv.legend.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, **kwargs):
		"""

      A class representing Legend Scalar.
    
      :param model: Model for the legend scalar. Default is active model.
      :type model: Union[Model, int, str]

      :param window: Window for the legend scalar. Default is active window.
      :type window: Union[Window, int]

      :param page: Page for the legend scalar. Default is active page.
      :type page: Union[Page, int, str]

      :param kwargs: To set the other attributes of LegendScalar class.
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
	def discreteColors(self):
		pass
	@discreteColors.setter
	def discreteColors(self):
		pass

	@property
	def footerFont(self):
		pass
	@footerFont.setter
	def footerFont(self):
		pass

	@property
	def footerText(self):
		pass
	@footerText.setter
	def footerText(self):
		pass

	@property
	def footerVisible(self):
		pass
	@footerVisible.setter
	def footerVisible(self):
		pass

	def getBoundingBox(self):
		"""
		Method to get the bounding box of the legend.

        :return: Bounding box.
        :rtype: dict  
        
		"""
		pass

	def getCategoryLabel(self,level_index: int =" 0"):
		"""
		Method to get the category label of level in legend.

        :param level_index: level index. 
        :type level_index: int

        :return: category label.
        :rtype: str  
        
		"""
		pass

	def getCategoryLabelList(self):
		"""
		Method to get the category label list of the legend.

        :return: Bounding box.
        :rtype: list  
        
		"""
		pass

	def getLevelColor(self,level_index: int =" 0"):
		"""
		Method to get the level color of the legend.
        
        :param level_index: Level index. 
        :type level_index: int

        :return: Level index color.
        :rtype: Color    
        
		"""
		pass

	def getLevelValue(self,level_index: int =" 0"):
		"""
		Method to get the level value of the legend.
        
        :param level_index: Level index. 
        :type level_index: int

        :return: Level legend value.
        :rtype: int    
        
		"""
		pass

	@property
	def headerFont(self):
		pass
	@headerFont.setter
	def headerFont(self):
		pass

	@property
	def headerText(self):
		pass
	@headerText.setter
	def headerText(self):
		pass

	@property
	def headerVisible(self):
		pass
	@headerVisible.setter
	def headerVisible(self):
		pass

	def interpolate(self,lower_index: int =" 0", upper_index: int =" 0"):
		"""
		Method to interpolate level colors of the legend.
        
        :param lower_index: Lower level index. 
        :type lower_index: int  

        :param lower_index: Upper level index. 
        :type lower_index: int  
        
		"""
		pass

	@property
	def interpolateColors(self):
		pass
	@interpolateColors.setter
	def interpolateColors(self):
		pass

	@property
	def interpolation(self):
		pass
	@interpolation.setter
	def interpolation(self):
		pass

	@property
	def maxValue(self):
		pass
	@maxValue.setter
	def maxValue(self):
		pass

	@property
	def minValue(self):
		pass
	@minValue.setter
	def minValue(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def multiplier(self):
		pass
	@multiplier.setter
	def multiplier(self):
		pass

	@property
	def numberFont(self):
		pass
	@numberFont.setter
	def numberFont(self):
		pass

	@property
	def numberOfLevels(self):
		pass
	@numberOfLevels.setter
	def numberOfLevels(self):
		pass

	@property
	def numericFormat(self):
		pass
	@numericFormat.setter
	def numericFormat(self):
		pass

	@property
	def numericPrecision(self):
		pass
	@numericPrecision.setter
	def numericPrecision(self):
		pass

	@property
	def offset(self):
		pass
	@offset.setter
	def offset(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def resetLevelValue(self,level_index: int =" 0"):
		"""
		Method to reset level value of the legend.

        :param level_index: Level index. 
        :type level_index: int  
        
		"""
		pass

	@property
	def reverse(self):
		pass
	@reverse.setter
	def reverse(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the Legend attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	def setLevelColor(self,level_index: Any =" 0", level_color: Any = None):
		"""
		Method to set the level color of the legend.
        
        :param level_index: level index. 
        :type level_index: Union[int, list]

        :param level_color: level color. 
        :type level_color: Union[Color, list, tuple] 
        
		"""
		pass

	def setLevelValue(self,level_index: Any =" 0", level_value: Any = None):
		"""
		Method to set the level value of the legend.
        
        :param level_index: level index. 
        :type level_index: Union[int, list]

        :param level_value: level value. 
        :type level_value: Union[int, float]  
        
		"""
		pass

	@property
	def showByModel(self):
		pass
	@showByModel.setter
	def showByModel(self):
		pass

	@property
	def showCategoryID(self):
		pass
	@showCategoryID.setter
	def showCategoryID(self):
		pass

	@property
	def showEntityLabel(self):
		pass
	@showEntityLabel.setter
	def showEntityLabel(self):
		pass

	@property
	def showMax(self):
		pass
	@showMax.setter
	def showMax(self):
		pass

	@property
	def showMaxLocal(self):
		pass
	@showMaxLocal.setter
	def showMaxLocal(self):
		pass

	@property
	def showMin(self):
		pass
	@showMin.setter
	def showMin(self):
		pass

	@property
	def showMinLocal(self):
		pass
	@showMinLocal.setter
	def showMinLocal(self):
		pass

	@property
	def style(self):
		pass
	@style.setter
	def style(self):
		pass

	@property
	def thresholdMax(self):
		pass
	@thresholdMax.setter
	def thresholdMax(self):
		pass

	@property
	def thresholdMaxValue(self):
		pass
	@thresholdMaxValue.setter
	def thresholdMaxValue(self):
		pass

	@property
	def thresholdMin(self):
		pass
	@thresholdMin.setter
	def thresholdMin(self):
		pass

	@property
	def thresholdMinValue(self):
		pass
	@thresholdMinValue.setter
	def thresholdMinValue(self):
		pass

	@property
	def titleFont(self):
		pass
	@titleFont.setter
	def titleFont(self):
		pass

	@property
	def titleText(self):
		pass
	@titleText.setter
	def titleText(self):
		pass

	@property
	def titleVisible(self):
		pass
	@titleVisible.setter
	def titleVisible(self):
		pass

	@property
	def transparency(self):
		pass
	@transparency.setter
	def transparency(self):
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class LegendTensor:
	def __init__(self,resType: hw_module.hv.legend.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, **kwargs):
		"""

      A class representing Legend Tensor.
    
      :param model: Model for the legend tensor. Default is active model.
      :type model: Union[Model,int,str]

      :param window: Window for the legend tensor. Default is active window.
      :type window: Union[Window,int]

      :param page: Page for the legend tensor. Default is active page.
      :type page: Union[Page,int,str]

      :param kwargs: To set the other attributes of LegendTensor class.
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
	def footerFont(self):
		pass
	@footerFont.setter
	def footerFont(self):
		pass

	@property
	def footerText(self):
		pass
	@footerText.setter
	def footerText(self):
		pass

	@property
	def footerVisible(self):
		pass
	@footerVisible.setter
	def footerVisible(self):
		pass

	def getBoundingBox(self):
		"""
		Method to get the bounding box of the legend.

        :return: Bounding box.
        :rtype: dict  
        
		"""
		pass

	def getCategoryLabel(self,level_index: int =" 0"):
		"""
		Method to get the category label of level in legend.

        :param level_index: level index. 
        :type level_index: int

        :return: category label.
        :rtype: str  
        
		"""
		pass

	def getCategoryLabelList(self):
		"""
		Method to get the category label list of the legend.

        :return: Bounding box.
        :rtype: list  
        
		"""
		pass

	def getLevelColor(self,level_index: int =" 0"):
		"""
		Method to get the level color of the legend.
        
        :param level_index: Level index. 
        :type level_index: int

        :return: Level index color.
        :rtype: Color    
        
		"""
		pass

	def getLevelValue(self,level_index: int =" 0"):
		"""
		Method to get the level value of the legend.
        
        :param level_index: Level index. 
        :type level_index: int

        :return: Level legend value.
        :rtype: int    
        
		"""
		pass

	@property
	def headerFont(self):
		pass
	@headerFont.setter
	def headerFont(self):
		pass

	@property
	def headerText(self):
		pass
	@headerText.setter
	def headerText(self):
		pass

	@property
	def headerVisible(self):
		pass
	@headerVisible.setter
	def headerVisible(self):
		pass

	def interpolate(self,lower_index: int =" 0", upper_index: int =" 0"):
		"""
		Method to interpolate level colors of the legend.
        
        :param lower_index: Lower level index. 
        :type lower_index: int  

        :param lower_index: Upper level index. 
        :type lower_index: int  
        
		"""
		pass

	@property
	def interpolation(self):
		pass
	@interpolation.setter
	def interpolation(self):
		pass

	@property
	def maxValue(self):
		pass
	@maxValue.setter
	def maxValue(self):
		pass

	@property
	def minValue(self):
		pass
	@minValue.setter
	def minValue(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def multiplier(self):
		pass
	@multiplier.setter
	def multiplier(self):
		pass

	@property
	def numberFont(self):
		pass
	@numberFont.setter
	def numberFont(self):
		pass

	@property
	def numberOfLevels(self):
		pass
	@numberOfLevels.setter
	def numberOfLevels(self):
		pass

	@property
	def numericFormat(self):
		pass
	@numericFormat.setter
	def numericFormat(self):
		pass

	@property
	def numericPrecision(self):
		pass
	@numericPrecision.setter
	def numericPrecision(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def resetLevelValue(self,level_index: int =" 0"):
		"""
		Method to reset level value of the legend.

        :param level_index: Level index. 
        :type level_index: int  
        
		"""
		pass

	@property
	def reverse(self):
		pass
	@reverse.setter
	def reverse(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the Legend attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	def setLevelColor(self,level_index: Any =" 0", level_color: Any = None):
		"""
		Method to set the level color of the legend.
        
        :param level_index: level index. 
        :type level_index: Union[int, list]

        :param level_color: level color. 
        :type level_color: Union[Color, list, tuple] 
        
		"""
		pass

	def setLevelValue(self,level_index: Any =" 0", level_value: Any = None):
		"""
		Method to set the level value of the legend.
        
        :param level_index: level index. 
        :type level_index: Union[int, list]

        :param level_value: level value. 
        :type level_value: Union[int, float]  
        
		"""
		pass

	@property
	def showByModel(self):
		pass
	@showByModel.setter
	def showByModel(self):
		pass

	@property
	def showCategoryID(self):
		pass
	@showCategoryID.setter
	def showCategoryID(self):
		pass

	@property
	def showEntityLabel(self):
		pass
	@showEntityLabel.setter
	def showEntityLabel(self):
		pass

	@property
	def showMax(self):
		pass
	@showMax.setter
	def showMax(self):
		pass

	@property
	def showMaxLocal(self):
		pass
	@showMaxLocal.setter
	def showMaxLocal(self):
		pass

	@property
	def showMin(self):
		pass
	@showMin.setter
	def showMin(self):
		pass

	@property
	def showMinLocal(self):
		pass
	@showMinLocal.setter
	def showMinLocal(self):
		pass

	@property
	def style(self):
		pass
	@style.setter
	def style(self):
		pass

	@property
	def thresholdMax(self):
		pass
	@thresholdMax.setter
	def thresholdMax(self):
		pass

	@property
	def thresholdMaxValue(self):
		pass
	@thresholdMaxValue.setter
	def thresholdMaxValue(self):
		pass

	@property
	def thresholdMin(self):
		pass
	@thresholdMin.setter
	def thresholdMin(self):
		pass

	@property
	def thresholdMinValue(self):
		pass
	@thresholdMinValue.setter
	def thresholdMinValue(self):
		pass

	@property
	def titleFont(self):
		pass
	@titleFont.setter
	def titleFont(self):
		pass

	@property
	def titleText(self):
		pass
	@titleText.setter
	def titleText(self):
		pass

	@property
	def titleVisible(self):
		pass
	@titleVisible.setter
	def titleVisible(self):
		pass

	@property
	def transparency(self):
		pass
	@transparency.setter
	def transparency(self):
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class LegendVector:
	def __init__(self,resType: hw_module.hv.legend.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, **kwargs):
		"""

      A class representing Legend Vector.
    
      :param model: Model for the legend vector. Default is active model.
      :type model: Union[Model, int, str]

      :param window: Window for the legend vector. Default is active window.
      :type window: Union[Window, int]

      :param page: Page for the legend vector. Default is active page.
      :type page: Union[Page, int, str]

      :param kwargs: To set the other attributes of LegendVector class.
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
	def footerFont(self):
		pass
	@footerFont.setter
	def footerFont(self):
		pass

	@property
	def footerText(self):
		pass
	@footerText.setter
	def footerText(self):
		pass

	@property
	def footerVisible(self):
		pass
	@footerVisible.setter
	def footerVisible(self):
		pass

	def getBoundingBox(self):
		"""
		Method to get the bounding box of the legend.

        :return: Bounding box.
        :rtype: dict  
        
		"""
		pass

	def getCategoryLabel(self,level_index: int =" 0"):
		"""
		Method to get the category label of level in legend.

        :param level_index: level index. 
        :type level_index: int

        :return: category label.
        :rtype: str  
        
		"""
		pass

	def getCategoryLabelList(self):
		"""
		Method to get the category label list of the legend.

        :return: Bounding box.
        :rtype: list  
        
		"""
		pass

	def getLevelColor(self,level_index: int =" 0"):
		"""
		Method to get the level color of the legend.
        
        :param level_index: Level index. 
        :type level_index: int

        :return: Level index color.
        :rtype: Color    
        
		"""
		pass

	def getLevelValue(self,level_index: int =" 0"):
		"""
		Method to get the level value of the legend.
        
        :param level_index: Level index. 
        :type level_index: int

        :return: Level legend value.
        :rtype: int    
        
		"""
		pass

	@property
	def headerFont(self):
		pass
	@headerFont.setter
	def headerFont(self):
		pass

	@property
	def headerText(self):
		pass
	@headerText.setter
	def headerText(self):
		pass

	@property
	def headerVisible(self):
		pass
	@headerVisible.setter
	def headerVisible(self):
		pass

	def interpolate(self,lower_index: int =" 0", upper_index: int =" 0"):
		"""
		Method to interpolate level colors of the legend.
        
        :param lower_index: Lower level index. 
        :type lower_index: int  

        :param lower_index: Upper level index. 
        :type lower_index: int  
        
		"""
		pass

	@property
	def interpolation(self):
		pass
	@interpolation.setter
	def interpolation(self):
		pass

	@property
	def maxValue(self):
		pass
	@maxValue.setter
	def maxValue(self):
		pass

	@property
	def minValue(self):
		pass
	@minValue.setter
	def minValue(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def multiplier(self):
		pass
	@multiplier.setter
	def multiplier(self):
		pass

	@property
	def numberFont(self):
		pass
	@numberFont.setter
	def numberFont(self):
		pass

	@property
	def numberOfLevels(self):
		pass
	@numberOfLevels.setter
	def numberOfLevels(self):
		pass

	@property
	def numericFormat(self):
		pass
	@numericFormat.setter
	def numericFormat(self):
		pass

	@property
	def numericPrecision(self):
		pass
	@numericPrecision.setter
	def numericPrecision(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def resetLevelValue(self,level_index: int =" 0"):
		"""
		Method to reset level value of the legend.

        :param level_index: Level index. 
        :type level_index: int  
        
		"""
		pass

	@property
	def reverse(self):
		pass
	@reverse.setter
	def reverse(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the Legend attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	def setLevelColor(self,level_index: Any =" 0", level_color: Any = None):
		"""
		Method to set the level color of the legend.
        
        :param level_index: level index. 
        :type level_index: Union[int, list]

        :param level_color: level color. 
        :type level_color: Union[Color, list, tuple] 
        
		"""
		pass

	def setLevelValue(self,level_index: Any =" 0", level_value: Any = None):
		"""
		Method to set the level value of the legend.
        
        :param level_index: level index. 
        :type level_index: Union[int, list]

        :param level_value: level value. 
        :type level_value: Union[int, float]  
        
		"""
		pass

	@property
	def showByModel(self):
		pass
	@showByModel.setter
	def showByModel(self):
		pass

	@property
	def showCategoryID(self):
		pass
	@showCategoryID.setter
	def showCategoryID(self):
		pass

	@property
	def showEntityLabel(self):
		pass
	@showEntityLabel.setter
	def showEntityLabel(self):
		pass

	@property
	def showMax(self):
		pass
	@showMax.setter
	def showMax(self):
		pass

	@property
	def showMaxLocal(self):
		pass
	@showMaxLocal.setter
	def showMaxLocal(self):
		pass

	@property
	def showMin(self):
		pass
	@showMin.setter
	def showMin(self):
		pass

	@property
	def showMinLocal(self):
		pass
	@showMinLocal.setter
	def showMinLocal(self):
		pass

	@property
	def style(self):
		pass
	@style.setter
	def style(self):
		pass

	@property
	def thresholdMax(self):
		pass
	@thresholdMax.setter
	def thresholdMax(self):
		pass

	@property
	def thresholdMaxValue(self):
		pass
	@thresholdMaxValue.setter
	def thresholdMaxValue(self):
		pass

	@property
	def thresholdMin(self):
		pass
	@thresholdMin.setter
	def thresholdMin(self):
		pass

	@property
	def thresholdMinValue(self):
		pass
	@thresholdMinValue.setter
	def thresholdMinValue(self):
		pass

	@property
	def titleFont(self):
		pass
	@titleFont.setter
	def titleFont(self):
		pass

	@property
	def titleText(self):
		pass
	@titleText.setter
	def titleText(self):
		pass

	@property
	def titleVisible(self):
		pass
	@titleVisible.setter
	def titleVisible(self):
		pass

	@property
	def transparency(self):
		pass
	@transparency.setter
	def transparency(self):
		pass

	@property
	def type(self):
		pass
	@type.setter
	def type(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class Model:
	def __init__(self,model: Any = None, page: int|hw_module.page.Page = None, window: int|hw_module.window.Window = None, id: int = None):
		"""

    A class representing the Model.

    :param model: Model. Default is active model
    :type model: Union[Model, int]

    :param page: Page in which the model is present. Default is the active page.
    :type page: Union[Page, int, str]

    :param window: Window in which the model is present. Default is the active window.
    :type window: Union[Window, int]

    :param id: Model ID.
    :type id: int
    
"""
		pass

	def delete(self,entity, objOrId: list|str):
		"""
		Method to delete an entity collection
        
        :param entity: Entity like Collection 
        :type entity: Collection

        :param objOrId: Collection object, list of objects or **all**.
        :type objOrId: Union[Collection, list, str]
        
		"""
		pass

	def get(self,tag, id_or_lab, pool=None):
		"""
		Method to get the entity like Element, Node, Part, PartSet, PartAssembly.
        
        :param tag: Entity class, like Element, Node, Part, PartSet, PartAssembly. 
        :type tag: Union[Element, Node, Part, PartSet, PartAssembly]

        :param id_or_lab: level index. 
        :type id_or_lab: int

        :param pool: Pool of the Entity. Default is None.
        :type pool: str

        :return: Requested entity object.
        :rtype: Union[Element, Node, Part, PartSet, PartAssembly]  
        
		"""
		pass

	def hide(self,colobj):
		"""
		Method to hide the collection
        
        :param colobj: Collection object. 
        :type colobj: Union[Element, Node, Part, PartSet, PartAssembly]
        
		"""
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	def isolate(self,colobj):
		"""
		Method to isolate the collection
        
        :param colobj: Collection object. 
        :type colobj: Union[Element, Node, Part, PartSet, PartAssembly]
        
		"""
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def show(self,colobj):
		"""
		Method to show the collection
        
        :param colobj: Collection object. 
        :type colobj: Union[Element, Node, Part, PartSet, PartAssembly]
        
		"""
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class Node:
	def __init__(self,id, pool=None, model: hw_module.hv.model.Model = None):
		"""

    A class representing a Node. Get a Node for the given model.
    Raises an Exception parameter if it does not point to a valid Node.
    
    :param id: ID of Node.
    :type id: int

    :param pool: The specific pool, default is None.
    :type pool: str

    :param model: The specific model, default is active model.
    :type model: Union[int, str, Model]
    
"""
		pass

	@property
	def coords(self):
		pass
	@coords.setter
	def coords(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def part(self):
		pass
	@part.setter
	def part(self):
		pass

	@property
	def partId(self):
		pass
	@partId.setter
	def partId(self):
		pass

	@property
	def pool(self):
		pass
	@pool.setter
	def pool(self):
		pass

class Note:
	def __init__(self,window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int =" 0", **kwargs):
		"""

      A class representing Note.

      :param window: Window for the Note. Default is the active window.
      :type window: Union[Window, int]

      :param page: Page for the Note. Default is active page.
      :type page: Union[Page, int, str]

      :param id: id of the Note. Default is 1.
      :type id: int

      :param kwargs: To set the other attributes of Note class.
      :type kwargs: dict

     
"""
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def attachment(self):
		pass
	@attachment.setter
	def attachment(self):
		pass

	@property
	def attachmentType(self):
		pass
	@attachmentType.setter
	def attachmentType(self):
		pass

	@property
	def autoHide(self):
		pass
	@autoHide.setter
	def autoHide(self):
		pass

	@property
	def borderColor(self):
		pass
	@borderColor.setter
	def borderColor(self):
		pass

	@property
	def borderColorMode(self):
		pass
	@borderColorMode.setter
	def borderColorMode(self):
		pass

	@property
	def borderThickness(self):
		pass
	@borderThickness.setter
	def borderThickness(self):
		pass

	@property
	def fillColor(self):
		pass
	@fillColor.setter
	def fillColor(self):
		pass

	@property
	def fillColorMode(self):
		pass
	@fillColorMode.setter
	def fillColorMode(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def fontSize(self):
		pass
	@fontSize.setter
	def fontSize(self):
		pass

	def getBoundingBox(self):
		"""
		Method to get the bounding box of the Note.

        :return: Bounding box.
        :rtype: dict  
        
		"""
		pass

	def getFieldDictionary(self):
		"""
		Method to get the field dictionary of the Note.

        :return: field dictionary.
        :rtype: dict  
        
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def moveToEntity(self):
		pass
	@moveToEntity.setter
	def moveToEntity(self):
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
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	@property
	def positionType(self):
		pass
	@positionType.setter
	def positionType(self):
		pass

	@property
	def rotationAngle(self):
		pass
	@rotationAngle.setter
	def rotationAngle(self):
		pass

	@property
	def screenAnchor(self):
		pass
	@screenAnchor.setter
	def screenAnchor(self):
		pass

	def setAttributes(self,**kwargs):
		pass

	@property
	def shape(self):
		pass
	@shape.setter
	def shape(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def textAsDisplayed(self):
		pass
	@textAsDisplayed.setter
	def textAsDisplayed(self):
		pass

	@property
	def textColor(self):
		pass
	@textColor.setter
	def textColor(self):
		pass

	@property
	def textColorMode(self):
		pass
	@textColorMode.setter
	def textColorMode(self):
		pass

	@property
	def transparency(self):
		pass
	@transparency.setter
	def transparency(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class Part:
	def __init__(self,id_or_lab, pool=None, model: hw_module.hv.model.Model = None):
		"""

    A class representing a Part (Component). Get a Part of the given model.
    Raises an Exception parameter if it does not points to a valid Part.
    
    :param id_or_lab: id or label of the Part.
    :type id_or_lab: Union[int, str]

    :param pool: The specific pool, default is None.
    :type pool: str

    :param model: The specific model, default is the active model.
    :type model: Union[int, str, Model]
    
"""
		pass

	@property
	def color(self):
		pass
	@color.setter
	def color(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def idVisibility(self):
		pass
	@idVisibility.setter
	def idVisibility(self):
		pass

	@property
	def meshMode(self):
		pass
	@meshMode.setter
	def meshMode(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def pool(self):
		pass
	@pool.setter
	def pool(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the Part attributes.
		"""
		pass

	@property
	def useInFit(self):
		pass
	@useInFit.setter
	def useInFit(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

class PartAssembly:
	def __init__(self,id_or_lab, model: hw_module.hv.model.Model = None):
		"""

    A class representing a PartAssembly. Get a PartAssembly of the given model.
    Raises an Exception parameter if it does not point to a valid PartAssembly.
    
    :param id_or_lab: id or label of PartAssembly.
    :type id_or_lab: Union[int, str]

    :param model: The specific model, default is active model.
    :type model: Union[int, str, Model]
    
"""
		pass

	@property
	def color(self):
		pass
	@color.setter
	def color(self):
		pass

	@property
	def componentId(self):
		pass
	@componentId.setter
	def componentId(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def materialId(self):
		pass
	@materialId.setter
	def materialId(self):
		pass

	@property
	def materialName(self):
		pass
	@materialName.setter
	def materialName(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def pdmId(self):
		pass
	@pdmId.setter
	def pdmId(self):
		pass

	@property
	def pdmMaterial(self):
		pass
	@pdmMaterial.setter
	def pdmMaterial(self):
		pass

	@property
	def pdmMaterialId(self):
		pass
	@pdmMaterialId.setter
	def pdmMaterialId(self):
		pass

	@property
	def pdmPropertyId(self):
		pass
	@pdmPropertyId.setter
	def pdmPropertyId(self):
		pass

	@property
	def pdmRevision(self):
		pass
	@pdmRevision.setter
	def pdmRevision(self):
		pass

	@property
	def pdmThickness(self):
		pass
	@pdmThickness.setter
	def pdmThickness(self):
		pass

	@property
	def positionX0Y0Z0(self):
		pass
	@positionX0Y0Z0.setter
	def positionX0Y0Z0(self):
		pass

	@property
	def positiondX1dY1dZ1(self):
		pass
	@positiondX1dY1dZ1.setter
	def positiondX1dY1dZ1(self):
		pass

	@property
	def positiondX2dY2dZ2(self):
		pass
	@positiondX2dY2dZ2.setter
	def positiondX2dY2dZ2(self):
		pass

	@property
	def positiondX3dY3dZ3(self):
		pass
	@positiondX3dY3dZ3.setter
	def positiondX3dY3dZ3(self):
		pass

	@property
	def propertyId(self):
		pass
	@propertyId.setter
	def propertyId(self):
		pass

	@property
	def representation(self):
		pass
	@representation.setter
	def representation(self):
		pass

	@property
	def representationFile(self):
		pass
	@representationFile.setter
	def representationFile(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the PartAssembly attributes.
		"""
		pass

	@property
	def uId(self):
		pass
	@uId.setter
	def uId(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

class PartSet:
	def __init__(self,id_or_lab, model: hw_module.hv.model.Model = None):
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

class Result:
	def __init__(self,model: hw_module.hv.model.Model = None, page: int = None, window: int = None, **kwargs):
		"""

    A class representing the Result information.

    :param model: Model. Default is the active model
    :type model: Union[Model, int]

    :param page: Page in which the model is present. Default is the active page.
    :type page: Union[Page, int, str]

    :param window: Window in which the model is present. Default is the active window.
    :type window: Union[Window, int]

    :param kwargs: To set the other attributes of the Result class.
    :type kwargs: dict

    
"""
		pass

	def cache(self,res_def: hw_module.hv.resultdefinition.ResultDefinition|str):
		"""
		Method to cache the ResultDefinition

        :param res_def: ResultDefinition object, list or string value **all**.
        :type res_def: Union[ResultDefinitionScalar, ResultDefinitionIso]
        
		"""
		pass

	def clearIso(self,res_def=None):
		"""
		Method to clear the iso plotted result

        :param res_def: ResultDefinitionScalar or ResultDefinitionIso object
        :type res_def: Union[ResultDefinitionScalar, ResultDefinitionIso]
        
		"""
		pass

	def clearPlot(self,res_def: hw_module.hv.resultdefinition.ResultDefinition):
		"""
		Method to clear the plotted result

        :param res_def: ResultDefinitionScalar, ResultDefinitionVector, ResultDefinitionTensor object.
        :type res_def: Union[ResultDefinitionScalar, ResultDefinitionVector, ResultDefinitionTensor]
        
		"""
		pass

	def getDataComponents(self,datatype: str, subcase: int|str = None):
		"""
		Method to get the data components of the subcase.

        :param datatype: Datatype. 
        :type datatype: str

        :param subcase: Subcase.
        :type subcase: Union[int,str]

        :return: Data components.
        :rtype: list  
        
		"""
		pass

	def getDataTypeBinding(self,datatype: str, subcase: int|str = None):
		"""
		Method to get the data type binding of the subcase.

        :param datatype: Datatype. 
        :type datatype: str

        :param subcase: Subcase.
        :type subcase: Union[int,str])

        :return: Data type binding.
        :rtype: str  
        
		"""
		pass

	def getDataTypeFormat(self,datatype: str, subcase: int|str = None):
		"""
		Method to get the data type format of the subcase.

        :param datatype: Datatype. 
        :type datatype: str

        :param subcase: Subcase.
        :type subcase: Union[int,str]

        :return: Data type format.
        :rtype: str  
        
		"""
		pass

	def getDataTypes(self,subcase: int|str = None, context: str =" 0"):
		"""
		Method to get the data types of the subcase.
        
        :param subcase: Subcase. 
        :type subcase: Union[int,str]

        :param context: Default is scalar context.
        :type context: str

        :return: Data type list.
        :rtype: list  
        
		"""
		pass

	def getSimulationIds(self,subid: int = None):
		"""
		Method to get the simulation ID list.

        :param subid: Subcase ID
        :type subid: int

        :return: Simulation ID list.
        :rtype: list. 
        
		"""
		pass

	def getSimulationLabel(self,subid: int, simid: int):
		"""
		Method to get the simulation label

        :param subid: Subcase ID.
        :type subid: int

        :param simid: Simulation ID.
        :type simid: int

        :return: Simulation label.
        :rtype: str
        
		"""
		pass

	def getSimulationLabels(self,subid: int = None):
		"""
		Method to get the simulation label list.

        :param subid: Subcase ID
        :type subid: int

        :return: Simulation label list.
        :rtype: list. 
        
		"""
		pass

	def getSubcaseIds(self):
		"""
		Method to get the subcase ID list.

        :return: Subcase id list.
        :rtype: list. 
        
		"""
		pass

	def getSubcaseLabels(self):
		"""
		Method to get the subcase label list.

        :return: Subcase label list.
        :rtype: list. 
        
		"""
		pass

	def getTag(self):
		"""
		Method to get page,window,model string format
		"""
		pass

	def loadAnimation(self,subcase: Any = None, frame: str|list|range|int = None, _unload=False):
		"""
		Method to load the simulation.
        
        :param subcase: Subcase ID, list, range or one of string options **first**, **last**, and **all**.
        :type subcase: Union[int, list, range, str]

        :param frame: Simulation ID,list, range or one of string options **first**, **last**, and **all**.
        :type frame: Union[int, list, range, str]
        
		"""
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def plot(self,res_def: hw_module.hv.resultdefinition.ResultDefinition, waitTillLoaded: bool = False):
		"""
		Method to plot the result

        :param res_def: Scalar,Vector,Tensor ResultDefinition object
        :type res_def: Union[ResultDefinitionScalar, ResultDefinitionVector, ResultDefinitionTensor]

        :param waitTillLoaded: Flag to wait till load result. Valid in Multi-Core profile.
        :type waitTillLoaded: bool
        
		"""
		pass

	def plotIso(self,res_def: hw_module.hv.resultdefinition.ResultDefinition):
		"""
		Method to plot the iso result

        :param res_def: Iso ResultDefinition object
        :type res_def: ResultDefinitionIso object.
        
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the Result attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def simulation(self):
		pass
	@simulation.setter
	def simulation(self):
		pass

	@property
	def subcase(self):
		pass
	@subcase.setter
	def subcase(self):
		pass

	def uncache(self,res_def: hw_module.hv.resultdefinition.ResultDefinition):
		"""
		Method to uncache the ResultDefinition

        :param res_def: ResultDefinition object, list or string value **all**.
        :type res_def: Union[ResultDefinitionScalar, ResultDefinitionIso]
        
		"""
		pass

	def unloadAnimation(self,subcase: int = None, frame: str|list|range|int = None):
		"""
		Method to unload the simulation.

        :param subcase: Subcase ID, list, range or one of string options *first**, **last**, and **all**.
        :type subcase: Union[int, list, range, str]

        :param frame: Simulation ID, list, range or one of string options *first**, **last**, and **all**.
        :type frame: Union[int, list, range, str]
        
		"""
		pass

	def update(self,res_def: hw_module.hv.resultdefinition.ResultDefinition):
		"""
		Method to update the ResultDefinition

        :param res_def: ResultDefinition object, list or string value **all**.
        :type res_def: Union[ResultDefinitionScalar, ResultDefinitionIso]
        
		"""
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class ResultDefinitionIso:
	def __init__(self,type: hw_module.hv.resultdefinition.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int = 1, label: str = None, **kwargs):
		"""

    A class representing the ResultDefinitionIso.

    :param model: Model for the ResultDefinitionIso. Default is the active model.
    :type model: Union[Model, int, str]

    :param window: Window for the ResultDefinitionIso. Default is the active window.
    :type window: Union[Window, int]

    :param page: Page for the ResultDefinitionIso. Default is the active page.
    :type page: Union[Page, int, str]

    :param id: ResultDefinitionIso ID. Default is 1.
    :type id: int

    :param label: ResultDefinitionIso label.
    :type label: str

    :param kwargs: To set the other attributes of the ResultDefinitionIso class.
    :type kwargs: dict

    
"""
		pass

	@property
	def averageAcrossBoundaries(self):
		pass
	@averageAcrossBoundaries.setter
	def averageAcrossBoundaries(self):
		pass

	@property
	def averageFactor(self):
		pass
	@averageFactor.setter
	def averageFactor(self):
		pass

	@property
	def averageFeatureangle(self):
		pass
	@averageFeatureangle.setter
	def averageFeatureangle(self):
		pass

	@property
	def averageMode(self):
		pass
	@averageMode.setter
	def averageMode(self):
		pass

	@property
	def cached(self):
		pass
	@cached.setter
	def cached(self):
		pass

	@property
	def collection(self):
		pass
	@collection.setter
	def collection(self):
		pass

	@property
	def complexFilter(self):
		pass
	@complexFilter.setter
	def complexFilter(self):
		pass

	@property
	def cornerData(self):
		pass
	@cornerData.setter
	def cornerData(self):
		pass

	@property
	def dataComponent(self):
		pass
	@dataComponent.setter
	def dataComponent(self):
		pass

	@property
	def dataType(self):
		pass
	@dataType.setter
	def dataType(self):
		pass

	def display(self):
		"""
		Method to plot the result definition like ResultDefinitionScalar, ResultDefinitionVector and ResultDefinitionTensor
		"""
		pass

	@property
	def envelopeTraceplot(self):
		pass
	@envelopeTraceplot.setter
	def envelopeTraceplot(self):
		pass

	@property
	def featureAngle(self):
		pass
	@featureAngle.setter
	def featureAngle(self):
		pass

	@property
	def filterMode(self):
		pass
	@filterMode.setter
	def filterMode(self):
		pass

	@property
	def filterValue(self):
		pass
	@filterValue.setter
	def filterValue(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def ignoreFlippedNormals(self):
		pass
	@ignoreFlippedNormals.setter
	def ignoreFlippedNormals(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def layer(self):
		pass
	@layer.setter
	def layer(self):
		pass

	@property
	def layerFilter(self):
		pass
	@layerFilter.setter
	def layerFilter(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def projectionRule(self):
		pass
	@projectionRule.setter
	def projectionRule(self):
		pass

	@property
	def resultType(self):
		pass
	@resultType.setter
	def resultType(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the ResultDefinition attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def showMidnodeResults(self):
		pass
	@showMidnodeResults.setter
	def showMidnodeResults(self):
		pass

	@property
	def system(self):
		pass
	@system.setter
	def system(self):
		pass

	@property
	def topBottom(self):
		pass
	@topBottom.setter
	def topBottom(self):
		pass

	@property
	def useTracking(self):
		pass
	@useTracking.setter
	def useTracking(self):
		pass

	@property
	def variation(self):
		pass
	@variation.setter
	def variation(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class ResultDefinitionScalar:
	def __init__(self,type: hw_module.hv.resultdefinition.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int = 1, label: str = None, **kwargs):
		"""

    A class representing ResultDefinitionScalar.

    :param model: Model for the ResultDefinitionScalar. Default is the active model.
    :type model: Union[Model, int, str]

    :param window: Window for the ResultDefinitionScalar. Default is the active window.
    :type window: Union[Window, int]

    :param page: Page for the ResultDefinitionScalar. Default is the active page.
    :type page: Union[Page, int, str]

    :param id: ResultDefinitionScalar ID. Default is 1.
    :type id: int

    :param label: ResultDefinitionScalar label.
    :type label: str

    :param kwargs: To set the other attributes of ResultDefinitionScalar class.
    :type kwargs: dict

    
"""
		pass

	@property
	def averageAcrossBoundaries(self):
		pass
	@averageAcrossBoundaries.setter
	def averageAcrossBoundaries(self):
		pass

	@property
	def averageFactor(self):
		pass
	@averageFactor.setter
	def averageFactor(self):
		pass

	@property
	def averageFeatureangle(self):
		pass
	@averageFeatureangle.setter
	def averageFeatureangle(self):
		pass

	@property
	def averageMode(self):
		pass
	@averageMode.setter
	def averageMode(self):
		pass

	@property
	def cached(self):
		pass
	@cached.setter
	def cached(self):
		pass

	@property
	def collection(self):
		pass
	@collection.setter
	def collection(self):
		pass

	@property
	def complexFilter(self):
		pass
	@complexFilter.setter
	def complexFilter(self):
		pass

	@property
	def cornerData(self):
		pass
	@cornerData.setter
	def cornerData(self):
		pass

	@property
	def dataComponent(self):
		pass
	@dataComponent.setter
	def dataComponent(self):
		pass

	@property
	def dataType(self):
		pass
	@dataType.setter
	def dataType(self):
		pass

	def display(self):
		"""
		Method to plot the result definition like ResultDefinitionScalar, ResultDefinitionVector and ResultDefinitionTensor
		"""
		pass

	@property
	def envelopeTraceplot(self):
		pass
	@envelopeTraceplot.setter
	def envelopeTraceplot(self):
		pass

	@property
	def featureAngle(self):
		pass
	@featureAngle.setter
	def featureAngle(self):
		pass

	@property
	def filterMode(self):
		pass
	@filterMode.setter
	def filterMode(self):
		pass

	@property
	def filterValue(self):
		pass
	@filterValue.setter
	def filterValue(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def ignoreFlippedNormals(self):
		pass
	@ignoreFlippedNormals.setter
	def ignoreFlippedNormals(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def layer(self):
		pass
	@layer.setter
	def layer(self):
		pass

	@property
	def layerFilter(self):
		pass
	@layerFilter.setter
	def layerFilter(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def projectionRule(self):
		pass
	@projectionRule.setter
	def projectionRule(self):
		pass

	@property
	def resultType(self):
		pass
	@resultType.setter
	def resultType(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the ResultDefinition attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def showMidnodeResults(self):
		pass
	@showMidnodeResults.setter
	def showMidnodeResults(self):
		pass

	@property
	def system(self):
		pass
	@system.setter
	def system(self):
		pass

	@property
	def topBottom(self):
		pass
	@topBottom.setter
	def topBottom(self):
		pass

	@property
	def useTracking(self):
		pass
	@useTracking.setter
	def useTracking(self):
		pass

	@property
	def variation(self):
		pass
	@variation.setter
	def variation(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class ResultDefinitionTensor:
	def __init__(self,type: hw_module.hv.resultdefinition.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int = 1, label: str = None, **kwargs):
		"""

    A class representing the ResultDefinitionTensor.
    
    :param model: Model for the ResultDefinitionTensor. Default is the active model.
    :type model: Union[Model, int, str]

    :param window: Window for the ResultDefinitionTensor. Default is the active window.
    :type window: Union[Window, int]

    :param page: Page for the ResultDefinitionTensor. Default is the active page.
    :type page: Union[Page, int, str]

    :param id: ResultDefinitionTensor ID. Default is 1.
    :type id: int

    :param label: ResultDefinitionTensor label.
    :type label: str

    :param kwargs: To set the other attributes of the ResultDefinitionTensor class.
    :type kwargs: dict

    
"""
		pass

	@property
	def averageAtNode(self):
		pass
	@averageAtNode.setter
	def averageAtNode(self):
		pass

	@property
	def cached(self):
		pass
	@cached.setter
	def cached(self):
		pass

	@property
	def collection(self):
		pass
	@collection.setter
	def collection(self):
		pass

	@property
	def colorMode(self):
		pass
	@colorMode.setter
	def colorMode(self):
		pass

	@property
	def cornerData(self):
		pass
	@cornerData.setter
	def cornerData(self):
		pass

	@property
	def dataType(self):
		pass
	@dataType.setter
	def dataType(self):
		pass

	def display(self):
		"""
		Method to plot the result definition like ResultDefinitionScalar, ResultDefinitionVector and ResultDefinitionTensor
		"""
		pass

	@property
	def displayMode(self):
		pass
	@displayMode.setter
	def displayMode(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def fontSize(self):
		pass
	@fontSize.setter
	def fontSize(self):
		pass

	@property
	def format(self):
		pass
	@format.setter
	def format(self):
		pass

	def getComponentColor(self,name: str):
		"""
		Method to get the data component color of the ResultDefinitionTensor.
        
        :param name: Name of the Component. Options are **xx**, **yy**, **zz**, **xy**, **yz** and **zx**.
        :type name: str
        
		"""
		pass

	def getComponentStatus(self,cm: Any):
		"""
		Method to get the data component display mode of the ResultDefinitionTensor.

        :param name: Name of the data Component.Options are **xx**, **yy**, **zz**, **xy**, **yz** and **zx**.
        :type name: str
        
		"""
		pass

	def getPrincipalColor(self,name: str):
		"""
		Method to get the principal data component color of the ResultDefinitionTensor.

        :param name: Name of the principal data component.Options are **p1**, **p2** and **p3**.
        :type name: str
        
		"""
		pass

	def getPrincipalStatus(self,cm: str):
		"""
		Method to get the principal data component display mode of the ResultDefinitionTensor.
        
        :param name: Name of the principal data Component.Options are **p1**, **p2** and **p3**.
        :type name: str
        
		"""
		pass

	@property
	def headType(self):
		pass
	@headType.setter
	def headType(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def layer(self):
		pass
	@layer.setter
	def layer(self):
		pass

	@property
	def layerFilter(self):
		pass
	@layerFilter.setter
	def layerFilter(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def projectionRule(self):
		pass
	@projectionRule.setter
	def projectionRule(self):
		pass

	@property
	def resultType(self):
		pass
	@resultType.setter
	def resultType(self):
		pass

	@property
	def scale(self):
		pass
	@scale.setter
	def scale(self):
		pass

	@property
	def scaleMode(self):
		pass
	@scaleMode.setter
	def scaleMode(self):
		pass

	@property
	def scaleShearComponent(self):
		pass
	@scaleShearComponent.setter
	def scaleShearComponent(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the ResultDefinition attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	def setComponentColor(self,**kwargs):
		"""
		Method to set the data component color of the ResultDefinitionTensor.

        :param kwargs: Dict of the Name of the Component and color.
        :type kwargs: dict 
        
		"""
		pass

	def setComponentStatus(self,**kwargs):
		"""
		Method to set the data component display mode of the ResultDefinitionTensor.
        
        :param kwargs: Dict of the Name of the data component and boolean.
        :type kwargs: dict 
        
		"""
		pass

	def setPrincipalColor(self,**kwargs):
		"""
		Method to set the principal data component color of the ResultDefinitionTensor.

        :param kwargs: Dict of the Name of the principal data component and color.
        :type kwargs: dict 
        
		"""
		pass

	def setPrincipalStatus(self,**kwargs):
		"""
		Method to set the principal data component display mode of the ResultDefinitionTensor.
        
        :param kwargs: Dictionary of the name of the principal data component and boolean value.
        :type kwargs: dict 
        
		"""
		pass

	@property
	def showMidnodeResults(self):
		pass
	@showMidnodeResults.setter
	def showMidnodeResults(self):
		pass

	@property
	def showPrefixNormal(self):
		pass
	@showPrefixNormal.setter
	def showPrefixNormal(self):
		pass

	@property
	def showPrefixShear(self):
		pass
	@showPrefixShear.setter
	def showPrefixShear(self):
		pass

	@property
	def showValueNormal(self):
		pass
	@showValueNormal.setter
	def showValueNormal(self):
		pass

	@property
	def showValueShear(self):
		pass
	@showValueShear.setter
	def showValueShear(self):
		pass

	@property
	def system(self):
		pass
	@system.setter
	def system(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class ResultDefinitionVector:
	def __init__(self,type: hw_module.hv.resultdefinition.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int = 1, label: str = None, **kwargs):
		"""

    A class representing the ResultDefinitionVector.
    
    :param model: Model for the ResultDefinitionVector. Default is the active model.
    :type model: Union[Model, int, str]

    :param window: Window for the ResultDefinitionVector. Default is the active window.
    :type window: Union[Window, int]

    :param page: Page for the ResultDefinitionVector. Default is the active page.
    :type page: Union[Page, int, str]

    :param id: ResultDefinitionVector ID. Default is 1.
    :type id: int

    :param label:ResultDefinitionVector label.
    :type label: str

    :param kwargs: To set the other attributes of the ResultDefinitionVector class.
    :type kwargs: dict

    
"""
		pass

	@property
	def cached(self):
		pass
	@cached.setter
	def cached(self):
		pass

	@property
	def collection(self):
		pass
	@collection.setter
	def collection(self):
		pass

	@property
	def colorMode(self):
		pass
	@colorMode.setter
	def colorMode(self):
		pass

	@property
	def cornerData(self):
		pass
	@cornerData.setter
	def cornerData(self):
		pass

	@property
	def dataType(self):
		pass
	@dataType.setter
	def dataType(self):
		pass

	def display(self):
		"""
		Method to plot the result definition like ResultDefinitionScalar, ResultDefinitionVector and ResultDefinitionTensor
		"""
		pass

	@property
	def drawPosition(self):
		pass
	@drawPosition.setter
	def drawPosition(self):
		pass

	@property
	def evenlyDistributed(self):
		pass
	@evenlyDistributed.setter
	def evenlyDistributed(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def fontSize(self):
		pass
	@fontSize.setter
	def fontSize(self):
		pass

	def getComponentColor(self,name: str):
		"""
		Method to get the component color of the ResultDefinitionVector.

        :param name: Name of the Component or Resultant. Options are **x**, **y**, **z**, **xy**, **yz**, **zx**, and **xyz**.
        :type name: str
        
		"""
		pass

	def getDisplayMode(self,name: str):
		"""
		Method to get the display mode of the ResultDefinitionVector.

        :param name: Name of the Component or Resultant. Options are **x**, **y**, **z**, **xy**, **yz**, **zx**, **xyz**, **prefix** or **value**.
        :type name: str
        
		"""
		pass

	@property
	def headType(self):
		pass
	@headType.setter
	def headType(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def layer(self):
		pass
	@layer.setter
	def layer(self):
		pass

	@property
	def layerFilter(self):
		pass
	@layerFilter.setter
	def layerFilter(self):
		pass

	@property
	def model(self):
		pass
	@model.setter
	def model(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def projected(self):
		pass
	@projected.setter
	def projected(self):
		pass

	@property
	def resultType(self):
		pass
	@resultType.setter
	def resultType(self):
		pass

	@property
	def scale(self):
		pass
	@scale.setter
	def scale(self):
		pass

	@property
	def scaleMode(self):
		pass
	@scaleMode.setter
	def scaleMode(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the ResultDefinition attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	def setComponentColor(self,**kwargs):
		"""
		Method to set the Component color of the ResultDefinitionVector.
        
        :param kwargs: Dictionary of the Name of the Component or Resultant and color.
        :type kwargs: dict 
        
		"""
		pass

	def setDisplayMode(self,**kwargs):
		"""
		Method to set the display mode of the ResultDefinitionVector.

        :param kwargs: Dictionary of the Name of the Component or Resultant and Boolean.
        :type kwargs: dict 
        
		"""
		pass

	@property
	def showMidnodeResults(self):
		pass
	@showMidnodeResults.setter
	def showMidnodeResults(self):
		pass

	@property
	def system(self):
		pass
	@system.setter
	def system(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class ResultDisplayIso:
	def __init__(self,type: hw_module.hv.resultdefinition.ResultPlotType = None, model=None, window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int = 1, label: str = None, _add: bool = True, **kwargs):
		"""

    A class representing the ResultDisplayIso.
    
    :param model: Model for the ResultDisplayIso. Default is the active model.
    :type model: Union[Model, int, str]

    :param window: Window for the ResultDisplayIso. Default is the active window.
    :type window: Union[Window, int]

    :param page: Page for the ResultDisplayIso. Default is the active page.
    :type page: Union[Page, int, str]

    :param id: ResultDisplayIso ID. Default is 1.
    :type id: int

    :param label: ResultDisplayIso label.
    :type label: str

    :param kwargs: To set the other attributes of the ResultDisplayIso class.
    :type kwargs: dict

    
"""
		pass

	@property
	def color(self):
		pass
	@color.setter
	def color(self):
		pass

	@property
	def displayMode(self):
		pass
	@displayMode.setter
	def displayMode(self):
		pass

	@property
	def increment(self):
		pass
	@increment.setter
	def increment(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the ResultDisplayIso attributes.

        :param kwargs: Attribute dictionary.
        :type kwargs: dict
        
		"""
		pass

	@property
	def showColor(self):
		pass
	@showColor.setter
	def showColor(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def valueRange(self):
		pass
	@valueRange.setter
	def valueRange(self):
		pass

class ScalarType:
	"""
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
"""
	pass

class SectionCutPlanar:
	def __init__(self,window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int = None, **kwargs):
		"""

      A class representing the SectionCut Planar.

      :param window: Window for the SectionCut Planar. Default is the active window.
      :type window: Union[Window, int]

      :param page: Page for the SectionCut Planar. Default is the active page.
      :type page: Union[Page, int, str]

      :param id: id of the SectionCut Planar. Default is 1.
      :type id: int

      :param kwargs: To set the other attributes of the SectionCutPlanar class.
      :type kwargs: dict

     
"""
		pass

	@property
	def baseCoordinates(self):
		pass
	@baseCoordinates.setter
	def baseCoordinates(self):
		pass

	@property
	def baseFrame(self):
		pass
	@baseFrame.setter
	def baseFrame(self):
		pass

	@property
	def baseTime(self):
		pass
	@baseTime.setter
	def baseTime(self):
		pass

	@property
	def clipAbove(self):
		pass
	@clipAbove.setter
	def clipAbove(self):
		pass

	@property
	def clipElements(self):
		pass
	@clipElements.setter
	def clipElements(self):
		pass

	@property
	def color(self):
		pass
	@color.setter
	def color(self):
		pass

	@property
	def crossSectionOnly(self):
		pass
	@crossSectionOnly.setter
	def crossSectionOnly(self):
		pass

	@property
	def deformable(self):
		pass
	@deformable.setter
	def deformable(self):
		pass

	@property
	def featureLines(self):
		pass
	@featureLines.setter
	def featureLines(self):
		pass

	@property
	def gridLines(self):
		pass
	@gridLines.setter
	def gridLines(self):
		pass

	@property
	def gridSpaceX(self):
		pass
	@gridSpaceX.setter
	def gridSpaceX(self):
		pass

	@property
	def gridSpaceY(self):
		pass
	@gridSpaceY.setter
	def gridSpaceY(self):
		pass

	@property
	def gridText(self):
		pass
	@gridText.setter
	def gridText(self):
		pass

	@property
	def gridTextPrecision(self):
		pass
	@gridTextPrecision.setter
	def gridTextPrecision(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def orientationVector(self):
		pass
	@orientationVector.setter
	def orientationVector(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	def reverse(self):
		"""
		Method to reverse the direction of SectionCut.
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the SectionCut attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	def setBaseNode(self,node: int|hw_module.hv.entity.Node, model: int|hw_module.hv.model.Model = None):
		"""
		Method to set the base node of the SectionCutPlanar.
        
        :param node: Node id or obect.
        :type node: Union[int, Node]

        :param model: Model id or object. 
        :type model: Union[int,Model] 
        
		"""
		pass

	def setOrientationByAligneView(self):
		"""
		Method to set the orientation node of the SectionCutPlanar by the align view method.
		"""
		pass

	def setOrientationByAxis(self,orientationAxis: str =" y", node: int|hw_module.hv.entity.Node = None):
		"""
		Method to set the orientation axis of the SectionCutPlanar.
        
        :param orientationAxis: Orientation axis. 'x','y' or 'z'.
        :type orientationAxis:str

        :param node: Node id or obect.
        :type node: Union[int, Node]
        
		"""
		pass

	def setOrientationByNode(self,n1: int|hw_module.hv.entity.Node, n2: int|hw_module.hv.entity.Node, n3: int|hw_module.hv.entity.Node = None, base: int|hw_module.hv.entity.Node|list|tuple = None):
		"""
		Method to set the orientation node of the SectionCutPlanar.

        :param n1: First node id or obect.
        :type n1: Union[int, Node]

        :param n2: Second node id or obect.
        :type n2: Union[int, Node]

        :param n3: Third node id or obect.
        :type n3: Union[int, Node]

        :param base: Base node id or obect.
        :type base: Union[int, Node]
        
		"""
		pass

	def setOrientationByNormalToScreen(self,node: int|hw_module.hv.entity.Node|list|tuple = None):
		"""
		Method to set the normal to screen orientation of the SectionCutPlanar.

        :param node: Node id,Node obect or Node coodinates.
        :type node: Union[int, Node,list,tuple]
        
		"""
		pass

	@property
	def showColor(self):
		pass
	@showColor.setter
	def showColor(self):
		pass

	@property
	def thickness(self):
		pass
	@thickness.setter
	def thickness(self):
		pass

	@property
	def transparency(self):
		pass
	@transparency.setter
	def transparency(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class SectionCutSpherical:
	def __init__(self,window: hw_module.window.Window = None, page: hw_module.page.Page = None, id: int = None, **kwargs):
		"""

       A class representing SectionCut Spherical.

       :param window: Window for the SectionCut Spherical. Default is the active window.
       :type window: Union[Window, int]

       :param page: Page for the SectionCut Spherical. Default is the active page.
       :type page: Union[Page, int, str]

       :param id: id of the SectionCut Spherical. Default is 1.
       :type id: int

       :param kwargs: To set the other attributes of the SectionCutSpherical class.
       :type kwargs: dict

      
"""
		pass

	@property
	def baseFrame(self):
		pass
	@baseFrame.setter
	def baseFrame(self):
		pass

	@property
	def baseTime(self):
		pass
	@baseTime.setter
	def baseTime(self):
		pass

	@property
	def center(self):
		pass
	@center.setter
	def center(self):
		pass

	@property
	def clipElements(self):
		pass
	@clipElements.setter
	def clipElements(self):
		pass

	@property
	def clipInside(self):
		pass
	@clipInside.setter
	def clipInside(self):
		pass

	@property
	def color(self):
		pass
	@color.setter
	def color(self):
		pass

	@property
	def crossSectionOnly(self):
		pass
	@crossSectionOnly.setter
	def crossSectionOnly(self):
		pass

	@property
	def deformable(self):
		pass
	@deformable.setter
	def deformable(self):
		pass

	@property
	def featureLines(self):
		pass
	@featureLines.setter
	def featureLines(self):
		pass

	@property
	def id(self):
		pass
	@id.setter
	def id(self):
		pass

	@property
	def label(self):
		pass
	@label.setter
	def label(self):
		pass

	@property
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def radius(self):
		pass
	@radius.setter
	def radius(self):
		pass

	def reverse(self):
		"""
		Method to reverse the direction of SectionCut.
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		Method to set the SectionCut attributes.
        
        :param kwargs: attributes
        :type kwargs: dict
        
		"""
		pass

	@property
	def showColor(self):
		pass
	@showColor.setter
	def showColor(self):
		pass

	@property
	def sphere(self):
		pass
	@sphere.setter
	def sphere(self):
		pass

	@property
	def thickness(self):
		pass
	@thickness.setter
	def thickness(self):
		pass

	@property
	def transparency(self):
		pass
	@transparency.setter
	def transparency(self):
		pass

	@property
	def visibility(self):
		pass
	@visibility.setter
	def visibility(self):
		pass

	@property
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class Union:
	def __init__(self,*args, **kwds):
		"""
Internal indicator of special typing constructs.
    See _doc instance attribute for specific docs.
    
"""
		pass

def abstractmethod(funcobj):
	"""
A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass="ABCMeta"):
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    
"""
	pass

class co:
	pass

class collection:
	pass

class config_map:
	"""
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
"""
	pass

class ent:
	pass

class entity:
	pass

class enum:
	pass

class export:
	pass

class ffont:
	pass

class filter:
	pass

class fit:
	pass

class hw:
	pass

class hwi:
	pass

def isin(element, test_elements, assume_unique=False, invert=False):
	"""

    Calculates `element in test_elements`, broadcasting over `element` only.
    Returns a boolean array of the same shape as `element` that is True
    where an element of `element` is in `test_elements` and False otherwise.

    Parameters
    ----------
    element : array_like
        Input array.
    test_elements : array_like
        The values against which to test each value of `element`.
        This argument is flattened if it is an array or array_like.
        See notes for behavior with non-array-like parameters.
    assume_unique : bool, optional
        If True, the input arrays are both assumed to be unique, which
        can speed up the calculation.  Default is False.
    invert : bool, optional
        If True, the values in the returned array are inverted, as if
        calculating `element not in test_elements`. Default is False.
        ``np.isin(a, b, invert=True)`` is equivalent to (but faster
        than) ``np.invert(np.isin(a, b))``.

    Returns
    -------
    isin : ndarray, bool
        Has the same shape as `element`. The values `element[isin]`
        are in `test_elements`.

    See Also
    --------
    in1d                  : Flattened version of this function.
    numpy.lib.arraysetops : Module with a number of other functions for
                            performing set operations on arrays.

    Notes
    -----

    `isin` is an element-wise function version of the python keyword `in`.
    ``isin(a, b)`` is roughly equivalent to
    ``np.array([item in b for item in a])`` if `a` and `b` are 1-D sequences.

    `element` and `test_elements` are converted to arrays if they are not
    already. If `test_elements` is a set (or other non-sequence collection)
    it will be converted to an object array with one element, rather than an
    array of the values contained in `test_elements`. This is a consequence
    of the `array` constructor's way of handling non-sequence collections.
    Converting the set to a list usually gives the desired behavior.

    .. versionadded:: 1.13.0

    Examples
    --------
    >>> element = 2*np.arange(4).reshape((2, 2))
    >>> element
    array([[0, 2],
           [4, 6]])
    >>> test_elements = [1, 2, 4, 8]
    >>> mask = np.isin(element, test_elements)
    >>> mask
    array([[False,  True],
           [ True, False]])
    >>> element[mask]
    array([2, 4])

    The indices of the matched values can be obtained with `nonzero`:

    >>> np.nonzero(mask)
    (array([0, 1]), array([1, 0]))

    The test can also be inverted:

    >>> mask = np.isin(element, test_elements, invert=True)
    >>> mask
    array([[ True, False],
           [False,  True]])
    >>> element[mask]
    array([0, 6])

    Because of how `array` handles sets, the following does not
    work as expected:

    >>> test_set = {1, 2, 4, 8}
    >>> np.isin(element, test_set)
    array([[False, False],
           [False, False]])

    Casting the set to a list gives the expected result:

    >>> np.isin(element, list(test_set))
    array([[False,  True],
           [ True, False]])
    
"""
	pass

class legend:
	pass

class legendscalar:
	pass

class legendtensor:
	pass

class legendvector:
	pass

class mod:
	pass

class model:
	pass

class note:
	pass

class notehelper:
	pass

class noteheper:
	pass

class np:
	"""

NumPy
=====

Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://www.scipy.org>`_.

We recommend exploring the docstrings using
`IPython <https://ipython.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.

The docstring examples assume that `numpy` has been imported as `np`::

  >>> import numpy as np

Code snippets are indicated by three greater-than signs::

  >>> x = 42
  >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring::

  >>> help(np.sort)
  ... # doctest: +SKIP

For some objects, ``np.info(obj)`` may provide additional help.  This is
particularly true if you see the line "Help on ufunc object:" at the top
of the help() page.  Ufuncs are implemented in C, not Python, for speed.
The native Python help() does not know how to view their help, but our
np.info() function does.

To search for documents containing a keyword, do::

  >>> np.lookfor('keyword')
  ... # doctest: +SKIP

General-purpose documents like a glossary and help on the basic concepts
of numpy are available under the ``doc`` sub-module::

  >>> from numpy import doc
  >>> help(doc)
  ... # doctest: +SKIP

Available subpackages
---------------------
doc
    Topical documentation on broadcasting, indexing, etc.
lib
    Basic functions used by several sub-packages.
random
    Core Random Tools
linalg
    Core Linear Algebra Tools
fft
    Core FFT routines
polynomial
    Polynomial tools
testing
    NumPy testing tools
f2py
    Fortran to Python Interface Generator.
distutils
    Enhancements to distutils with support for
    Fortran compilers support and more.

Utilities
---------
test
    Run numpy unittests
show_config
    Show numpy build configuration
dual
    Overwrite certain functions with high-performance SciPy tools.
    Note: `numpy.dual` is deprecated.  Use the functions from NumPy or Scipy
    directly instead of importing them from `numpy.dual`.
matlib
    Make everything matrices.
__version__
    NumPy version string

Viewing documentation using IPython
-----------------------------------
Start IPython with the NumPy profile (``ipython -p numpy``), which will
import `numpy` under the alias `np`.  Then, use the ``cpaste`` command to
paste examples into the shell.  To see which functions are available in
`numpy`, type ``np.<TAB>`` (where ``<TAB>`` refers to the TAB key), or use
``np.*cos*?<ENTER>`` (where ``<ENTER>`` refers to the ENTER key) to narrow
down the list.  To view the docstring for a function, use
``np.cos?<ENTER>`` (to view the docstring) and ``np.cos??<ENTER>`` (to view
the source code).

Copies vs. in-place operation
-----------------------------
Most of the functions in `numpy` return a copy of the array argument
(e.g., `np.sort`).  In-place versions of these functions are often
available as array methods, i.e. ``x = np.array([1,2,3]); x.sort()``.
Exceptions to this rule are documented.


"""
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

class pg:
	pass

class rd:
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

class res:
	pass

class result:
	pass

class resultdefinition:
	pass

class resultdefinitioniso:
	pass

class resultdefinitionscalar:
	pass

class resultdefinitiontensor:
	pass

class resultdefinitionvector:
	pass

class resultdisplayiso:
	pass

class sectioncut:
	pass

class sectioncutplanar:
	pass

class sectioncutspherical:
	pass

class sess:
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

class win:
	pass

