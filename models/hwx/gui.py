from typing import TypeVar
var0=TypeVar('uiAction',str)
var1=TypeVar('uiActionList',str)
var2=TypeVar('uiWidget',str)
var3=TypeVar('char const *',str)
var4=TypeVar('uiPoint',str)
var5=TypeVar('hwTSignal',str)
var6=TypeVar('bool const',str)
var7=TypeVar('uiObject',str)
var8=TypeVar('unsigned int',str)
var9=TypeVar('uiWidget::GeomMgrStartXHintEnum',str)
var10=TypeVar('uiRect',str)
var11=TypeVar('ui::InputMethodQuery',str)
var12=TypeVar('uiStringList',str)
var13=TypeVar('hwString const &',str)
var14=TypeVar('uiPaintEvent',str)
var15=TypeVar('uiString',str)
var16=TypeVar('ui::Alignment',str)
var17=TypeVar('uiColorGroup::ColorRole',str)
var18=TypeVar('uiWidget::BadgeAlignmentEnum',str)
var19=TypeVar('hwt::Color const &',str)
var20=TypeVar('ui::ContextMenuPolicy',str)
var21=TypeVar('uiCursor',str)
var22=TypeVar('uiSize',str)
var23=TypeVar('uiPixmap',str)
var24=TypeVar('uiWidget::FocusPolicyEnum',str)
var25=TypeVar('hwt::Font const &',str)
var26=TypeVar('uiFrame::Shadow',str)
var27=TypeVar('uiFrame::Shape',str)
var28=TypeVar('uiLayout',str)
var29=TypeVar('uiBitmap',str)
var30=TypeVar('ui::BackgroundMode',str)
var31=TypeVar('uiPalette',str)
var32=TypeVar('ui::WindowModality',str)
var33=TypeVar('double',str)
var34=TypeVar('QWidget',str)
var35=TypeVar('bool *',str)
var36=TypeVar('std::vector< hwString >::value_type const &',str)
var37=TypeVar('std::vector< hwString >::size_type',str)
var38=TypeVar('_hwStringList_vector',str)
var39=TypeVar('uiModelIndex',str)
var40=TypeVar('uiPainter',str)
var41=TypeVar('uiAbstractItemView::SelectionFlag',str)
var42=TypeVar('uiAbstractItemView::DragDropModeEnum',str)
var43=TypeVar('uiAbstractItemView::EditTriggersType',str)
var44=TypeVar('uiAbstractItemDelegate',str)
var45=TypeVar('uiAbstractItemModel',str)
var46=TypeVar('uiAbstractItemView::SelectionBehaviorType',str)
var47=TypeVar('uiAbstractItemView::SelectionModeType',str)
var48=TypeVar('ui::Orientation',str)
var49=TypeVar('uiSortFilterHandler *',str)
var50=TypeVar('QModelIndex const &',str)
var51=TypeVar('Object',str)
var52=TypeVar('ObjectList',str)
var53=TypeVar('Property',str)
var54=TypeVar('VariantList',str)
var55=TypeVar('FileElement',str)
var56=TypeVar('size_t',str)
var57=TypeVar('bool const &',str)
var58=TypeVar('Variant',str)
var59=TypeVar('ObjectRenderer',str)

