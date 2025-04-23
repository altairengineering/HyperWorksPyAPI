from typing import TypeVar

class Chapter:
	def __init__(self,name=None, parent=None, **kwargs):
		"""

    Chapter class creates new chapter object as a child of either a document or and other chapter.
    
    If 'name' value is None, creates new chapter with unique name.
    
    If 'name' value is not None and no entity of same name exists in the specified report session, new chapter gets created with the given name.
    
    If 'name' value is not None and entity of same name exists in the specified session, an error is returned.
    
    :param name: The chapter name.
    :type name: str
    
    :param parent: Parent of this chapter.
    :type parent: Document | Chapter
    
"""
		pass

	def getChildren(self,childrenLevel="0", type=[], name=None):
		"""
		
        Returns children of this document as list. 
        
        :param childrenLevel:

            0 - Returns only direct children of this document. (default)

            1 - Returns children and immediate grand-children of this document. Based on level value, returns all children until that level.

            -1 - Returns all children until last level.
            
            It also takes string as input. Valid values are:
            
            'current' - Returns only direct children of this document.

            'next' - Returns children and immediate grand-children of this document.

            'all' - Returns all children until that last level.

        :type childrenLevel: str | int
        
        :param type: Filters children based on type. By default, no filter is applied. Valid values are 'DocImage', 'DocTable', 'DocText', 'Chapter'. Default is empty list.
        :type type: list
        
        :return: List of children of this document.
        :rtype: list
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

class DocImage:
	def __init__(self,*args, **kwargs):
		"""

    DocImage class constructor can create both new image entity or a reference to an existing image entity present in the library.

    In case of a reference, any property changes made on the library image will be reflected in all references. If any changes need to be made to a DocImage, a copy of image gets created and the changes are applied to the copy so the original remains unchanged.
    
    If the specified name does not exists in the report session, a new image/reference is created with given name.

    If the specified name exists in the active report session, an error is returned.
    
    :param parent: Parent of the image
    :type parent: Document | Chapter
    :param image: If type is 'Image', reference-image gets created. If type is 'str' or 'numpy-ndarray', a new image gets created.
    :type image: Image | str | numpy-ndarray
    :param name: Unique name for the image
    :type name: str
    
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
	def page(self):
		pass
	@page.setter
	def page(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def path(self):
		pass
	@path.setter
	def path(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Set multiple attributes.

        :param kwargs: Valid keywords are name, caption, source, width, height, page, window, and binarydata.
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
	def window(self):
		pass
	@window.setter
	def window(self):
		pass

class DocTable:
	def __init__(self,*args, **kwargs):
		"""

    DocTable class can create both a new table entity or a reference to an existing table entity present in the library.

    In case of reference, any property value changes made in library table, it will reflect in all references.
    Also in case of reference entity, if any changes need to be made to 'DocTable', copy of table gets created and then update the changes. So that, original table remains unchanged.
    
    If 'name' does not exists in report session, then new table/reference gets created with given name.

    If 'name' exists in active report-session, then error thrown.
    
    :param parent: Parent of this table.
    :type parent: Document | Chapter
    :param table: If type is 'Table', reference-table gets created. If type is csv-filepath, new table gets created.
    :type table: Table | str
    :param name: Unique name for this table
    :type name: str
    
"""
		pass

	def addColumn(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	def cell(self):
		pass

	@property
	def columns(self):
		pass
	@columns.setter
	def columns(self):
		pass

	def exportCsv(self,file: str):
		"""
		
        Method to export table data to a CSV file.
        
        :param file: The CSV file path.
        :type file: str
        
		"""
		pass

	@property
	def file(self):
		pass
	@file.setter
	def file(self):
		pass

	def getCellValue(self,row: int, col: int):
		"""
		
        Method to get a cell value.
        
        :param row: Row index
        :type row: int
        :param col: Column index
        :type col: int
        
        :return: Cell value
        :rtype: hwVariant
        
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	def mergeCells(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def removeColumn(self):
		pass

	def removeRow(self):
		pass

	@property
	def rows(self):
		pass
	@rows.setter
	def rows(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are name, caption, source, file, width, and height.
        :type kwargs: dict
        
		"""
		pass

	def setCellValue(self):
		pass

	def setColumnWidth(self):
		pass

	def setDT(self):
		pass

	def setDimension(self):
		pass

	def setRowHeight(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class DocText:
	def __init__(self,*args, **kwargs):
		"""

    DocText class can create both new text entity or reference to existing text entity present in the library.

    In case of a reference, any property value changes made in library text will reflect in all references.

    In case of a reference entity, if any changes need to be made to 'DocText', a copy of text gets created and then changes are applied so the original text remains unchanged.
    
    If 'name' does not exists in report session, a new text or reference gets created with the given name.

    If 'name' exists in active report-session, an error is returned.
    
    :param parent: Parent of this text.
    :type parent: Document | Chapter
    :param text: If type is 'Text', reference-text gets created. If type is 'str', new text gets created.
    :type text: Text | str
    :param name: Unique name for this text
    :type name: str
    
"""
		pass

	def addFormatedText(self):
		pass

	def addImage(self):
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def boldFont(self):
		pass
	@boldFont.setter
	def boldFont(self):
		pass

	@property
	def fontColor(self):
		pass
	@fontColor.setter
	def fontColor(self):
		pass

	@property
	def fontName(self):
		pass
	@fontName.setter
	def fontName(self):
		pass

	@property
	def fontSize(self):
		pass
	@fontSize.setter
	def fontSize(self):
		pass

	@property
	def hyperLink(self):
		pass
	@hyperLink.setter
	def hyperLink(self):
		pass

	@property
	def italicFont(self):
		pass
	@italicFont.setter
	def italicFont(self):
		pass

	@property
	def lineBreak(self):
		pass
	@lineBreak.setter
	def lineBreak(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are name, fontName, fontColor, fontSize, boldFont, italicFont, underline, lineBreak, tabSpace, hyperLink, textcontent, and alignment.
        :type kwargs: dict
        
		"""
		pass

	@property
	def tabSpace(self):
		pass
	@tabSpace.setter
	def tabSpace(self):
		pass

	@property
	def textcontent(self):
		pass
	@textcontent.setter
	def textcontent(self):
		pass

	@property
	def underline(self):
		pass
	@underline.setter
	def underline(self):
		pass

class Document:
	def __init__(self,name=None, **kwargs):
		"""

    Document class creates document object under Report object.
    
    If 'name' value is None, creates new document with unique name.
    
    If 'name' value is not None and no entity of same name exists in specified report session, a new image gets created with given name.
    
    If 'name' value is not None and any entity of same name exists in specified session, an error is returned.
    
    :param name: Document name
    :type name: str
    
"""
		pass

	def getChildren(self,childrenLevel="0", type=[], name=None):
		"""
		
        Returns children of this document as list. 
        
        :param childrenLevel:
            0 - Returns only direct children of this document. (default)

            1 - Returns children and immediate grand-children of this document. Based on level value, returns all children until that level.

            -1 - Returns all children until last level.
            
            It also takes string as input:

            'current' - Returns only direct children of this document.

            'next' - Returns children and immediate grand-children of this document.

            'all' - Returns all children until that last level.

        :type childrenLevel: str | integer
        
        :param type: Filters children based on type. By default, no filter is applied. Valid values are 'DocImage', 'DocTable', 'DocText', 'Chapter'. Default is empty list.

        :type type: list
        
        :return: Return list of children of this document.
        :rtype: list
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def saveAsHTML(self,path, open=False):
		"""
		
        Saves output as HTML file.
        
        :param path: File path for HTML file.
        :type path: str
        :param open: Opens file after creation (default False)
        :type open: bool
        
		"""
		pass

	def saveDocx(self,path=None, **kwargs):
		"""
		
        Save output document file
        
        :param path: Generated document file path
        :type path: str
        :param kwargs: Possible keys are open, mode
        :type kwargs: dict
        
		"""
		pass

	def savePDF(self,path=None, **kwargs):
		"""
		
        Method to save a PDF file.
        
        :param path: Generated PDF file path
        :type path: str
        :param kwargs: Valid keyword is open.
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
		
        Set multiple attributes

        :param kwargs: Valid keywords are name, template
        :type kwargs: dict
        
		"""
		pass

	@property
	def template(self):
		pass
	@template.setter
	def template(self):
		pass

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

