from typing import TypeVar
class Model:
	pass
class hwdescriptor_module:
	class Uid:
		pass
	class Identifier:
		pass
	class Value:
		pass
	class EntityFullType:
		pass
	class Model:
		pass
class MDIObject:
	pass
class Identifier:
	pass
class Entity2IdentifierList:
	pass
class Allowables:
	pass
class IdentifierList:
	pass
class Entity:
	pass
class Identifier2BagMap:
	pass
class Value:
	pass
class EntityList:
	pass
class EntityFullType:
	pass
class hw_module:
	class mdi:
		class attribute:
			class Action:
				pass
			class Attribute:
				pass

class Accelerometer:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Alefsiprojection:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Alereferencesystemcurve:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Alereferencesystemgroup:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Alereferencesystemnode:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Alereferencesystemswitch:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Alesmoothing:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Aletanktest:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Analysis:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Analysisparameter:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Attachment:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Attachmentcontrol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Attachmentcontroldefault:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Axisymmetry:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Bag:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Beamsectcol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Beamsection:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Behavior:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Block:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Body:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Box:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Card:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Chart:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Clearance:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Collection:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Collision:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Comment:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Component:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Configuration:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Connector:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Connectorcontrol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Connectorcontroldefault:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Connectorset:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Constrainedextranode:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Constrainedrigidbody:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Constraint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Contactbehavior:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Contactgroup:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Contactsurf:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Controlvol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Crosssection:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Curve:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Damping:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Ddval:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Dequation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointImpactPoint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointTargetPoint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointUndefined:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointmethodESAComp:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointmethodUndefined:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetBeam:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetBeamJoint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetBeamMember:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetBeamShell:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetBeamShellMember:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetBeamShellSingle:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetDummy:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetGeneric:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetInstrumentPanelImpactPoint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetPanelComposite:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetPanelMetallic:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetPanelStiffened:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetPedestrian:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetRivets:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class DesignpointsetSprings:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Designvar:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Desvarlink:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Directmatrixinput:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Dobjref:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Domain:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Dvprel:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Element:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Elementbehavior:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Elementcluster:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Encryption:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Enginefile:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Equation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Exploration:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Face:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Failure:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Feature:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Field:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Freebodygroup:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Freebodysection:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Frequency:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Frequencyset:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Friction:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Geometricrepresentation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Group:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Handle:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Hourglass:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Initialstate:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Integrationrule:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Interfacecomponent:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Interfacelinking:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Joint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Laminate:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Legend:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Line:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class List:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadAcceleration:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadConstraint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadFlux:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadForce:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadMoment:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadPressure:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadTemperature:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class LoadVelocity:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Loadcol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Loadstep:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Material:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Materialbehavior:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Mechanism:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Mechanismconstraint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Member:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Memberjoint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Memberpanel:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Membersection:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Membersegment:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Meshcontrol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Modelcheckcheck:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Modelcheckcorrection:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Morphconstraint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Morphvolume:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Nctlayer:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Node:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Noisecontroltreatment:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Objective:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Opticonstraint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Opticontrol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Optidscreen:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Optiresponse:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Outputblock:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Outputrequest:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Panel:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Parameter:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Part:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PartInstance:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PartPrototype:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PartRealizationFacets:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PartRepresentationDefinition:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PartRoot:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		"""
PartRoot UID is same as model name
"""
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Partset:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Perturbation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Physicalquantity:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Plot:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PlotcontrolContour:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PlotcontrolDeformed:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PlotcontrolFBD:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PlotcontrolMarker:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PlotcontrolTensor:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class PlotcontrolVector:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Ply:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Point:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Polycage:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Position:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Pretensioner:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Property:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Referencegeometry:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Region:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Resource:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Response:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Result:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Resultsimulation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Resultsubcase:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Retractor:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Rigidbody:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Rigidwall:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Scenario:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Seamexcitation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Seamjunction:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Seamsubsystem:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Seasubsystem:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Seatbelt:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Seatbeltcontrolpoint:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Section:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Sensor:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Sequence:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Session:
	def __init__(self):
		pass

	def chache_signals(self):
		pass

	def define_action(self,handle: int, action: hw_module.mdi.attribute.Action):
		pass

	def define_attribute(self,handle: int, attribute: hw_module.mdi.attribute.Attribute):
		pass

	def define_metaclass(self,mdiclass: str, version: str, base: str = None, isabstract=False):
		pass

	def define_uid_attribute(self,handle: int, attribute_name: str):
		pass

	def define_uid_attribute_versioning(self,handle: int, attribute_revision: str, attribute_branch: str):
		pass

	def flush_signals(self):
		pass

	def get_all_models(self):
		pass

	def get_entityfulltype_from_classname(self,metaclass: str):
		pass

	def get_entityfulltype_from_metaclass(self,handle: int):
		pass

	def get_ownership(self,owner_handle: int, child):
		pass

	def get_uid_attributename(self,fulltype):
		pass

	def getclass(self,fulltype: hwdescriptor_module.EntityFullType):
		pass

	def getclasses(self,concrete_only=False):
		pass

	def getderivedclasses(self,klass, recursive=False, leaves_only=False, concrete_only=False):
		pass

	def getversion(self,handle: int):
		pass

	def has_any_ownership(self,owner_handle: int, child):
		pass

	def has_single_child_ownership(self,owner_handle: int, child):
		pass

	def instance(self):
		pass

	def is_valid_entitytype(self,fulltype: hwdescriptor_module.EntityFullType):
		pass

	def model_exists(self,name: str):
		pass

	def on_metaclass_defined(self):
		pass

	def on_model_changed(self):
		pass

	def remove_model(self,model: hwdescriptor_module.Model):
		pass

	def set_ownership(self,owner_handle: int, child, attribute_handle: int):
		pass