class Action:
	def __init__(self,parent=None,name: str="", **kwds):
		"""
GUI command used in Menus and ToolBars.

     An action contains text, icons and a command callback.
     The action can be inserted into menus and/or toolbars.
     When the menu or toolbar button is clicked the action is called.
     Actions are used in Tool Wheel. The text displayed in the Tool Wheel is
     based on the text attribute which should be passed to tr() before.

     Actions are modeled after Qts Action class. Refer to the Qt documentation
     for more information.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.

    Warning, make sure to remove the action from the ui before destroying or
    this will crash!
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def exclusive(self):
		pass
	@exclusive.setter
	def exclusive(self):
		pass

	def get(self,name):
		"""
		Returns the named action from defined in active profile.

    Args:
      name (str): Action name.
    
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def ison(self):
		pass
	@ison.setter
	def ison(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self):
		"""
		Calls command callback method when an Action is clicked.
		"""
		pass

	def onToggle(self,on):
		"""
		Acts when an Action is toggled.

      - If is coupled to dialog it will show or hide the dialog.
      - If is coupled to a context it will get in and out the context.
      - If is coupled to callback it will run the callback with state or not.

    Args:
      on (bool): Determines whether to toggle on or off.
    
		"""
		pass

	@property
	def selectable(self):
		pass
	@selectable.setter
	def selectable(self):
		pass

	@property
	def statustip(self):
		pass
	@statustip.setter
	def statustip(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	def toggle(self,on=None):
		"""
		Simulate clicking the action.
    
    Args:
      on(bool | None): Pass True/False to ensure you are toggling on or off.
        None flips the state.
    
		"""
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def whatsthis(self):
		pass
	@whatsthis.setter
	def whatsthis(self):
		pass

class ActionDialog:
	def __init__(self,action=None, children=None, **kwds):
		"""
Dialog that pops up under the specified SpriteAction.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def createContents(self):
		"""
		To be implemented in derived class.
		"""
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Get singleton when dialog is implemented as a subclass
    
      Used by associated Button/SpriteActions.
    
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def positionUnder(self,relativeTo, checkWasMoved=True, xoffset=0):
		"""
		Positions the dialog under or over the relataveTo widget.

    Args:
      relativeTo (Widget): The widget to position relative to.
      checkWasMoved (bool): Determines whether to check if widget is moved or not. 
      xoffset (int): The offset value for the widget for x-axis.
    
		"""
		pass

	def resize(self,width, height):
		"""
		Resize width/height of dialog.

    This does not prevent the user from manually resizing like setting the
    width/height does.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def title(self):
		pass
	@title.setter
	def title(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ActionGroup:
	def __init__(self,parent=None,name: str="", **kwds):
		"""
A grouping of Actions to create a cascading menu.

  ActionGroups are modeled after Qts ActionGroup class, refer to the Qt documentation 
  for more information.
  
"""
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.

    Warning, make sure to remove the action from the ui before destroying or
    this will crash!
    
		"""
		pass

	@property
	def exclusive(self):
		pass
	@exclusive.setter
	def exclusive(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

class Actions:
	"""

Contains:
  Action              - GUI command used in menus
  ActionGroup         - Group of Actions
  SpriteAction        - GUI command that is part of a SpriteActionGroup
  SpriteActionGroup   - Palette of SpriteActions
  SpriteActionCounter - SpriteAction to display an integer value
  SpriteCommand       - Syntactic sugar for a SpriteActionGroup with one
                        SpriteAction

"""
	pass

class AnimationToolbar:
	def __init__(self,parent=None, **kwds):
		"""
An AnimationToolbar Widget.

  AnimationToolbar is a widget used to display the controls for the animation.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self):
		"""
		Adds extra widgets.

    You need to call the addWidget method.
    
		"""
		pass

	def addWidget(self,widget):
		"""
		Adds a widget to the AnimationToolbar.

    Args:
      widget (Widget): The widget to be added to the layout.

    Returns:
      Widget: The added widget.
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def animatingState(self):
		pass
	@animatingState.setter
	def animatingState(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frame(self):
		pass
	@frame.setter
	def frame(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onAnimRangeEnabled(self,enabled):
		"""
		Callback method when the animation range is enabled or disabled.

    Args:
      enabled (bool): Animation range is enabled/disabled.
    
		"""
		pass

	def onAnimationRangeChange(self,start_frame, end_frame):
		"""
		Callback method when animation range has been changed.

    Args:
      start_frame (int): Starting frame number of the range.
      end_frame (int): Ending frame number of the range.
    
		"""
		pass

	def onCommand(self,event=None):
		pass

	def onFrameChange(self,frame, spontaneous):
		"""
		Callback method when animation frame changes.

    Args:
      frame (int): Frame number changed.
      spontaneous (bool): Specifies if the frame change is spontaneous.
    
		"""
		pass

	def onPause(self):
		"""
		Callback method when the animation pauses.
		"""
		pass

	def onResume(self):
		"""
		Callback method when the animation resumes.
		"""
		pass

	def onStart(self):
		"""
		Callback method when the animation starts.
		"""
		pass

	def onStop(self):
		"""
		Callback method when the animation stops.
		"""
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def resetRange(self):
		"""
		Resets the animation range.
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def timeSteps(self):
		pass
	@timeSteps.setter
	def timeSteps(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Bool:
	def __init__(self,label: str="", readOnly=False, computed=False, **kwds):
		pass

	def castForSet(self,value):
		pass

	def getProperty(self,prop, row):
		pass

	def getValue(self,row):
		pass

	def init(self,i, name):
		pass

	def setProperty(self,prop, row):
		pass

class BoxLayout:
	def __init__(self,*childrenList, **kwds):
		"""
Base class for HBoxLayout and VBoxLayout.
"""
		pass

	def addChildren(self,children):
		"""
		Adds the specified children in the BoxLayout.

    Args:
      children (list[Widget]): The items to be added.
    
		"""
		pass

	@property
	def border(self):
		pass
	@border.setter
	def border(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def resizeMode(self):
		pass
	@resizeMode.setter
	def resizeMode(self):
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	@property
	def spacing(self):
		pass
	@spacing.setter
	def spacing(self):
		pass

class Button:
	def __init__(self,text=None, **kwds):
		"""
A PushButton.
  
  Push the button to command the computer to preform some action.

  The push button, or command button, is perhaps the most commonly used widget 
  in any graphical user interface. Typical buttons are OK, Apply, Cancel, Close, 
  Yes, No and Help.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ButtonBase:
	def __init__(self):
		"""
Abstract base class for all buttons.
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ButtonGroup:
	def __init__(self,buttons, **kwds):
		"""
A ButtonGroup is a group of mutually exclusive buttons.

  Used with RadioButton, CheckBox to so only one is checked at a time
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class CheckBox:
	def __init__(self,text: str="", **kwds):
		"""
A CheckBox is a bool control with a text label.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Checkboxes:
	def __init__(self,values, value=0, **kwds):
		"""
Group of Checkboxes. Any number of checkbox can be checked within the same
  container.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Destroys the button.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns a set of checked values in the Checkboxes.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,values):
		"""
		Check/Uncheck the value in the Checkboxes.

    Args:
      values (list[str]): The list of values corresponding to each checkbox.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Specify the options. A button is created for each option.

    Args:
      values (list[str, str]): list of (value, displayName) tuples.
      value (list[str] | list[int] ): Set new values.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Col:
	def __init__(self,label: str="", readOnly=False, computed=False, **kwds):
		pass

	def castForSet(self,value):
		pass

	def getProperty(self,prop, row):
		pass

	def getValue(self,row):
		pass

	def init(self,i, name):
		pass

	def setProperty(self,prop, row):
		pass

class CollapsibleFrame:
	def __init__(self,text, children, expanded=False, **kwds):
		"""
A Frame with a flat button and subfame that is toggled visible/invisible
  as the label is clicked.

  The button causes the container to expand or contract. It is used  when there 
  is a need to consolidate and hide/show grouped widgets.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def resizeForAlignment(self,frames, val=35):
		"""
		Adjust sizes so things line up
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ComboBox:
	def __init__(self,values=None, **kwds):
		"""
A ComboBox is used for displaying various options.
  Only one option can be selected.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Update options user can select.

    Args:
      values (list[list[value, label]]): List of (value, label) pairs.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ComboButton:
	def __init__(self,values=None, value=None, icons=None, tooltips=None, advancedTooltips=None, **kwds):
		"""
A combobox-like button with popup items that are images.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values=None, value=None, icons=None, tooltips=None):
		"""
		Change the contents if value is specified, set with the specified value.

    Args:
      values (str,list[str]): values to set for the ComboButton.
      value (str): value to set for the CombooButton.
      icons (list[str]): list of icon names to be set.
      tooltips (list[str]): list of tooltips to be set.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ComboButtonsWidgetStack:
	def __init__(self,label, values, spacing=0, **kwds):
		"""
A Frame containing a ComboBox and subframes associated with each value 
  of the ComboBox.
  
  Only the frame for value of the CombBox is visible.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Container:
	def __init__(self):
		"""
Base class for all Dialog, ActionDialog, DockWindow, MicroDialog and GuideBar.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def createContents(self):
		"""
		To be implemented in derived class.
		"""
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class CsvFileDialog:
	def __init__(self):
		"""
A Dialog that prompts for read/write csv file names.

  It remembers the last directory a csv file was read/written.
  
"""
		pass

	def getOpenFileName(self,filter: str="Comma Separated Values *.csv", remember:str="write_csv", **kwds):
		"""
		Returns the csv filename opened.
		"""
		pass

	def getSaveFileName(self,filter: str="Comma Separated Values *.csv", remember:str="write_csv", **kwds):
		"""
		Returns the csv filename saved.
		"""
		pass

class Cursor:
	def __init__(self):
		"""
The cursor of the application.
  
"""
		pass

	def get(self,cursor):
		"""
		Returns the named cursor.
		"""
		pass

	def register(self,name, icon, pickmask=None, x=0, y=0):
		"""
		Registers a cursor so it can be set
    
		"""
		pass

	def set(self,cursor=None):
		"""
		Sets the named cursor.

    If the cursor is None, uses the standard cursor.
    
		"""
		pass

class Dialog:
	def __init__(self,parent: str="MainWindow",name: str="", children=None, **kwds):
		"""
A top-level window mostly used for short-term tasks and brief communications
     with the user.
  
"""
		pass

	def accept(self,returnValue):
		"""
		Close the dialog and returnValue from exec.
		"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def closeOnEscape(self):
		pass
	@closeOnEscape.setter
	def closeOnEscape(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def createContents(self):
		"""
		To be implemented in derived class.
		"""
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	def exec(self):
		"""
		Show as a model dialog, blocking code execution until it is closed.
    
    This is typically used to get user input before continuing.
    Dialog code returns the input from exec by calling self.accept(value).

    Returns:
      The accepted value or None if the dialog is closed in any other way.
    
		"""
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Get singleton when dialog is implemented as a subclass
    
      Used by associated Button/SpriteActions.
    
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def positionUnder(self,relativeTo, checkWasMoved=True, xoffset=0):
		"""
		Positions the dialog under or over the relataveTo widget.

    Args:
      relativeTo (Widget): The widget to position relative to.
      checkWasMoved (bool): Determines whether to check if widget is moved or not. 
      xoffset (int): The offset value for the widget for x-axis.
    
		"""
		pass

	def reject(self):
		"""
		Syntactic sugar to close the exec dialog without accepting a value.
    None is returned from exec.
    
		"""
		pass

	def resize(self,width, height):
		"""
		Resize width/height of dialog.

    This does not prevent the user from manually resizing like setting the
    width/height does.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the dialog and continues with script execution.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def title(self):
		pass
	@title.setter
	def title(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class DialogBase:
	def __init__(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def createContents(self):
		"""
		To be implemented in derived class.
		"""
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Get singleton when dialog is implemented as a subclass
    
      Used by associated Button/SpriteActions.
    
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def positionUnder(self,relativeTo, checkWasMoved=True, xoffset=0):
		"""
		Positions the dialog under or over the relataveTo widget.

    Args:
      relativeTo (Widget): The widget to position relative to.
      checkWasMoved (bool): Determines whether to check if widget is moved or not. 
      xoffset (int): The offset value for the widget for x-axis.
    
		"""
		pass

	def resize(self,width, height):
		"""
		Resize width/height of dialog.

    This does not prevent the user from manually resizing like setting the
    width/height does.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def title(self):
		pass
	@title.setter
	def title(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Dialogs:
	pass

class DockWindow:
	def __init__(self,area: str="left",parent: str="MainWindow",name: str="", children=None, **kwds):
		"""
A dockable window.
  
  It can exist in a floating state or can be attached to the main application window.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def caption(self):
		pass
	@caption.setter
	def caption(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def createContents(self):
		"""
		To be implemented in derived class.
		"""
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def docked(self):
		pass
	@docked.setter
	def docked(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Get singleton when dialog is implemented as a subclass
    
      Used by associated Button/SpriteActions.
    
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def positionUnder(self,relativeTo, checkWasMoved=True, xoffset=0):
		"""
		Positions the dialog under or over the relataveTo widget.

    Args:
      relativeTo (Widget): The widget to position relative to.
      checkWasMoved (bool): Determines whether to check if widget is moved or not. 
      xoffset (int): The offset value for the widget for x-axis.
    
		"""
		pass

	def resize(self,width, height):
		"""
		Resize width/height of dialog.

    This does not prevent the user from manually resizing like setting the
    width/height does.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def title(self):
		pass
	@title.setter
	def title(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class DoubleEdit:
	def __init__(self,value=0.0, units=None,alignment: str="right", format=None, **kwds):
		"""
A widget that can display/edit a double.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Gets the value converted to base units.
    
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def readonly(self):
		pass
	@readonly.setter
	def readonly(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		"""
		Sets the value converted to user units with the units label.

    Args:
      value (str, float): A float value or a string with the units.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	def validate(self,widget):
		"""
		Validates whether the value entered is a double and convert to base units.

    Args:
      widget (Widget): Widget where the value is entered.

    Returns:
      bool: True if the widget value entered is an int, otherwise False.
    
		"""
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Enum:
	def __init__(self,values, **kwds):
		pass

	def castForSet(self,value):
		pass

	def getProperty(self,prop, row):
		pass

	def getValue(self,row):
		pass

	def getValues(self,row):
		pass

	def init(self,i, name):
		pass

	def setProperty(self,prop, row):
		pass

class Events:
	pass

class ExpanderButton:
	def __init__(self,content=None, checkbox=None, radiobutton=None, **kwds):
		"""
Button used to control the visibility of another widget.
     
  It can be constructed with an associated checkbox or radiobutton which 
  will sync with the state of the controlled widget.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def content(self):
		pass
	@content.setter
	def content(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def expanded(self):
		pass
	@expanded.setter
	def expanded(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ExpanderFrame:
	def __init__(self,*childrenList, **kwds):
		"""
A Widget that manages expanding and collapsing the area containing
  widgets that follow and the ExpanderButton.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ExpanderLayout:
	def __init__(self,*childrenList, **kwds):
		"""
Gridlayout that also manages expanding and collapsing the area containing the
     widgets that follow and ExpanderButton.
  
"""
		pass

	def addChildren(self,children, nrows=None, ncols=None):
		"""
		Add the children in the grid layout.

    Args:
      children (list[Widget]): The items to be added in the layout.
      nrows (int): The number of rows in the grid. 
      ncols (int): The number of columns in the grid.
    
		"""
		pass

	@property
	def border(self):
		pass
	@border.setter
	def border(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def resizeMode(self):
		pass
	@resizeMode.setter
	def resizeMode(self):
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	@property
	def spacing(self):
		pass
	@spacing.setter
	def spacing(self):
		pass

class ExtensionManager:
	def __init__(self,*args, **kwargs):
		"""
The ExtensionManager class is used to register and load user-defined extensions
  in the Extension Manager.

  An extension provides the means to extend the application through shared 
  libraries or scripts. 
  Use extensions to create new clients, profiles, contexts, model views etc.
  Sample extensions that illustrate the various use cases are included in the 
  Extension Manager. All the extensions located under the default extensions directory 
  (/Documents/Altair/CustomPlugins) specified under the preferences dialog are 
  automatically registered by the Extension Manager. 

  An Extension is a physical folder with extension.xml and related scripts and 
  resources placed in it.
  An extension.xml is the manifest file for the extension that defines metadata of 
  the extension such as name, version, minimum supported product version etc. 

  Table 1. Supported attributes in extension.xml

  +------------------------+---------------------------------------------------+
  |Attributes              | Description                                       |
  +========================+===================================================+
  | name                   | Name of the Extension                             | 
  +------------------------+---------------------------------------------------+
  | minProductVersion      | The minimum version of the product that is        |
  |                        | supported by this extension.                      | 
  +------------------------+---------------------------------------------------+
  | description            | A short description about this extension that is  |
  |                        | displayed in the Extension Manager user interface.|
  +------------------------+---------------------------------------------------+
  | documentation          | HTML file with the detailed description of the    | 
  |                        | extension that can be opened in a web browser     |
  |                        | through the Extension Manager UI.                 | 
  +------------------------+---------------------------------------------------+
  | author                 | The author of this extension.                     | 
  +------------------------+---------------------------------------------------+
  | script                 | Script that should be executed when this extension|
  |                        | is loaded.                                        | 
  +------------------------+---------------------------------------------------+
  | resources              | Location of the resourcess' directory relative to |
  |                        | the extensions' directory.                        |
  +------------------------+---------------------------------------------------+ 
  | settings               | An xml file that defines the settings of this     |
  |                        | extension.                                        | 
  +------------------------+---------------------------------------------------+
  | advancedToolTip        | An xml file that defines the tooltips related to  |
  |                        | this extension.                                   | 
  +------------------------+---------------------------------------------------+
  | workFlowHelp           | An xml file that defines the workflow help content| 
  |                        | of this extension.                                | 
  +------------------------+---------------------------------------------------+
  | required               | The plugin that should be loaded as a             |
  |                        | pre-requisite for this extension.                 |
  +------------------------+---------------------------------------------------+ 
  | extends                | The plugin after which this plugin is an          |
  |                        | auto loaded.                                      | 
  +------------------------+---------------------------------------------------+
  | client                 | The name of the client that is implemented in this|
  |                        | extension or the name of the client to which the  |
  |                        | profile implemented in this extension belongs to. |
  +------------------------+---------------------------------------------------+
  | profile                | The name of the profile implemented in            | 
  |                        | this extension.                                   | 
  +------------------------+---------------------------------------------------+

  
"""
		pass

	def get(self):
		"""
		Returns the singleton instance of the Extension Manager.
    
		"""
		pass

	def load(self,name):
		"""
		Load a registered extension.

    This runs the plugin script making it active.

    Args:
      name (str): The name specified in the extensions's plugin.xml
    
		"""
		pass

	def onUnload(self,callback):
		"""
		Register function to cleanup the currently loading plugin.
    
    Make sure to remove any gui (typically SpriteActions).
    
    Args:
      callback (function): Cleanup function
    
		"""
		pass

	def register(self,path):
		"""
		Register an extension
    
    This makes it appear in the File->Extension Manager.
    Use extensionManager.load to activate it.

    Args:
      path (str): Path to a plugin.xml or a directory containing one.

    Raises:
        FileNotFoundError
    
		"""
		pass

	def unload(self,name):
		"""
		Unloads an extension.

    Any Actions added by the plugin are removed from the gui.

    Args:
      name (str): The name specified in the extensions's plugin.xml
    
		"""
		pass

	def unregister(self,name):
		"""
		Unregister an extension.

    Args:
      name (str): The name specified in the extensions's plugin.xml
    
		"""
		pass

class Float:
	def __init__(self,units=None,format: str="modeling", **kwds):
		pass

	def castForSet(self,value):
		pass

	def getProperty(self,prop, row):
		pass

	def getValue(self,row):
		pass

	def init(self,i, name):
		pass

	def setProperty(self,prop, row):
		pass

class Frame:
	def __init__(self,flags=0, **kwds):
		"""
Generic Widget container. 
  
  Base class for VFrame, HFrame and GridFrame, IconLabel, CollapsibleFrame, 
  ComboButtonsWidgetStack and RadioButtonsWithWidgets.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GridFrame:
	def __init__(self,*childrenList, **kwds):
		"""
A Frame with a GridLayout.

  GridFrame groups controls in a grid layout so they can be sized and/or 
  decorated as one.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GridLayout:
	def __init__(self,*childrenList, **kwds):
		"""
Layout widgets in rows and columns.
"""
		pass

	def addChildren(self,children, nrows=None, ncols=None):
		"""
		Add the children in the grid layout.

    Args:
      children (list[Widget]): The items to be added in the layout.
      nrows (int): The number of rows in the grid. 
      ncols (int): The number of columns in the grid.
    
		"""
		pass

	@property
	def border(self):
		pass
	@border.setter
	def border(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def resizeMode(self):
		pass
	@resizeMode.setter
	def resizeMode(self):
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	@property
	def spacing(self):
		pass
	@spacing.setter
	def spacing(self):
		pass

class Gui:
	"""

Module level methods

"""
	pass

class GuideBar:
	def __init__(self,relativeto=None, **kwds):
		"""
A popup dialog.
  
  It is typically used in a context to guide a user though the workflow.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	@property
	def activebutton(self):
		pass
	@activebutton.setter
	def activebutton(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	def button(self,**kwds):
		"""
		Adds a button to self.

    Returns:
      Button: The added button.
    
		"""
		pass

	def buttonGroup(self,buttons, **kwds):
		"""
		Groups all the buttons specified in a ButtonGroup.

    Args:
      buttons (list[Button]): List of buttons to be added to the group.
      kwds (dict): Any other properties needed to be set for the ButtonGroup.

    Returns:
      ButtonGroup: A ButtonGroup.
    
		"""
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def comboBox(self,**kwds):
		"""
		Creates a new ComboButton and inserts it into self.

    Args:
      kwds (dict): Any other properties user wants to set for the ComboButton.

    Returns:
      ComboButton: The new ComboButton.
    
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def createContents(self):
		"""
		To be implemented in derived class.
		"""
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	def executeCreateandExitButton(self,command, **kwds):
		"""
		Shortcut for creating green check button that
      executes the command, calls clearAllLists, then calls .pop().

    Args:
      command (callback): Callback method to be called when the button is clicked.

    Returns:
      Button: A check button.
    
		"""
		pass

	def executePlayButton(self,command, **kwds):
		"""
		Shortcut for creating a play button that executes the given command.

    Args:
      command(callback): Callback method to be called when the button is clicked.

    Returns:
      Button: The new play button.
    
		"""
		pass

	def exitButton(self,**kwds):
		"""
		Shortcut for creating a button that has the red x icon and pops the
       context.

    Args:
      kwds (dict): Any other properties user wants to set for the exit button.

    Returns:
      Button: The new exit button.
    
		"""
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	def legend(self,values, delayShow=False, **kwds):
		"""
		Sets and returns the legends.

    Args:
      values (LegendWidget): Legend widgets to be added in guide bar.
      delayShow (bool): Determines whether to delay the showing of the legends or not.
      kwds (dict): Any other properties user wants to set for the legend.

    Returns:
       Legend: All the legends.
    
		"""
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	def menu(self,autoshow=True, autohide=True, **kwds):
		"""
		Creates a new menu button.

    Args:
      autoshow(bool): Determines whether to automatically show the menu button or not.
      autohide(bool): Determines whether to automatically hide the menu button or not.
      kwds(dict): Any other properties user wants to set for the menu button.

    Returns:
       Button: A menu button.
    
		"""
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def resetButton(self,**kwds):
		"""
		Shortcut for creating a button that has the reset icon and calls
      clearAllLists.

    Returns:
      Button: The new reset button.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	def toggleButton(self,**kwds):
		"""
		Creates a new ToggleButton and inserted into self.

    Args:
      kwds (dict): Any other properties user wants to set for the ToggleButton.

    Returns:
      ToggleButton: The new ToggleButton.
    
		"""
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	def widget(self,widget, stretch=0):
		"""
		Adds a widget to self.

    Args:
      widget (Widget): The widget to add to the layout. 
        It is expected to be a child of the wrapped widget.
      stretch (int): The stretch value of the widget that will be added. 

    Returns:
      Widget: The added widget.
    
		"""
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GuideBarButton:
	def __init__(self,parent, **kwds):
		"""
Clickable button that can be added to a GuideBar.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def autoshowmode(self):
		pass
	@autoshowmode.setter
	def autoshowmode(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns True if checked.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	@property
	def helptext(self):
		pass
	@helptext.setter
	def helptext(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	def menu(self,autoshow=True, autohide=True, **kwds):
		"""
		Creates a new menu button.
		"""
		pass

	@property
	def menuwidget(self):
		pass
	@menuwidget.setter
	def menuwidget(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		"""
		Callback method to be called when the button is clicked.
		"""
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		"""
		Set Checked
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	def showDialog(self):
		"""
		Show guidbar and dialog.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GuideBarComboButton:
	def __init__(self,parent, **kwds):
		"""
Clickable ComboButton that can be added to a GuideBar.
   
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def autoshowmode(self):
		pass
	@autoshowmode.setter
	def autoshowmode(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the value at current index.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	@property
	def helptext(self):
		pass
	@helptext.setter
	def helptext(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	def menu(self,autoshow=True, autohide=True, **kwds):
		"""
		Creates a new menu button.
		"""
		pass

	@property
	def menuwidget(self):
		pass
	@menuwidget.setter
	def menuwidget(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		"""
		Callback method to be called when the button is clicked.
		"""
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		"""
		Sets the current index on the value specified.

    Args:
      value(str): Value which should be selected in GuidebarComboButton.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Set multiple values or single value for the ComboButton.

    Args:
      values (list | dict | tuple): The collection of values to be set.
      value (str): value to be set.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	def showDialog(self):
		"""
		Show guidbar and dialog.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GuideBarMenu:
	def __init__(self,parent, autoshow=True, autohide=True, scrollbar=False, **kwds):
		"""
Clickable Menu that can be added to a GuideBar.
   
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def anchorbutton(self):
		pass
	@anchorbutton.setter
	def anchorbutton(self):
		pass

	@property
	def autohide(self):
		pass
	@autohide.setter
	def autohide(self):
		pass

	@property
	def autoshow(self):
		pass
	@autoshow.setter
	def autoshow(self):
		pass

	def button(self,**kwds):
		"""
		Adds a button to the Guide bar menu layout.

    Args:
      kwds(dict): Any other properties needed to be set for the Button.

    Returns:
      Button: The added button.
    
		"""
		pass

	def checkBox(self,checked=False, **kwds):
		"""
		Adds a checkbox to the Guide bar menu layout.

    Args:
      checked(bool): Determines whether the button is checked or not.
      kwds(dict): Any other properties needed to be set for the check box.

    Returns:
      Button: The check box.
    
		"""
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	def widget(self,widget, stretch=0):
		"""
		Adds a widget to self.

    Args:
      widget (Widget): The widget to add to the layout. 
        It is expected to be a child of the wrapped widget.
      stretch (int): The stretch value of the widget that will be added. 

    Returns:
      Widget: The added widget.
    
		"""
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GuidePanelButtons:
	def __init__(self,name: str="", parent=None, **kwds):
		"""
The GuidePanelButtons class provides a widget that contains the OK,
  Apply, Reset, Cancel buttons.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	def applyButton(self):
		"""
		Returns apply push button.
		"""
		pass

	def cancelButton(self):
		"""
		Returns cancel push button.
		"""
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def okButton(self):
		"""
		Returns ok push button.
		"""
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def resetButton(self):
		"""
		Returns reset push button.
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def visibleButtons(self):
		pass
	@visibleButtons.setter
	def visibleButtons(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GuidePanelContent:
	def __init__(self,name: str="", parent=None, **kwds):
		"""
The GuidePanelContent class provides a widget that should contains a grid
   layout with section headers and section content rows. The bottom two lines of
   the grid should be used for the uiGuidePanelButtons instance and some margin
   above.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def defaultWidgetHeight(self):
		pass
	@defaultWidgetHeight.setter
	def defaultWidgetHeight(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minLabelWidth(self):
		pass
	@minLabelWidth.setter
	def minLabelWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def pushButtonHeight(self):
		pass
	@pushButtonHeight.setter
	def pushButtonHeight(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	@property
	def selectorButtonHeight(self):
		pass
	@selectorButtonHeight.setter
	def selectorButtonHeight(self):
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GuidePanelGroup:
	def __init__(self,name: str="", parent=None, **kwds):
		"""
The GuidePanelGroup class provides a widget that should contains a grid
  layout with a section header label and section content rows.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class GuidePanelGroupRow:
	def __init__(self,name: str="", parent=None, **kwds):
		"""
The GuidePanelGroupRow class provides a widget that contains a horizontal
  layout
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class HBoxLayout:
	def __init__(self,*childrenList, **kwds):
		"""
Layout widgets horizontally.
"""
		pass

	def addChildren(self,children):
		"""
		Adds the specified children in the BoxLayout.

    Args:
      children (list[Widget]): The items to be added.
    
		"""
		pass

	@property
	def border(self):
		pass
	@border.setter
	def border(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def resizeMode(self):
		pass
	@resizeMode.setter
	def resizeMode(self):
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	@property
	def spacing(self):
		pass
	@spacing.setter
	def spacing(self):
		pass

class HCheckboxes:
	def __init__(self,values, value=0, **kwds):
		"""
Group of Checkboxes layed out horizontally.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Destroys the button.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns a set of checked values in the Checkboxes.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,values):
		"""
		Check/Uncheck the value in the Checkboxes.

    Args:
      values (list[str]): The list of values corresponding to each checkbox.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Specify the options. A button is created for each option.

    Args:
      values (list[str, str]): list of (value, displayName) tuples.
      value (list[str] | list[int] ): Set new values.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class HFrame:
	def __init__(self,*childrenList, **kwds):
		"""
A Frame with a HBoxLayout.

  HFrame groups controls horizontally so they can be sized and/or decorated as 
  one.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class HRadioButtons:
	def __init__(self,values, value=0, **kwds):
		"""
Group of mutually exclusive RadioButtons layed out horizontally.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Destroys the button.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the checked item.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		"""
		Set the item checked.

    Args:
      v (int): Index of the item to checked.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Specify the options. A button is created for each option.

    Args:
      values (list[str, str]): list of (value, displayName) tuples.
      value (list[str] | list[int] ): Set new values.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

def HScrollBar(**kwds):
	pass

def HSlider(**kwds):
	pass

class HSplitter:
	def __init__(self,*childrenList, **kwds):
		"""
A Splitter with horizontal orientation.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def collapsible(self):
		pass
	@collapsible.setter
	def collapsible(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def opaqueResize(self):
		pass
	@opaqueResize.setter
	def opaqueResize(self):
		pass

	@property
	def orientation(self):
		pass
	@orientation.setter
	def orientation(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def sizes(self):
		pass
	@sizes.setter
	def sizes(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class HasMethodsToHide:
	def __init__(self):
		"""
Baseclass implementing custom __dir__ to hide swig methods.
     This keeps them from showing up in the IPython auto-complete widget.

     To be used on base classes in hwx that inherit a swig class since user
     should be calling the wrapped functions/properties not swig functions.
     
     Non swig functions can be hidden by underscoring them or setting
     _hideFromDir on them.
     
     If __dir__ is overridden it must be a classmethod since it is used
     for generating class documentation.
  
"""
		pass

class IconLabel:
	def __init__(self,icon, helptopic=None, **kwds):
		"""
A Widget that displays an icon from an IconSet file.

  An IconLabel is used to indicate a separate section in a Dialog. When clicked, 
  it can be used to display help.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Int:
	def __init__(self,label: str="", readOnly=False, computed=False, **kwds):
		pass

	def castForSet(self,value):
		pass

	def getProperty(self,prop, row):
		pass

	def getValue(self,row):
		pass

	def init(self,i, name):
		pass

	def setProperty(self,prop, row):
		pass

class IntEdit:
	def __init__(self,value=0,alignment: str="right", **kwds):
		"""
A widget that can display/edit an integer.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Overloaded method that returns the value as in integer.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maxValue(self):
		pass
	@maxValue.setter
	def maxValue(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minValue(self):
		pass
	@minValue.setter
	def minValue(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def readonly(self):
		pass
	@readonly.setter
	def readonly(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,text):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	def validate(self,widget):
		"""
		Validates whether the value entered is an integer and in [minValue, maxValue] range.

    Args:
      widget (Widget): The widget where the value is entered.

    Returns:
      bool: True if the widget value entered is an int, otherwise False.
    
		"""
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ItemMap:
	def __init__(self,tree):
		"""
Get TreeItem from uiListViewItem 

     Should be a more Swig way to do this but I could not find it
     so use the 10th column of TreeItem to hold an unique id
  
"""
		pass

	def add(self,item):
		pass

	def clear(self):
		pass

	def get(self,item):
		pass

	def remove(self,item):
		pass

class Iterable:
	def __init__(self):
		pass

class Key:
	def __init__(self,value, names=None, module=None, qualname=None, type=None, start=1):
		"""
An enumeration.
"""
		pass

class KeyEvent:
	def __init__(self,*args):
		pass

class Label:
	def __init__(self,text: str="", **kwds):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Layout:
	def __init__(self):
		"""
Base class for BoxLayout and GridLayout.
  
"""
		pass

	@property
	def border(self):
		pass
	@border.setter
	def border(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def resizeMode(self):
		pass
	@resizeMode.setter
	def resizeMode(self):
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	@property
	def spacing(self):
		pass
	@spacing.setter
	def spacing(self):
		pass

class Legend:
	def __init__(self,parent=None, values=[], **kwds):
		"""
A color coded legend.

  A Legend widget contains color and labels. The items in the legend can be 
  selected and an action performed. 
  Legends are used to easily change between discrete values with associated colors.

  For example, when defining the type of joint among three options (Active, Locked, Free).
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	@property
	def activeValues(self):
		pass
	@activeValues.setter
	def activeValues(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Clears all the legends.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the legend value.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,itemid):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values):
		"""
		List of legend properties to be set.

    Args:
      values (list): A list of properties.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def values(self):
		pass
	@values.setter
	def values(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class LineEdit:
	def __init__(self,text: str="", validator=None, **kwds):
		"""
A LineEdit Widget that can display/edit a string.
  
  A line edit allows the user to enter and edit a single line of plain text
  with a useful collection of editing functions, including undo and redo,
  cut and paste, and drag and drop.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def alignment(self):
		pass
	@alignment.setter
	def alignment(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def readonly(self):
		pass
	@readonly.setter
	def readonly(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,text):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	def validate(self,widget):
		"""
		Validates the value of the widget.
    
		"""
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ListBox:
	def __init__(self,items=[],name: str="", parent=None, flags=0, **kwds):
		"""
A ListBox widget.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	def append(self,item):
		"""
		Appends an item to the end of the ListBox.

    Args:
      item (str): Text value to be inserted.
    
		"""
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Removes all items of the List Box.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the text of curren row.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	def insert(self,item, index=9999999):
		"""
		Inserts an item in the ListBox at position index. 

    By default it gets appended to the end.

    Args:
      item (str): Text value to be inserted.
      index (int): Index at which item is inserted. 
    
		"""
		pass

	def isChecked(self,index):
		"""
		Returns whether the item at the specified index is checked or not.

    Args:
      index (int)

    Returns:
      bool
    
		"""
		pass

	@property
	def items(self):
		pass
	@items.setter
	def items(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def remove(self,index):
		"""
		Remove item at index from List Box.

    Args:
      index (int): index of item to be removed.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def select(self,index):
		"""
		Select an index.
    
    Same as setting the selectedIndex except the command callback gets called.
    
		"""
		pass

	@property
	def selectedIndex(self):
		pass
	@selectedIndex.setter
	def selectedIndex(self):
		pass

	@property
	def selectedIndexes(self):
		pass
	@selectedIndexes.setter
	def selectedIndexes(self):
		pass

	@property
	def selectionMode(self):
		pass
	@selectionMode.setter
	def selectionMode(self):
		pass

	def set(self,text):
		"""
		Sets the text in current row.
		"""
		pass

	def setChecked(self,index, value=True):
		"""
		Checks or unchecks the item at the specified index.

    Args:
      index (int)
      value (bool)
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	def sort(self,ascending=True):
		"""
		Sorts the items in the ListBox, based on their text.

    Args:
      ascending (bool): If set to True, sort the items in ascending order.
    
		"""
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def viewMode(self):
		pass
	@viewMode.setter
	def viewMode(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class MessageDialog:
	def __init__(self,message, parent=None,name: str="",button1: str="",button2: str="",button3: str="",behavior: str="normal", **kwds):
		"""
A popup message dialog.

  Used to display messages to the user. It may contain upto three buttons.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self,v):
		"""
		Returns the message text.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def message(self):
		pass
	@message.setter
	def message(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,buttonId=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		"""
		Sets the specified message.

    Args:
      v (str): Message text to be displayed.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the MessageDialog and pauses exection till one button is clicked.

    Returns:
      int: The button clicked.
    
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class MicroDialog:
	def __init__(self,parent: str="CentralWidget",name: str="", children=None, **kwds):
		"""
A light-weight dialog residing inside the graphics area that typically 
     contains entry fields and buttons that have an immediate effect.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.

    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def createContents(self):
		"""
		To be implemented in derived class.
		"""
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def position(self):
		pass
	@position.setter
	def position(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def spacing(self):
		pass
	@spacing.setter
	def spacing(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class MouseEvent:
	def __init__(self,*args):
		"""
TODO explanation of common properties goes here.
"""
		pass

class NoteBook:
	def __init__(self,**kwds):
		"""
NoteBook with tabs.

  A NoteBook presents multiple mutually exclusive panes of content in the same 
  area. It includes a tabbed control area with 'text' and a content area.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	def addTab(self,child, text: str="", icon=None):
		"""
		Inserts a new tab with the specified child.

    Args:
      child (Widget): The widget to be added to the tab.
      text (str): The text to be displayed on the tab.
      icon (str): The icon to be shown in the tab.
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def current(self):
		pass
	@current.setter
	def current(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	def insertTab(self,child, text: str="", icon=None, index=-1):
		"""
		Inserts a new tab with the specified child.

    Args:
      child (Widget): The widget to be added to the tab.
      text (str): The text to be displayed on the tab.
      icon (str): The icon to be shown in the tab.
      index (int): The index where to insert the tab.
    
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class NumericalEntryField:
	def __init__(self,name: str="", parent=None, createDefaultLineEdit=True, **kwds):
		"""
A placeholder for a widget (or set of widgets) that handles numerical
  values.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getLineEditWidget(self):
		"""
		Returns LineEdit widget
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Path:
	def __init__(self,*args, **kwargs):
		"""
PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiate a PosixPath or WindowsPath directly,
    but cannot instantiate a WindowsPath on a POSIX system or vice versa.
    
"""
		pass

	def absolute(self):
		"""
		Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        
		"""
		pass

	@property
	def anchor(self):
		pass
	@anchor.setter
	def anchor(self):
		pass

	def as_posix(self):
		"""
		Return the string representation of the path with forward (/)
        slashes.
		"""
		pass

	def as_uri(self):
		"""
		Return the path as a 'file' URI.
		"""
		pass

	def chmod(self,mode):
		"""
		
        Change the permissions of the path, like os.chmod().
        
		"""
		pass

	def cwd(self):
		"""
		Return a new path pointing to the current working directory
        (as returned by os.getcwd()).
        
		"""
		pass

	@property
	def drive(self):
		pass
	@drive.setter
	def drive(self):
		pass

	def exists(self):
		"""
		
        Whether this path exists.
        
		"""
		pass

	def expanduser(self):
		"""
		 Return a new path with expanded ~ and ~user constructs
        (as returned by os.path.expanduser)
        
		"""
		pass

	def glob(self,pattern):
		"""
		Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        
		"""
		pass

	def group(self):
		"""
		
        Return the group name of the file gid.
        
		"""
		pass

	def home(self):
		"""
		Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
        
		"""
		pass

	def is_absolute(self):
		"""
		True if the path is absolute (has both a root and, if applicable,
        a drive).
		"""
		pass

	def is_block_device(self):
		"""
		
        Whether this path is a block device.
        
		"""
		pass

	def is_char_device(self):
		"""
		
        Whether this path is a character device.
        
		"""
		pass

	def is_dir(self):
		"""
		
        Whether this path is a directory.
        
		"""
		pass

	def is_fifo(self):
		"""
		
        Whether this path is a FIFO.
        
		"""
		pass

	def is_file(self):
		"""
		
        Whether this path is a regular file (also True for symlinks pointing
        to regular files).
        
		"""
		pass

	def is_mount(self):
		"""
		
        Check if this path is a POSIX mount point
        
		"""
		pass

	def is_reserved(self):
		"""
		Return True if the path contains one of the special names reserved
        by the system, if any.
		"""
		pass

	def is_socket(self):
		"""
		
        Whether this path is a socket.
        
		"""
		pass

	def is_symlink(self):
		"""
		
        Whether this path is a symbolic link.
        
		"""
		pass

	def iterdir(self):
		"""
		Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        
		"""
		pass

	def joinpath(self,*args):
		"""
		Combine this path with one or several arguments, and return a
        new path representing either a subpath (if all arguments are relative
        paths) or a totally different path (if one of the arguments is
        anchored).
        
		"""
		pass

	def lchmod(self,mode):
		"""
		
        Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
        
		"""
		pass

	def link_to(self,target):
		"""
		
        Make the target path a hard link pointing to this path.

        Note this function does not make this path a hard link to *target*,
        despite the implication of the function and argument names. The order
        of arguments (target, link) is the reverse of Path.symlink_to, but
        matches that of os.link.

        
		"""
		pass

	def lstat(self):
		"""
		
        Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
        
		"""
		pass

	def match(self,path_pattern):
		"""
		
        Return True if this path matches the given pattern.
        
		"""
		pass

	def mkdir(self,mode=511, parents=False, exist_ok=False):
		"""
		
        Create a new directory at this given path.
        
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def open(self,mode:str="r", buffering=-1, encoding=None, errors=None, newline=None):
		"""
		
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.
        
		"""
		pass

	def owner(self):
		"""
		
        Return the login name of the file owner.
        
		"""
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def parents(self):
		pass
	@parents.setter
	def parents(self):
		pass

	@property
	def parts(self):
		pass
	@parts.setter
	def parts(self):
		pass

	def read_bytes(self):
		"""
		
        Open the file in bytes mode, read it, and close the file.
        
		"""
		pass

	def read_text(self,encoding=None, errors=None):
		"""
		
        Open the file in text mode, read it, and close the file.
        
		"""
		pass

	def relative_to(self,*other):
		"""
		Return the relative path to another path identified by the passed
        arguments.  If the operation is not possible (because this is not
        a subpath of the other path), raise ValueError.
        
		"""
		pass

	def rename(self,target):
		"""
		
        Rename this path to the target path.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        
		"""
		pass

	def replace(self,target):
		"""
		
        Rename this path to the target path, overwriting if that path exists.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        
		"""
		pass

	def resolve(self,strict=False):
		"""
		
        Make the path absolute, resolving all symlinks on the way and also
        normalizing it (for example turning slashes into backslashes under
        Windows).
        
		"""
		pass

	def rglob(self,pattern):
		"""
		Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        
		"""
		pass

	def rmdir(self):
		"""
		
        Remove this directory.  The directory must be empty.
        
		"""
		pass

	@property
	def root(self):
		pass
	@root.setter
	def root(self):
		pass

	def samefile(self,other_path):
		"""
		Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        
		"""
		pass

	def stat(self):
		"""
		
        Return the result of the stat() system call on this path, like
        os.stat() does.
        
		"""
		pass

	@property
	def stem(self):
		pass
	@stem.setter
	def stem(self):
		pass

	@property
	def suffix(self):
		pass
	@suffix.setter
	def suffix(self):
		pass

	@property
	def suffixes(self):
		pass
	@suffixes.setter
	def suffixes(self):
		pass

	def symlink_to(self,target, target_is_directory=False):
		"""
		
        Make this path a symlink pointing to the target path.
        Note the order of arguments (link, target) is the reverse of os.symlink.
        
		"""
		pass

	def touch(self,mode=438, exist_ok=True):
		"""
		
        Create this file with the given access mode, if it doesn't exist.
        
		"""
		pass

	def unlink(self,missing_ok=False):
		"""
		
        Remove this file or link.
        If the path is a directory, use rmdir() instead.
        
		"""
		pass

	def with_name(self,name):
		"""
		Return a new path with the file name changed.
		"""
		pass

	def with_suffix(self,suffix):
		"""
		Return a new path with the file suffix changed.  If the path
        has no suffix, add given suffix.  If the given suffix is an empty
        string, remove the suffix from the path.
        
		"""
		pass

	def write_bytes(self,data):
		"""
		
        Open the file in bytes mode, write to it, and close the file.
        
		"""
		pass

	def write_text(self,data, encoding=None, errors=None):
		"""
		
        Open the file in text mode, write to it, and close the file.
        
		"""
		pass

class PluginLoader:
	"""

This module manages loading of plugins (plugin.py) or manifest files
(manifest.py).

Plugins are searched for first inside of the scripts/python/hwx folder and then
all paths defined in the colon/semicolon separated HWX_PLUGINS environment
variable.

Plugin.py is where a developer or end user can define additional capabilities to
the unity framework.  It can be a new client, a new profile, or simply
additional buttons added to an existing client/profile.

Since folders and subfolders are scanned for plugins, a manifest.py file was
introduced to speed things up (it also allows for defining the order plugins are
loaded).  Methods that can be called in manifest.py are:
  loadPlugin       - loads a plugin in a certain folder
  loadAllPlugins   - loads plugins recursively from a certain folder 
"""
	pass

class PopupMenu:
	def __init__(self,widget=None, onPopup=None, items=None, fontSize=None, advancedTooltip=None, **kwds):
		"""
A PopupMenu Widget.

  The PopupMenu is a specialized control that has the abilty of being selected.
  You can add items and commands to the popup menu.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Remove all items.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getIDs(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	def insertItem(self,text, menu=None, icon=None, command=None, enabled=True, visible=True, accel=None, checked=None, advancedTooltip=None):
		"""
		Inserts item and command into menu.

    Args:
      text (str): The item text to be displayed.
      menu (PopupMenu): The menu object to insert.
      icon (str): The icon file to be inserted on the left side of text.
      command (callback): The callback method to be executed when item is clicked.
      enabled (bool): Determines whether to enable the inserted item.
      visible (bool): Determines whether the inserted item is visible.
      accel (str): Keyboard accelerator to execute the command (e.g. 'Del')
      checked (bool): Determines if the item is checkable.
        True or False makes it checkable.
      advancedTooltip (str): UUID to display advanced tooltips.

    Returns:
      int: The index where the item has been inserted.
    
		"""
		pass

	def insertMenu(self,text, menu=None):
		"""
		Adds and returns a cascading menu.

    Args:
      text (str): Text to be displayed in the menu.
      menu (PopupMenu): Cascading menu.

    Returns:
      PopupMenu: Returns a cascading menu.
    
		"""
		pass

	def insertSeparator(self):
		"""
		Inserts a separator in the Pop menu.
		"""
		pass

	def insertWidget(self,widget):
		"""
		Inserts a widget into the menu
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def numOfItems(self):
		pass
	@numOfItems.setter
	def numOfItems(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def popup(self,event=None):
		"""
		Shows the Popup menu.

    Args:
      event (MouseEvent): The event to get the mouse position.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setItemEnabled(self,index, enabled=True):
		"""
		Enables or Disables the menu item at the specified index.
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Profile:
	def __init__(self,name=None,baseProfile: str="BaseProfile", pluginName=None):
		"""
A profile is the UI state of a client that defines menus, ribbon pages,
    toolbars and dock windows. There can be multiple profiles for a client, but
    only one can be active (displayed) at a time.

    Splitting functionality into profiles can reduce screen clutter allowing the
    user to focus on specific tasks.

    Profiles can be hierarchical with a profile having sub-profiles.

    Sub-profiles can make use of their base profile's functionality and implement
    additional functionality as required.

    There can be two types of profiles, stand-alone and add-on .

        - A stand-alone profile re-configures the entire UI of a client.
        - An add-on profile contributes added functionality to an existing profile.
  
"""
		pass

	def activate(self):
		pass

	def build(self):
		pass

	def deactivate(self):
		pass

class ProgressBar:
	def __init__(self,name: str="", parent=None, totalSteps=None, **kwds):
		"""
A Widget that shows the running status of a process.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def centerIndicator(self):
		pass
	@centerIndicator.setter
	def centerIndicator(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def percentageVisible(self):
		pass
	@percentageVisible.setter
	def percentageVisible(self):
		pass

	@property
	def progress(self):
		pass
	@progress.setter
	def progress(self):
		pass

	def reset(self):
		"""
		Reset the ProgressBar.
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def totalSteps(self):
		pass
	@totalSteps.setter
	def totalSteps(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class PushButton:
	def __init__(self,text=None, **kwds):
		"""
A PushButton.
  
  Push the button to command the computer to preform some action.

  The push button, or command button, is perhaps the most commonly used widget 
  in any graphical user interface. Typical buttons are OK, Apply, Cancel, Close, 
  Yes, No and Help.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class PygmentStyles:
	"""
Defines 2 new pygments syntax highlighting styles (Light, Dark) for use in
the Python Window and Python API Demos.

Use getCurrentStyle() to choose the style based on the Unity theme.

"""
	pass

class RadioButton:
	def __init__(self,text=None, **kwds):
		"""
A RadioButton

  A RadioButton is a widget that can be switched on/off.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def centerAlign(self):
		pass
	@centerAlign.setter
	def centerAlign(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class RadioButtons:
	def __init__(self,values, value=0, **kwds):
		"""
Group of mutually exclusive RadioButtons.

  RadioButtons are mutually exclusive with other RadioButtons in the same container.

  Only one radio botton can be switched on within the same container.

  RadioButtons are usually used to create composite controls like VRadioButtons 
  or HRadioButtons. 
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Destroys the button.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the checked item.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		"""
		Set the item checked.

    Args:
      v (int): Index of the item to checked.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Specify the options. A button is created for each option.

    Args:
      values (list[str, str]): list of (value, displayName) tuples.
      value (list[str] | list[int] ): Set new values.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class RadioButtonsWithWidgets:
	def __init__(self,values, **kwds):
		"""
A Frame with vertical layout of exclusive RadioButtons that have associated 
  widgets to the right of the buttons.

  Only the widgets for the button that is on are enabled.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Ribbon:
	def __init__(self):
		"""
A Ribbon is a top level menu that appears on the main application.
  
  Any widgets that are parented to the Ribbon appear under it.
  The Ribbon requires a unique identifier.

  The Ribbon allows you to quickly access tools and standard functions, 
  and is located at the top of the Inspire workspace. You can use it to add tools 
  that you frequently use.
  
"""
		pass

	@property
	def activePage(self):
		pass
	@activePage.setter
	def activePage(self):
		pass

	def add(self,location, item, **kwds):
		"""
		Adds the specified item in the ribbon location.

    Args:
      location (str): Location can be a page or page group.
      item (RibbonPageGroup | SpriteActionGroup): item to be added
    
		"""
		pass

	def get(self):
		pass

	def remove(self,location):
		"""
		Removes specified ribbon page.
    
    All the children get deleted when the page gets deleted.

    Args:
      location (str): Location can be a page or page group.
    
		"""
		pass

class RibbonPage:
	def __init__(self,name: str="",text: str="", children=(), before=None, after=None):
		"""
Ribbon tab.

    It is the Toolbar replacement and a Container of SpriteActionGroups and 
    RibbonPageGroups.
  
"""
		pass

	def activate(self):
		"""
		Select the page
		"""
		pass

	def add(self,item, after=None):
		"""
		Adds the specified item to the RibbonPage.
    
    Args:
      item (RibbonPageGroup | str): The item to be added.
      after (RibbonPageGroup | str): The item to insert after.
    
		"""
		pass

	def addFrame(self,text: str="", name: str=""):
		"""
		Adds and returns a frame to this RibbonPage
    
    The frame can be used to add any Widgets.

    Args:
      text (str): The name/displayName of the ribbon page.
      name (str): The name of the Frame widget.

    Returns:
      Frame: The frame object added to the Ribbon page.
    
		"""
		pass

	@property
	def displayName(self):
		pass
	@displayName.setter
	def displayName(self):
		pass

	def get(self,name):
		"""
		Lookup the RibbonPage by name.

    Args:
      name (str)

    Returns:
      RibbonPage
    
		"""
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def remove(self,item):
		"""
		Removes the specified item from the RibbonPage.
     
    Args:
      item (Action | str): The item to remove.
    
		"""
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

def RibbonPageFrame(ribbonPage, **kwds):
	"""
Syntactic sugar for ribbonPage.addFrame for consistancy with RibbonPageGroup.
      
     Unlike the RibbonPageGroup, the ribbonPage argument is required.
  
"""
	pass

class RibbonPageGroup:
	def __init__(self,parent=None,text: str="", children=None, menus=None,name: str=""):
		"""
Logical grouping of SpriteActionGroups in a RibbonPage.
  
"""
		pass

	def add(self,action, after=None, index=None):
		"""
		Adds the SpriteAction/SpriteActionGroup.

    Args:
      action (str | SpriteAction | SpriteActionGroup): The action to be added
      after (str | SpriteAction | SpriteActionGroup): Determines whether to 
        insert the specified item after the group or not.
      index (int): Index at which action needs to be inserted.
    
		"""
		pass

	def get(self,name):
		"""
		Gets the RibbonPageGroup with the specified name.

    Args:
      name (str): The RibbonPageGroup name to get.

    Returns:
      RibbonPageGroup: The page group.
    
		"""
		pass

	def hide(self):
		"""
		Hides the RibbonPageGroup. 
		"""
		pass

	def isShown(self):
		"""
		Returns True if it shown, False otherwise.
		"""
		pass

	def remove(self,action):
		"""
		Removes the sprite action group from RibbonPageGroup.

    Args:
      action (SpriteActionGroup): The action to be removed.

    
		"""
		pass

	def show(self):
		"""
		Shows the RibbonPageGroup. 
		"""
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

class Row:
	def __init__(self,table, data):
		"""
A class representing a row of the table.

  Row is like a list but has also some nice features
  1. it casts values before they are set.
  2. it gives access by attribute.
  
"""
		pass

class ScrollBar:
	def __init__(self,orientation: str="horizontal", **kwds):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def maxvalue(self):
		pass
	@maxvalue.setter
	def maxvalue(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def minvalue(self):
		pass
	@minvalue.setter
	def minvalue(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def orientation(self):
		pass
	@orientation.setter
	def orientation(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def tracking(self):
		pass
	@tracking.setter
	def tracking(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ScrollLayout:
	def __init__(self,**kwds):
		pass

	def AcceptDrops(self):
		pass

	def Action(self,*args):
		pass

	def Actions(self):
		pass

	def AddAction(self,action: var0):
		pass

	def AddActions(self,actions: var1):
		pass

	def AddChild(self,child: var2, x: int = 0, y: int = 0):
		pass

	def AdjustSize(self):
		pass

	def AdvancedToolTipId(self):
		pass

	def Alignment(self):
		pass

	def AllowHiddenScrollBars(self):
		pass

	def AsConcreteListener(self):
		pass

	def AsListener(self):
		pass

	def AutoFillBackground(self):
		pass

	def AverageWidth(self,chars: int):
		pass

	def BackgroundDarkness(self):
		pass

	def BackgroundMode(self):
		pass

	def BackgroundRole(self):
		pass

	def BadgeAlignment(self):
		pass

	def BadgeColor(self):
		pass

	def BaseSize(self):
		pass

	def CanMove(self):
		pass

	def CanResize(self):
		pass

	def Caption(self):
		pass

	def Child(self,objName: var3, inheritsClass: var3 = None, recursiveSearch: bool = True):
		pass

	def ChildAt(self,*args):
		pass

	def Children(self):
		pass

	def ChildrenRect(self):
		pass

	def ClassName(self):
		pass

	def ClearFocus(self):
		pass

	def ClearMask(self):
		pass

	def Close(self,alsoDelete: bool = False):
		pass

	def Color0(self):
		pass

	def Color1(self):
		pass

	def ColorBlack(self):
		pass

	def ColorBlue(self):
		pass

	def ColorCyan(self):
		pass

	def ColorDarkBlue(self):
		pass

	def ColorDarkCyan(self):
		pass

	def ColorDarkGray(self):
		pass

	def ColorDarkGreen(self):
		pass

	def ColorDarkMagenta(self):
		pass

	def ColorDarkRed(self):
		pass

	def ColorDarkYellow(self):
		pass

	def ColorGray(self):
		pass

	def ColorGreen(self):
		pass

	def ColorGroup(self):
		pass

	def ColorLightGray(self):
		pass

	def ColorMagenta(self):
		pass

	def ColorRed(self):
		pass

	def ColorWhite(self):
		pass

	def ColorYellow(self):
		pass

	def ContentsHeight(self):
		pass

	def ContentsRect(self):
		pass

	def ContentsToViewport(self,p: var4):
		pass

	def ContentsWidth(self):
		pass

	def ContentsX(self):
		pass

	def ContentsY(self):
		pass

	def ContextMenuPolicy(self):
		pass

	def Cursor(self):
		pass

	def CustomFocusNextPrevChild(self,next: bool):
		pass

	def CustomSizeHint(self):
		pass

	def DeleteLater(self):
		pass

	def Disconnect(self,sender: var5, force: var6 = False):
		pass

	def DisconnectAll(self,force: var6 = False):
		pass

	def DluHeight(self,*args):
		pass

	def DluPixelHeight(self,pixels: int):
		pass

	def DluPixelSize(self,pixelWidth: int, pixelHeight: int):
		pass

	def DluPixelWidth(self,pixels: int):
		pass

	def DluWidth(self,*args):
		pass

	def DownCast(self,o: var7):
		pass

	def DumpTree(self):
		pass

	def EnsureVisible(self,x: int, y: int, xmargin: int = 50, ymargin: int = 50):
		pass

	def EnsureWidgetVisible(self,childWidget: var2, xmargin: int = 50, ymargin: int = 50):
		pass

	def EraseColor(self):
		pass

	def ErasePixmap(self):
		pass

	def EventInfo(self):
		pass

	def EventPropagation(self):
		pass

	def ExcludeOverrideCursor(self):
		pass

	def Find(self,winId: var8):
		pass

	def FindBackgroundDarkness(self):
		pass

	def FocusNextPrevChild(self,next: bool):
		pass

	def FocusPolicy(self):
		pass

	def FocusProxy(self):
		pass

	def FocusWidget(self):
		pass

	def Font(self):
		pass

	def FontMetrics(self):
		pass

	def ForceBackgroundPainting(self):
		pass

	def ForegroundColor(self):
		pass

	def ForegroundRole(self):
		pass

	def FrameGeometry(self):
		pass

	def FrameRect(self):
		pass

	def FrameShadow(self):
		pass

	def FrameShape(self):
		pass

	def FrameSize(self):
		pass

	def FrameStyle(self):
		pass

	def FrameWidth(self):
		pass

	def GeomMgrAutoHideManagedWidgetsFlag(self):
		pass

	def GeomMgrCanBeTopWidget(self):
		pass

	def GeomMgrIgnoreHideOnMinimizeFlag(self):
		pass

	def GeomMgrPriority(self):
		pass

	def GeomMgrShowTopLeft(self):
		pass

	def GeomMgrStartX(self,hint: var9, firstItemWidth: int):
		pass

	def GeomMgrStartXHint(self):
		pass

	def GeomMgrXOffset(self):
		pass

	def GeomMgrYOffset(self):
		pass

	def Geometry(self):
		pass

	def Grab(self,rect: var10):
		pass

	def GrabKeyboard(self):
		pass

	def GrabMouse(self,*args):
		pass

	def HScrollBarMode(self):
		pass

	def Handle(self):
		pass

	def HasBadge(self):
		pass

	def HasChild(self,child: var2):
		pass

	def HasFocus(self):
		pass

	def HasIcon(self):
		pass

	def HasMouse(self):
		pass

	def HasMouseTracking(self):
		pass

	def Height(self):
		pass

	def HeightForWidth(self,w: int):
		pass

	def Hide(self):
		pass

	def HorizontalScrollBar(self):
		pass

	def Icon(self):
		pass

	def IconText(self):
		pass

	def InputMethodQuery(self,query: var11):
		pass

	def InsertAction(self,before: var0, action: var0):
		pass

	def InsertActions(self,before: var0, actions: var1):
		pass

	def IsA(self,classType: var3):
		pass

	def IsAction(self,id: int = 0):
		pass

	def IsActiveWindow(self):
		pass

	def IsChildOf(self,parent: var7):
		pass

	def IsConnectedTo(self,*args):
		pass

	def IsContainer(self):
		pass

	def IsDesktop(self):
		pass

	def IsDialog(self):
		pass

	def IsEnabled(self):
		pass

	def IsEnabledTo(self,ancestor: var2):
		pass

	def IsFullScreen(self):
		pass

	def IsHidden(self):
		pass

	def IsInputMethodEnabled(self):
		pass

	def IsMaximized(self):
		pass

	def IsMinimized(self):
		pass

	def IsModal(self):
		pass

	def IsPopup(self):
		pass

	def IsShown(self):
		pass

	def IsTopLevel(self):
		pass

	def IsUpdatesEnabled(self):
		pass

	def IsUsingBackingStore(self):
		pass

	def IsVisible(self):
		pass

	def IsVisibleTo(self,ancestor: var2):
		pass

	def IsWidgetType(self):
		pass

	def IsWindowModified(self):
		pass

	def KeyboardGrabber(self):
		pass

	def KillTimer(self,id: int):
		pass

	def Layout(self):
		pass

	def LineWidth(self):
		pass

	def Lower(self):
		pass

	def MapFrom(self,parent: var2, pos: var4):
		pass

	def MapFromGlobal(self,pos: var4):
		pass

	def MapFromParent(self,pos: var4):
		pass

	def MapTo(self,parent: var2, pos: var4):
		pass

	def MapToGlobal(self,pos: var4):
		pass

	def MapToParent(self,pos: var4):
		pass

	def MaxWidthOfStrings(self,strings: var12):
		pass

	def MaximumHeight(self):
		pass

	def MaximumSize(self):
		pass

	def MaximumWidth(self):
		pass

	def MidLineWidth(self):
		pass

	def MinimumHeight(self):
		pass

	def MinimumSize(self):
		pass

	def MinimumSizeHint(self):
		pass

	def MinimumWidth(self):
		pass

	def MouseGrabber(self):
		pass

	def Move(self,*args):
		pass

	def MoveToScreenCenter(self,screen: int = -1):
		pass

	def Name(self):
		pass

	def NeedsHorizontalScrollBar(self):
		pass

	def NeedsVerticalScrollBar(self):
		pass

	def ObjectFromUUID(self,uuid: var13):
		pass

	def OnAboutToShow(self):
		pass

	def OnAboutToShowAdvancedToolTip(self):
		pass

	def OnChange(self):
		pass

	def OnChildEvent(self):
		pass

	def OnClose(self):
		pass

	def OnContentsDragEnter(self):
		pass

	def OnContentsDragLeave(self):
		pass

	def OnContentsDragMove(self):
		pass

	def OnContentsDrop(self):
		pass

	def OnContentsMouseDoubleClick(self):
		pass

	def OnContentsMouseMove(self):
		pass

	def OnContentsMousePress(self):
		pass

	def OnContentsMouseRelease(self):
		pass

	def OnContentsMoving(self):
		pass

	def OnContextMenu(self):
		pass

	def OnDebugMessage(self):
		pass

	def OnDestroy(self):
		pass

	def OnDestroyItem(self):
		pass

	def OnDragEnter(self):
		pass

	def OnDragLeave(self):
		pass

	def OnDragMove(self):
		pass

	def OnDrop(self):
		pass

	def OnEnter(self):
		pass

	def OnFatalMessage(self):
		pass

	def OnFocusIn(self):
		pass

	def OnFocusOut(self):
		pass

	def OnHide(self):
		pass

	def OnHorizontalSliderPress(self):
		pass

	def OnHorizontalSliderRelease(self):
		pass

	def OnKeyPress(self):
		pass

	def OnKeyRelease(self):
		pass

	def OnLeave(self):
		pass

	def OnMouseDoubleClick(self):
		pass

	def OnMouseMove(self):
		pass

	def OnMousePress(self):
		pass

	def OnMouseRelease(self):
		pass

	def OnMove(self):
		pass

	def OnPaint(self):
		pass

	def OnPaintHandler(self,event: var14):
		pass

	def OnResize(self):
		pass

	def OnShow(self):
		pass

	def OnTraceMessage(self):
		pass

	def OnVerticalSliderPress(self):
		pass

	def OnVerticalSliderRelease(self):
		pass

	def OnWheel(self):
		pass

	def OnWinIdChange(self):
		pass

	def OverrideBackgroundMode(self):
		pass

	def OwnCursor(self):
		pass

	def OwnFont(self):
		pass

	def OwnPalette(self):
		pass

	def Palette(self):
		pass

	def PaletteBackgroundColor(self):
		pass

	def PaletteBackgroundPixmap(self):
		pass

	def PaletteForegroundColor(self):
		pass

	def Parent(self):
		pass

	def ParentWidget(self,*args):
		pass

	def ParentWidgetBelow(self,widget: var2):
		pass

	def PixelHeight(self,pixels: int):
		pass

	def PixelSize(self,pixelWidth: int, pixelHeight: int):
		pass

	def PixelWidth(self,pixels: int):
		pass

	def Pos(self):
		pass

	def PositionInsideDesktop(self):
		pass

	def PrepareForOffscreenRendering(self):
		pass

	def Raise(self):
		pass

	def Rect(self):
		pass

	def ReleaseKeyboard(self):
		pass

	def ReleaseMouse(self):
		pass

	def RemoveAction(self,action: var0):
		pass

	def RemoveChild(self,child: var2):
		pass

	def RemoveConnection(self,*args):
		pass

	def Render(self,*args):
		pass

	def Repaint(self,*args):
		pass

	def RepaintChildren(self):
		pass

	def RepaintContents(self,*args):
		pass

	def Reparent(self,*args):
		pass

	def Resize(self,*args):
		pass

	def ResizeContents(self,w: int, h: int):
		pass

	def Scroll(self,*args):
		pass

	def ScrollBy(self,dx: int, dy: int):
		pass

	def Sender(self):
		pass

	def SetAcceptDrops(self,arg0: bool):
		pass

	def SetActiveWindow(self):
		pass

	def SetAdvancedToolTipId(self,uuid: var15):
		pass

	def SetAlignment(self,arg2: var16):
		pass

	def SetAllowHiddenScrollBars(self,state: bool):
		pass

	def SetAutoFillBackground(self,arg2: bool):
		pass

	def SetBackgroundDarkness(self,darkness: int):
		pass

	def SetBackgroundMode(self,*args):
		pass

	def SetBackgroundRole(self,role: var17):
		pass

	def SetBadgeAlignment(self,align: var18):
		pass

	def SetBadgeColor(self,color: var19):
		pass

	def SetBaseSize(self,*args):
		pass

	def SetCanMove(self,canMove: bool):
		pass

	def SetCanResize(self,canResize: bool):
		pass

	def SetCaption(self,name: var15):
		pass

	def SetConnection(self,*args):
		pass

	def SetContentsPos(self,x: int, y: int):
		pass

	def SetContextMenuPolicy(self,policy: var20):
		pass

	def SetCursor(self,cursor: var21):
		pass

	def SetCustomSizeHint(self,size: var22):
		pass

	def SetDisabled(self,state: bool = True):
		pass

	def SetDropShadow(self,state: bool):
		pass

	def SetEnabled(self,state: bool = True):
		pass

	def SetEraseColor(self,color: var19):
		pass

	def SetErasePixmap(self,pixmap: var23):
		pass

	def SetEventPropagation(self,propagate: var6):
		pass

	def SetExcludeOverrideCursor(self,excludeOverrideCursor: bool):
		pass

	def SetFixedHeight(self,h: int):
		pass

	def SetFixedSize(self,*args):
		pass

	def SetFixedWidth(self,w: int):
		pass

	def SetFocus(self):
		pass

	def SetFocusPolicy(self,policy: var24):
		pass

	def SetFocusProxy(self,widget: var2):
		pass

	def SetFont(self,font: var25):
		pass

	def SetForceBackgroundPainting(self,state: bool):
		pass

	def SetForegroundRole(self,role: var17):
		pass

	def SetFrameRect(self,rect: var10):
		pass

	def SetFrameShadow(self,shadow: var26):
		pass

	def SetFrameShape(self,shape: var27):
		pass

	def SetFrameStyle(self,style: int):
		pass

	def SetGeomMgrAutoHideManagedWidgetsFlag(self,value: bool):
		pass

	def SetGeomMgrCanBeTopWidget(self,canBeTopWidget: bool):
		pass

	def SetGeomMgrIgnoreHideOnMinimizeFlag(self,value: bool):
		pass

	def SetGeomMgrPriority(self,priority: int):
		pass

	def SetGeomMgrShowTopLeft(self,showTopLeft: bool):
		pass

	def SetGeomMgrStartXHint(self,hint: var9):
		pass

	def SetGeomMgrXOffset(self,xOffset: int):
		pass

	def SetGeomMgrYOffset(self,yOffset: int):
		pass

	def SetGeometry(self,*args):
		pass

	def SetHScrollBarMode(self,arg0: int):
		pass

	def SetHasBadge(self,hasBadge: bool):
		pass

	def SetHidden(self,hide: bool):
		pass

	def SetIcon(self,pixmap: var23):
		pass

	def SetInputMethodEnabled(self,state: bool):
		pass

	def SetIsContainer(self,state: bool):
		pass

	def SetLayout(self,layout: var28):
		pass

	def SetLineWidth(self,width: int):
		pass

	def SetMask(self,bitmap: var29):
		pass

	def SetMaximumHeight(self,h: int):
		pass

	def SetMaximumSize(self,*args):
		pass

	def SetMaximumWidth(self,w: int):
		pass

	def SetMidLineWidth(self,width: int):
		pass

	def SetMinimumHeight(self,h: int):
		pass

	def SetMinimumSize(self,*args):
		pass

	def SetMinimumWidth(self,w: int):
		pass

	def SetMouseTracking(self,enable: bool):
		pass

	def SetName(self,name: var15):
		pass

	def SetOverrideBackgroundMode(self,mode: var30):
		pass

	def SetPalette(self,palette: var31):
		pass

	def SetPaletteBackgroundColor(self,color: var19):
		pass

	def SetPaletteBackgroundPixmap(self,pixmap: var23):
		pass

	def SetPaletteForegroundColor(self,color: var19):
		pass

	def SetShown(self,show: bool):
		pass

	def SetSizeIncrement(self,*args):
		pass

	def SetSizePolicy(self,*args):
		pass

	def SetStyle(self,*args):
		pass

	def SetTabOrder(self,first: var2, second: var2):
		pass

	def SetToolTip(self,*args):
		pass

	def SetTransparentBackground(self):
		pass

	def SetUUID(self,uuid: var13):
		pass

	def SetUpdatesEnabled(self,state: bool):
		pass

	def SetUseAlternateColor(self,state: bool):
		pass

	def SetUseHighlightColor(self,state: bool):
		pass

	def SetUseUnityStyle(self,state: bool):
		pass

	def SetUsesBackingStore(self,state: bool):
		pass

	def SetVScrollBarMode(self,arg0: int):
		pass

	def SetViewport(self,viewport: var2):
		pass

	def SetWhatsThis(self,text: var15):
		pass

	def SetWidget(self,widget: var2):
		pass

	def SetWidgetResizable(self,resizable: bool):
		pass

	def SetWidthForWidestString(self,strings: var12, horizMargin: int = 0):
		pass

	def SetWindowModality(self,windowModality: var32):
		pass

	def SetWindowModified(self,value: bool):
		pass

	def SetWindowOpacity(self,level: var33):
		pass

	def SetWindowState(self,windowState: var8):
		pass

	def Show(self):
		pass

	def ShowFullScreen(self):
		pass

	def ShowMaximized(self):
		pass

	def ShowMinimized(self):
		pass

	def ShowNormal(self):
		pass

	def SignalName(self,*args):
		pass

	def Size(self):
		pass

	def SizeHint(self):
		pass

	def SizeIncrement(self):
		pass

	def SizePolicy(self):
		pass

	def StackUnder(self,widget: var2):
		pass

	def Style(self):
		pass

	def TestAndDrawBadge(self):
		pass

	def TestWFlags(self,flags: var8):
		pass

	def ToolTip(self,*args):
		pass

	def TopLevelWidget(self):
		pass

	def TransparentBackground(self):
		pass

	def UUID(self):
		pass

	def UnsetCursor(self):
		pass

	def UnsetFont(self):
		pass

	def UnsetPalette(self):
		pass

	def Update(self,*args):
		pass

	def UpdateChildren(self):
		pass

	def UpdateContents(self,*args):
		pass

	def UpdateFont(self):
		pass

	def UpdateGeometry(self):
		pass

	def UseAlternateColor(self):
		pass

	def UseHighlightColor(self):
		pass

	def UsesUnityStyle(self):
		pass

	def VScrollBarMode(self):
		pass

	def VerticalScrollBar(self):
		pass

	def Viewport(self):
		pass

	def ViewportToContents(self,vp: var4):
		pass

	def VisibleHeight(self):
		pass

	def VisibleWidth(self):
		pass

	def WhatsThis(self):
		pass

	def Widget(self):
		pass

	def WidgetResizable(self):
		pass

	def Width(self):
		pass

	def WinId(self):
		pass

	def WindowModality(self):
		pass

	def WindowOpacity(self):
		pass

	def WindowState(self):
		pass

	def Wrap(self,widget: var34, createdWidget: var35 = None):
		pass

	def X(self):
		pass

	def Y(self):
		pass

	def addChildren(self,children):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class SecondaryRibbon:
	def __init__(self,*childrenArgs, children=None, persistSelected=True, allowAllOff=False, **kwds):
		"""
A sub Ribbon containing a list of SpriteActionGroups that appears under
     a SpriteActionGroup in the Ribbon.
  
"""
		pass

	@property
	def action(self):
		pass
	@action.setter
	def action(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def add(self,action, index=None):
		"""
		Adds the SpriteAction/SpriteActionGroup to Secondary Ribbon.

    Args:
      action (str | SpriteActionGroup): The action to be added.
      index (int): Index at which to insert the action.
    
		"""
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def allowAllOff(self):
		pass
	@allowAllOff.setter
	def allowAllOff(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def persistSelected(self):
		pass
	@persistSelected.setter
	def persistSelected(self):
		pass

	def remove(self,action):
		"""
		Removes the SpriteAction/SpriteActionGroup from Secondary Ribbon.

    Args:
      action (SpriteActionGroup): The action to be removed.

    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Signal:
	def __init__(self,wraps=None, emit=None, doc=None):
		"""
Wrap a C++ signal
"""
		pass

	def connect(self,obj, slot):
		pass

	def emit(self,slots, *args):
		pass

class Slider:
	def __init__(self,orientation: str="horizontal", **kwds):
		"""
A Slider Widget.
  
  The Slider is the classic widget for controlling a bounded value.

  A Slider Widget displays a range of values from which a user selects a single 
  value between a minimum and a maximum value.

  Slider widgets are usually created to control discrete integer values such as 
  the number of coils of a coil spring .
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the slider widget value.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def maxvalue(self):
		pass
	@maxvalue.setter
	def maxvalue(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def minvalue(self):
		pass
	@minvalue.setter
	def minvalue(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def pageStep(self):
		pass
	@pageStep.setter
	def pageStep(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value, emit=True):
		"""
		"Sets the slider widget value.
     Args:
       value (int): Value to set.
       emit (bool): If False, no signals emitted on value change otherwise emit
        the value change signal.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def tracking(self):
		pass
	@tracking.setter
	def tracking(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class SpacerItem:
	def __init__(self,width, height,spacing: str="horizontal", **kwds):
		"""
A Widget that adds a horizontal and vertical spacer.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	def isEmpty(self):
		"""
		Checks if the spacer item is empty.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def resize(self,width, height, spacing: str ='horizontal'):
		"""
		Resize the spacer item is empty.

    Args:
      width (float): Resize width of the spacer item.
      height (float): Resize height of the spacer item.
      spacing (str): It can be either 'horizontal' or 'vertical'.
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class SpinBox:
	def __init__(self,**kwds):
		"""
A SpinBox Widget.

  SpinBox allows to choose a value by clicking the up/down buttons or 
  pressing up/down on the keyboard to increase/decrease the displayed value.

  The upper and lower bounds are defined by the min and max properties.
  The user can also type the value manually. The SpinBox supports integer values
  and invokes the callback command every time the value is changed.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def max(self):
		pass
	@max.setter
	def max(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def min(self):
		pass
	@min.setter
	def min(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def prefix(self):
		pass
	@prefix.setter
	def prefix(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValue(self,value):
		"""
		Sets the specified value after converting it into an integer.

    Args:
      value (int): The numeric value to be set for the SpinBox.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def step(self):
		pass
	@step.setter
	def step(self):
		pass

	@property
	def suffix(self):
		pass
	@suffix.setter
	def suffix(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Splitter:
	def __init__(self,*childrenList, **kwds):
		"""
A Splitter Widget.
  
  A Splitter controls the relative size of the children widgets by 
  modifying the boundary between them.
  Splitter widget allows to create and control a dynamic layout of resizeable and 
  collapsible panes. This can be useful when the areas that the splitter divides
  have variable dimensions. 
  
  For example, the Demo dialog box shows a splitter 
  between the text edit area and the run edit. When the mouse pointer is located 
  in proximity of the splitter, it will change appearance. 
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def collapsible(self):
		pass
	@collapsible.setter
	def collapsible(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def opaqueResize(self):
		pass
	@opaqueResize.setter
	def opaqueResize(self):
		pass

	@property
	def orientation(self):
		pass
	@orientation.setter
	def orientation(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def sizes(self):
		pass
	@sizes.setter
	def sizes(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class SpriteAction:
	def __init__(self,parent=None,name: str="", **kwds):
		"""
A SpriteAction is a palette of PushButtons with icons.

  SpriteActions MUST be children of the SpriteActionGroup.
  The SpriteActionGroup can then be placed into the Unity RibbonPage.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.

    Warning, make sure to remove the action from the ui before destroying or
    this will crash!
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def exclusive(self):
		pass
	@exclusive.setter
	def exclusive(self):
		pass

	def get(self,name):
		"""
		Returns the named action from defined in active profile.

    Args:
      name (str): Action name.
    
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def ison(self):
		pass
	@ison.setter
	def ison(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self):
		"""
		Calls command callback method when an Action is clicked.
		"""
		pass

	def onToggle(self,on):
		"""
		Acts when an Action is toggled.

      - If is coupled to dialog it will show or hide the dialog.
      - If is coupled to a context it will get in and out the context.
      - If is coupled to callback it will run the callback with state or not.

    Args:
      on (bool): Determines whether to toggle on or off.
    
		"""
		pass

	@property
	def selectable(self):
		pass
	@selectable.setter
	def selectable(self):
		pass

	@property
	def statustip(self):
		pass
	@statustip.setter
	def statustip(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	def toggle(self,on=None):
		"""
		Simulate clicking the action.
    
    Args:
      on(bool | None): Pass True/False to ensure you are toggling on or off.
        None flips the state.
    
		"""
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def whatsthis(self):
		pass
	@whatsthis.setter
	def whatsthis(self):
		pass

class SpriteActionGroup:
	def __init__(self,parent=None,name: str="", **kwds):
		"""
A Palette of SpriteActions. 
  
  A SpriteActionGroup can be placed into a RibbonPage.
  
"""
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.

    Warning, make sure to remove the action from the ui before destroying or
    this will crash!
    
		"""
		pass

	@property
	def dropDown(self):
		pass
	@dropDown.setter
	def dropDown(self):
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def exclusive(self):
		pass
	@exclusive.setter
	def exclusive(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def showProgress(self,value, outOf=None, tooltip: str=""):
		"""
		Shows a progress meter icon to the left of the label text.

    Args:
      value (Union[float, bool]): Upper value of progress meter.
      outOf (float): Factor to divide value with.
      tooltip (str): The tool tip to show to the user if mouse cursor is on
        the progress bar.
    
		"""
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

def SpriteCommand(parent=None,name: str="", size=None, text=None, tooltip=None, visible=None, enabled=None, advancedTooltip=None, **kwds):
	"""
Syntactic sugar for groups which one action
    This create the group and the action and returns the group

  Args:
    parent(obj): parent of the sprite action group
    name(str): name of the sprite action
    size(float): size of the sprite action group
    text(str): Text to be displayed for the sprite action group
    tooltip(str): String to be displayed when mouse cursor is hovered over the
      sprite action group
    visible(bool): True/False if the sprite action group is visible
    enabled(bool): True/False if the sprite action group is enabled
    advancedTooltip(uuid): Provide the uuid to get the advanced tool tip from
      advancedTooltip.xml file

  Returns:
    returns a SpriteActionGroup
  
"""
	pass

class SpriteCounterAction:
	def __init__(self,parent=None,name: str="", **kwds):
		"""
A type of SpriteAction to display numbers.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.

    Warning, make sure to remove the action from the ui before destroying or
    this will crash!
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def exclusive(self):
		pass
	@exclusive.setter
	def exclusive(self):
		pass

	def get(self,name):
		"""
		Returns the named action from defined in active profile.

    Args:
      name (str): Action name.
    
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def ison(self):
		pass
	@ison.setter
	def ison(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self):
		"""
		Calls command callback method when an Action is clicked.
		"""
		pass

	def onToggle(self,on):
		"""
		Acts when an Action is toggled.

      - If is coupled to dialog it will show or hide the dialog.
      - If is coupled to a context it will get in and out the context.
      - If is coupled to callback it will run the callback with state or not.

    Args:
      on (bool): Determines whether to toggle on or off.
    
		"""
		pass

	@property
	def selectable(self):
		pass
	@selectable.setter
	def selectable(self):
		pass

	@property
	def statustip(self):
		pass
	@statustip.setter
	def statustip(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	def toggle(self,on=None):
		"""
		Simulate clicking the action.
    
    Args:
      on(bool | None): Pass True/False to ensure you are toggling on or off.
        None flips the state.
    
		"""
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def whatsthis(self):
		pass
	@whatsthis.setter
	def whatsthis(self):
		pass

class Stretch:
	def __init__(self,amount=1):
		"""
The stretchability of a BoxLayout.
  
"""
		pass

class String:
	def __init__(self,label: str="", readOnly=False, computed=False, **kwds):
		pass

	def castForSet(self,value):
		pass

	def getProperty(self,prop, row):
		pass

	def getValue(self,row):
		pass

	def init(self,i, name):
		pass

	def setProperty(self,prop, row):
		pass

class TabWidget:
	def __init__(self,**kwds):
		"""
NoteBook with tabs.

  A NoteBook presents multiple mutually exclusive panes of content in the same 
  area. It includes a tabbed control area with 'text' and a content area.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	def addTab(self,child, text: str="", icon=None):
		"""
		Inserts a new tab with the specified child.

    Args:
      child (Widget): The widget to be added to the tab.
      text (str): The text to be displayed on the tab.
      icon (str): The icon to be shown in the tab.
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def current(self):
		pass
	@current.setter
	def current(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	def insertTab(self,child, text: str="", icon=None, index=-1):
		"""
		Inserts a new tab with the specified child.

    Args:
      child (Widget): The widget to be added to the tab.
      text (str): The text to be displayed on the tab.
      icon (str): The icon to be shown in the tab.
      index (int): The index where to insert the tab.
    
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Table:
	def __init__(self,**kwds):
		"""
A Table widget used to display/edit a list of list of values.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	def addColumn(self,*values):
		"""
		Appends a column of values.

    Args:
      values (list[list[str]]): The values to be set in column of the table
    
		"""
		pass

	def addRow(self,*values):
		"""
		Appends a row of values.

    Args:
      values (list[list[str]]): The values to be set in row of the table
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clearSelection(self):
		"""
		Unselects all cells.
		"""
		pass

	@property
	def columnLabels(self):
		pass
	@columnLabels.setter
	def columnLabels(self):
		pass

	@property
	def columnStretchability(self):
		pass
	@columnStretchability.setter
	def columnStretchability(self):
		pass

	@property
	def columnWidth(self):
		pass
	@columnWidth.setter
	def columnWidth(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getCellTooltip(self,row, col):
		"""
		Gets the tooltip for specified row and column.

    Args:
      row (int): The row index of the table.
      col (int): The column index of the table.

    Returns:
      str: The tooltip at the specified row and column.
    
		"""
		pass

	def getColumnWidth(self,col=all):
		"""
		Gets the width of the column.

    Args:
      col (str | list[int]): The indices of columns.
      
    Returns:
      int: The width of the column.
    
		"""
		pass

	def getData(self,row, col):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	def getRowHeight(self,row=all):
		"""
		Gets the row height.

    Args:
       row (str | list[int]): A list of indices of rows.
    
		"""
		pass

	def getSelectedRows(self,full=False):
		"""
		Returns a list of row indices that are selected.
    
    Args:
      full (bool): If full is False, then if at least one cell in the row has to 
        selected to return the row index. If full is True, then every cell in the row 
        must be selected to return the row index. 
    
		"""
		pass

	def getValue(self,row, col):
		"""
		Gets the value from the specified row and column.

    Args:
      row (int): The row index of the table.
      col (int): The column index of the table.

    Returns:
      str: The text at the specified row and column.
    
		"""
		pass

	@property
	def hResizeMode(self):
		pass
	@hResizeMode.setter
	def hResizeMode(self):
		pass

	@property
	def hTooltips(self):
		pass
	@hTooltips.setter
	def hTooltips(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	def hideColumn(self,col):
		"""
		Hide specified column of the table.

    Args:
      col (int): The column index of the table.
    
		"""
		pass

	def hideRow(self,row):
		"""
		Hide specified row of the table.

    Args:
      row (int): The column index of the table.
    
		"""
		pass

	def isSelected(self,row, col):
		"""
		Returns True if the specified cell is selected, False otherwise.

    Args:
      row (int): The index of row.
      col (int): The index of col.
    
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def numCols(self):
		pass
	@numCols.setter
	def numCols(self):
		pass

	@property
	def numRows(self):
		pass
	@numRows.setter
	def numRows(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def readOnly(self):
		pass
	@readOnly.setter
	def readOnly(self):
		pass

	def removeColumn(self,indices):
		"""
		Removes a column or columns based on their indices.

    Args:
      indices (list[int]): The indices of columns to be removed from the table.
    
		"""
		pass

	def removeRow(self,indices):
		"""
		Removes a row or rows based on their indices.

    Args:
      indices (list[int], None): The indices of rows to be removed from the table.
        If none removes the last row of the table.
    
		"""
		pass

	@property
	def rowHeight(self):
		pass
	@rowHeight.setter
	def rowHeight(self):
		pass

	@property
	def rowLabels(self):
		pass
	@rowLabels.setter
	def rowLabels(self):
		pass

	@property
	def rowStretchability(self):
		pass
	@rowStretchability.setter
	def rowStretchability(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def selectCells(self,row=all, col=all, select=True, clear=True):
		"""
		Selects the specified cells.

    Args:
      row (str | list[int]): The indices of rows. 
      col (str | list[int]): The indices of columns.
      select (bool): Determines whether the specified cells will be selected.
      clear (bool):  Determines whether the previously selected will be cleared.
    
		"""
		pass

	def selectRow(self,row, clear=True):
		"""
		Selects all cells of a row and ensures the row is visible.

    Args:
      row (int): The row to be selected.
      clear (bool): Determines whether the previously selected will be cleared.
    
		"""
		pass

	def selectRows(self,rows=[], clear=True):
		"""
		Selects all specified rows.

    Args:
      row (list): The rows to be selected.
      clear (bool): Determines whether the previously selected will be cleared.
    
		"""
		pass

	@property
	def selectionBehavior(self):
		pass
	@selectionBehavior.setter
	def selectionBehavior(self):
		pass

	@property
	def selectionMode(self):
		pass
	@selectionMode.setter
	def selectionMode(self):
		pass

	def set(self,v):
		pass

	def setCellImage(self,row, col, file):
		"""
		Set image to specified cell of the table.

    Args:
      row (int): The row index of the table.
      col (int): The column index of the table.
      file (str): Image file name.
    
		"""
		pass

	def setCellTooltip(self,row, col, value):
		"""
		Sets the tooltip for specified row and column.

    Args:
      row (int): The row index of the table.
      col (int): The column index of the table.
      value (str): The tool tip to be set.
    
		"""
		pass

	def setColumnWidth(self,width, col=all):
		"""
		Sets the column width.

    Args:
      width (int): The width the column.
      col (str | list[int]): The indices of columns.
    
		"""
		pass

	def setData(self,row, col, data):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setHResizeMode(self,mode, col=all):
		"""
		Controls resize behavior of horizontal header.

    Args:
      mode (Table.ResizeMode)
      col (int | 'all')
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setRowHeight(self,height=20, row=all):
		"""
		Sets specific row height.

    Args:
      height (int): height to set the rows.
      row (str | list[int]): A list of indices of rows.
    
		"""
		pass

	def setVResizeMode(self,mode, row=all):
		"""
		Controls resize behavior of vertical header.

    Args:
      mode (Table.ResizeMode)
      row (int | 'all')
    
		"""
		pass

	def setValue(self,row, col, value):
		"""
		Sets the value from the specified row and column.

    Args:
      row (int): The row index of the table.
      col (int): The column index of the table.
      value (str): The value to be set.
    
		"""
		pass

	def setValues(self,values, rowOrder=False):
		"""
		Sets the cell text from the list of list of values.

    Args:
      values (list[list[str]]): The values to be set in cell of the table
      rowOrder (bool): Determines if values will be transposed.
    
		"""
		pass

	@property
	def shape(self):
		pass
	@shape.setter
	def shape(self):
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	def showColumn(self,col):
		"""
		Show specified column of the table if hidden.

    Args:
      col (int): The column index of the table.
    
		"""
		pass

	def showRow(self,row):
		"""
		Show specified row of the table if hidden.

    Args:
      row (int): The column index of the table.
    
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	def unselectCells(self,row=all, col=all):
		"""
		Deselects the specified cells.

    Args:
      row (str | list[int]): The indices of rows. 
      col (str | list[int]): The indices of columns.
    
		"""
		pass

	@property
	def vResizeMode(self):
		pass
	@vResizeMode.setter
	def vResizeMode(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def values(self):
		pass
	@values.setter
	def values(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class TableView:
	def __init__(self,values=[], **kwds):
		"""
A widget that presents data in a spreadsheet-like table view and
  provides means of visual observation and interaction with them.

  The data stored in TableView.values are a list of list.
  The outer list contains the rows and each nested list contains the values for the columns.
  When defyining a TableView, one MUST define the columns of the TableView.
  A column must contain information of the same data type.
  Consequently, each nested list of TableView.values must provide data of the correct type,
  and be of size equal to the TableView.columns.

  Examples of columns types are: views.Bool, views.Int, views.String, views.Float and views.Enum.

  To use it, it's suggested to inherit from it and define the type of columns.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	def addRow(self,row):
		"""
		Appends a row.
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clearSelection(self,emit=False):
		"""
		Unselects all cells.

    Args:
      emit (bool): Determines whether slots connected to onSelectionChange will
        be called or not.
    
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		"""
		(list[list]) The data the TableView holds.

    The outer list contains the rows and each nested list contains the values
    for the columns.
    
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	def getSelectedCells(self):
		"""
		A list of tuples specifying which cells are selected and in which order.

    Returns:
      list(tuple)
    
		"""
		pass

	def getSelectedRows(self):
		"""
		A list of indices specifying which rows are selected and in which order.

    Returns:
      list
    
		"""
		pass

	@property
	def hResizeMode(self):
		pass
	@hResizeMode.setter
	def hResizeMode(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def numCols(self):
		pass
	@numCols.setter
	def numCols(self):
		pass

	@property
	def numRows(self):
		pass
	@numRows.setter
	def numRows(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def removeRow(self,index):
		"""
		Deletes a row based on index.
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def selectCell(self,row, col, clear=True, emit=False):
		"""
		Selects a cells.

    Args:
      row (int): The index of the row to be selected.
      col (int): The index of the column to be selected.
      clear (bool): Determines whether the previously selected will be cleared.
      emit (bool): Determines whether slots connected to onSelectionChange
        will be called or not.
    
		"""
		pass

	def selectColumn(self,col, clear=True, emit=False):
		"""
		Selects all cells of a column.

    Args:
      col (int): The index of the column to be selected.
      clear (bool): Determines whether the previously selected will be cleared.
      emit (bool): Determines whether slots connected to onSelectionChange will
        be called or not.
    
		"""
		pass

	def selectRow(self,row, clear=True, emit=False):
		"""
		Selects all cells of a row.

    Args:
      row (int): The index of the row to be selected.
      clear (bool): Determines whether the previously selected will be cleared.
      emit (bool): Determines whether slots connected to onSelectionChange will
        be called or not.
    
		"""
		pass

	@property
	def selectionBehavior(self):
		pass
	@selectionBehavior.setter
	def selectionBehavior(self):
		pass

	@property
	def selectionMode(self):
		pass
	@selectionMode.setter
	def selectionMode(self):
		pass

	def set(self,values):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setHResizeMode(self,mode, col=all):
		"""
		Controls resize behavior of the cells in the horizontal axis.

    Args:
      mode (TableView.ResizeMode)
      col (int | 'all')
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setVResizeMode(self,mode, row=all):
		"""
		Controls resize behavior of the cells in the vertical axis.

    Args:
      mode (TableView.ResizeMode)
      row (int | 'all')
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def vResizeMode(self):
		pass
	@vResizeMode.setter
	def vResizeMode(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def values(self):
		pass
	@values.setter
	def values(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class TextEdit:
	def __init__(self,text: str="", **kwds):
		"""
A TextEdit Widget.
  
  It is used to display and modify formatted and HTML text.
  It can be editable or not. Ctrl+Wheel zooms in/out.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self,*args):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def html(self):
		pass
	@html.setter
	def html(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	def onKeyPress(self,event):
		"""
		Callback method when a key is pressed on the TextEdit widget.

    <Ret> adds a new line, lets add <Shift+Ret> for onCommand.

    Args:
      event (KeyEvent): Event to get key pressed.
    
		"""
		pass

	def onWheelHandler(self,event):
		"""
		Callback method when the mouse wheel is rotated inside the TextEdit widget.

    Ctrl+Wheel Zooms in/out.

    Args:
      event (KeyEvent, MouseEvent): The key event to capture the ctrl pressed and
        mouse wheel event to determine if is used zoom in or out.
    
		"""
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	@property
	def readonly(self):
		pass
	@readonly.setter
	def readonly(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setStyleToSection(self,paraFrom, indexFrom, paraTo, indexTo, color=None, size=None, bold=False, italic=False):
		"""
		Function to set style (color/bold/italic/size) to a particular section
    in text.

    Args:
      paraFrom (int): Starting paragraph number.
      indexFrom (int): Index in starting paragraph.
      paraTo (int): Ending paragraph number.
      indexTo (int): Index in ending paragraph.
      color (string | tupleint)): Text color. It can be RGB values in form of
        tuple or color name.
      size (int): Text size.
      bold (bool): If True, text will be bold.
      italic (bool): If True, text will be italic.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ToggleButton:
	def __init__(self,text=None, **kwds):
		"""
A ToggleButton

  Toggle on off the Button to command the computer to preform some action.
  ToggleButton is usually used in a ToolBar without text.

  The ToggleButton is a specialized control that has the abilty of being selected.
  ToggleButtons, when clicked, display their state (selected or unselected). 
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class ToolButton:
	def __init__(self,text=None, **kwds):
		"""
A ToolButton.

  Click the Tool Button to do something. 
  Tool Button is usually used in a ToolBar without text.
  
"""
		pass

	@property
	def accel(self):
		pass
	@accel.setter
	def accel(self):
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def autoRepeat(self):
		pass
	@autoRepeat.setter
	def autoRepeat(self):
		pass

	@property
	def checkable(self):
		pass
	@checkable.setter
	def checkable(self):
		pass

	@property
	def checked(self):
		pass
	@checked.setter
	def checked(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	@property
	def dialog(self):
		pass
	@dialog.setter
	def dialog(self):
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def flat(self):
		pass
	@flat.setter
	def flat(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Ensure proper order of setting properties.

    Args:
      kwds: A dict so the  order of the properties are set is unpredictable
        checkable must be set before checked, or checked will not take effect.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Tree:
	def __init__(self,headers=None, **kwds):
		"""
Hierarchical list of items.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def add(self,parent=None, text=None, icon=None, **kwds):
		"""
		Adds a TreeItem to the Tree.

    Args:
      parent (TreeItem): A TreeItem to define hierarchy. 
      text (str|list[str]): Text or List of text that gets displayed in column.
      icon (str|list[str]): Absolute path of the icon or a list of icons.

    Returns:
      TreeItem: the added TreeItem.
    
		"""
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	def addColumn(self,label, width=-1):
		"""
		Adds one or more columns to the tree, width pixes wide.

    All columns apart from the first one are inserted to the right of the
    existing ones. 
    If width is negative, the new column's width is set to maximum.

    Args:
      label (str|list[str]): Name of the column.
      width (int|list[int]): How wide each column is in pixels.
    
    Returns:
      list[int]: The indices of the new columns.
    
		"""
		pass

	def addWidget(self,widget, col, item):
		"""
		Add any widget to a tree item.

    Args:
      widget (gui.Widget): Widget needs to be inserted.
      col (int): Column index of TreeItem in which widget needs to be inserted.
      item (TreeItem): TreeItem in which widget needs to be inserted.

    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Removes all items from the tree.
		"""
		pass

	def collapseAll(self):
		"""
		Collapses all items.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableEdit(self,col=None, edit=True):
		"""
		Makes all tree items or specific tree column to be editable.

    Args:
      col (int): Column index needs to be make editable.
      edit (bool): If True, column is editable else not.

    
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	def ensureItemVisible(self,item):
		"""
		Scrolls view so this item is visible.

    Args:
      item (TreeItem): TreeItem to make visible.
    
		"""
		pass

	def expandAll(self,expanded=True):
		"""
		Expands (or collapses) all items.

    Args:
      expanded (bool): Determines whether to expand or not. 
    
		"""
		pass

	def fitColumns(self):
		"""
		Fit the columns in the tree.
		"""
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the current selected item.
    
		"""
		pass

	def getChildren(self,parent=None):
		"""
		Overloaded Widget method for 'children' property.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	def getSelected(self):
		"""
		Returns a list of the selected items.
		"""
		pass

	@property
	def header(self):
		pass
	@header.setter
	def header(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	def hideColumn(self,column):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	@property
	def numCols(self):
		pass
	@numCols.setter
	def numCols(self):
		pass

	def onCommand(self,event=None):
		pass

	def onSelectionChange(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def remove(self,item):
		"""
		Removes the specified item from the tree.

    Args:
      item (TreeItem): Item to be removed.
    
		"""
		pass

	def removeColumn(self,indices):
		"""
		Removes columns based on their initial indices.

    Args:
      indices (int|list[int])
    
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	@property
	def selectionMode(self):
		pass
	@selectionMode.setter
	def selectionMode(self):
		pass

	def set(self,v):
		pass

	def setColumnWidth(self,column, width):
		"""
		Set the width of a particular column in a tree.

    Args:
      column (int): Column index of tree.
      width (int): Width of the column.

    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setSelected(self,items, selected=True, clear=True):
		"""
		Selects the specified items.

    Args:
      items (list[TreeItem]): list of TreeItems to be selected.
      selected (bool): Determines if items will be selected or not. 
      clear (bool): Determines if al previously selected items will be cleared or not.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	def showColumn(self,column):
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	def sort(self,column, ascending):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class TreeItem:
	def __init__(self,tree, parent, text, data=None, icon=None, **kwds):
		"""
An item in a Tree.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def add(self,text, icon=None, **kwds):
		"""
		Adds a TreeItem to the Tree.

    Args:
      text (str): Text that gets displayed.
      icon (str): Absolute path of the icon.

    Returns:
      TreeItem: The added TreeItem.
    
		"""
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Removes all the children from the tree.
		"""
		pass

	def collapse(self):
		"""
		Collapse the tree item.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableEdit(self,col, edit=True):
		"""
		Makes a column of a tree item editable.

    Args:
      col (int): Column index needs to be make editable.
      edit (bool): If True, column is editable else not.

    
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	def ensureVisible(self):
		"""
		Ensures this TreeItem is visible.
		"""
		pass

	def expand(self):
		"""
		Expand the tree item.
		"""
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getChildren(self):
		"""
		Overloaded Widget method for 'children' property.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def icon(self):
		pass
	@icon.setter
	def icon(self):
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def remove(self):
		"""
		Removes the item from the Tree.
		"""
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def selectAndShow(self,clear=True):
		"""
		Selects and makes this TreeItem visible.
    
		"""
		pass

	@property
	def selectable(self):
		pass
	@selectable.setter
	def selectable(self):
		pass

	@property
	def selected(self):
		pass
	@selected.setter
	def selected(self):
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def text(self):
		pass
	@text.setter
	def text(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class VBoxLayout:
	def __init__(self,*childrenList, **kwds):
		"""
Layout widgets vertically.
"""
		pass

	def addChildren(self,children):
		"""
		Adds the specified children in the BoxLayout.

    Args:
      children (list[Widget]): The items to be added.
    
		"""
		pass

	@property
	def border(self):
		pass
	@border.setter
	def border(self):
		pass

	@property
	def margin(self):
		pass
	@margin.setter
	def margin(self):
		pass

	@property
	def resizeMode(self):
		pass
	@resizeMode.setter
	def resizeMode(self):
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	@property
	def spacing(self):
		pass
	@spacing.setter
	def spacing(self):
		pass

class VCheckboxes:
	def __init__(self,values, value=0, **kwds):
		"""
Group of Checkboxes layed out verically.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Destroys the button.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns a set of checked values in the Checkboxes.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,values):
		"""
		Check/Uncheck the value in the Checkboxes.

    Args:
      values (list[str]): The list of values corresponding to each checkbox.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Specify the options. A button is created for each option.

    Args:
      values (list[str, str]): list of (value, displayName) tuples.
      value (list[str] | list[int] ): Set new values.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class VFrame:
	def __init__(self,*childrenList, **kwds):
		"""
A Frame with a VBoxLayout.

  VFrame groups controls vertically so they can be sized and/or decorated as 
  one.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	@property
	def frameShape(self):
		pass
	@frameShape.setter
	def frameShape(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class VRadioButtons:
	def __init__(self,values, value=0, **kwds):
		"""
Group of mutually exclusive RadioButtons layed out verically.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	def clear(self):
		"""
		Destroys the button.
		"""
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		"""
		Returns the checked item.
		"""
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		"""
		Set the item checked.

    Args:
      v (int): Index of the item to checked.
    
		"""
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def setValues(self,values, value=None):
		"""
		Specify the options. A button is created for each option.

    Args:
      values (list[str, str]): list of (value, displayName) tuples.
      value (list[str] | list[int] ): Set new values.
    
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

def VScrollBar(**kwds):
	pass

def VSlider(**kwds):
	pass

class VSplitter:
	def __init__(self,*childrenList, **kwds):
		"""
A Splitter with vertical orientation.
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def collapsible(self):
		pass
	@collapsible.setter
	def collapsible(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def opaqueResize(self):
		pass
	@opaqueResize.setter
	def opaqueResize(self):
		pass

	@property
	def orientation(self):
		pass
	@orientation.setter
	def orientation(self):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def sizes(self):
		pass
	@sizes.setter
	def sizes(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Widget:
	def __init__(self):
		"""
Abstract base class for all widgets.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,v):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class WidgetStack:
	def __init__(self,widgets=[], **kwds):
		"""
A WidgetStack is used to display one widget at a time, generally depending 
  on conditions or actions of other widgets.
  
"""
		pass

	@property
	def active(self):
		pass
	@active.setter
	def active(self):
		pass

	def addChildren(self,children):
		"""
		Add child widgets/layouts into this widget.
    
    Widget children get layed out using a VBoxLayout.

    Typically, you'll pass the parent/children into the constructor instead of
    calling this function directly.

    Args:
      children (list[Widget] | Layout)
    
		"""
		pass

	@property
	def advancedTooltip(self):
		pass
	@advancedTooltip.setter
	def advancedTooltip(self):
		pass

	@property
	def children(self):
		pass
	@children.setter
	def children(self):
		pass

	@property
	def command(self):
		pass
	@command.setter
	def command(self):
		pass

	@property
	def descendents(self):
		pass
	@descendents.setter
	def descendents(self):
		pass

	def destroy(self):
		"""
		Deletes this and all its children.
		"""
		pass

	def enableGlobalActions(self,enable):
		"""
		Sets the state of Global Actions.

    Disable the global actions to get key events.

    Args:
      enable (bool): Determines whether to enable or disable global actions.
    
		"""
		pass

	@property
	def enabled(self):
		pass
	@enabled.setter
	def enabled(self):
		pass

	@property
	def font(self):
		pass
	@font.setter
	def font(self):
		pass

	def get(self):
		pass

	def getMousePosition(self):
		"""
		Returns the mouse position.
		"""
		pass

	def getRelativeMousePosition(self):
		"""
		Returns the mouse position relative to this widget.
		"""
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def helpTopic(self):
		pass
	@helpTopic.setter
	def helpTopic(self):
		pass

	def hide(self):
		"""
		Hides the widget.
		"""
		pass

	@property
	def layout(self):
		pass
	@layout.setter
	def layout(self):
		pass

	@property
	def maximumHeight(self):
		pass
	@maximumHeight.setter
	def maximumHeight(self):
		pass

	@property
	def maximumWidth(self):
		pass
	@maximumWidth.setter
	def maximumWidth(self):
		pass

	@property
	def minimumHeight(self):
		pass
	@minimumHeight.setter
	def minimumHeight(self):
		pass

	@property
	def minimumWidth(self):
		pass
	@minimumWidth.setter
	def minimumWidth(self):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def onCommand(self,event=None):
		pass

	@property
	def parent(self):
		pass
	@parent.setter
	def parent(self):
		pass

	def saveAsPng(self,fname):
		"""
		Saves the widget as a .png file.

    Args:
      fname (str): The file name for the .png

    Returns:
      bool : True if it was saved succesfully, False otherwise. 
    
		"""
		pass

	def set(self,value):
		pass

	def setF1HelpTopic(self,helptopic):
		"""
		Popup web-browser helps when the user hits F1 when over this.

    Args:
      helptopic (str): Topic name user needs help in.
    
		"""
		pass

	def setProperties(self,kwds):
		"""
		Internal method called from constructors.
		"""
		pass

	def show(self):
		"""
		Shows the widget.
		"""
		pass

	@property
	def size(self):
		pass
	@size.setter
	def size(self):
		pass

	@property
	def tooltip(self):
		pass
	@tooltip.setter
	def tooltip(self):
		pass

	@property
	def value(self):
		pass
	@value.setter
	def value(self):
		pass

	@property
	def visible(self):
		pass
	@visible.setter
	def visible(self):
		pass

	@property
	def visibleWidget(self):
		pass
	@visibleWidget.setter
	def visibleWidget(self):
		pass

	@property
	def widgets(self):
		pass
	@widgets.setter
	def widgets(self):
		pass

	@property
	def width(self):
		pass
	@width.setter
	def width(self):
		pass

class Widgets:
	"""

This module implements the gui widgets and layouts

  Containers:
    Frame         - Generic widget container
    VFrame        - Frame with a VBoxLayout
    HFrame        - Frame with a HBoxLayout
    GridFrame     - Frame with a GridLayout
    NoteBook      - Tabbed pages
    Legend        - Color and text association

  Widgets:
    Label         - Show some text
    IconLabel     - Show an icon strip
    LineEdit      - Show/Edit a string
    DoubleEdit    - LineEdit for Doubles
    TextEdit      - Show/Edit rich text or html
    PushButton    - Click to do something
    RadioButton   - On/Off button
    VRadioButtons - Group of RadioButtons layed out vertically
    HRadioButtons - Group of RadioButtons layed out horizontally
    CheckBox      - True/False
    ComboBox      - Select one of
    SpinBox       - Set an integer
    Slider        - Control a bounded value

  Layouts:
    VBoxLayout    - Layout widgets horizontally
    HBoxLayout    - Layout widgets vertically
    GridLayout    - Layout widgets in rows and columns
    WidgetStack   - One widget displayed at a time

  Other
    ButtonGroup   - Make Buttons mutually exclusive
    Stretch       - Add stretchability to a layout
    Cursors       - Set the cursor

  Composites:
    CollapsibleFrame
    ComboButtonsWidgetStack
    RadioButtonsWithWidgets


"""
	pass

class XyPlot:
	pass

def addResourcePath(path, recursive=True):
	"""
Add the path to list of paths used to lookup resources like icons.
    The path can be a full path name, relative to the system directory
    where the application is installed.

  Args:
    path(str): resource path to be added
    recursive(bool): True/False to add the path recursively, defaults to True
  
"""
	pass

class cached_property:
	def __init__(self,func):
		pass

class classproperty:
	def __init__(self,fget=None, fset=None, fdel=None, doc=None):
		"""
Like classmethod but for properties.
  
  Used to give cls.attr a docstring and run a function.
  
  Use inspect.getattr_static to get the descriptor.
  
"""
		pass

class collections:
	pass

class contextlib:
	"""
Utilities for with-statement contexts.  See PEP 343.
"""
	pass

class cycle:
	def __init__(self,iterable):
		"""
Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.
"""
		pass

class enum:
	pass

def extendProfile(profile, command):
	"""
Extend an existing profile with a new ribbon

  Args:
    profile(str): Name of the profile
    command(callback): a callback to create the ribbon
  
"""
	pass

def findInResourcePath(filename):
	"""
Lookup full file path in folders added to gui.addResourcePath(...).
  
  Args:
    filename (str)
    
  Returns:
    str
  
"""
	pass

def getAction(action):
	"""
Gets the named action for the current profile

  Args:
    action(str): name of the action

  Returns:
    Profile: returns the action from the current profile
  
"""
	pass

def getDemoFilePath(file):
	pass

def getExistingDirectory(startWith: str="",caption: str="", dirOnly=True, resolveSymLinks=True):
	"""
Pops up a file dialog to specify a list of names of files to read.

  Args:
    startWith (str): File or Directory to start the selection. 
    caption (str):  Text displayed in the title bar.
    dirOnly (bool): Determines whether to show directories only.
    resolveSymLinks (bool): For Linux/Mac.

  Returns:
    str: The directory name.
  
"""
	pass

def getExtensionManager():
	"""
Returns the singleton instance of the Extension Manager.
"""
	pass

def getMainWindow():
	"""
Return the main application window
"""
	pass

def getOpenFileName(startWith: str="",filter: str="",caption: str="", resolveSymLinks=True, remember=None,selectedFilter: str="", returnFilter=False, forget=None):
	"""
Pops up a file dialog to specify a name of a file to read.

  Args:
    startWith (str): File or Directory to start the selection. 
    filter (str): Show only those files which match the filter.
      The filter is a string with a description followed by file extensions in
      parentheses. Multiple filters can be specified by separating them with 
      double semicolons: filter = "Text files(*.txt);;All Files(*.*)".
    caption (str):  Text displayed in the title bar.
    resolveSymLinks (bool): For Linux/Mac.
    remember ([type]): Determines whether to remember the last directory the user navigated to.
    selectedFilter (str): The filter that is preselected.
    returnFilter (bool): Determines whether to return the chosen filter.
    forget (signal object): Upon emitting the signal, it clears the user's previously accessed directory.

  Returns:
    str: The file name.
  
"""
	pass

def getOpenFileNames(startWith: str="",filter: str="",caption: str="", resolveSymLinks=True,selectedFilter: str="", returnFilter=False):
	"""
Pops up a file dialog to specify a list of names of files to read.

  Args:
    startWith (str): File or Directory to start the selection. 
    filter (str): Show only those files which match the filter.
      The filter is a string with a description followed by file extensions in
      parentheses. Multiple filters can be specified by separating them with 
      double semicolons: filter = "Text files(*.txt);;All Files(*.*)".
    caption (str):  Text displayed in the title bar.
    resolveSymLinks (bool): For Linux/Mac.
    selectedFilter (str): The filter that is preselected.
    returnFilter (bool): Determines whether to return the chosen filter.

  Returns:
    str: The file name.
  
"""
	pass

def getProfile(profile=None):
	"""
Gets the named profile, if no profile is specified returns the active
     profile.

  Args:
    profile(str): Name of the profile you want to get

  Returns:
     Profile: returns the named profile
  
"""
	pass

def getResource(resource):
	"""
Lookup and return a file name for a resource
    The resource paths are set using addResourcePath

  Args:
    resource(str): resource to be searched

  Returns:
    str: returns the filename of the resource
  
"""
	pass

def getSaveFileName(startWith: str="",filter: str="",caption: str="", resolveSymLinks=True, confirmOverwrite=True, remember=None,selectedFilter: str="", returnFilter=False, forget=None):
	"""
Pops up a file dialog to specify a name of a file to write.

  Args:
    startWith (str): File or Directory to start the selection. 
    filter (str): Show only those files which match the filter.
      The filter is a string with a description followed by file extensions in
      parentheses. Multiple filters can be specified by separating them with 
      double semicolons: filter = "Text files(*.txt);;All Files(*.*)".
    caption (str):  Text displayed in the title bar.
    resolveSymLinks (bool): For Linux/Mac.
    confirmOverwrite (bool): Prompt the user when about to overwrite an existing file.
    remember ([type]): Determines whether to remember the last directory the user navigated to.
    selectedFilter (str): The filter that is preselected.
    returnFilter (bool): Determines whether to return the chosen filter.
    forget (signal object): Upon emitting the signal, it clears the user's previously accessed directory.

  Returns:
    str: The file name.
  
"""
	pass

def getSystemDirectory():
	"""
Return the path to the installation
"""
	pass

class gui:
	"""

  Client independent GUI code
  
  Framework - create new clients or add new profiles to existing clients
  Ribbon    - add a new ribbon page to an existing profile
  Widgets   - standard GUI controls
  Dialogs   - Dialog boxes
  Tree      - Hierachical list 
  Actions   - GUI commands including SpriteActions

"""
	pass

class hwStringList:
	def __init__(self,*args):
		pass

	def append(self,x: var36):
		pass

	def assign(self,n: var37, x: var36):
		pass

	def back(self):
		pass

	def begin(self):
		pass

	def capacity(self):
		pass

	def clear(self):
		pass

	def empty(self):
		pass

	def end(self):
		pass

	def erase(self,*args):
		pass

	def front(self):
		pass

	def get_allocator(self):
		pass

	def insert(self,*args):
		pass

	def iterator(self):
		pass

	def pop(self):
		pass

	def pop_back(self):
		pass

	def push_back(self,x: var36):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: var37):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: var38):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwappwidgets:
	pass

class hwfwc:
	pass

class hwfwg:
	pass

class hwtableview:
	pass

class hwtypes:
	pass

class hwui:
	pass

class hwuiCanvas:
	pass

class hwuiExtensions:
	pass

def installTranslations(file):
	"""
Install the translation file (*.qm) to handle internationalization.

     NOTE: Translation must currently be in unity/config/translations.

  Args:
    file(str): Only the basename of the file minus the locale
      (ex. Inspire for Inspire_en_US.qm). Locale will automatically be added on.
  
"""
	pass

def isAltDown():
	"""
Lets the user know if Alt key is pressed down
"""
	pass

def isCtrlDown():
	"""
Lets the user know if Ctrl key is pressed down
"""
	pass

def isShiftDown():
	"""
Lets the user know if Shift key is pressed down
"""
	pass

def iterate(x):
	"""
Iterate over x or yield x if not iterable
"""
	pass

class math:
	"""
This module provides access to the mathematical functions
defined by the C standard.
"""
	pass

def onIdle(func, *args, **kwds):
	"""
Delay executing the function until we process idle events.  
    
       Arguments can be specified via args, kwds - for convenience.
"""
	pass

class onIdleOnceDecorator:
	def __init__(self):
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

class pathlib:
	pass

def processEvents():
	"""
Let the user interact with the gui during long operations
  
"""
	pass

def registerToolTipFile(file):
	"""
Register advanced tool tip xml file containing tooltip for all the
    action on loaning plugins

  Args:
    file(str): advanced tool tip xml file
  
"""
	pass

def runClient(client, profile=None, **kwds):
	"""
Startup product with client and profile.

     Useful to create a standalone application by customizing an existing
     client/profile.

     This is done by calling runClient from a script that is run with:
     hwx -f <path to script>

     Then customize...

  Args:
    client(str): Name of the client
    profile(str): Name of the profile to run
  
"""
	pass

def runningInDarkTheme():
	"""
Return True if the application runs in dark theme, False otherwise.
  
  Returns:
    bool : Returns True in dark theme, else False.
  
"""
	pass

def setCursor(cursor=None):
	"""
Sets the specified cursor

  Args:
    cursor(str): name of the cursor to be set
  
"""
	pass

def setFileTypes(openFileTypes=None, saveFileTypes=None, removeOpenFileTypes=None, removeSaveFileTypes=None):
	"""
Update the open/save file filters.

  Args:
    openFileTypes(list[str]): Acceptable file types while opening of a file
    saveFileTypes(list[str]): Acceptable file types while saving a file
    removeOpenFileTypes(list[str]): Unacceptable file types while opening of a file
    removeSaveFileTypes(list[str]: Unacceptable file types while saving of a file
  
"""
	pass

def setStatusBarMessage(message, ms=None):
	"""
Write a message to the status bar.

  Args:
    message (str): message to be displayed.
    ms (str): milli-seconds value to be shown in the status bar, the message will
      be cleared after ms milli-seconds.
  
"""
	pass

def show(widget):
	"""
Provision to copy/paste demo code into the Python Window
"""
	pass

def showError(message):
	"""
Popup up the MessageDialog with an error

  Args:
    message (str): The error message to be displayed in the message dialog.
  
"""
	pass

def showHelp(helptopic):
	"""
Popup webbrowser help for topic

  Args:
    helptopic(str): Topic name which the user needs help in
  
"""
	pass

def showSuccess(message,color: str="green"):
	"""
Popup up the MessageDialog with a message displaying a check.

  Args:
    message (str): The success message to be displayed in the message dialog.
    color (str): The background color of the check icon. 
      Acceptable values are 'green' and 'red'.
  
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

def tellUser(message):
	"""
Popup up the MessageDialog with information

  Args:
    message (str): The information message to be displayed in the message dialog.
  
"""
	pass

def tr(string, **kwds):
	pass

def translate(string, context=None, comment=None, args=None):
	"""
Return the string translated into the users language

  Using the tr method in a file indicates what strings are to be translated
  The translation processes includes reading source file, extracting strings
  inside tr methods and placing them in a source translation file.
  This file is input to a tool used by translators to create language
  specific files.

  Not-Pythonic but makes them consistent with the C++ messages for the
  person generating the translation files

  Args:
    string(str): When the application runs and this method is called, the
      translated string from the language specific file is returned.
    context: Is used to make the string unique so the same string can be used
      but translated differently.
    comments(str) :are added to the translation source file to help the
      translator with the translation.
    args(list): A list/tuple of values that are inserted into the string
      the location of the values are indicated using a one(1) based position
      notation identified with a %.
      For example:
          tr ("The first value %2 and the second value %1", args=(2,1))

  Returns:
    str: returns the translated string
  
"""
	pass

class uiAbstractItemView:
	def __init__(self,*args):
		pass

	def AcceptDrops(self):
		pass

	def Action(self,*args):
		pass

	def Actions(self):
		pass

	def AddAction(self,action: var0):
		pass

	def AddActions(self,actions: var1):
		pass

	def AddChild(self,child: var2, x: int = 0, y: int = 0):
		pass

	def AdjustSize(self):
		pass

	def AdvancedToolTipId(self):
		pass

	def Alignment(self):
		pass

	def AllowHiddenScrollBars(self):
		pass

	def AsConcreteListener(self):
		pass

	def AsListener(self):
		pass

	def AutoFillBackground(self):
		pass

	def AverageWidth(self,chars: int):
		pass

	def BackgroundDarkness(self):
		pass

	def BackgroundMode(self):
		pass

	def BackgroundRole(self):
		pass

	def BadgeAlignment(self):
		pass

	def BadgeColor(self):
		pass

	def BaseSize(self):
		pass

	def CanMove(self):
		pass

	def CanResize(self):
		pass

	def Caption(self):
		pass

	def CellGeometry(self,index: var39):
		pass

	def Child(self,objName: var3, inheritsClass: var3 = None, recursiveSearch: bool = True):
		pass

	def ChildAt(self,*args):
		pass

	def Children(self):
		pass

	def ChildrenRect(self):
		pass

	def ClassName(self):
		pass

	def ClearFocus(self):
		pass

	def ClearMask(self):
		pass

	def ClearSelection(self):
		pass

	def Close(self,alsoDelete: bool = False):
		pass

	def ClosePersistentEditor(self,index: var39):
		pass

	def Color0(self):
		pass

	def Color1(self):
		pass

	def ColorBlack(self):
		pass

	def ColorBlue(self):
		pass

	def ColorCyan(self):
		pass

	def ColorDarkBlue(self):
		pass

	def ColorDarkCyan(self):
		pass

	def ColorDarkGray(self):
		pass

	def ColorDarkGreen(self):
		pass

	def ColorDarkMagenta(self):
		pass

	def ColorDarkRed(self):
		pass

	def ColorDarkYellow(self):
		pass

	def ColorGray(self):
		pass

	def ColorGreen(self):
		pass

	def ColorGroup(self):
		pass

	def ColorLightGray(self):
		pass

	def ColorMagenta(self):
		pass

	def ColorRed(self):
		pass

	def ColorWhite(self):
		pass

	def ColorYellow(self):
		pass

	def ContentsHeight(self):
		pass

	def ContentsRect(self):
		pass

	def ContentsToViewport(self,p: var4):
		pass

	def ContentsWidth(self):
		pass

	def ContentsX(self):
		pass

	def ContentsY(self):
		pass

	def ContextMenuPolicy(self):
		pass

	def CurrentIndex(self):
		pass

	def Cursor(self):
		pass

	def CustomFocusNextPrevChild(self,next: bool):
		pass

	def CustomSizeHint(self):
		pass

	def DeleteLater(self):
		pass

	def Disconnect(self,sender: var5, force: var6 = False):
		pass

	def DisconnectAll(self,force: var6 = False):
		pass

	def DluHeight(self,*args):
		pass

	def DluPixelHeight(self,pixels: int):
		pass

	def DluPixelSize(self,pixelWidth: int, pixelHeight: int):
		pass

	def DluPixelWidth(self,pixels: int):
		pass

	def DluWidth(self,*args):
		pass

	def DownCast(self,o: var7):
		pass

	def DragDropMode(self):
		pass

	def DragEnabled(self):
		pass

	def DrawHighlightIndicators(self,p: var40, rect: var10, index: var39):
		pass

	def DumpTree(self):
		pass

	def Edit(self,index: var39):
		pass

	def EditTriggers(self):
		pass

	def EnsureWidgetVisible(self,childWidget: var2, xmargin: int = 50, ymargin: int = 50):
		pass

	def EraseColor(self):
		pass

	def ErasePixmap(self):
		pass

	def EventInfo(self):
		pass

	def EventPropagation(self):
		pass

	def ExcludeOverrideCursor(self):
		pass

	def Find(self,winId: var8):
		pass

	def FindBackgroundDarkness(self):
		pass

	def FocusNextPrevChild(self,next: bool):
		pass

	def FocusPolicy(self):
		pass

	def FocusProxy(self):
		pass

	def FocusWidget(self):
		pass

	def Font(self):
		pass

	def FontMetrics(self):
		pass

	def ForceBackgroundPainting(self):
		pass

	def ForegroundColor(self):
		pass

	def ForegroundRole(self):
		pass

	def FrameGeometry(self):
		pass

	def FrameRect(self):
		pass

	def FrameShadow(self):
		pass

	def FrameShape(self):
		pass

	def FrameSize(self):
		pass

	def FrameStyle(self):
		pass

	def FrameWidth(self):
		pass

	def GeomMgrAutoHideManagedWidgetsFlag(self):
		pass

	def GeomMgrCanBeTopWidget(self):
		pass

	def GeomMgrIgnoreHideOnMinimizeFlag(self):
		pass

	def GeomMgrPriority(self):
		pass

	def GeomMgrShowTopLeft(self):
		pass

	def GeomMgrStartX(self,hint: var9, firstItemWidth: int):
		pass

	def GeomMgrStartXHint(self):
		pass

	def GeomMgrXOffset(self):
		pass

	def GeomMgrYOffset(self):
		pass

	def Geometry(self):
		pass

	def GetPrehighlightRow(self):
		pass

	def Grab(self,rect: var10):
		pass

	def GrabKeyboard(self):
		pass

	def GrabMouse(self,*args):
		pass

	def HScrollBarMode(self):
		pass

	def Handle(self):
		pass

	def HasBadge(self):
		pass

	def HasChild(self,child: var2):
		pass

	def HasFocus(self):
		pass

	def HasIcon(self):
		pass

	def HasMouse(self):
		pass

	def HasMouseTracking(self):
		pass

	def HasSelection(self):
		pass

	def Height(self):
		pass

	def HeightForWidth(self,w: int):
		pass

	def Hide(self):
		pass

	def HorizontalScrollBar(self):
		pass

	def Icon(self):
		pass

	def IconSize(self):
		pass

	def IconText(self):
		pass

	def IndexAt(self,point: var4):
		pass

	def IndexWidget(self,index: var39):
		pass

	def InputMethodQuery(self,query: var11):
		pass

	def InsertAction(self,before: var0, action: var0):
		pass

	def InsertActions(self,before: var0, actions: var1):
		pass

	def IsA(self,classType: var3):
		pass

	def IsAction(self,id: int = 0):
		pass

	def IsActiveWindow(self):
		pass

	def IsChildOf(self,parent: var7):
		pass

	def IsConnectedTo(self,*args):
		pass

	def IsContainer(self):
		pass

	def IsDesktop(self):
		pass

	def IsDialog(self):
		pass

	def IsEnabled(self):
		pass

	def IsEnabledTo(self,ancestor: var2):
		pass

	def IsFullScreen(self):
		pass

	def IsHidden(self):
		pass

	def IsIndexSelected(self,index: var39):
		pass

	def IsInputMethodEnabled(self):
		pass

	def IsMaximized(self):
		pass

	def IsMinimized(self):
		pass

	def IsModal(self):
		pass

	def IsPersistentEditorOpen(self,index: var39):
		pass

	def IsPopup(self):
		pass

	def IsShown(self):
		pass

	def IsTopLevel(self):
		pass

	def IsUpdatesEnabled(self):
		pass

	def IsUsingBackingStore(self):
		pass

	def IsVisible(self):
		pass

	def IsVisibleTo(self,ancestor: var2):
		pass

	def IsWidgetType(self):
		pass

	def IsWindowModified(self):
		pass

	def ItemDelegate(self):
		pass

	def ItemDelegateForColumn(self,column: int):
		pass

	def KeyboardGrabber(self):
		pass

	def KillTimer(self,id: int):
		pass

	def Layout(self):
		pass

	def LineWidth(self):
		pass

	def Lower(self):
		pass

	def MapFrom(self,parent: var2, pos: var4):
		pass

	def MapFromGlobal(self,pos: var4):
		pass

	def MapFromParent(self,pos: var4):
		pass

	def MapTo(self,parent: var2, pos: var4):
		pass

	def MapToGlobal(self,pos: var4):
		pass

	def MapToParent(self,pos: var4):
		pass

	def MaxWidthOfStrings(self,strings: var12):
		pass

	def MaximumHeight(self):
		pass

	def MaximumSize(self):
		pass

	def MaximumWidth(self):
		pass

	def MidLineWidth(self):
		pass

	def MinimumHeight(self):
		pass

	def MinimumSize(self):
		pass

	def MinimumSizeHint(self):
		pass

	def MinimumWidth(self):
		pass

	def Model(self):
		pass

	def ModelIndex(self,row: int, col: int, parentIndex: var39):
		pass

	def MouseGrabber(self):
		pass

	def Move(self,*args):
		pass

	def MoveToScreenCenter(self,screen: int = -1):
		pass

	def Name(self):
		pass

	def NeedsHorizontalScrollBar(self):
		pass

	def NeedsVerticalScrollBar(self):
		pass

	def ObjectFromUUID(self,uuid: var13):
		pass

	def OnAboutToShow(self):
		pass

	def OnAboutToShowAdvancedToolTip(self):
		pass

	def OnActivatePixmap(self):
		pass

	@property
	def OnActivatePixmapMap_(self):
		pass
	@OnActivatePixmapMap_.setter
	def OnActivatePixmapMap_(self):
		pass

	def OnActivated(self):
		pass

	@property
	def OnActivatedMap_(self):
		pass
	@OnActivatedMap_.setter
	def OnActivatedMap_(self):
		pass

	def OnChange(self):
		pass

	def OnChildEvent(self):
		pass

	def OnClickedIndex(self):
		pass

	@property
	def OnClickedIndexMap_(self):
		pass
	@OnClickedIndexMap_.setter
	def OnClickedIndexMap_(self):
		pass

	def OnClose(self):
		pass

	def OnContentsDragEnter(self):
		pass

	def OnContentsDragLeave(self):
		pass

	def OnContentsDragMove(self):
		pass

	def OnContentsDrop(self):
		pass

	def OnContentsMouseDoubleClick(self):
		pass

	def OnContentsMouseMove(self):
		pass

	def OnContentsMousePress(self):
		pass

	def OnContentsMouseRelease(self):
		pass

	def OnContentsMoving(self):
		pass

	def OnContextMenu(self):
		pass

	def OnCurrentChange(self):
		pass

	@property
	def OnCurrentChangeMap_(self):
		pass
	@OnCurrentChangeMap_.setter
	def OnCurrentChangeMap_(self):
		pass

	def OnDebugMessage(self):
		pass

	def OnDestroy(self):
		pass

	def OnDestroyItem(self):
		pass

	def OnDoubleClickedIndex(self):
		pass

	@property
	def OnDoubleClickedIndexMap_(self):
		pass
	@OnDoubleClickedIndexMap_.setter
	def OnDoubleClickedIndexMap_(self):
		pass

	def OnDragEnter(self):
		pass

	def OnDragLeave(self):
		pass

	def OnDragMove(self):
		pass

	def OnDrop(self):
		pass

	def OnEnter(self):
		pass

	def OnEnterHandler(self):
		pass

	def OnEnteredIndex(self):
		pass

	@property
	def OnEnteredIndexMap_(self):
		pass
	@OnEnteredIndexMap_.setter
	def OnEnteredIndexMap_(self):
		pass

	def OnFatalMessage(self):
		pass

	def OnFocusIn(self):
		pass

	def OnFocusOut(self):
		pass

	def OnHide(self):
		pass

	def OnHorizontalSliderPress(self):
		pass

	def OnHorizontalSliderRelease(self):
		pass

	def OnKeyPress(self):
		pass

	def OnKeyRelease(self):
		pass

	def OnLeave(self):
		pass

	def OnLeaveHandler(self):
		pass

	def OnMouseDoubleClick(self):
		pass

	def OnMouseMove(self):
		pass

	def OnMousePress(self):
		pass

	def OnMouseRelease(self):
		pass

	def OnMove(self):
		pass

	def OnOnViewport(self):
		pass

	@property
	def OnOnViewportMap_(self):
		pass
	@OnOnViewportMap_.setter
	def OnOnViewportMap_(self):
		pass

	def OnPaint(self):
		pass

	def OnPaintHandler(self,event: var14):
		pass

	def OnPressedIndex(self):
		pass

	@property
	def OnPressedIndexMap_(self):
		pass
	@OnPressedIndexMap_.setter
	def OnPressedIndexMap_(self):
		pass

	def OnResize(self):
		pass

	def OnSelectionChange(self):
		pass

	@property
	def OnSelectionChangeMap_(self):
		pass
	@OnSelectionChangeMap_.setter
	def OnSelectionChangeMap_(self):
		pass

	def OnShow(self):
		pass

	def OnStartDrag(self):
		pass

	def OnStartDragHandler(self,supportedActions: int):
		pass

	@property
	def OnStartDragMap_(self):
		pass
	@OnStartDragMap_.setter
	def OnStartDragMap_(self):
		pass

	def OnTraceMessage(self):
		pass

	def OnVerticalSliderPress(self):
		pass

	def OnVerticalSliderRelease(self):
		pass

	def OnWheel(self):
		pass

	def OnWinIdChange(self):
		pass

	def OpenPersistentEditor(self,index: var39):
		pass

	def OverrideBackgroundMode(self):
		pass

	def OwnCursor(self):
		pass

	def OwnFont(self):
		pass

	def OwnPalette(self):
		pass

	def Palette(self):
		pass

	def PaletteBackgroundColor(self):
		pass

	def PaletteBackgroundPixmap(self):
		pass

	def PaletteForegroundColor(self):
		pass

	def Parent(self):
		pass

	def ParentWidget(self,*args):
		pass

	def ParentWidgetBelow(self,widget: var2):
		pass

	def PixelHeight(self,pixels: int):
		pass

	def PixelSize(self,pixelWidth: int, pixelHeight: int):
		pass

	def PixelWidth(self,pixels: int):
		pass

	def Pos(self):
		pass

	def PositionInsideDesktop(self):
		pass

	def PrepareForOffscreenRendering(self):
		pass

	def Raise(self):
		pass

	def Rect(self):
		pass

	def ReleaseKeyboard(self):
		pass

	def ReleaseMouse(self):
		pass

	def RemoveAction(self,action: var0):
		pass

	def RemoveChild(self,child: var2):
		pass

	def RemoveConnection(self,*args):
		pass

	def Render(self,*args):
		pass

	def Repaint(self,*args):
		pass

	def RepaintChildren(self):
		pass

	def RepaintContents(self,*args):
		pass

	def Reparent(self,*args):
		pass

	def Resize(self,*args):
		pass

	def ResizeContents(self,w: int, h: int):
		pass

	def Scroll(self,*args):
		pass

	def ScrollBy(self,dx: int, dy: int):
		pass

	def ScrollTo(self,*args):
		pass

	def SelectAll(self):
		pass

	def SelectIndex(self,index: var39, flag: var41):
		pass

	def SelectIndexes(self,start: var39, last: var39, flag: var41):
		pass

	def SelectedIndexes(self):
		pass

	def SelectedRows(self,column: int = 0):
		pass

	def SelectionBehavior(self):
		pass

	def SelectionMode(self):
		pass

	def Sender(self):
		pass

	def SetAcceptDrops(self,arg0: bool):
		pass

	def SetActiveWindow(self):
		pass

	def SetAdvancedToolTipId(self,uuid: var15):
		pass

	def SetAlignment(self,arg2: var16):
		pass

	def SetAllowHiddenScrollBars(self,state: bool):
		pass

	def SetAutoFillBackground(self,arg2: bool):
		pass

	def SetBackgroundDarkness(self,darkness: int):
		pass

	def SetBackgroundMode(self,*args):
		pass

	def SetBackgroundRole(self,role: var17):
		pass

	def SetBadgeAlignment(self,align: var18):
		pass

	def SetBadgeColor(self,color: var19):
		pass

	def SetBaseSize(self,*args):
		pass

	def SetCanMove(self,canMove: bool):
		pass

	def SetCanResize(self,canResize: bool):
		pass

	def SetCaption(self,name: var15):
		pass

	def SetConnection(self,*args):
		pass

	def SetContentsPos(self,x: int, y: int):
		pass

	def SetContextMenuPolicy(self,policy: var20):
		pass

	def SetCurrentIndex(self,index: var39):
		pass

	def SetCursor(self,cursor: var21):
		pass

	def SetCustomSizeHint(self,size: var22):
		pass

	def SetDisabled(self,state: bool = True):
		pass

	def SetDragDropMode(self,behavior: var42):
		pass

	def SetDragEnabled(self,enable: bool):
		pass

	def SetDropIndicatorShown(self,enable: bool):
		pass

	def SetDropShadow(self,state: bool):
		pass

	def SetEditTriggers(self,trigger: var43):
		pass

	def SetEnabled(self,state: bool = True):
		pass

	def SetEraseColor(self,color: var19):
		pass

	def SetErasePixmap(self,pixmap: var23):
		pass

	def SetEventPropagation(self,propagate: var6):
		pass

	def SetExcludeOverrideCursor(self,excludeOverrideCursor: bool):
		pass

	def SetFixedHeight(self,h: int):
		pass

	def SetFixedSize(self,*args):
		pass

	def SetFixedWidth(self,w: int):
		pass

	def SetFocus(self):
		pass

	def SetFocusPolicy(self,policy: var24):
		pass

	def SetFocusProxy(self,widget: var2):
		pass

	def SetFont(self,font: var25):
		pass

	def SetForceBackgroundPainting(self,state: bool):
		pass

	def SetForegroundRole(self,role: var17):
		pass

	def SetFrameRect(self,rect: var10):
		pass

	def SetFrameShadow(self,shadow: var26):
		pass

	def SetFrameShape(self,shape: var27):
		pass

	def SetFrameStyle(self,style: int):
		pass

	def SetGeomMgrAutoHideManagedWidgetsFlag(self,value: bool):
		pass

	def SetGeomMgrCanBeTopWidget(self,canBeTopWidget: bool):
		pass

	def SetGeomMgrIgnoreHideOnMinimizeFlag(self,value: bool):
		pass

	def SetGeomMgrPriority(self,priority: int):
		pass

	def SetGeomMgrShowTopLeft(self,showTopLeft: bool):
		pass

	def SetGeomMgrStartXHint(self,hint: var9):
		pass

	def SetGeomMgrXOffset(self,xOffset: int):
		pass

	def SetGeomMgrYOffset(self,yOffset: int):
		pass

	def SetGeometry(self,*args):
		pass

	def SetHScrollBarMode(self,arg0: int):
		pass

	def SetHasBadge(self,hasBadge: bool):
		pass

	def SetHidden(self,hide: bool):
		pass

	def SetIcon(self,pixmap: var23):
		pass

	def SetIconSize(self,size: var22):
		pass

	def SetIndexWidget(self,index: var39, widget: var2):
		pass

	def SetInputMethodEnabled(self,state: bool):
		pass

	def SetIsContainer(self,state: bool):
		pass

	def SetItemDelegate(self,delegate: var44):
		pass

	def SetItemDelegateForColumn(self,column: int, delegate: var44):
		pass

	def SetLayout(self,layout: var28):
		pass

	def SetLineWidth(self,width: int):
		pass

	def SetMask(self,bitmap: var29):
		pass

	def SetMaximumHeight(self,h: int):
		pass

	def SetMaximumSize(self,*args):
		pass

	def SetMaximumWidth(self,w: int):
		pass

	def SetMidLineWidth(self,width: int):
		pass

	def SetMinimumHeight(self,h: int):
		pass

	def SetMinimumSize(self,*args):
		pass

	def SetMinimumWidth(self,w: int):
		pass

	def SetModel(self,model: var45):
		pass

	def SetMouseTracking(self,enable: bool):
		pass

	def SetName(self,name: var15):
		pass

	def SetOverrideBackgroundMode(self,mode: var30):
		pass

	def SetPalette(self,palette: var31):
		pass

	def SetPaletteBackgroundColor(self,color: var19):
		pass

	def SetPaletteBackgroundPixmap(self,pixmap: var23):
		pass

	def SetPaletteForegroundColor(self,color: var19):
		pass

	def SetPrehighlightRow(self,row: int):
		pass

	def SetSelectionBehavior(self,mode: var46):
		pass

	def SetSelectionMode(self,mode: var47):
		pass

	def SetShown(self,show: bool):
		pass

	def SetSizeIncrement(self,*args):
		pass

	def SetSizePolicy(self,*args):
		pass

	def SetStyle(self,*args):
		pass

	def SetTabKeyNavigation(self,b: bool):
		pass

	def SetTabOrder(self,first: var2, second: var2):
		pass

	def SetToolTip(self,*args):
		pass

	def SetTransparentBackground(self):
		pass

	def SetUUID(self,uuid: var13):
		pass

	def SetUpdatesEnabled(self,state: bool):
		pass

	def SetUseAlternateColor(self,state: bool):
		pass

	def SetUseHighlightColor(self,state: bool):
		pass

	def SetUseUnityStyle(self,state: bool):
		pass

	def SetUsesBackingStore(self,state: bool):
		pass

	def SetVScrollBarMode(self,arg0: int):
		pass

	def SetViewport(self,viewport: var2):
		pass

	def SetWhatsThis(self,text: var15):
		pass

	def SetWidget(self,widget: var2):
		pass

	def SetWidgetResizable(self,resizable: bool):
		pass

	def SetWidthForWidestString(self,strings: var12, horizMargin: int = 0):
		pass

	def SetWindowModality(self,windowModality: var32):
		pass

	def SetWindowModified(self,value: bool):
		pass

	def SetWindowOpacity(self,level: var33):
		pass

	def SetWindowState(self,windowState: var8):
		pass

	def Show(self):
		pass

	def ShowDropIndicator(self):
		pass

	def ShowFullScreen(self):
		pass

	def ShowMaximized(self):
		pass

	def ShowMinimized(self):
		pass

	def ShowNormal(self):
		pass

	def SignalName(self,*args):
		pass

	def Size(self):
		pass

	def SizeHint(self):
		pass

	def SizeIncrement(self):
		pass

	def SizePolicy(self):
		pass

	def StackUnder(self,widget: var2):
		pass

	def Style(self):
		pass

	def TabKeyNavigation(self):
		pass

	def TestAndDrawBadge(self):
		pass

	def TestWFlags(self,flags: var8):
		pass

	def ToolTip(self,*args):
		pass

	def TopLevelWidget(self):
		pass

	def TransparentBackground(self):
		pass

	def UUID(self):
		pass

	def UnsetCursor(self):
		pass

	def UnsetFont(self):
		pass

	def UnsetPalette(self):
		pass

	def Update(self,*args):
		pass

	def UpdateChildren(self):
		pass

	def UpdateContents(self,*args):
		pass

	def UpdateFont(self):
		pass

	def UpdateGeometry(self):
		pass

	def UpdateIndex(self,index: var39):
		pass

	def UseAlternateColor(self):
		pass

	def UseHighlightColor(self):
		pass

	def UsesUnityStyle(self):
		pass

	def VScrollBarMode(self):
		pass

	def VerticalScrollBar(self):
		pass

	def Viewport(self):
		pass

	def ViewportToContents(self,vp: var4):
		pass

	def VisibleHeight(self):
		pass

	def VisibleWidth(self):
		pass

	def WhatsThis(self):
		pass

	def Widget(self):
		pass

	def WidgetResizable(self):
		pass

	def Width(self):
		pass

	def WinId(self):
		pass

	def WindowModality(self):
		pass

	def WindowOpacity(self):
		pass

	def WindowState(self):
		pass

	def Wrap(self,widget: var34, createdWidget: var35 = None):
		pass

	def X(self):
		pass

	def Y(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class uiHeader:
	def __init__(self,*args):
		pass

	def AcceptDrops(self):
		pass

	def Action(self,*args):
		pass

	def Actions(self):
		pass

	def AddAction(self,action: var0):
		pass

	def AddActions(self,actions: var1):
		pass

	def AddChild(self,child: var2, x: int = 0, y: int = 0):
		pass

	def AddLabel(self,*args):
		pass

	def AdjustHeaderSize(self):
		pass

	def AdjustSize(self):
		pass

	def AdvancedToolTipId(self):
		pass

	def Alignment(self):
		pass

	def AllowHiddenScrollBars(self):
		pass

	def AreFilterButtonsEnabled(self):
		pass

	def AsConcreteListener(self):
		pass

	def AsListener(self):
		pass

	def AutoFillBackground(self):
		pass

	def AverageWidth(self,chars: int):
		pass

	def BackgroundDarkness(self):
		pass

	def BackgroundMode(self):
		pass

	def BackgroundRole(self):
		pass

	def BadgeAlignment(self):
		pass

	def BadgeColor(self):
		pass

	def BaseSize(self):
		pass

	def CanMove(self):
		pass

	def CanResize(self):
		pass

	def Caption(self):
		pass

	def CellGeometry(self,index: var39):
		pass

	def Child(self,objName: var3, inheritsClass: var3 = None, recursiveSearch: bool = True):
		pass

	def ChildAt(self,*args):
		pass

	def Children(self):
		pass

	def ChildrenRect(self):
		pass

	def ClassName(self):
		pass

	def ClearFocus(self):
		pass

	def ClearMask(self):
		pass

	def ClearSelection(self):
		pass

	def Close(self,alsoDelete: bool = False):
		pass

	def ClosePersistentEditor(self,index: var39):
		pass

	def Color0(self):
		pass

	def Color1(self):
		pass

	def ColorBlack(self):
		pass

	def ColorBlue(self):
		pass

	def ColorCyan(self):
		pass

	def ColorDarkBlue(self):
		pass

	def ColorDarkCyan(self):
		pass

	def ColorDarkGray(self):
		pass

	def ColorDarkGreen(self):
		pass

	def ColorDarkMagenta(self):
		pass

	def ColorDarkRed(self):
		pass

	def ColorDarkYellow(self):
		pass

	def ColorGray(self):
		pass

	def ColorGreen(self):
		pass

	def ColorGroup(self):
		pass

	def ColorLightGray(self):
		pass

	def ColorMagenta(self):
		pass

	def ColorRed(self):
		pass

	def ColorWhite(self):
		pass

	def ColorYellow(self):
		pass

	def ContentsHeight(self):
		pass

	def ContentsRect(self):
		pass

	def ContentsToViewport(self,p: var4):
		pass

	def ContentsWidth(self):
		pass

	def ContentsX(self):
		pass

	def ContentsY(self):
		pass

	def ContextMenuPolicy(self):
		pass

	def Count(self):
		pass

	def CurrentIndex(self):
		pass

	def Cursor(self):
		pass

	def CustomFocusNextPrevChild(self,next: bool):
		pass

	def CustomSizeHint(self):
		pass

	def DefaultAlignment(self):
		pass

	def DefaultSectionSize(self):
		pass

	def DeleteLater(self):
		pass

	def Disconnect(self,sender: var5, force: var6 = False):
		pass

	def DisconnectAll(self,force: var6 = False):
		pass

	def DluHeight(self,*args):
		pass

	def DluPixelHeight(self,pixels: int):
		pass

	def DluPixelSize(self,pixelWidth: int, pixelHeight: int):
		pass

	def DluPixelWidth(self,pixels: int):
		pass

	def DluWidth(self,*args):
		pass

	def DownCast(self,o: var7):
		pass

	def DragDropMode(self):
		pass

	def DragEnabled(self):
		pass

	def DrawHighlightIndicators(self,p: var40, rect: var10, index: var39):
		pass

	def DumpTree(self):
		pass

	def Edit(self,index: var39):
		pass

	def EditTriggers(self):
		pass

	def EnableFilterButtons(self,enable: bool):
		pass

	def EnsureWidgetVisible(self,childWidget: var2, xmargin: int = 50, ymargin: int = 50):
		pass

	def EraseColor(self):
		pass

	def ErasePixmap(self):
		pass

	def EventInfo(self):
		pass

	def EventPropagation(self):
		pass

	def ExcludeOverrideCursor(self):
		pass

	def Find(self,winId: var8):
		pass

	def FindBackgroundDarkness(self):
		pass

	def FocusNextPrevChild(self,next: bool):
		pass

	def FocusPolicy(self):
		pass

	def FocusProxy(self):
		pass

	def FocusWidget(self):
		pass

	def Font(self):
		pass

	def FontMetrics(self):
		pass

	def ForceBackgroundPainting(self):
		pass

	def ForegroundColor(self):
		pass

	def ForegroundRole(self):
		pass

	def FrameGeometry(self):
		pass

	def FrameRect(self):
		pass

	def FrameShadow(self):
		pass

	def FrameShape(self):
		pass

	def FrameSize(self):
		pass

	def FrameStyle(self):
		pass

	def FrameWidth(self):
		pass

	def GeomMgrAutoHideManagedWidgetsFlag(self):
		pass

	def GeomMgrCanBeTopWidget(self):
		pass

	def GeomMgrIgnoreHideOnMinimizeFlag(self):
		pass

	def GeomMgrPriority(self):
		pass

	def GeomMgrShowTopLeft(self):
		pass

	def GeomMgrStartX(self,hint: var9, firstItemWidth: int):
		pass

	def GeomMgrStartXHint(self):
		pass

	def GeomMgrXOffset(self):
		pass

	def GeomMgrYOffset(self):
		pass

	def Geometry(self):
		pass

	def GetPrehighlightRow(self):
		pass

	def GetResizeMode(self,logicalIndex: int):
		pass

	def Grab(self,rect: var10):
		pass

	def GrabKeyboard(self):
		pass

	def GrabMouse(self,*args):
		pass

	def HScrollBarMode(self):
		pass

	def Handle(self):
		pass

	def HasBadge(self):
		pass

	def HasChild(self,child: var2):
		pass

	def HasFocus(self):
		pass

	def HasIcon(self):
		pass

	def HasMouse(self):
		pass

	def HasMouseTracking(self):
		pass

	def HasSelection(self):
		pass

	def HeaderWidth(self):
		pass

	def Height(self):
		pass

	def HeightForWidth(self,w: int):
		pass

	def Hide(self):
		pass

	def HighlightSections(self):
		pass

	def HorizontalScrollBar(self):
		pass

	def Icon(self):
		pass

	def IconSet(self,section: int):
		pass

	def IconSize(self):
		pass

	def IconText(self):
		pass

	def IndexAt(self,point: var4):
		pass

	def IndexWidget(self,index: var39):
		pass

	def InputMethodQuery(self,query: var11):
		pass

	def InsertAction(self,before: var0, action: var0):
		pass

	def InsertActions(self,before: var0, actions: var1):
		pass

	def IsA(self,classType: var3):
		pass

	def IsAction(self,id: int = 0):
		pass

	def IsActiveWindow(self):
		pass

	def IsChildOf(self,parent: var7):
		pass

	def IsClickEnabled(self,section: int = -1):
		pass

	def IsConnectedTo(self,*args):
		pass

	def IsContainer(self):
		pass

	def IsDesktop(self):
		pass

	def IsDialog(self):
		pass

	def IsEnabled(self):
		pass

	def IsEnabledTo(self,ancestor: var2):
		pass

	def IsFullScreen(self):
		pass

	def IsHidden(self):
		pass

	def IsIndexSelected(self,index: var39):
		pass

	def IsInputMethodEnabled(self):
		pass

	def IsMaximized(self):
		pass

	def IsMinimized(self):
		pass

	def IsModal(self):
		pass

	def IsMovingEnabled(self):
		pass

	def IsPersistentEditorOpen(self,index: var39):
		pass

	def IsPopup(self):
		pass

	def IsResizeEnabled(self,section: int = -1):
		pass

	def IsSectionCheckable(self,logicalIndex: int):
		pass

	def IsSectionChecked(self,logicalIndex: int):
		pass

	def IsSectionHidden(self,logicalIndex: int):
		pass

	def IsShown(self):
		pass

	def IsSortFilterEnabled(self,logicalIndex: int):
		pass

	def IsStretchEnabled(self,*args):
		pass

	def IsTopLevel(self):
		pass

	def IsUpdatesEnabled(self):
		pass

	def IsUsingBackingStore(self):
		pass

	def IsVisible(self):
		pass

	def IsVisibleTo(self,ancestor: var2):
		pass

	def IsWidgetType(self):
		pass

	def IsWindowModified(self):
		pass

	def ItemDelegate(self):
		pass

	def ItemDelegateForColumn(self,column: int):
		pass

	def KeyboardGrabber(self):
		pass

	def KillTimer(self,id: int):
		pass

	def Label(self,section: int):
		pass

	def LabelDirection(self,section: int):
		pass

	def Layout(self):
		pass

	def LineWidth(self):
		pass

	def Lower(self):
		pass

	def MapFrom(self,parent: var2, pos: var4):
		pass

	def MapFromGlobal(self,pos: var4):
		pass

	def MapFromParent(self,pos: var4):
		pass

	def MapTo(self,parent: var2, pos: var4):
		pass

	def MapToGlobal(self,pos: var4):
		pass

	def MapToIndex(self,section: int):
		pass

	def MapToParent(self,pos: var4):
		pass

	def MapToSection(self,index: int):
		pass

	def MaxWidthOfStrings(self,strings: var12):
		pass

	def MaximumHeight(self):
		pass

	def MaximumSize(self):
		pass

	def MaximumWidth(self):
		pass

	def MidLineWidth(self):
		pass

	def MinimumHeight(self):
		pass

	def MinimumSectionSize(self):
		pass

	def MinimumSize(self):
		pass

	def MinimumSizeHint(self):
		pass

	def MinimumWidth(self):
		pass

	def Model(self):
		pass

	def ModelIndex(self,row: int, col: int, parentIndex: var39):
		pass

	def MouseGrabber(self):
		pass

	def Move(self,*args):
		pass

	def MoveSection(self,section: int, toIndex: int):
		pass

	def MoveToScreenCenter(self,screen: int = -1):
		pass

	def Name(self):
		pass

	def NeedsHorizontalScrollBar(self):
		pass

	def NeedsVerticalScrollBar(self):
		pass

	def ObjectFromUUID(self,uuid: var13):
		pass

	def Offset(self):
		pass

	def OnAboutToShow(self):
		pass

	def OnAboutToShowAdvancedToolTip(self):
		pass

	def OnActivatePixmap(self):
		pass

	@property
	def OnActivatePixmapMap_(self):
		pass
	@OnActivatePixmapMap_.setter
	def OnActivatePixmapMap_(self):
		pass

	def OnActivated(self):
		pass

	@property
	def OnActivatedMap_(self):
		pass
	@OnActivatedMap_.setter
	def OnActivatedMap_(self):
		pass

	def OnChange(self):
		pass

	def OnChildEvent(self):
		pass

	def OnClicked(self):
		pass

	def OnClickedIndex(self):
		pass

	@property
	def OnClickedIndexMap_(self):
		pass
	@OnClickedIndexMap_.setter
	def OnClickedIndexMap_(self):
		pass

	def OnClose(self):
		pass

	def OnContentsDragEnter(self):
		pass

	def OnContentsDragLeave(self):
		pass

	def OnContentsDragMove(self):
		pass

	def OnContentsDrop(self):
		pass

	def OnContentsMouseDoubleClick(self):
		pass

	def OnContentsMouseMove(self):
		pass

	def OnContentsMousePress(self):
		pass

	def OnContentsMouseRelease(self):
		pass

	def OnContentsMoving(self):
		pass

	def OnContextMenu(self):
		pass

	def OnCurrentChange(self):
		pass

	@property
	def OnCurrentChangeMap_(self):
		pass
	@OnCurrentChangeMap_.setter
	def OnCurrentChangeMap_(self):
		pass

	def OnDebugMessage(self):
		pass

	def OnDestroy(self):
		pass

	def OnDestroyItem(self):
		pass

	def OnDoubleClickedIndex(self):
		pass

	@property
	def OnDoubleClickedIndexMap_(self):
		pass
	@OnDoubleClickedIndexMap_.setter
	def OnDoubleClickedIndexMap_(self):
		pass

	def OnDragEnter(self):
		pass

	def OnDragLeave(self):
		pass

	def OnDragMove(self):
		pass

	def OnDrop(self):
		pass

	def OnEnter(self):
		pass

	def OnEnterHandler(self):
		pass

	def OnEnteredIndex(self):
		pass

	@property
	def OnEnteredIndexMap_(self):
		pass
	@OnEnteredIndexMap_.setter
	def OnEnteredIndexMap_(self):
		pass

	def OnFatalMessage(self):
		pass

	def OnFocusIn(self):
		pass

	def OnFocusOut(self):
		pass

	def OnHide(self):
		pass

	def OnHorizontalSliderPress(self):
		pass

	def OnHorizontalSliderRelease(self):
		pass

	def OnIndexChanged(self):
		pass

	def OnKeyPress(self):
		pass

	def OnKeyRelease(self):
		pass

	def OnLeave(self):
		pass

	def OnLeaveHandler(self):
		pass

	def OnMouseDoubleClick(self):
		pass

	def OnMouseMove(self):
		pass

	def OnMousePress(self):
		pass

	def OnMouseRelease(self):
		pass

	def OnMove(self):
		pass

	def OnOnViewport(self):
		pass

	@property
	def OnOnViewportMap_(self):
		pass
	@OnOnViewportMap_.setter
	def OnOnViewportMap_(self):
		pass

	def OnPaint(self):
		pass

	def OnPaintHandler(self,event: var14):
		pass

	def OnPressed(self):
		pass

	def OnPressedIndex(self):
		pass

	@property
	def OnPressedIndexMap_(self):
		pass
	@OnPressedIndexMap_.setter
	def OnPressedIndexMap_(self):
		pass

	def OnReleased(self):
		pass

	def OnResize(self):
		pass

	def OnSectionCheckStateChanged(self):
		pass

	def OnSectionHandleDoubleClicked(self):
		pass

	def OnSelectionChange(self):
		pass

	@property
	def OnSelectionChangeMap_(self):
		pass
	@OnSelectionChangeMap_.setter
	def OnSelectionChangeMap_(self):
		pass

	def OnShow(self):
		pass

	def OnSizeChanged(self):
		pass

	def OnStartDrag(self):
		pass

	def OnStartDragHandler(self,supportedActions: int):
		pass

	@property
	def OnStartDragMap_(self):
		pass
	@OnStartDragMap_.setter
	def OnStartDragMap_(self):
		pass

	def OnTraceMessage(self):
		pass

	def OnVerticalSliderPress(self):
		pass

	def OnVerticalSliderRelease(self):
		pass

	def OnWheel(self):
		pass

	def OnWinIdChange(self):
		pass

	def OpenPersistentEditor(self,index: var39):
		pass

	def Orientation(self):
		pass

	def OverrideBackgroundMode(self):
		pass

	def OwnCursor(self):
		pass

	def OwnFont(self):
		pass

	def OwnPalette(self):
		pass

	def PaintSection(self,painter: var40, rect: var10, logicalIndex: int):
		pass

	def Palette(self):
		pass

	def PaletteBackgroundColor(self):
		pass

	def PaletteBackgroundPixmap(self):
		pass

	def PaletteForegroundColor(self):
		pass

	def Parent(self):
		pass

	def ParentWidget(self,*args):
		pass

	def ParentWidgetBelow(self,widget: var2):
		pass

	def PixelHeight(self,pixels: int):
		pass

	def PixelSize(self,pixelWidth: int, pixelHeight: int):
		pass

	def PixelWidth(self,pixels: int):
		pass

	def Pos(self):
		pass

	def PositionInsideDesktop(self):
		pass

	def PrepareForOffscreenRendering(self):
		pass

	def Raise(self):
		pass

	def Rect(self):
		pass

	def ReleaseKeyboard(self):
		pass

	def ReleaseMouse(self):
		pass

	def RemoveAction(self,action: var0):
		pass

	def RemoveChild(self,child: var2):
		pass

	def RemoveConnection(self,*args):
		pass

	def RemoveLabel(self,section: int):
		pass

	def Render(self,*args):
		pass

	def Repaint(self,*args):
		pass

	def RepaintChildren(self):
		pass

	def RepaintContents(self,*args):
		pass

	def Reparent(self,*args):
		pass

	def Resize(self,*args):
		pass

	def ResizeContents(self,w: int, h: int):
		pass

	def ResizeSection(self,section: int, s: int):
		pass

	def RestoreState(self,state: var15):
		pass

	def SaveState(self):
		pass

	def Scroll(self,*args):
		pass

	def ScrollBy(self,dx: int, dy: int):
		pass

	def ScrollTo(self,*args):
		pass

	def SectionAdvancedToolTipId(self,logicalIndex: int):
		pass

	def SectionAlignment(self,section: int):
		pass

	def SectionAt(self,pos: int):
		pass

	def SectionPos(self,section: int):
		pass

	def SectionSize(self,section: int):
		pass

	def SelectAll(self):
		pass

	def SelectIndex(self,index: var39, flag: var41):
		pass

	def SelectIndexes(self,start: var39, last: var39, flag: var41):
		pass

	def SelectedIndexes(self):
		pass

	def SelectedRows(self,column: int = 0):
		pass

	def SelectionBehavior(self):
		pass

	def SelectionMode(self):
		pass

	def Sender(self):
		pass

	def SetAcceptDrops(self,arg0: bool):
		pass

	def SetActiveWindow(self):
		pass

	def SetAdvancedToolTipId(self,uuid: var15):
		pass

	def SetAlignment(self,arg2: var16):
		pass

	def SetAllowHiddenScrollBars(self,state: bool):
		pass

	def SetAutoFillBackground(self,arg2: bool):
		pass

	def SetBackgroundDarkness(self,darkness: int):
		pass

	def SetBackgroundMode(self,*args):
		pass

	def SetBackgroundRole(self,role: var17):
		pass

	def SetBadgeAlignment(self,align: var18):
		pass

	def SetBadgeColor(self,color: var19):
		pass

	def SetBaseSize(self,*args):
		pass

	def SetCanMove(self,canMove: bool):
		pass

	def SetCanResize(self,canResize: bool):
		pass

	def SetCaption(self,name: var15):
		pass

	def SetClickEnabled(self,enable: bool, section: int = -1):
		pass

	def SetConnection(self,*args):
		pass

	def SetContentsPos(self,x: int, y: int):
		pass

	def SetContextMenuPolicy(self,policy: var20):
		pass

	def SetCurrentIndex(self,index: var39):
		pass

	def SetCursor(self,cursor: var21):
		pass

	def SetCustomSizeHint(self,size: var22):
		pass

	def SetDefaultAlignment(self,align: var16):
		pass

	def SetDefaultSectionSize(self,size: int):
		pass

	def SetDisabled(self,state: bool = True):
		pass

	def SetDragDropMode(self,behavior: var42):
		pass

	def SetDragEnabled(self,enable: bool):
		pass

	def SetDropIndicatorShown(self,enable: bool):
		pass

	def SetDropShadow(self,state: bool):
		pass

	def SetEditTriggers(self,trigger: var43):
		pass

	def SetEnabled(self,state: bool = True):
		pass

	def SetEraseColor(self,color: var19):
		pass

	def SetErasePixmap(self,pixmap: var23):
		pass

	def SetEventPropagation(self,propagate: var6):
		pass

	def SetExcludeOverrideCursor(self,excludeOverrideCursor: bool):
		pass

	def SetFixedHeight(self,h: int):
		pass

	def SetFixedSize(self,*args):
		pass

	def SetFixedWidth(self,w: int):
		pass

	def SetFocus(self):
		pass

	def SetFocusPolicy(self,policy: var24):
		pass

	def SetFocusProxy(self,widget: var2):
		pass

	def SetFont(self,font: var25):
		pass

	def SetForceBackgroundPainting(self,state: bool):
		pass

	def SetForegroundRole(self,role: var17):
		pass

	def SetFrameRect(self,rect: var10):
		pass

	def SetFrameShadow(self,shadow: var26):
		pass

	def SetFrameShape(self,shape: var27):
		pass

	def SetFrameStyle(self,style: int):
		pass

	def SetGeomMgrAutoHideManagedWidgetsFlag(self,value: bool):
		pass

	def SetGeomMgrCanBeTopWidget(self,canBeTopWidget: bool):
		pass

	def SetGeomMgrIgnoreHideOnMinimizeFlag(self,value: bool):
		pass

	def SetGeomMgrPriority(self,priority: int):
		pass

	def SetGeomMgrShowTopLeft(self,showTopLeft: bool):
		pass

	def SetGeomMgrStartXHint(self,hint: var9):
		pass

	def SetGeomMgrXOffset(self,xOffset: int):
		pass

	def SetGeomMgrYOffset(self,yOffset: int):
		pass

	def SetGeometry(self,*args):
		pass

	def SetHScrollBarMode(self,arg0: int):
		pass

	def SetHasBadge(self,hasBadge: bool):
		pass

	def SetHidden(self,hide: bool):
		pass

	def SetHighlightSections(self,highlight: bool):
		pass

	def SetIcon(self,pixmap: var23):
		pass

	def SetIconSize(self,size: var22):
		pass

	def SetIndexWidget(self,index: var39, widget: var2):
		pass

	def SetInputMethodEnabled(self,state: bool):
		pass

	def SetIsContainer(self,state: bool):
		pass

	def SetItemDelegate(self,delegate: var44):
		pass

	def SetItemDelegateForColumn(self,column: int, delegate: var44):
		pass

	def SetLabel(self,*args):
		pass

	def SetLabelDirection(self,direction: var48, section: int = -1):
		pass

	def SetLayout(self,layout: var28):
		pass

	def SetLineWidth(self,width: int):
		pass

	def SetMask(self,bitmap: var29):
		pass

	def SetMaximumHeight(self,h: int):
		pass

	def SetMaximumSize(self,*args):
		pass

	def SetMaximumWidth(self,w: int):
		pass

	def SetMidLineWidth(self,width: int):
		pass

	def SetMinimumHeight(self,h: int):
		pass

	def SetMinimumSectionSize(self,size: int):
		pass

	def SetMinimumSize(self,*args):
		pass

	def SetMinimumWidth(self,w: int):
		pass

	def SetModel(self,model: var45):
		pass

	def SetMouseTracking(self,enable: bool):
		pass

	def SetMovingEnabled(self,enable: bool):
		pass

	def SetName(self,name: var15):
		pass

	def SetOffset(self,pos: int):
		pass

	def SetOverrideBackgroundMode(self,mode: var30):
		pass

	def SetPalette(self,palette: var31):
		pass

	def SetPaletteBackgroundColor(self,color: var19):
		pass

	def SetPaletteBackgroundPixmap(self,pixmap: var23):
		pass

	def SetPaletteForegroundColor(self,color: var19):
		pass

	def SetPrehighlightRow(self,row: int):
		pass

	def SetResizeEnabled(self,enable: bool, section: int = -1):
		pass

	def SetResizeMode(self,*args):
		pass

	def SetSectionAdvancedToolTipId(self,logicalIndex: int, uuid: var15):
		pass

	def SetSectionAlignment(self,section: int, alignment: int):
		pass

	def SetSectionCheckable(self,logicalIndex: int, checkable: bool):
		pass

	def SetSectionChecked(self,logicalIndex: int, checked: bool):
		pass

	def SetSelectionBehavior(self,mode: var46):
		pass

	def SetSelectionMode(self,mode: var47):
		pass

	def SetShown(self,show: bool):
		pass

	def SetSizeIncrement(self,*args):
		pass

	def SetSizePolicy(self,*args):
		pass

	def SetSortFilterEnabled(self,logicalIndex: int, enabled: bool):
		pass

	def SetSortFilterHandler(self,handler: var49):
		pass

	def SetSortIndicator(self,section: int, order: int):
		pass

	def SetSortIndicatorShown(self,state: bool):
		pass

	def SetStretchEnabled(self,*args):
		pass

	def SetStretchLastSection(self,stretch: bool):
		pass

	def SetStyle(self,*args):
		pass

	def SetTabKeyNavigation(self,b: bool):
		pass

	def SetTabOrder(self,first: var2, second: var2):
		pass

	def SetToolTip(self,section: int, tooltip: var15):
		pass

	def SetTransparentBackground(self):
		pass

	def SetUUID(self,uuid: var13):
		pass

	def SetUpdatesEnabled(self,state: bool):
		pass

	def SetUseAlternateColor(self,state: bool):
		pass

	def SetUseHighlightColor(self,state: bool):
		pass

	def SetUseUnityStyle(self,state: bool):
		pass

	def SetUsesBackingStore(self,state: bool):
		pass

	def SetVScrollBarMode(self,arg0: int):
		pass

	def SetViewport(self,viewport: var2):
		pass

	def SetWhatsThis(self,text: var15):
		pass

	def SetWidget(self,widget: var2):
		pass

	def SetWidgetResizable(self,resizable: bool):
		pass

	def SetWidthForWidestString(self,strings: var12, horizMargin: int = 0):
		pass

	def SetWindowModality(self,windowModality: var32):
		pass

	def SetWindowModified(self,value: bool):
		pass

	def SetWindowOpacity(self,level: var33):
		pass

	def SetWindowState(self,windowState: var8):
		pass

	def Show(self):
		pass

	def ShowDropIndicator(self):
		pass

	def ShowFullScreen(self):
		pass

	def ShowMaximized(self):
		pass

	def ShowMinimized(self):
		pass

	def ShowNormal(self):
		pass

	def SignalName(self,*args):
		pass

	def Size(self):
		pass

	def SizeHint(self):
		pass

	def SizeIncrement(self):
		pass

	def SizePolicy(self):
		pass

	def SortFilterHandler(self):
		pass

	def SortIndicatorOrder(self):
		pass

	def SortIndicatorSection(self):
		pass

	def StackUnder(self,widget: var2):
		pass

	def StretchLastSection(self):
		pass

	def Style(self):
		pass

	def SwapSections(self,first: int, second: int):
		pass

	def TabKeyNavigation(self):
		pass

	def TestAndDrawBadge(self):
		pass

	def TestWFlags(self,flags: var8):
		pass

	def ToolTip(self,*args):
		pass

	def TopLevelWidget(self):
		pass

	def TransparentBackground(self):
		pass

	def UUID(self):
		pass

	def UnsetCursor(self):
		pass

	def UnsetFont(self):
		pass

	def UnsetPalette(self):
		pass

	def Update(self,*args):
		pass

	def UpdateChildren(self):
		pass

	def UpdateContents(self,*args):
		pass

	def UpdateFont(self):
		pass

	def UpdateGeometry(self):
		pass

	def UpdateIndex(self,index: var39):
		pass

	def UseAlternateColor(self):
		pass

	def UseHighlightColor(self):
		pass

	def UsesUnityStyle(self):
		pass

	def VScrollBarMode(self):
		pass

	def VerticalScrollBar(self):
		pass

	def Viewport(self):
		pass

	def ViewportToContents(self,vp: var4):
		pass

	def VisibleHeight(self):
		pass

	def VisibleWidth(self):
		pass

	def WhatsThis(self):
		pass

	def Widget(self):
		pass

	def WidgetResizable(self):
		pass

	def Width(self):
		pass

	def WinId(self):
		pass

	def WindowModality(self):
		pass

	def WindowOpacity(self):
		pass

	def WindowState(self):
		pass

	def Wrap(self,widget: var34, createdWidget: var35 = None):
		pass

	def X(self):
		pass

	def Y(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class uiModelIndex:
	def __init__(self,*args):
		pass

	def Column(self):
		pass

	def Data(self,*args):
		pass

	def InternalPointer(self):
		pass

	def IsValid(self):
		pass

	def Model(self):
		pass

	def PyInternalPointer(self):
		pass

	def Row(self):
		pass

	def Wrap(self,impl: var50):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class uiObject:
	def __init__(self,root, row):
		pass

	def AddProperty(self,*args):
		pass

	def ChildCount(self):
		pass

	def ChildIndex(self,child: var51):
		pass

	def ClassName(self):
		pass

	def Copy(self,parent: var51):
		pass

	def Delete(self):
		pass

	def DeleteAllChildren(self):
		pass

	def EliminateChildren(self,arg1: var52):
		pass

	def EmitBeginDestroy(self,*args):
		pass

	def EmitCreated(self):
		pass

	def EmitDeleted(self,*args):
		pass

	def EmitHighlighted(self):
		pass

	def EmitModified(self,*args):
		pass

	def EmitRequested(self,arg0: var53):
		pass

	def EmitSelected(self):
		pass

	def EmitUnhighlighted(self):
		pass

	def EmitUnselected(self):
		pass

	def ExecuteMethod(self,name: var13, parameters: var54):
		pass

	def FillAndGetProperty(self,arg2: var53):
		pass

	def FillProperty(self,arg2: var53):
		pass

	def GenerateName(self,prefix: var13):
		pass

	def GetByFullName(self,fullName: var13):
		pass

	def GetChild(self,*args):
		pass

	def GetChildren(self,*args):
		pass

	def GetCurrentObjectFromType(self,type: var13):
		pass

	def GetFullName(self):
		pass

	def GetModel(self):
		pass

	def GetName(self):
		pass

	def GetNamePropertyName(self):
		pass

	def GetParent(self,*args):
		pass

	def GetProperty(self,*args, **kwds):
		pass

	def GetPropertyNames(self,*args, **kwds):
		pass

	def GetRenderer(self):
		pass

	def IsA(self,arg0: var13):
		pass

	def OnAddProperty(self):
		pass

	def OnGetProperty(self):
		pass

	def OnRemoveProperty(self):
		pass

	def OnSetProperty(self):
		pass

	def Read(self,arg0: var55):
		pass

	def RemoveProperty(self,name: var13):
		pass

	def SetBit(self,bit: var56, flag: var57):
		pass

	def SetName(self,arg2: var13):
		pass

	def SetNamePropertyName(self,name: var13):
		pass

	def SetParent(self,parent: var51, index: int = -1):
		pass

	def SetProperty(self,*args, **kwds):
		pass

	def SetPropertyValue(self,name: var13, value: var58):
		pass

	def SetRenderer(self,renderer: var59):
		pass

	def TestBit(self,bit: var56):
		pass

	def Write(self,arg0: var55):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class uuid:
	"""
UUID objects (universally unique identifiers) according to RFC 4122.

This module provides immutable UUID objects (class UUID) and the functions
uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5
UUIDs as specified in RFC 4122.

If all you want is a unique ID, you should probably call uuid1() or uuid4().
Note that uuid1() may compromise privacy since it creates a UUID containing
the computer's network address.  uuid4() creates a random UUID.

Typical usage:

    >>> import uuid

    # make a UUID based on the host ID and current time
    >>> uuid.uuid1()    # doctest: +SKIP
    UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

    # make a UUID using an MD5 hash of a namespace UUID and a name
    >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
    UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

    # make a random UUID
    >>> uuid.uuid4()    # doctest: +SKIP
    UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

    # make a UUID using a SHA-1 hash of a namespace UUID and a name
    >>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

    # make a UUID from a string of hex digits (braces and hyphens ignored)
    >>> x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

    # convert a UUID to a string of hex digits in standard form
    >>> str(x)
    '00010203-0405-0607-0809-0a0b0c0d0e0f'

    # get the raw 16 bytes of the UUID
    >>> x.bytes
    b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

    # make a UUID from a 16-byte string
    >>> uuid.UUID(bytes=x.bytes)
    UUID('00010203-0405-0607-0809-0a0b0c0d0e0f')

"""
	pass

class views:
	pass

class virtualMethodDecorator:
	def __init__(self,default=None,exceptions: str="<class Exception>,)"):
		"""
Decorate overloaded virtual methods to handle Python Exceptions

     Python exceptions in virtual methods can cause application crashes
     because of invalid return value.
     This decorator wraps the method with a try/except and returns the
     specified default value.
  
"""
		pass

def waitCursor(cursor: str="wait", message=None):
	"""
Context for displaying a wait cursor.

  Args:
    cursor(str): cursor name.
    message(str): message to be displayed in the status bar.
  
"""
	pass

def warnUser(message):
	"""
Popup up the MessageDialog with a warning

  Args:
    message (str): The warning message to be displayed in the message dialog.
  
"""
	pass

