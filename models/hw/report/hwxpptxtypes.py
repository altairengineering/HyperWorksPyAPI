from typing import TypeVar

class Image:
	def __init__(self,name=None, **kwargs):
		"""

    Image class creates new image entity
    
    If 'name' value is None, creates new image with unique name.

    If 'name' value is not None and session of 'name' does not exists, then new image gets created with given name.
    
    If 'name' value is not None and session of 'name' exists, then error thrown.
    
    :param name: Image name.
    :type name: str
    :param session: Session name. If not specified, uses currently active report session name
    :type session: str
    :param path: Source image file path.
    :type path: str
    :param source: Valid values are 'graphic' and 'file' (default).
    :type source: str
    
"""
		pass

	@property
	def binarydata(self):
		pass
	@binarydata.setter
	def binarydata(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def ensureFit(self):
		pass
	@ensureFit.setter
	def ensureFit(self):
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
	def path(self):
		pass
	@path.setter
	def path(self):
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.
        
        :param kwargs: Valid keywords are name, source, type, path, caption, page, and window.
        :type kwargs: dict
        
		"""
		pass

	@property
	def source(self):
		pass
	@source.setter
	def source(self):
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

class Layout:
	def __init__(self,name=None, **kwargs):
		"""

    Layout class creates a layout object as a child of the ReportLayout object.
    
    :param name: Layout name
    :type name: str
    
"""
		pass

	def getPlaceholderInfo(self):
		"""
		
        Method to print the placeholder details of this layout.
        
        :return: Placeholders present in this layout
        :rtype: list
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

class Location:
	def __init__(self,layout, **kwargs):
		"""

    Location class creates a placeholder object as a child of layout.
    
    :param layout: Layout object
    :type layout: Layout
    :param session: ReportSession object (optional)
    :type session: ReportSession
    
"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
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

class Presentation:
	def __init__(self,name=None, **kwargs):
		"""

    Presentation class creates a new powerpoint presentation object in specified session.

    If 'name' value is None, creates new presentation with unique name.
    
    If 'name' value is not None and no entity of same name exists in specified report session, a new presentation gets created with given name.
    
    If 'name' value is not None and entity of same name exists in specified session, an error is returned.
    
    :param name: Presentation name.
    :type name: str
    
"""
		pass

	def exportPresentationReport(self,output_path):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def resolution(self):
		pass
	@resolution.setter
	def resolution(self):
		pass

	def saveAsHTML(self,outfile, open=False):
		pass

	def savePDF(self,path=None, **kwargs):
		"""
		
        Method to save the presentation as a PDF file.
        
        :param path: The presentation file path.
        :type path: str
        :param kwargs: Valid keywords are range and open.
        :type kwargs: dict
        
		"""
		pass

	def savePPTX(self,path=None, **kwargs):
		"""
		
        Method to save the presentation as a PPTX file.
        
        :param path: The presentation file path.
        :type path: str
        :param kwargs: Valid keywords are range, mode, and open.
        :type kwargs: dict
        
		"""
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.
        
        :param kwargs: Valid keywords are name, resolution, and template.
        :type kwargs: dict
        
		"""
		pass

	def size(self,aspect_ratio):
		"""
		
        Method to set aspect ratio for all slides. Valid values are '16:9', '4:3', and '16:10'.
        
        :param aspect_ratio: Slides aspect ratio
        :type aspect_ratio: str
        
		"""
		pass

	@property
	def template(self):
		pass
	@template.setter
	def template(self):
		pass

class ReportManager:
	def __init__(self,**kwargs):
		"""

    ReportManager class can provide information about all available report sessions and the active report session.
    
"""
		pass

	@property
	def activeSession(self):
		pass
	@activeSession.setter
	def activeSession(self):
		pass

	def getAllSessionNames(self):
		"""
		
        Method to return list of all available report session names.
        
        :return: All report session names
        :rtype: list
        
		"""
		pass

class ReportSession:
	def __init__(self,name=None, **kwargs):
		"""

    ReportSession can create new report session or return an existing report session.
    
    If 'name' value is None, ReportSession can create new session with unique name.

    If 'name' value is not None and session of 'name' does not exists, then ReportSession creates new session.
    
    If 'name' value is not None and session of 'name' exists, then ReportSession returns existing session.
    
    :param value: Report session name
    :type value: str
    
"""
		pass

	@property
	def activePresentation(self):
		pass
	@activePresentation.setter
	def activePresentation(self):
		pass

	def close(self):
		pass

	def delete(self,objects):
		"""
		
        Method to delete entities from the session.
        
        :param objects: Entity object to be deleted or list of entity objects to be deleted
        :type objects: Single object or list of Table | Text | Image | Presentation | Slide | SlideImage | SlideTable | SlideText | Chapter | Document | DocImage | DocTable | DocText
        
		"""
		pass

	def get(self,entity_type, entity_name):
		"""
		
        Method to find and return an entity object based on entity type and name. If not found, returns None.
        
        :param entity_type: Entity class type
        :type entity_type: Table | Text | Image | Presentation | Slide | SlideImage | SlideTable | SlideText | Chapter | Document
        :param entity_name: Name of entity to be found
        :type entity_name: str
        
        :return: Report entity object
        :rtype: Table | Text | Image | Presentation | Slide | SlideImage | SlideTable | SlideText | Chapter | Document
        
		"""
		pass

	def getLayouts(self,output_type=None):
		"""
		
        Method to return all layout objects or layout names in the session. 
        
        :param output_type: Valid values are 'name' and None.
        :type output_type: str | None
        
        :return: List of layout names or layout objects
        :rtype: list
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def paste(self,paste_objects, destination):
		"""
		
        Method to copy entities and create new entities in the destination.
        
        :param paste_objects: Entity object to be pasted or list of entity objects to be pasted
        :type paste_objects: Single object or list of DocImage | DocTable | DocText
        :param destination: Destination object where entity will be pasted
        :type destination: Document | Chapter
        
		"""
		pass

	def reset(self):
		"""
		
        Method to delete all entities present in the report session.
        
		"""
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

class Slide:
	def __init__(self,name=None, presentation=None, **kwargs):
		"""

    Slide class creates slide object as child of presentation.

    If 'name' value is None, creates new slide with unique name.
    
    If 'name' value is not None and no entity of same name exists in specified report session, a new slide gets created with given name.
    
    If 'name' value is not None and any entity of same name exists in specified session, an error is returned.
    
    :param name: Slide name
    :type name: str
    :param presentation: Presentation object. If not specified, the active presentation is used.
    :type presentation: Presentation
    
"""
		pass

	def add(self,obj, name, position=None):
		"""
		
        Method to add a text, image, or table as a child of the slide.
        
        :param obj: The object to clone as a slide child
        :type obj: Text | Image | Table object
        :param name: Name of the entity to be created. It should be unique name in the active session.
        :type name: str
        :param position: Position and dimension for the new object. Can be defined as a location object, a list of values in [x, y, width, height] format, or as a placeholder name.
        :type position: Location | list | str
        
		"""
		pass

	def applySlidePlaceholderList(self,index):
		"""
		
        Method to enable the slide to use placeholder information of slide available at 'index' in presentation.
        
        :param index: Slide index
        :type index: int
        
		"""
		pass

	def layout(self,value):
		"""
		
        Method to set the slide layout.
        
        :param value: Layout name
        :type value: str
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def presentation(self):
		pass
	@presentation.setter
	def presentation(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are name and titleText.
        :type kwargs: dict
        
		"""
		pass

	def titlePosition(self,x, y, width, height):
		"""
		
        Method to set title position for slide title.

        :param x: Title x position
        :type x: int
        :param y: Title y position
        :type y: int
        :param width: Title width
        :type width: int
        :param height: Title height
        :type height: int
        
		"""
		pass

	@property
	def titleText(self):
		pass
	@titleText.setter
	def titleText(self):
		pass

class SlideImage:
	def __init__(self,**kwargs):
		"""

    SlideImage creates reference of already existing image (parent of existing image is ReportPalette object). This means any property value changes made in palette image get reflected in SlideImage.

    If any changes need to be made to 'SlideImage', create copy of image and then update the changes. So that, original image remains unchanged.
    
    :param slide: Parent of this slide image.
    :type slide: Slide
    :param image: Reference of this image gets created
    :type image: Image
    :param location: Position and dimension information for image as a location object or a list in [x, y, width, height] format
    :type location: Location | list
    
"""
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def path(self):
		pass
	@path.setter
	def path(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are name, source, type, path, caption, position, x, y, width, and height.
        :type kwargs: dict
        
		"""
		pass

	@property
	def source(self):
		pass
	@source.setter
	def source(self):
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

class SlideLocation:
	def __init__(self,**kwargs):
		"""

    Base class for SlideImage, SlideText, and SlideTable.
    
"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def setAttributes(self,key, value):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are position, x, y, width, and height.
        :type kwargs: dict
        
		"""
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
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

class SlideTable:
	def __init__(self,**kwargs):
		"""

    SlideTable creates reference of already existing table (parent of existing table is ReportPalette object). This means, any property value changes made in palette table, gets reflected in SlideTable.

    If any changes need to be made to 'SlideTable', copy of table gets created and then update the changes. So that, original table remains unchanged.
    
    :param slide: Parent of this slide table.
    :type slide: Slide
    :param table: Reference of this table gets created
    :type table: Table
    :param location: Position and dimension information for table as a location object or a list in [x, y, width, height] format
    :type location: Location | list
    
"""
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def csvFile(self):
		pass
	@csvFile.setter
	def csvFile(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def maxColumns(self):
		pass
	@maxColumns.setter
	def maxColumns(self):
		pass

	@property
	def maxRows(self):
		pass
	@maxRows.setter
	def maxRows(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are name, csvFile, caption, split, splitBy, maxRows, maxColumns, position, x, y, width, and height.
        :type kwargs: dict
        
		"""
		pass

	@property
	def split(self):
		pass
	@split.setter
	def split(self):
		pass

	@property
	def splitBy(self):
		pass
	@splitBy.setter
	def splitBy(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
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

class SlideText:
	def __init__(self,**kwargs):
		"""

    SlideText creates reference of already existing text (Parent of existing text is ReportPalette object). This means, any property value changes made in palette text, gets reflected in SlideText.

    If any changes need to be made to 'SlideText', copy of text gets created and then update the changes. So that, original text remains unchanged
    
    :param slide: Parent of this slide text.
    :type slide: Slide
    :param text: Reference of this text gets created
    :type text: Text
    :param location: Position and dimension information for table as a location object or a list in [x, y, width, height] format
    :type location: Location | list
    
"""
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are name, text, position, x, y, width, height, and alignment.
        :type kwargs: dict
        
		"""
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
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

class Table:
	def __init__(self,name=None, **kwargs):
		"""

    Table class creates table entity.
    
    If 'name' value is None, creates new table with unique name.
    
    If 'name' value is not None and no entity of same name exists in specified report session, a new table gets created with given name.
    
    If 'name' value is not None and any entity of same name exists in specified session, an error is returned.
    
    :param name: Table name.
    :type name: str
    :param session: Session name. If not specified, uses currently active report session name.
    :type session: ReportSession
    :param datafile: CSV file path.
    :type datafile: str
    
"""
		pass

	def addColumn(self):
		"""
		
        Method to add new column to table.
        
		"""
		pass

	@property
	def autoFilter(self):
		pass
	@autoFilter.setter
	def autoFilter(self):
		pass

	@property
	def autoSort(self):
		pass
	@autoSort.setter
	def autoSort(self):
		pass

	@property
	def autoToolTip(self):
		pass
	@autoToolTip.setter
	def autoToolTip(self):
		pass

	@property
	def borderVisibility(self):
		pass
	@borderVisibility.setter
	def borderVisibility(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	def cell(self,row_idx, col_idx):
		"""
		
        Method to get access to a specific cell.
        
        :param row_idx: Row index
        :type row_idx: int
        :param col_idx: Column index
        :type col_idx: int
        
        :return: Table cell object
        :rtype: TableCell
        
		"""
		pass

	@property
	def columns(self):
		pass
	@columns.setter
	def columns(self):
		pass

	@property
	def csvFile(self):
		pass
	@csvFile.setter
	def csvFile(self):
		pass

	@property
	def ensureFit(self):
		pass
	@ensureFit.setter
	def ensureFit(self):
		pass

	def exportCsv(self,file: str):
		"""
		
        Method to export the table content to a CSV file.
        
        :param file: CSV file path
        :type file: str
        
		"""
		pass

	@property
	def fontsize(self):
		pass
	@fontsize.setter
	def fontsize(self):
		pass

	def getCellValue(self,row: int, col: int):
		"""
		
        Method to get cell value for at particular index.
        
        :param row: Row index
        :type row: int
        :param col: Column index
        :type col: int
        
        :return: Cell value
        :rtype: hwVariant
        
		"""
		pass

	def loadCsv(self,file: str):
		"""
		
        Method to loads content of a CSV file to the table entity.
        
        :param file: CSV file path
        :type file: str
        
		"""
		pass

	@property
	def maxColumns(self):
		pass
	@maxColumns.setter
	def maxColumns(self):
		pass

	@property
	def maxRows(self):
		pass
	@maxRows.setter
	def maxRows(self):
		pass

	def mergeCells(self,cell1, cell2):
		"""
		
        Method to merge table cells.
        
        :param cell1: Cell index
        :type cell1: TableCell
        :param cell2: Cell index
        :type cell2: TableCell
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def removeColumn(self,index: int):
		"""
		
        Method to remove column at specified index.
        
        :param col: Column index
        :type col: int
        
		"""
		pass

	def removeRow(self,index: int):
		"""
		
        Method to remove row at specified index.
        
        :param row: Row index
        :type row: int
        
		"""
		pass

	@property
	def rows(self):
		pass
	@rows.setter
	def rows(self):
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.
        
        :param kwargs: Valid keywords are name, csvFile, caption, split, splitBy, maxRows, maxColumns, and stretch.
        :type kwargs: dict
        
		"""
		pass

	def setCellValue(self,row: int, col: int, value):
		"""
		
        Method to set cell value for at particular index.
        
        :param row: Row index
        :type row: int
        :param col: Column index
        :type col: int
        
		"""
		pass

	def setColumnColor(self,index: int = 0, color: list =[0, 0, 0]):
		"""
		
        Method to set column color.
        
        :param index: Column index
        :type index: int
        :param color: RGB color
        :type color: list
        
		"""
		pass

	def setColumnWidth(self,index: int, width: float):
		"""
		
        Method to set column width.
        
        :param index: Column index
        :type index: int
        :param width: Column width
        :type width: float
        
		"""
		pass

	def setDT(self,dtsession_name: str, db_name: str, dtset_name: str):
		"""
		
        Method to set DT session, database, set name and load data into table.
        
        :param dtsession_name: DT session name
        :type dtsession_name: str
        :param db_name: DTDB name
        :type db_name: str
        :param dtset_name: DT set name
        :type dtset_name: str
        
		"""
		pass

	def setDimension(self,rows: int, cols: int):
		"""
		
        Method to set number of rows and columns for table.
        
        :param rows: Row count
        :type rows: int
        :param cols: Column count
        :type cols: int
        
		"""
		pass

	def setRowColor(self,index: int = 0, color: list =[0, 0, 0]):
		"""
		
        Method to set row color.
        
        :param index: Row index
        :type index: int
        :param color: RGB color
        :type color: list
        
		"""
		pass

	def setRowHeight(self,row_index: int, height: float):
		"""
		
        Method to set row height.
        
        :param index: Row index
        :type index: int
        :param height: Row height
        :type height: float
        
		"""
		pass

	@property
	def split(self):
		pass
	@split.setter
	def split(self):
		pass

	@property
	def splitBy(self):
		pass
	@splitBy.setter
	def splitBy(self):
		pass

	@property
	def stretch(self):
		pass
	@stretch.setter
	def stretch(self):
		pass

class TableBordersVisibility:
	def __init__(self,value, names=None, module=None, qualname=None, type=None, start=1):
		"""
An enumeration.
"""
		pass

class Text:
	def __init__(self,name=None, **kwargs):
		"""

    Text class creates a new text entity.

    If 'name' value is None, creates new text with unique name.

    If 'name' value is not None and session of 'name' does not exists, then new text gets created with given name
    
    If 'name' value is not None and session of 'name' exists, then error thrown.
    
    :param name: Text entity name
    :type name: str
    :param session: Session name. If not specified, uses currently active report session name.
    :type session: ReportSession
    :param text: Text content
    :type text: str
    
"""
		pass

	def addParagraph(self):
		"""
		
        Method to add new paragraph.
        
        :return: Paragraph entity
        :rtype: Paragraph
        
		"""
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def ensureFit(self):
		pass
	@ensureFit.setter
	def ensureFit(self):
		pass

	def getParagraph(self,index: int = 0):
		"""
		
        Method to return paragraph present at 'index'.
        
        :param index: Index of paragraph in text runs
        :type index: int
        :return: Paragraph entity
        :rtype: Paragraph
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def removeParagraph(self,index: int):
		"""
		
        Method to remove paragraph present at 'index'.
        
        :param index: Index of paragraph in text runs
        :type index: int
        
		"""
		pass

	@property
	def session(self):
		pass
	@session.setter
	def session(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.
        
        :param kwargs: Valid keywords are name, text, ensureFit, and alignment.
        :type kwargs: dict
        
		"""
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

