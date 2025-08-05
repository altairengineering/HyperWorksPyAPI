from typing import TypeVar

class numpy_module:
	class ndarray:
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
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
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
	def captionposition(self):
		pass
	@captionposition.setter
	def captionposition(self):
		pass

	@property
	def crop(self):
		pass
	@crop.setter
	def crop(self):
		pass

	@property
	def ensureFit(self):
		pass
	@ensureFit.setter
	def ensureFit(self):
		pass

	@property
	def format(self):
		pass
	@format.setter
	def format(self):
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
	def previewImage(self):
		pass
	@previewImage.setter
	def previewImage(self):
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

	def setSteplistH3D(self):
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

    Layout class creates a layout object.
    
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

class MsBulletType:
	def __init__(self,value, names=None, module=None, qualname=None, type=None, start=1):
		"""
An enumeration.
"""
		pass

class PARAGRAPH_ALIGN:
	def __init__(self,value, names=None, module=None, qualname=None, type=None, start=1):
		"""
An enumeration.
"""
		pass

class Paragraph:
	def __init__(self,parent=None, name: str = None, **kwargs):
		"""

    Class representing a Paragraph object. Each paragraph object represents text or a block of different texts formats inserted in a paragraph. 
    Existing paragraph can be fetched using getParagraph method of a Text object.
    New paragraph can be created/added with Text object as parent. 

    :param parent: Parent of this paragraph. 
    :type parent: Text 
    :param name: Name of this Paragraph. Optional
    :type name: str
    
"""
		pass

	def addRun(self,text:str|None=" ", equation: str|None = None,font_name:str|None=" ", font_size: int|None = 9, font_color: list[int]|None =[0, 0, 0], bold: bool|None = False, italic: bool|None = False, underline: bool|None = False, line_break: bool|None = False, tab_space: bool|None = False,image_path:str|None=" ",hyperlink:str|None=" ", image_stream: numpy_module.ndarray|None = None):
		"""
		
        Method to add a Run object (text) in the current Paragraph object. 

        :param text: New run text. 
        :type text: str 

        :param equation: New run equation. 
        :type equation: str 

        :param font_name: New run font name 
        :type font_name: str 

        :param font_size: New run font size. 
        :type font_size: int 

        :param font_color: New run font color. 
        :type font_color: List[int] 

        :param bold: New run bold status. 
        :type bold: bool 

        :param italic: New run italic status. 
        :type italic: bool 

        :param underline: New run underline status. 
        :type underline: bool 

        :param line_break: New run linebreak status. 
        :type line_break: bool 

        :param tab_space: New run tabspace status. 
        :type tab_space: bool 

        :param image_path: New run image path. 
        :type image_path: str 

        :param hyperlink: New run hyperlink. 
        :type hyperlink: str 

        :param image_stream: New run image stream. 
        :type image_stream: numpy.ndarray
        
		"""
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def bulletLevel(self):
		pass
	@bulletLevel.setter
	def bulletLevel(self):
		pass

	@property
	def bulletStyle(self):
		pass
	@bulletStyle.setter
	def bulletStyle(self):
		pass

	@property
	def bulletType(self):
		pass
	@bulletType.setter
	def bulletType(self):
		pass

	def getRun(self,index: int = 0):
		"""
		
        Return run or equation object present at 'index' in the paragraph.
        
        :param index: Index of run in paragraph.
        :type index: int
        
        :return: Run or Equation object.
        :rtype: Run or Equation
        
		"""
		pass

	@property
	def lineBreak(self):
		pass
	@lineBreak.setter
	def lineBreak(self):
		pass

	@property
	def lineSpacing(self):
		pass
	@lineSpacing.setter
	def lineSpacing(self):
		pass

	def removeRun(self,index: int):
		"""
		
        Method to remove run or equation object present at 'index' in the paragraph.
        
        :param index: Index of run or equation in paragraph.
        :type index: int
        
		"""
		pass

	def setAttributes(self,**kwargs):
		"""
		
        Method to set multiple attributes.

        :param kwargs: Valid keywords are alignment, bulletLevel, bulletStyle, bulletType, lineBreak, lineSpacing, spaceAfter, spaceBefore, text
        :type kwargs: dict
        
		"""
		pass

	@property
	def spaceAfter(self):
		pass
	@spaceAfter.setter
	def spaceAfter(self):
		pass

	@property
	def spaceBefore(self):
		pass
	@spaceBefore.setter
	def spaceBefore(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

class PpBulletCharStyle:
	def __init__(self,value, names=None, module=None, qualname=None, type=None, start=1):
		"""
An enumeration.
"""
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

	def saveAsHTML(self,path=None, outputtemplate: str="", open=False, **kwargs):
		"""
		
        Method to export presentation report as HTML.  

        :param path: Path of the exported presentation 
        :type index: str 

        :param outputtemplate: Path of output html template (layout). 
        :type outputtemplate: str 

        :param open: Flag to open or not the exported HTML. 
        :type open: bool 

        :return: Export result and exported filepath 
        :rtype: HwxReportResult and str 
        
		"""
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
        :param kwargs: Valid keywords are range, mode, open and newname.
        :type kwargs: dict
        
        :return: Export result and exported filepath
        :rtype: HwxReportResult, str
        
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

	@property
	def templateHTML(self):
		pass
	@templateHTML.setter
	def templateHTML(self):
		pass

	def update(self,val=None):
		"""
		
        Method to capture specific images/models based on their page and window id from GUI. 
        By default, it captures all the Image/SlideImage objects inside the presentation, in which the source is equal to 'graphic'. 

        :param val: None or List of objects to be processed in GUI capturing. If none, all children gets processed.
        :type val: list of Image | SlideImage | Slide  
        
		"""
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
		"""
		
        Method to close the report session. This method will delete the report session and destroy the model.
        
		"""
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

	@property
	def tempdir(self):
		pass
	@tempdir.setter
	def tempdir(self):
		pass

class Run:
	def __init__(self,parent, **kwargs):
		"""

    Class representing a Run object. 
    Existing Run can be fetched using getRun method of a Paragraph object.
    New Run can be created/added with Paragraph object as parent. 
    
    :param parent: Parent of this run. 
    :type parent: Paragraph 
    
"""
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
	def runImagePath(self):
		pass
	@runImagePath.setter
	def runImagePath(self):
		pass

	@property
	def runImageStream(self):
		pass
	@runImageStream.setter
	def runImageStream(self):
		pass

	@property
	def runText(self):
		pass
	@runText.setter
	def runText(self):
		pass

	@property
	def tabSpace(self):
		pass
	@tabSpace.setter
	def tabSpace(self):
		pass

	@property
	def underline(self):
		pass
	@underline.setter
	def underline(self):
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

	@property
	def cssclassidHTML(self):
		pass
	@cssclassidHTML.setter
	def cssclassidHTML(self):
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

    SlideImage creates reference of already existing image (existing image is an Image object). This means any property value changes made in image get reflected in SlideImage.

    If any changes need to be made to 'SlideImage', create copy of image and then update the changes. So that, original image remains unchanged.
    
    :param slide: Parent of this slide image.
    :type slide: Slide
    :param image: Reference of this image gets created.
    :type image: Image
    :param location: Position and dimension information for image as a location object or a list in [x, y, width, height] format.
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
	def crop(self):
		pass
	@crop.setter
	def crop(self):
		pass

	@property
	def format(self):
		pass
	@format.setter
	def format(self):
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

	def setSteplistH3D(self):
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

    SlideTable creates reference of already existing table (existing table is a Table object). This means, any property value changes made in table, gets reflected in SlideTable.

    If any changes need to be made to 'SlideTable', copy of table gets created and then update the changes. So that, original table remains unchanged.    

    :param slide: Parent of this slide table.
    :type slide: Slide
    :param table: Reference of this table gets created.
    :type table: Table
    :param location: Position and dimension information for table as a location object or a list in [x, y, width, height] format.
    :type location: Location | list
    
"""
		pass

	@property
	def autoSortHTML(self):
		pass
	@autoSortHTML.setter
	def autoSortHTML(self):
		pass

	@property
	def autoToolTipHTML(self):
		pass
	@autoToolTipHTML.setter
	def autoToolTipHTML(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def captionposition(self):
		pass
	@captionposition.setter
	def captionposition(self):
		pass

	@property
	def columnColorGradient(self):
		pass
	@columnColorGradient.setter
	def columnColorGradient(self):
		pass

	@property
	def csvFile(self):
		pass
	@csvFile.setter
	def csvFile(self):
		pass

	@property
	def filterTypeHTML(self):
		pass
	@filterTypeHTML.setter
	def filterTypeHTML(self):
		pass

	@property
	def fontsize(self):
		pass
	@fontsize.setter
	def fontsize(self):
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
	def rowColorGradient(self):
		pass
	@rowColorGradient.setter
	def rowColorGradient(self):
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

        :param kwargs: Valid keywords are name, csvFile, caption, splitAuto, splitMaxRows, splitMaxColumns, position, x, y, width, and height.
        :type kwargs: dict
        
		"""
		pass

	def setColumnColor(self,index: int = 0, color: str =[0, 0, 0]):
		"""
		
        Method to set the color of a column in the table.
        Only for HTML export.

        :param index: The index of the column.
        :type index: int
        :param color: The color of the column in RGB format.
        :type color: list
        
		"""
		pass

	def setExportRange(self):
		pass

	def setRowColor(self,index: int = 0, color: str =[0, 0, 0]):
		"""
		
        Method to set the color of a row in the table.
        Only for HTML export.

        :param index: The index of the row.
        :type index: int
        :param color: The color of the row in RGB format.
        :type color: list
        
		"""
		pass

	@property
	def splitAuto(self):
		pass
	@splitAuto.setter
	def splitAuto(self):
		pass

	@property
	def splitMaxColumns(self):
		pass
	@splitMaxColumns.setter
	def splitMaxColumns(self):
		pass

	@property
	def splitMaxRows(self):
		pass
	@splitMaxRows.setter
	def splitMaxRows(self):
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

    SlideText creates reference of already existing text (existing text is a Text object). This means, any property value changes made in text, gets reflected in SlideText.

    If any changes need to be made to 'SlideText', copy of text gets created and then update the changes. So that, original text remains unchanged.   
    
    :param slide: Parent of this slide text.
    :type slide: Slide
    :param text: Reference of this text gets created.
    :type text: Text
    :param location: Position and dimension information for table as a location object or a list in [x, y, width, height] format.
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
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def autoSortHTML(self):
		pass
	@autoSortHTML.setter
	def autoSortHTML(self):
		pass

	@property
	def autoToolTipHTML(self):
		pass
	@autoToolTipHTML.setter
	def autoToolTipHTML(self):
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

	@property
	def captionposition(self):
		pass
	@captionposition.setter
	def captionposition(self):
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
	def columnColorGradient(self):
		pass
	@columnColorGradient.setter
	def columnColorGradient(self):
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
	def filterTypeHTML(self):
		pass
	@filterTypeHTML.setter
	def filterTypeHTML(self):
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
	def rowColorGradient(self):
		pass
	@rowColorGradient.setter
	def rowColorGradient(self):
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
        :param value: Cell value
        :type value: str|int|float
        
		"""
		pass

	def setColumnColor(self,index: int = 0, color: list =[0, 0, 0]):
		"""
		
        Method to set column color.
        Only for HTML export.
        
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

	def setExportRange(self,row_start: int, col_start: int, row_end: int, col_end: int):
		"""
		
        Method to select cell range of table to export.
        
        :param row_start: Start row index. Starts from 0.
        :type row_start: int
        :param col_start: Start column index. Starts from 0.
        :type col_start: int
        :param row_end: End row index.
        :type row_end: int
        :param col_end: End column index.
        :type col_end: int
        
		"""
		pass

	def setRowColor(self,index: int = 0, color: list =[0, 0, 0]):
		"""
		
        Method to set row color.
        Only for HTML export.
        
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
	def splitAuto(self):
		pass
	@splitAuto.setter
	def splitAuto(self):
		pass

	@property
	def splitMaxColumns(self):
		pass
	@splitMaxColumns.setter
	def splitMaxColumns(self):
		pass

	@property
	def splitMaxRows(self):
		pass
	@splitMaxRows.setter
	def splitMaxRows(self):
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

class backgroundColor:
	"""

        Flag to set the cell background color.

        :getter: Gets the RGB list of background
        :setter: Sets the RGB list of background
        :type: List[int]
        
"""
	pass

class boldFont:
	"""

        Flag to activate or deactivate the cell text bold status.

        :getter: Gets the bold status of cell text
        :setter: Sets the bold status of cell text
        :type: bool
        
"""
	pass

class fontName:
	"""

        Flag to get/set font name of cell text content.
        
        :getter: Gets the font name
        :setter: Sets the font name
        :type: str
        
"""
	pass

class fontSize:
	"""

        Flag to get/set the font size of cell text.

        :getter: Gets the font size
        :setter: Sets the font size
        :type: int
        
"""
	pass

def getColumnIndex(self):
	"""

        Method to get column index of the cell.
        
        :return: Column index
        :rtype: int
        
"""
	pass

def getRowIndex(self):
	"""

        Method to get row index of the cell.
        
        :return: Row index
        :rtype: int
        
"""
	pass

def getValue(self):
	"""

        Method to get text content of the cell.
        
        :return: Cell text content
        :rtype: str|int|float
        
"""
	pass

def horizontalAlignment():
	"""

        Flag to get/set the horizontal alignment of cell content. Valid values are 'none', 'left', 'center', 'right'.

        :getter: Gets horizontal alignment of cell.
        :setter: Sets horizontal alignment of cell
        :type: str
        
"""
	pass

def italicFont():
	"""

        Flag to activate or deactivate the cell text italics status.

        :getter: Gets italics status of cell text
        :setter: Sets italics status of cell text
        :type: bool
        
"""
	pass

def setAttributes(**kwargs):
	"""

        Method to set multiple attributes.

        :param kwargs: Valid keywords are backgroundColor, horizontalAlignment, verticalAlign, fontName, textColor, fontSize, boldFont, italicFont, underline, backgroundColor.
        :type kwargs: dict
        
"""
	pass

def setValue(text=None, imagepath=None, hyperlink=None):
	"""

        Method to set cell value which can be either text or image.
        Hyperlink can be set for both text and image.
        If text is an equation, then hyperlink is not supported.
        
        :param text: Cell text content
        :type text: str
        :param imagepath: Image path
        :type imagepath: str
        :param hyperlink: Hyperlink path
        :type hyperlink: str
        
"""
	pass

def textColor():
	"""

        Flag to set/get text color of cell text.
        
        :getter: Gets the RGB list of text color
        :setter: Sets the RGB list of text color
        :type: List[int]
        
"""
	pass

def underline():
	"""

        Flag to activate or deactivate the cell text undeline status.

        :getter: Gets underline status of cell text
        :setter: Sets underline status of cell text
        :type: bool
        
"""
	pass

def verticalAlignment():
	"""

        Flag to get/set the vertical alignment of cell content. Valid values are 'none', 'bottom', 'center', 'top', 'mixed'. 

        :getter: Gets the cell vertical alignment
        :setter: Sets the cell vertical alignment
        :type: str
        
"""
	pass