class Set:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Shape:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Shape3d:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Skeleton:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Sketch:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Slipring:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Solid:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Solvermass:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Solverrepresentation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Solversetting:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Solversubmodel:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Stateequation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyBeam:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyDummyTargets:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyEjectionMitigationIP:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyGeneric:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyHeadForm:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyInstrumentPanelIP:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyLowerLegForm:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyPanelComposite:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyPanelMetallic:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyRivet:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertySpring:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyUndefined:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class StructuralpropertyUpperLegForm:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Study:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Subsystem:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Subsystemconfiguration:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Subsystemset:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Surface:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Symmetry:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Symmetrypivot:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Systcol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class System:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Table:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Tag:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Termination:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Timestepcontrol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Title:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Transformation:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class UpdateOccurrenceWorkflow:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getactions(self):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getitems(self):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Vector:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Vectorcol:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Weldline:
	def __init__(self,amodel: Model, uid: hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid = None, connection: str = None,owner: MDIObject=None, ownership_attribute: hwdescriptor_module.Identifier = None, *args, **kwargs):
		pass

	def GetActionDefinition(self,identifier: Identifier):
		pass

	def GetAllReferredBy(self,refEntity2IdentifierList: Entity2IdentifierList):
		pass

	def GetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def GetAttributeDefinition(self,identifier: Identifier):
		pass

	def GetAttributeEditability(self,identifier: Identifier):
		pass

	def GetAttributeVisibility(self,identifier: Identifier):
		pass

	def GetAttributes(self,aIdentifier: IdentifierList, onlyVisible: bool  = False, onlyEditable: bool  = False):
		pass

	def GetEntity(self,entity: Entity):
		pass

	def GetEntityFullType(self):
		pass

	def GetMetaclass(self):
		pass

	def GetModel(self):
		pass

	def GetOwned(self,*args):
		pass

	def GetOwner(self,owner: Entity, identifier: Identifier):
		pass

	def GetReferred(self,referred: Identifier2BagMap):
		pass

	def GetValue(self,identifier: Identifier, value: Value):
		pass

	def InvokeAction(self,identifier: Identifier):
		pass

	def IsValid(self):
		pass

	def ReferredBy(self,entitylist: EntityList, fromtype: EntityFullType, identifier: Identifier):
		pass

	def SetAllowables(self,identifier: Identifier, allowables: Allowables):
		pass

	def SetAttributeEditability(self,identifier: Identifier, edit: bool = True):
		pass

	def SetAttributeVisibility(self,identifier: Identifier, visible: bool = True):
		pass

	def SetValue(self,identifier: Identifier, value: Value):
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	@property
	def entity(self):
		pass
	@entity.setter
	def entity(self):
		pass

	def get_action_definition(self,identifier: str):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def get_attribute_value(self,identifier: str):
		pass

	def getaction(self,action_name):
		pass

	def getattribute(self,name):
		"""
		
        return the attribute object if in class, or 
        # create an attribute on the fly 
        
		"""
		pass

	def getattributenames(self,visible=True, editable=False):
		pass

	def getattributes(self,visible=True, editable=False):
		pass

	def getreferredby(self,fromtype, attribute_name: str):
		pass

	def invoke(self,identifier: hwdescriptor_module.Identifier):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	@property
	def name_attribute(self):
		pass
	@name_attribute.setter
	def name_attribute(self):
		pass

	def name_onupdate(self):
		pass

	def owned(self,attribute_name: str):
		pass

	@property
	def owner(self):
		pass
	@owner.setter
	def owner(self):
		pass

	def set_attribute_value(self,identifier: str, value: hwdescriptor_module.Value):
		pass

	def set_values(self,**kwds):
		"""
		setattr on name/value pairs in the order the properties are specified.
        This is called from __init__ to process the kwds
        
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class controllers:
	pass

class designpointmethods:
	pass

class designpoints:
	pass

class designpointsets:
	pass

class loads:
	pass

class mdihmmetaobject:
	pass

class plotcontrols:
	pass

class structuralproperties:
	pass

