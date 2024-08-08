from typing import TypeVar
var0=TypeVar('unsigned int',str,str)
var1=TypeVar('unsigned char',str,str)
var2=TypeVar('std::vector< unsigned int >::size_type',str,str)
class Identifier:
	pass
class Value:
	pass
class CollectionRule:
	pass
class Collection:
	pass
class Entity:
	pass
class hm_module:
	class mdi:
		class apis:
			class HmModel:
				pass
	class Collection:
		pass
class hw_module:
	class mdi:
		class base:
			class TMDIObject:
				pass
			class MDIObject:
				pass
	class collection:
		class Collection:
			pass
	class adaptors:
		class datasource:
			class DataSource:
				pass
	class attribute:
		class Action:
			pass
	class Attribute:
		pass
class Uid:
	pass
class hwUIntList:
	pass
class EntityFullType:
	pass
class hwmathbasic_module:
	def hwTriple(self, *args):
		pass
class hwIntList:
	pass
class hwStringList:
	pass
class hwDoubleList:
	pass
class hwDoubleList2:
	pass
class EntityList:
	pass
class hwTriple:
	pass
class CollectionSet:
	pass
class EntityList2:
	pass
class hwBoolList:
	pass
class hwdescriptor_module:
	class Uid:
		pass
	class Identifier:
		pass
	class Collection:
		pass
	class CollectionSet:
		pass
	class Entity:
		pass
	class Metaobject:
		pass
	class MDIFormat:
		pass
	class EntityFullType:
		pass
	class Model:
		pass
	class uint_ptr:
		pass
class hwTripleIList:
	pass
class hwTripleList:
	pass
class _hwBoolList_vector:
	pass
class hwCouple:
	pass
class _hwDoubleList_vector:
	pass
class _hwDoubleListList_vector:
	pass
class _hwIntList_vector:
	pass
class _hwIntListList_vector:
	pass
class hwMatrix44:
	pass
class hwString:
	pass
class _hwStringList_vector:
	pass
class hwTripleI:
	pass
class _hwTripleIList_vector:
	pass
class _hwTripleList_vector:
	pass
class _hwUIntList_vector:
	pass
class EntityClass:
	pass
class hwIntList2:
	pass
class ostream:
	pass

CONTAINMENT_FULL=0

CONTAINMENT_PARTIAL=1

class Collection:
	def __init__(self,*args, **kwargs):
		"""

    Constructor codepaths:
        __init__([metaobject])
        __init__(model, [entity])
        __init__(model, EntityList)
        __init__(model, Filter)
        __init__(model, FilterByCollection, source_collection)
        __init__(model, type)
        __init__(model, type, string)
        __init__(model, type, bool)
        __init__(model, type, [uid (int/string)])
        __init__(model, type, [entities from source collection], [Identifiers] | None)
        __init__(model, type, [objects from source collection], [Identifiers] | None)
        __init__(model, type, Collection, [Identifiers] | None)
    
"""
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	def add(self,rule: CollectionRule, source: Collection = None):
		pass

	def begin(self,forPython: bool = False):
		pass

	def complement(self):
		pass

	def contains(self,entity: Entity):
		pass

	def delete_items(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	def empty(self):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def intersect(self,rule: CollectionRule, source: Collection = None):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	def set_items(self,identifier: str, value):
		pass

	def subtract(self,rule: CollectionRule, source: Collection = None):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

def CollectionByAdjacent(model: hm_module.mdi.apis.HmModel, source: hm_module.Collection):
	pass

def CollectionByAttached(model: hm_module.mdi.apis.HmModel, source: hm_module.Collection):
	pass

def CollectionByDisplayed(model: hm_module.mdi.apis.HmModel, entity_class: EntityClass):
	pass

def CollectionByFace(model: hm_module.mdi.apis.HmModel, source: hm_module.Collection, across_t_junctions: bool = False):
	pass

def CollectionByInteractiveSelection(model: hm_module.mdi.apis.HmModel, entity_class: EntityClass, highlight: bool = False):
	pass

class CollectionRule:
	def __init__(self,aclass: EntityClass):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class CollectionSet:
	def __init__(self,*args):
		pass

	def clear(self):
		pass

	@property
	def eclasses(self):
		pass
	@eclasses.setter
	def eclasses(self):
		pass

	@property
	def empty(self):
		pass
	@empty.setter
	def empty(self):
		pass

	def get(self,aclass: hw_module.mdi.base.TMDIObject):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	def set(self,collection: Collection):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	def unset(self,aclass: hw_module.mdi.base.TMDIObject):
		pass

class Entity:
	def __init__(self,*args):
		pass

	def GetEntityFullType(self):
		pass

	def GetIdRef(self,*args):
		pass

	def GetTopologyIndexRef(self,*args):
		pass

	def Serialize(self,stream: ostream):
		pass

	def SetUid(self,uid: Uid):
		pass

	@property
	def mdiclass(self):
		pass
	@mdiclass.setter
	def mdiclass(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def uid(self):
		pass
	@uid.setter
	def uid(self):
		pass

class EntityFullType:
	def __init__(self,*args):
		pass

	def GetAsString(self,string: hwString, minimal: bool  = True):
		pass

	def GetSubtypeNamed(self):
		pass

	def GetSubtypeNumeric(self):
		pass

	def GetTopologyType(self):
		pass

	def GetTypeNamed(self):
		pass

	def GetTypeNumeric(self):
		pass

	def HaveSubType(self):
		pass

	def IsSubTypeNumeric(self):
		pass

	def IsTypeNumeric(self):
		pass

	def IsValid(self):
		pass

	def Serialize(self,stream: ostream):
		pass

	def hash(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class EntityList:
	def __init__(self,*args):
		pass

	def GetEntity(self,entity: Entity, i: var0 ):
		pass

	def GetEntityFullType(self):
		pass

	def GetEntityIDType(self):
		pass

	def GetId(self,i: var0 , id: var0):
		pass

	def GetIdAndTopologyIndex(self,i: var0 , id: var0, topoIndex: str):
		pass

	def GetIdList(self,aId: hwUIntList):
		pass

	def GetIdListCount(self):
		pass

	def GetList(self,*args):
		pass

	def GetTopologyIndexList(self,*args):
		pass

	def GetUid(self,i: var0 , id: Uid):
		pass

	def GetUidList(self,*args):
		pass

	def GetUidListCount(self):
		pass

	def IsCombinedType(self):
		pass

	def IsEmpty(self):
		pass

	def IsIdType(self):
		pass

	def IsUidType(self):
		pass

	def IsValid(self):
		pass

	def Reserve(self,reserve: var0 ):
		pass

	def Resize(self,count: var0 ):
		pass

	def Serialize(self,stream: ostream):
		pass

	def SetEntity(self,entity: Entity, i: var0 ):
		pass

	def SetEntityFullType(self,entityFullType: EntityFullType):
		pass

	def SetId(self,i: var0 , id: var0 , topoIndex: str  =" 0"):
		pass

	def SetLists(self,*args):
		pass

	def SetUid(self,*args):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class EntityList2:
	def __init__(self,*args):
		pass

	def GetEntity(self,entity: Entity, i: var0 , j: var0 ):
		pass

	def GetEntityFullType(self):
		pass

	def GetEntityIDType(self):
		pass

	def GetId(self,i: var0 , j: var0 , id: var0):
		pass

	def GetIdListCount(self,dimensionIndex: var0  = 1):
		pass

	def GetList(self,*args):
		pass

	def GetUid(self,i: var0 , j: var0 , id: Uid):
		pass

	def GetUidList(self,*args):
		pass

	def GetUidListCount(self,dimensionIndex: var0  = 1):
		pass

	def IsEmpty(self):
		pass

	def IsValid(self):
		pass

	def Reserve(self,sizeDimFirst: var0 , sizeDimSecond: var0  =" 0"):
		pass

	def Resize(self,sizeDimFirst: var0 , sizeDimSecond: var0  =" 0"):
		pass

	def SetEntity(self,entity: Entity, i: var0 , j: var0 ):
		pass

	def SetEntityFullType(self,entityFullType: EntityFullType):
		pass

	def SetId(self,i: var0 , j: var0 , id: var0 ):
		pass

	def SetList(self,*args):
		pass

	def SetLists(self,*args):
		pass

	def SetUid(self,*args):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class FilterByAttribute:
	def __init__(self,aclass: EntityClass, expression: str):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def expression(self):
		pass
	@expression.setter
	def expression(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class FilterByBox:
	def __init__(self,aclass: EntityClass, corner1: list[float]|hwmathbasic_module.hwTriple, corner2: list[float]|hwmathbasic_module.hwTriple, relative_location="0", containment="0", displayed_only=False, tolerance="0.0"):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetPrimitiveType(self):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def containment(self):
		pass
	@containment.setter
	def containment(self):
		pass

	@property
	def corner1(self):
		pass
	@corner1.setter
	def corner1(self):
		pass

	@property
	def corner2(self):
		pass
	@corner2.setter
	def corner2(self):
		pass

	@property
	def displayed_only(self):
		pass
	@displayed_only.setter
	def displayed_only(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def relative_location(self):
		pass
	@relative_location.setter
	def relative_location(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def tolerance(self):
		pass
	@tolerance.setter
	def tolerance(self):
		pass

class FilterByCollection:
	def __init__(self,aclass: EntityClass, source_class: EntityClass, identifiers: list[str]|list[hwdescriptor_module.Identifier] = [], *args):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def aggregation(self):
		pass
	@aggregation.setter
	def aggregation(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def identifiers(self):
		pass
	@identifiers.setter
	def identifiers(self):
		pass

	@property
	def source(self):
		pass
	@source.setter
	def source(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class FilterByCone:
	def __init__(self,aclass: EntityClass, base: list[float]|hwmathbasic_module.hwTriple, normal: list[float]|hwmathbasic_module.hwTriple, base_radius: float, top_radius: float, height: float, relative_location="0", containment="0", displayed_only=False, tolerance="0.0"):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetPrimitiveType(self):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def base(self):
		pass
	@base.setter
	def base(self):
		pass

	@property
	def base_radius(self):
		pass
	@base_radius.setter
	def base_radius(self):
		pass

	@property
	def containment(self):
		pass
	@containment.setter
	def containment(self):
		pass

	@property
	def displayed_only(self):
		pass
	@displayed_only.setter
	def displayed_only(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def normal(self):
		pass
	@normal.setter
	def normal(self):
		pass

	@property
	def relative_location(self):
		pass
	@relative_location.setter
	def relative_location(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def tolerance(self):
		pass
	@tolerance.setter
	def tolerance(self):
		pass

	@property
	def top_radius(self):
		pass
	@top_radius.setter
	def top_radius(self):
		pass

class FilterByCylinder:
	def __init__(self,aclass: EntityClass, base: list[float]|hwmathbasic_module.hwTriple, normal: list[float]|hwmathbasic_module.hwTriple, radius: float, height: float, relative_location="0", containment="0", displayed_only=False, tolerance="0.0"):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetPrimitiveType(self):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def base(self):
		pass
	@base.setter
	def base(self):
		pass

	@property
	def containment(self):
		pass
	@containment.setter
	def containment(self):
		pass

	@property
	def displayed_only(self):
		pass
	@displayed_only.setter
	def displayed_only(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def height(self):
		pass
	@height.setter
	def height(self):
		pass

	@property
	def normal(self):
		pass
	@normal.setter
	def normal(self):
		pass

	@property
	def radius(self):
		pass
	@radius.setter
	def radius(self):
		pass

	@property
	def relative_location(self):
		pass
	@relative_location.setter
	def relative_location(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def tolerance(self):
		pass
	@tolerance.setter
	def tolerance(self):
		pass

class FilterByEnumeration:
	def __init__(self,aclass: EntityClass, ids: list[str]|list[hwdescriptor_module.uint_ptr]):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetEntities(self):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class FilterByInfiniteCylinder:
	def __init__(self,aclass: EntityClass, base: list[float]|hwmathbasic_module.hwTriple, direction: list[float]|hwmathbasic_module.hwTriple, relative_location="0", containment="0", displayed_only=False, radius="0.0"):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetPrimitiveType(self):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def base(self):
		pass
	@base.setter
	def base(self):
		pass

	@property
	def containment(self):
		pass
	@containment.setter
	def containment(self):
		pass

	@property
	def direction(self):
		pass
	@direction.setter
	def direction(self):
		pass

	@property
	def displayed_only(self):
		pass
	@displayed_only.setter
	def displayed_only(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def relative_location(self):
		pass
	@relative_location.setter
	def relative_location(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def tolerance(self):
		pass
	@tolerance.setter
	def tolerance(self):
		pass

class FilterByPlane:
	def __init__(self,aclass: EntityClass, base: list[float]|hwmathbasic_module.hwTriple, normal: list[float]|hwmathbasic_module.hwTriple, relative_location="0", containment="0", displayed_only=False, tolerance="0.0"):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetPrimitiveType(self):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def base(self):
		pass
	@base.setter
	def base(self):
		pass

	@property
	def containment(self):
		pass
	@containment.setter
	def containment(self):
		pass

	@property
	def displayed_only(self):
		pass
	@displayed_only.setter
	def displayed_only(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def normal(self):
		pass
	@normal.setter
	def normal(self):
		pass

	@property
	def relative_location(self):
		pass
	@relative_location.setter
	def relative_location(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def tolerance(self):
		pass
	@tolerance.setter
	def tolerance(self):
		pass

class FilterBySolid:
	def __init__(self,aclass: EntityClass, relative_location="0", containment="0", displayed_only=False, tolerance="0_module.0"):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetPrimitiveType(self):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def containment(self):
		pass
	@containment.setter
	def containment(self):
		pass

	@property
	def displayed_only(self):
		pass
	@displayed_only.setter
	def displayed_only(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def relative_location(self):
		pass
	@relative_location.setter
	def relative_location(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def tolerance(self):
		pass
	@tolerance.setter
	def tolerance(self):
		pass

class FilterBySphere:
	def __init__(self,aclass: EntityClass, center: list[float]|hwmathbasic_module.hwTriple, radius: float, relative_location="0", containment="0", displayed_only=False, tolerance="0.0"):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetPrimitiveType(self):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def center(self):
		pass
	@center.setter
	def center(self):
		pass

	@property
	def containment(self):
		pass
	@containment.setter
	def containment(self):
		pass

	@property
	def displayed_only(self):
		pass
	@displayed_only.setter
	def displayed_only(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def radius(self):
		pass
	@radius.setter
	def radius(self):
		pass

	@property
	def relative_location(self):
		pass
	@relative_location.setter
	def relative_location(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def tolerance(self):
		pass
	@tolerance.setter
	def tolerance(self):
		pass

class Identifier:
	def __init__(self,*args):
		pass

	def GetColumn(self):
		pass

	def GetNameKey(self):
		pass

	def GetNumericKey(self):
		pass

	def GetRow(self):
		pass

	def GetSolverIdx(self):
		pass

	def IsValid(self):
		pass

	def Serialize(self,stream: ostream):
		pass

	def SetColumn(self,column: var0 ):
		pass

	def SetNameKey(self,nameKey: hwString ):
		pass

	def SetNumericKey(self,numericKey: int ):
		pass

	def SetRow(self,row: var0 ):
		pass

	def SetSolverIdx(self,solverIdx: int ):
		pass

	def UsesNameKey(self):
		pass

	def UsesNumericKey(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class List:
	def __init__(self,*args, **kwargs):
		"""
The central part of internal API.

    This represents a generic version of type 'origin' with type arguments 'params'.
    There are two kind of these aliases: user defined and special. The special ones
    are wrappers around builtin collections and ABCs in collections.abc. These must
    have 'name' always set. If 'inst' is False, then the alias can't be instantiated,
    this is used by e.g. typing.List and typing.Dict.
    
"""
		pass

	def copy_with(self,params):
		pass

class Model:
	def __init__(self,name: str = None, *args, **kwargs):
		pass

	def AE_AttachmentAbsorb(self,entity_type: EntityFullType, integer_array: hwIntList, option: int, config: var0):
		pass

	def AE_AttachmentControlConvert(self,name: hwString , config: var0):
		pass

	def AE_AttachmentControlCreateFromAnother(self,new_name: hwString , old_name: hwString , reserved: int):
		pass

	def AE_AttachmentControlCreateFromDefault(self,name: hwString , name_of_default: hwString , reserved: int):
		pass

	def AE_AttachmentControlDefaultCreate(self,reserved1: hwString , reserved2: int):
		pass

	def AE_AttachmentCreateWithOptions(self,target_collection: Collection, location_collection: Collection, search_type: hwString , attachmentcontrol: var0  =" 0", maxdiameter: float  =" 0_module.0", mindiameter: float  =" 0_module.0", tolerance: float  =" 0_module.0", snaptocenter: int  =" 0"):
		pass

	def AE_ConvertBoltLinkToAttachment(self,collection: Collection):
		pass

	def AE_Realize(self,collection: Collection, options: int):
		pass

	def AE_Unrealize(self,collection: Collection):
		pass

	def AE_UpdateLink(self,collection: Collection, uid: hwString , pid: var0 =" 0"):
		pass

	def AdjustcomponentCmd(self,collection: Collection, x: float, y: float, z: float, hide: int, show: int):
		pass

	def BCM(self,collection: Collection, load_collection: Collection, config: int, type: int, filename: hwString , tolerance: float, facenode_collection: Collection, break_angle: float):
		pass

	def CE_AddLinkEntities(self,connector_collection: Collection, entity_collection: Collection):
		pass

	def CE_AddLinkEntitiesDirectByRule(self,collection: Collection, link_type: EntityFullType, link_rule: var0, link_state: var0, link_string_array: hwStringList, extra_link_integer_array: hwIntList, create_group: var0):
		pass

	def CE_AddLinkEntitiesWithArrays(self,integer_array: hwIntList, entity_collection: Collection, entity_state: var0, ce_rules: var0, ce_le_rule: var0, tolerance_flag: var0, float_array: hwDoubleList, keep_existing: var0, ce_spot_extralinknum: var0  =" 0", ce_seam_extralinknum: var0  =" 0", ce_spot_non_normal: int  =" 0", ce_area_non_normal: int  =" 0", prefer_diff_links_per_layer: var0  =" 0"):
		pass

	def CE_AddLinkEntitiesWithDetails(self,connector_collection: Collection, entity_collection: Collection, entity_state: var0, ce_rules: var0, ce_le_rule: var0, tolerance_flag: var0, tolerance: float, num_ents: int, ce_delete_links: int  =" 0", ce_spot_extralinknum: int  =" 0", ce_seam_extralinknum: int  =" 0"):
		pass

	def CE_AddLinkEntitiesWithRules(self,connector_collection: Collection, entity_collection: Collection, entity_state: var0, ce_rules: var0, ce_le_rule: var0, tolerance_flag: var0, tolerance: float, num_ents: int):
		pass

	def CE_AddLinkEntitiesWithXYZs(self,connector_collection: Collection, entity_collection: Collection, entity_state: var0, ce_rules: var0, ce_le_rule: var0, locator: var0, xyz_array: hwDoubleList):
		pass

	def CE_AutoCreateMatingConnectors(self,collection: Collection, Allow_Hole_to_Tube: bool  = False, Allow_mismatched_shapes: bool  = True, Allow_Self: bool  = False, Center_CE: bool  = False, Hole_Type: var0  = 7, Lateral_Distance: bool  = True, Max_Angle: float  =" 1_module.0", Max_dia: float  =" 10_module.0", Max_Distance: float  =" 10_module.0", Max_lateral_factor: float  =" 0_module.0", Min_dia: float  =" 0_module.0", Lateral_Factor: bool  = False, Max_lateral_distance: float  =" 1_module.0"):
		pass

	def CE_AutoReorganize(self,cemarkmask: Collection, criteria: var0):
		pass

	def CE_BoltAutoCreateFromAttachments(self,*args, **kwargs):
		"""
		CE_BoltAutoCreateFromAttachments(HMAPI self, Collection collection, double const tolerance=0.000000, double const mindiameter=0.000000, double const maxdiameter=0.000000, hwString const & ce_config_name="", hwString const & ce_controller_name="", int const only2layers=0, double const maxangle=0.000000)
		"""
		pass

	def CE_Cleanup(self,collection: Collection):
		pass

	def CE_ColinearityCheck(self,ce_incollection: Collection, outputcollection: Collection, angle: float, diameter: float, future1: int, future2: int, future3: int):
		pass

	def CE_ConnectorAlignment(self,ce_collection: Collection, search_dist: float):
		pass

	def CE_ConnectorAreaCreate(self,entitycollection: Collection, linkcollection: Collection, ent_state: var0, ce_rules: var0, ce_le_rule: var0, tol_flag: var0, tolerance: float, group: int, param1: int, param2: float):
		pass

	def CE_ConnectorAreaCreateFromList(self,entitylist: EntityList, width: float, offset: float, linkcollection: Collection, ent_state: var0, ce_rules: var0, ce_le_rule: var0, tol_flag: var0, tolerance: float, group: int, param1: int, param2: float):
		pass

	def CE_ConnectorAreaMapMesh(self,ce_collection: Collection, entitycollection: Collection, vectorptr: hwTriple, tolerance: float, param1: int):
		pass

	def CE_ConnectorAreaMesh(self,ce_collection: Collection, elementsize: float, elem_type: int, elem_type2: int, link_opposite_edge: int, size_control: int, skew_control: int, edge_mesh_algorithm: int, min_size: float, max_size: float, chordal_dev: float, max_angle: float, param1: int, param2: float):
		pass

	def CE_ConnectorAreaMeshWithDetails(self,collection: Collection, element_size: float, element_type: int, element_type2: int, link_opposite_edges: int, size_control: int, skew_control: int, edge_mesh_algorithm: int, min_size: float, max_size: float, chordal_deviation: float, max_angle: float, area_width: float, area_offset: float):
		pass

	def CE_ConnectorAreaTrim(self,collection: Collection, node_collection: EntityList, tolerance: float, snap: int, mode: int):
		pass

	def CE_ConnectorCombine(self,collection: Collection, tolerance: float, ignore_links: int =" 0", overlaps: int = 100):
		pass

	def CE_ConnectorCreate(self,collection: Collection):
		pass

	def CE_ConnectorCreateAndFERealizeForTrimMass(self,entitycollection: Collection, linkentitycollection: Collection, ce_rules: var0, ce_le_rule: var0, tolerance: float, num_ents: int, config: var0, mass: float, distribution_type: var0, param1: var0):
		pass

	def CE_ConnectorCreateByAutopitch(self,collection: Collection, feature_angle: float, consider_thin_solids: int, max_flange_width: float, max_proximity_distance: float, autopitch_interval: float, autopitch_offset: float, autopitch_to_edge_distance: float, create_points_in_middle: int, max_variation_percent: float):
		pass

	def CE_ConnectorCreateByAutopitchNew(self,collection: Collection, maxProximityDistance: float , autopitchInterval: float , autopitchToEdgeDistance: float , autopitchFeatureEdgeDistance: float , autopitchOffset: float  =" 0_module.0", considerThinSolids: var0  = 1, createPointsInMiddle: var0  =" 0", featureAngle: float  =" 180_module.0", maxFlangeWidth: float  =" 0_module.0", maxVariationPercent: float  =" 0_module.0", combineSpots: int  =" 0", maxLinks: int  = 2, excludeHolesWithWidthLessThan: float  =" 0_module.0"):
		pass

	def CE_ConnectorCreateByAutoseam(self,collection: Collection, options: hwString ):
		pass

	def CE_ConnectorCreateByList(self,*args, **kwargs):
		"""
		CE_ConnectorCreateByList(HMAPI self, EntityList list, hwString const & ce_style, int num_links, Collection link_collection, hwString const & link_elems_geom="", hwString const & link_rule="", hwString const & relink_rule="", int const tol_flag=0, double const tol=0.000000, int const line_preserve_nodes=0, double const line_spacing=1.000000, int const line_density=0, int const line_offset_flag=0, double const line_offset=0.000000, double const start_offset=0.000000, double const end_offset=0.000000, int const retain_line=1, int const seam_area_group=0, int const ce_nonnormal=0, double const area_width=0.000000, double const area_offset=0.000000, int const area_mesh_type=0, double const area_mesh_size=10.000000, int const loc_as_link=0, int const ce_extralinknum=0, int const ce_hexaoffsetcheck=0, double const area_linecombine=0.000000, int const ce_normal_link=0, int const ce_link_option=0, double const ce_normal_angle=0.000000, double const ce_center_pos=0.000000, double const ce_boltmindiameter=0.000000, double const ce_boltmaxdiameter=0.000000, int const ce_boltcenterset=0, int const ce_num_center=0, int const ce_maxlinkupto=0, hwString const & line_combine_option="", int const smooth_curve_nodes=0, hwTriple ce_boltcenter=hwTriple(0.000000, 0.000000, 0.000000), hwString const & ce_config_name="", hwString const & ce_engg_name="", double const ce_seam_vertex_angle=45.000000, int const line_preserve_joints=0, int const ce_seam_discontinuity=0, bool const eline_flag=False, int const disable_multilinks=0, bool const grouplinks=False, int const main_link_count=0, hwIntList main_link_ids=hwIntList())
		"""
		pass

	def CE_ConnectorCreateByListAndRealizeWithDetails(self,*args, **kwargs):
		"""
		CE_ConnectorCreateByListAndRealizeWithDetails(HMAPI self, EntityList list, hwString const & ce_style, int num_links, Collection link_collection, hwString const & solver_name, int config, int fe_type, double tolerance, double const area_offset=0.000000, double const area_width=1.000000, double const line_density=0.000000, double const line_offset=0.000000, unsigned int const line_offset_flag=0, double const line_spacing=1.000000, hwString const & link_elems_geom="elems", hwString const & link_rule="none", hwString const & relink_rule="none", int const seam_area_group=0, double const tol=0.000000, int const tol_flag=0, double const ce_appliedmass=0.000000, int const ce_appliedmassdis=0, double const ce_areaconstantthickness=0.000000, int const ce_areathicknesstype=0, int const ce_areastacksize=0, double const ce_boltmaxdiameter=1.000000, double const ce_boltmindiameter=0.000000, hwString const & ce_configfile="", int const ce_connectivity=0, double const ce_diameter=0.000000, hwString const & ce_dvstfile="", int const ce_fevectorreverse=0, int const ce_forcecollinear=0, int const ce_nonnormal=0, int const ce_propertyid=0, hwString const & ce_propertyscript="", int const ce_systems=0)
		"""
		pass

	def CE_ConnectorCreateByListWithCC(self,*args, **kwargs):
		"""
		CE_ConnectorCreateByListWithCC(HMAPI self, EntityList list, hwString const & ce_style, int num_links, Collection link_collection, EntityFullType cc_type, hwString const & cc_name, double const area_mesh_size=1.000000, int const area_mesh_type=0, double const area_offset=0.000000, double const area_width=1.000000, double const line_density=0.000000, double const line_offset=0.000000, int const line_offset_flag=0, double const line_spacing=1.000000, hwString const & link_elems_geom="geom", hwString const & link_rule="none", hwString const & relink_rule="none", int const seam_area_group=0, double const tol=0.000000, int const tol_flag=0)
		"""
		pass

	def CE_ConnectorCreateByMark(self,*args, **kwargs):
		"""
		CE_ConnectorCreateByMark(HMAPI self, Collection collection, hwString const & ce_style, int num_links, Collection link_collection, hwString const & link_elems_geom="", hwString const & link_rule="", hwString const & relink_rule="", int const tol_flag=0, double const tol=0.000000, int const line_preserve_nodes=0, double const line_spacing=1.000000, int const line_density=0, int const line_offset_flag=0, double const line_offset=0.000000, double const start_offset=0.000000, double const end_offset=0.000000, int const retain_line=1, int const seam_area_group=0, int const ce_nonnormal=0, double const area_width=0.000000, double const area_offset=0.000000, int const area_mesh_type=0, double const area_mesh_size=10.000000, int const loc_as_link=0, int const ce_extralinknum=0, int const ce_hexaoffsetcheck=0, double const area_linecombine=0.000000, int const ce_normal_link=0, int const ce_link_option=0, double const ce_normal_angle=0.000000, double const ce_center_pos=0.000000, double const ce_boltmindiameter=0.000000, double const ce_boltmaxdiameter=0.000000, int const ce_boltcenterset=0, int const ce_num_center=0, int const ce_maxlinkupto=0, hwString const & line_combine_option="", int const smooth_curve_nodes=0, hwTriple ce_boltcenter=hwTriple(0.000000, 0.000000, 0.000000), hwString const & ce_config_name="", hwString const & ce_engg_name="", double const ce_seam_vertex_angle=45.000000, int const line_preserve_joints=0, int const ce_seam_discontinuity=0, bool const eline_flag=False, int const disable_multilinks=0, bool const grouplinks=False, int const main_link_count=0, hwIntList main_link_ids=hwIntList())
		"""
		pass

	def CE_ConnectorCreateByMarkAndRealizeWithDetails(self,*args, **kwargs):
		"""
		CE_ConnectorCreateByMarkAndRealizeWithDetails(HMAPI self, Collection entitycollection, hwString const & ce_style, int num_ents, Collection linkentcollection, hwString const & solvername, int config, int fe_type, double tolerance, int const area_mesh_type=1, double const area_mesh_size=0.000000, hwString const & link_elems_geom="geom", hwString const & link_rule="none", hwString const & relink_rule="none", int const tol_flag=0, double const tol=0.000000, double const line_spacing=1.000000, unsigned int const line_density=0, unsigned int const line_offset_flag=0, double const line_offset=0.000000, int const seam_area_group=0, double const area_width=1.000000, double const area_offset=0.000000, unsigned int const ce_propertyid=0, int const ce_systems=0, int const ce_connectivity=0, int const ce_forcecollinear=0, double const ce_diameter=0.000000, int const ce_areathicknesstype=0, double const ce_areaconstthickness=0.000000, int const ce_areastacksize=0, double const ce_boltmindiameter=0.000000, double const ce_boltmaxdiameter=10.000000, double const ce_appliedmass=0.000000, int const ce_appliedmassdis=0, hwString const & ce_configfile="", hwString const & ce_dvstfile="", hwString const & ce_propertyscript="", int const ce_fevectorrevers=0)
		"""
		pass

	def CE_ConnectorCreateByMarkWithCC(self,*args, **kwargs):
		"""
		CE_ConnectorCreateByMarkWithCC(HMAPI self, Collection collection, hwString const & ce_style, int num_links, Collection link_collection, EntityFullType cc_type, hwString const & cc_name, double const area_mesh_size=10.000000, int const area_mesh_type=0, double const area_offset=0.000000, double const area_width=1.000000, double const line_density=0.000000, double const line_offset=0.000000, int const line_offset_flag=0, double const line_spacing=1.000000, hwString const & link_elems_geom="geom", hwString const & link_rule="none", hwString const & relink_rule="none", int const seam_area_group=0, double const tol=0.000000, int const tol_flag=0)
		"""
		pass

	def CE_ConnectorCreateWithRules(self,collection: Collection, entitycollection: Collection, ent_state: var0, ce_rules: var0, ce_le_rule: var0, tol_flag: var0, tolerance: float, num_ents: int):
		pass

	def CE_ConnectorGroup(self,connector_collection: Collection, group: int):
		pass

	def CE_ConnectorGroupCreateAndOrganizeConnectors(self,*args, **kwargs):
		"""
		CE_ConnectorGroupCreateAndOrganizeConnectors(HMAPI self, EntityFullType entity_type, unsigned int criteria=0, unsigned int delete_cleared_groups=0, unsigned int organize_all_ces=0, Collection ce_collection=s_defaultCollection)
		"""
		pass

	def CE_ConnectorLineCombineWithCC_bycollection(self,*args, **kwargs):
		"""
		CE_ConnectorLineCombineWithCC_bycollection(HMAPIBase self, Collection connectors, Collection collection, hwString const & ce_style, int const num_links, Collection link_collection, EntityFullType cc_type, hwString const & cc_name, double const area_mesh_size=10.0, int const area_mesh_type=1, double const area_offset=0.0, double const area_width=1.0, hwString const & line_combine_option="", unsigned int const line_density=0, double const line_offset=0.0, unsigned int const line_offset_flag=0, double const line_spacing=1.0, hwString const & link_elems_geom="geom", hwString const & link_rule="none", hwString const & relink_rule="none", int const seam_area_group=0, double const tol=0.0, unsigned int const tol_flag=0)
		"""
		pass

	def CE_ConnectorLineCombineWithCC_byentitylist(self,*args, **kwargs):
		"""
		CE_ConnectorLineCombineWithCC_byentitylist(HMAPIBase self, Collection connectors, EntityList entityList, hwString const & ce_style, int const num_links, Collection link_collection, EntityFullType cc_type, hwString const & cc_name, double const area_mesh_size=10.0, int const area_mesh_type=1, double const area_offset=0.0, double const area_width=1.0, hwString const & line_combine_option="", unsigned int const line_density=0, double const line_offset=0.0, unsigned int const line_offset_flag=0, double const line_spacing=1.0, hwString const & link_elems_geom="geom", hwString const & link_rule="none", hwString const & relink_rule="none", int const seam_area_group=0, double const tol=0.0, unsigned int const tol_flag=0)
		"""
		pass

	def CE_ConnectorLineCombine_bycollection(self,*args, **kwargs):
		"""
		CE_ConnectorLineCombine_bycollection(HMAPIBase self, Collection connectors, Collection collection, hwString const & ce_style, int const num_links, Collection link_collection, double const area_mesh_size=10.0, int const area_mesh_type=1, double const area_offset=0.0, double const area_width=1.0, hwString const & line_combine_option="", unsigned int const line_density=0, double const line_offset=0.0, unsigned int const line_offset_flag=0, double const line_spacing=1.0, hwString const & link_elems_geom="geom", hwString const & link_rule="none", hwString const & relink_rule="none", int const seam_area_group=0, double const tol=0.0, unsigned int const tol_flag=0)
		"""
		pass

	def CE_ConnectorLineCombine_byentitylist(self,*args, **kwargs):
		"""
		CE_ConnectorLineCombine_byentitylist(HMAPIBase self, Collection connectors, EntityList entityList, hwString const & ce_style, int const num_links, Collection link_collection, double const area_mesh_size=10.0, int const area_mesh_type=1, double const area_offset=0.0, double const area_width=1.0, hwString const & line_combine_option="", unsigned int const line_density=0, double const line_offset=0.0, unsigned int const line_offset_flag=0, double const line_spacing=1.0, hwString const & link_elems_geom="geom", hwString const & link_rule="none", hwString const & relink_rule="none", int const seam_area_group=0, double const tol=0.0, unsigned int const tol_flag=0)
		"""
		pass

	def CE_ConnectorLineCreate(self,collection: Collection, density: var0, spacing: float, half_spacing_offset: var0, offset: float):
		pass

	def CE_ConnectorLineCreateWithRules(self,collection: Collection, density: var0, spacing: float, half_spacing_offset: var0, offset: float, entitycollection: Collection, ent_state: var0, ce_rules: var0, ce_le_rule: var0, tol_flag: var0, tolerance: float, num_ents: int):
		pass

	def CE_ConnectorPartition(self,connector_collection: Collection, non_normal: int, use_tol: int, tol: float, passed_comp_type: int, passed_comp: hwString , number_passed_type: int, passed_start_id: int, failed_comp_type: int, failed_comp: hwString , number_failed_type: int, failed_start_id: int, backup: int, backup_comp_type: int, backup_comp: hwString , ce_pass_fail_organize: int =" 0"):
		pass

	def CE_ConnectorRemoveDuplicates(self,collection: Collection, tolerance: float, option: int, entities: EntityFullType, ignore_links: int, overlaps: int):
		pass

	def CE_ConnectorSeamCreateUsingLinelist(self,line_list: EntityList, density: var0, spacing: float, entitycollection: Collection, ent_state: var0, ce_rules: var0, ce_le_rule: var0, tol_flag: var0, tolerance: float, group: int, param1: int, param2: float):
		pass

	def CE_ConnectorSeamCreateUsingLines(self,entitycollection: Collection, density: var0, spacing: float, linkcollection: Collection, ent_state: var0, ce_rules: var0, ce_le_rule: var0, tol_flag: var0, tolerance: float, group: int, param1: int, param2: float):
		pass

	def CE_ConnectorSeamTrim(self,collection: Collection, node_collection: Collection, tolerance: float, snap: int, mode: int):
		pass

	def CE_ConnectorSetVectorById(self,ce_id: var0, type: var0, i: float, j: float, k: float, vector: Entity, node1: Entity, node2: Entity):
		pass

	def CE_ConnectorSetVectorByMark(self,collection: Collection, type: var0, i: float, j: float, k: float, vector: Entity, node1: Entity, node2: Entity):
		pass

	def CE_ConnectorSpotTrim(self,collection: Collection, node_collection: Collection, tolerance: float, snap: int, mode: int):
		pass

	def CE_ConnectorTrimAdvanced(self,style: hwString , collection: Collection, node_collection: Collection, tolerance: float, snap: int, mode1: int, mode2: int):
		pass

	def CE_ConnectorsUpdateByMetadata(self,*args, **kwargs):
		"""
		CE_ConnectorsUpdateByMetadata(HMAPI self, Collection connector_collection, hwString const & md_link_type="", hwString const & md_link="", hwString const & md_connector_type="", hwString const & md_isoprocess_type="")
		"""
		pass

	def CE_ConvertByMark(self,collection: Collection, source_style: hwString , target_style: hwString , reserved1: int, reserved2: int):
		pass

	def CE_ConvertByMark_new(self,collection: Collection, source_style: hwString , target_style: hwString , tolerance: float, angle: float, unrealized_flag: var0, combine_within_comp_only: var0, ignore_link: int =" 0"):
		pass

	def CE_ConvertLinksByMark(self,collection: Collection, target_entity_type: EntityFullType, link_index: int, target_link_rule: int =" 0", target_link_state: int =" 0", keep_current_state: var0 =" 0"):
		pass

	def CE_CreateNodeOnSeamConnector(self,collection: Collection, x: float =" 0_module.0", y: float =" 0_module.0", z: float =" 0_module.0"):
		pass

	def CE_CreateNodeOnSpotConnector(self,collection: Collection, x: float =" 0_module.0", y: float =" 0_module.0", z: float =" 0_module.0"):
		pass

	def CE_CreateXMCFData(self,collection: Collection):
		pass

	def CE_DetailDelete(self,ce_id: var0, detailType: hwString , detailName: hwString , unknownFlag: var0):
		pass

	def CE_DetailDeleteByMark(self,collection: Collection, detailType: hwString , detailName: hwString , unknownFlag: var0):
		pass

	def CE_DetailSetDouble(self,connector_id: var0, detail_name: hwString , float_value: float, reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetDoubleByMark(self,collection: Collection, detail_name: hwString , float_value: float, reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetInt(self,connector_id: var0, detail_name: hwString , integer_value: int, reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetIntByMark(self,collection: Collection, detail_name: hwString , integer_value: int, reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetString(self,connector_id: var0, detail_name: hwString , string_value: hwString , reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetStringByMark(self,collection: Collection, detail_name: hwString , string_value: hwString , reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetTriple(self,connector_id: var0, detail_name: hwString , triple_value1: float, triple_value2: float, triple_value3: float, reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetTripleByMark(self,collection: Collection, detail_name: hwString , triple_value1: float, triple_value2: float, triple_value3: float, reserved: var0, force_storage: var0):
		pass

	def CE_DetailSetUint(self,ce_id: var0, detailName: hwString , uint_val: var0, unknownFlag: var0, force_storage_flag: var0):
		pass

	def CE_DetailSetUintByMark(self,collection: Collection, detailName: hwString , uint_val: var0, unknownFlag: var0, force_storage_flag: var0):
		pass

	def CE_DetailsCopy(self,id: var0, collection: Collection, reserved: int):
		pass

	def CE_DetermineConnectionType(self,collection: Collection, option: int):
		pass

	def CE_EditSeamAndLineDetail(self,ce_collection: Collection, density: var0 =" 0", spacing: float =" 0_module.0", half_spacing_offset: var0 =" 0", offset: float =" 0_module.0", param1: var0 =" 0", param2: float =" 0_module.0", vertex_angle: float =" 0_module.0"):
		pass

	def CE_ErrorSet(self,id: var0, error_code: var0):
		pass

	def CE_ExportFile(self,collection: Collection, ce_style: hwString , filename: hwString , header_string: hwString , with_md: int, option: int, reserved1: hwString , reserved2: float, with_femd: int =" 0", with_appd: int =" 0"):
		pass

	def CE_ExportFiles(self,collection: Collection, ce_style: hwString , option: int, reserved1: hwString , reserved2: float, reserved3: int):
		pass

	def CE_ExportMainConnectorsFile(self,collection: Collection, filename: hwString , header_string: hwString , with_md: int):
		pass

	def CE_ExportOneFile(self,collection: Collection, ce_style: hwString , filename: hwString , option: int, reserved1: hwString , reserved2: float, reserved3: int):
		pass

	def CE_FE_1DQuality(self,ce_incollection: Collection, outputcollection: Collection, free1d: int, length_flag: int, length: float, angle_flag: int, angle: float):
		pass

	def CE_FE_3DQuality(self,ce_incollection: Collection, outputcollection: Collection, length_flag: int, length: float, jacobian_flag: int, jacobian: float):
		pass

	def CE_FE_Absorb(self,*args, **kwargs):
		"""
		CE_FE_Absorb(HMAPI self, int create_flag, hwString const & curr_solver, int num_body_cfgs, hwString const & body_cfgs, int num_head_cfgs, hwString const & head_cfgs, hwIntList elem_filter, Collection collection=s_defaultCollection, int const check_for_material=0, int const combine=0, int const conn_at_centernode=0, int const force_proj=0, int const link_by_card=0, int const link_by_interface=0, hwString const & mcf="", int const org=0, hwString const & rul="None", hwString const & shell_connect="none", hwString const & t_connect="none", int const thickness_type=0, double const tol=0.000000, int const type2_interface=0, hwString const & weld_cfg_name="", int const weld_type_num=0, hwString const & weld_type_name="", int const area_absorption=0, int const area_headonly=0, int const area_in_middle=0, int const cluster_identify=0, int const group_links=0, int const seam_absorption=0, int const seam_headonly=0, int const select_special=0, int const tie_contact=0)
		"""
		pass

	def CE_FE_AutoRegisterSharedEntitiesByMark(self,collection: Collection):
		pass

	def CE_FE_ConnectorUpdateByCC(self,ce_collection: Collection, cc_name: hwString , cc_type: EntityFullType):
		pass

	def CE_FE_CreateDCC(self,reserved: int):
		pass

	def CE_FE_CreateUCCFromConnector(self,cc_name: hwString , ce_id: var0):
		pass

	def CE_FE_CreateUCCFromDCC(self,cc_name: hwString , ccd_name: hwString ):
		pass

	def CE_FE_CreateUCCFromUCC(self,cc_name: hwString , cc_existing_name: hwString ):
		pass

	def CE_FE_GlobalFlags(self,ce_fe_flag: var0, function: var0):
		pass

	def CE_FE_LoadFeConfig(self,filename: hwString , load_option: int, overwrite: int):
		pass

	def CE_FE_RealizeWithDetails(self,*args, **kwargs):
		"""
		CE_FE_RealizeWithDetails(HMAPI self, Collection ce_collection, hwString const & ce_style, hwString const & solvername, int config, int fe_type, int collectorflag, double tolerance, int const ce_propertyid=0, int const ce_systems=0, int const ce_connectivity=0, int const ce_forcecollinear=0, int const ce_nonnormal=0, double const ce_diameter=0.000000, int const ce_areathicknesstype=0, double const ce_areaconstthickness=0.000000, int const ce_areastacksize=0, double const ce_boltmindiameter=0.000000, double const ce_boltmaxdiameter=10.000000, double const ce_appliedmass=0.000000, int const ce_appliedmassdis=0, hwString const & ce_configfile="", hwString const & ce_dvstfile="", hwString const & ce_propertyscript="", int const ce_fevectorreverse=0)
		"""
		pass

	def CE_FE_Register(self,connector: Entity, testpoint_idx: var0 , existing_entities: CollectionSet):
		pass

	def CE_FE_RegisterAdvanced(self,integer_array: EntityList):
		pass

	def CE_FE_SetCommonDetails(self,string_array: hwStringList, reserved: float):
		pass

	def CE_FE_SetDetails(self,collection: Collection, config: int, tolerance: float, property_id: var0, system_flag: int, snap_to_node: int, remesh: int, force_collinear: int, fe_type: int):
		pass

	def CE_FE_SetDetailsAndRealize(self,connector_collection: Collection, config: int, tolerance: float, property_id: var0, systems: int, snap_to_node: int, remesh: int, force_collinear: int, diameter: float, fe_type: int, file_names: hwStringList):
		pass

	def CE_FE_SetSpecificDetail(self,connector_collection: Collection, detail_type: int, integer_value: int, float_value: float):
		pass

	def CE_FE_SetSpecificDetailById(self,ce_id: var0, detail_type: int, int_val: int, dbl_val: float):
		pass

	def CE_FE_UCCUpdateByDCC(self,cc_name: hwString , ccd_name: hwString ):
		pass

	def CE_FE_UnregisterRealizedEntities_byallentitytypes(self,*args, **kwargs):
		"""
		CE_FE_UnregisterRealizedEntities_byallentitytypes(HMAPIBase self, Collection ce_collection, CollectionSet collection_set=hwDescriptor::CollectionSet())
		"""
		pass

	def CE_FE_UnregisterRealizedEntities_bycollection(self,ce_collection: Collection, collection: Collection):
		pass

	def CE_FE_UnregisterRealizedEntities_byentitytype(self,ce_collection: Collection, entity_type: EntityFullType):
		pass

	def CE_FE_UnregisterSharedEntitiesByMark(self,collection: Collection):
		pass

	def CE_FE_UpdateUCCUseConnector(self,ucc_name: hwString , ce_id: var0):
		pass

	def CE_GlobalSetDouble(self,name: hwString , value: float):
		pass

	def CE_GlobalSetInt(self,name: hwString , value: int):
		pass

	def CE_GlobalSetString(self,name: hwString , value: hwString ):
		pass

	def CE_InputSigPoints(self,entity_collection: Collection, connector_collection: Collection, tolerance: float  =" 0_module.0"):
		pass

	def CE_MarkCombineLinks(self,collection: Collection, search_type: EntityFullType, search_rule: var0, update_state: var0, search_string_array: hwStringList, keep_realized: var0 =" 0"):
		pass

	def CE_MarkRemoveLink(self,ce_collection: Collection, option: int, link_entity: Entity, link_name: hwString ):
		pass

	def CE_MarkRemoveLinkMark(self,collection: Collection, link_collection: Collection, update_layer_option: int):
		pass

	def CE_MarkReplaceLinkEntities(self,collection: Collection, link_collection: Collection, ce_style: hwString , num_ents: int, string_array: hwStringList):
		pass

	def CE_MarkSplitLink(self,collection: Collection, search_type: EntityFullType, search_rule: var0, search_string_array: hwStringList, keep_realized: var0 =" 0"):
		pass

	def CE_MarkUpdateLink(self,collection: Collection, search_entity: Entity, search_name: hwString , search_rule: var0, replace_entity: Entity, replace_name: hwString , replace_rule: var0, replace_state: var0):
		pass

	def CE_MarkUpdateLinkGroup(self,collection: Collection, search_type: EntityFullType, search_rule: var0, replace_type: EntityFullType, replace_rule: var0, search_list_and_update_list_string_array: hwStringList, search_list_length: var0, replace_state: var0, keep_current_state: var0):
		pass

	def CE_MarkUpdateLinkMark(self,collection: Collection, search_collection: Collection, replace_type: EntityFullType, replace_rule: var0, replace_state: var0, string_array: hwStringList, keep_current_state: var0 =" 0"):
		pass

	def CE_PositionConnectors(self,collection: Collection, center_source: var0, upon_state: var0):
		pass

	def CE_PreviewBoltCylinder(self,*args, **kwargs):
		"""
		CE_PreviewBoltCylinder(HMAPI self, Collection collection, hwString const & solver_name, int config, int fe_config, double tolerance, double const ce_bodylen=0.000000, double const ce_dia_factor=0.000000, double const ce_diameter=0.000000, hwTriple ce_ijk=hwTriple(0.000000, 0.000000, 0.000000), double const ce_l1=0.000000, double const ce_l1d1=0.000000, double const ce_l2=0.000000, double const ce_l2d2=0.000000, int const ce_passthroughce=0, int const ce_notuseijk=0)
		"""
		pass

	def CE_PreviewCombine(self,outputcollection: Collection, tolerance: float, ignore_links: int =" 0", overlaps: int = 100):
		pass

	def CE_PreviewDuplicates(self,outputcollection: Collection, tolerance: float, option: int, entities: EntityFullType, ignore_links: int, overlaps: int):
		pass

	def CE_ProjectionCheck(self,ce_incollection: Collection, ce_outcollection: Collection, length_flag: int, length: float, tolerance: float, sel_type: int, future1: int, future2: int, future3: int):
		pass

	def CE_ReadXmlString(self,string: hwString , reserved1: int, reserved2: int):
		pass

	def CE_Realize(self,collection: Collection):
		pass

	def CE_RemoveLink(self,ce_id: var0, option: int, link_entity: Entity, link_name: hwString ):
		pass

	def CE_RemoveSigPoints(self,ce_id: var0):
		pass

	def CE_RerunPost(self,ce_collection: Collection, option: int):
		pass

	def CE_ReverseSigPoints(self,connector_id: var0):
		pass

	def CE_ReviewConnectorCollectors(self,collection: Collection, operation_type: hwString , output_collection: CollectionSet, consider_geom: bool  = True, consider_HAZ_elems: bool  = True, filter_projection_entities: int  =" 0"):
		pass

	def CE_ReviewConnectors(self,collection_set: CollectionSet, operation_type: hwString , output_collection_set: CollectionSet, consider_geom: bool  = True, consider_HAZ_elems: bool  = True, find_twince_option: int  =" 0", filter_projection_entities: int  =" 0"):
		pass

	def CE_ReviewConnectorsReverse(self,entity_type: EntityFullType, output_collection_set: CollectionSet, first_connector_entity: var0  =" 0", linked_entity: var0  =" 0", realization_connector: var0  =" 0", second_connector_entity: var0  =" 0"):
		pass

	def CE_ReviewLinks(self,collection: Collection, operation_type: hwString , output_collection: CollectionSet, consider_geom: bool  = True, consider_HAZ_elems: bool  = True, find_twince_option: int  = 1, filter_projection_entities: int  =" 0"):
		pass

	def CE_SeamCombineByMark(self,collection: Collection, i_tolerance: float, i_angle: float, i_unrealize: var0, i_onecomp: var0, ignore_link: int =" 0"):
		pass

	def CE_SeamConnectorFromWeldLine(self,weldlines_collection: Collection, option: int):
		pass

	def CE_SeamConnectorTestPointAlignment(self,ce_collection: Collection, tolerance: float, option_1: int, option_2: int):
		pass

	def CE_SeamConnectorToWeldLine(self,ce_collection: Collection, option: int):
		pass

	def CE_SetGlobalSharedEntitySettings(self,setting: hwString , value: int):
		pass

	def CE_SetLinkChangeManagerSettings(self,perform: int, operation: int):
		pass

	def CE_SetSpecificDetail(self,ce_collection: Collection, detail_type: int, int_val: int, dbl_val: float):
		pass

	def CE_SetSpecificDetailById(self,ce_id: var0, detail_type: int, int_val: int, dbl_val: float):
		pass

	def CE_TooCloseToEdgeCheck(self,ce_collection: Collection, output_collection: Collection, distance: float, feature_ang: float, edge_option: int, auto_fix: int):
		pass

	def CE_Unrealize(self,collection: Collection):
		pass

	def CE_UpdateCustomMessage(self,id: var0, message_code: var0):
		pass

	def CE_UpdateLink(self,*args, **kwargs):
		"""
		CE_UpdateLink(HMAPI self, unsigned int id, Entity search_entity, hwString const & search_name, unsigned int search_rule, Entity replace_entity, hwString const & replace_name, unsigned int replace_rule, unsigned int replace_state, unsigned int keep_current_state=0, hwString const & search_uid=s_defaultString, hwString const & replace_uid=s_defaultString)
		"""
		pass

	def CE_postrealize_topologymodify(self,collection: Collection, elementsize: float, minelementsize: float, flags: int, param1: float, param2: float):
		pass

	def ChangeFldCurves(self,onoff: int, name: hwString ):
		pass

	def CheckBinderSetting(self,collection1: Collection, collection2: Collection):
		pass

	def Connect(self,*args):
		pass

	def Create(self,*args):
		pass

	def CreateCollectionByAdjacent(self,source: hw_module.mdi.collection.Collection):
		pass

	def CreateCollectionByAttached(self,source: hw_module.mdi.collection.Collection):
		pass

	def CreateCollectionByDisplayed(self,aclass: hw_module.mdi.base.TMDIObject):
		pass

	def CreateCollectionByFace(self,source: hw_module.mdi.collection.Collection, across_t_junctions: bool = False):
		pass

	def CreateCollectionByInteractiveSelection(self,aclass: hw_module.mdi.base.TMDIObject, highlight: bool = False):
		pass

	def Delete(self,entity: Entity):
		pass

	def DeleteThisComponent(self,name: hwString ):
		pass

	def Disconnect(self,connectionName: hwString ):
		pass

	def EdgeBasedSurfaceMesh(self,surfcollection: Collection, minSize: float, maxSize: float):
		pass

	def EntityDeleteEmpty(self,output_collection: Collection):
		pass

	def EntityDeleteUnused(self,output_collection: Collection):
		pass

	def EntityMoveUsingArray(self,collector_list: EntityList2, element_list: EntityList):
		pass

	def EntityPreviewEmpty(self,output_collection: Collection):
		pass

	def EntityPreviewUnused(self,output_collection: Collection):
		pass

	def ExportAssemblyAndGlobalEntities(self,file_path: hwString ):
		pass

	def FE_geometry_config(self,config_string: hwString ):
		pass

	def Fixed_Addendum_Machine(self,action: int, type: int, collection1: Collection, collection2: Collection, linlist: EntityList, radius1: float, radius2: float, radius3: float, fixed: int, split: int):
		pass

	def Free_Addendum_Machine(self,action: int, type: int, collection1: Collection, surfptr: Entity, collection2: Collection):
		pass

	def GetAllEntities(self,set: CollectionSet):
		pass

	def GetLatitudeLineHandles(self,collection1: Collection, collection2: Collection, selection_type: int):
		pass

	def GetName(self):
		pass

	def GetSession(self):
		pass

	def GetSigSlotHandler(self,*args):
		pass

	def HWRM(self,configureFile: hwString , exportTemplate: hwString , exportFile: hwString ):
		pass

	def Load(self,*args):
		pass

	def ME_ConvertIncludesToModules(self,include_id: var0, part_entity: Entity, recursive_flag: int, delete_flag: int, force_flag: int, entities: hwString ):
		pass

	def ME_CoreBehaviorAdjust(self,options: hwString ):
		pass

	def ME_ModuleExport(self,part_entity: Entity, recursive: int, filename: hwString , export_template: hwString , string_array: hwStringList):
		pass

	def ME_ModuleOccurrenceBackPropagate(self,part_entity: Entity, options: hwString ):
		pass

	def ME_ModuleOccurrenceClone(self,*args, **kwargs):
		"""
		ME_ModuleOccurrenceClone(HMAPI self, Entity part_entity, int const copy_contents=1, hwMatrix44 matrix=hwMatrix44(1.0), hwString const & name="")
		"""
		pass

	def ME_ModuleOccurrenceConvert(self,part_entity: Entity, type: hwString , reserved: hwString ):
		pass

	def ME_ModuleOccurrenceCreate(self,*args, **kwargs):
		"""
		ME_ModuleOccurrenceCreate(HMAPI self, hwString const & name, Entity parent_part_entity=hwDescriptor::Entity(), hwString const & structural_type="", hwString const & udm_id="")
		"""
		pass

	def ME_ModuleOccurrenceCreateForInstance(self,*args, **kwargs):
		"""
		ME_ModuleOccurrenceCreateForInstance(HMAPI self, hwString const & new_occ_name, unsigned int parent_id, hwString const & instance_name, hwString const & structural_type="", bool const static_behavior=True)
		"""
		pass

	def ME_ModuleOccurrenceDelete(self,part_entity: Entity):
		pass

	def ME_ModuleOccurrenceInstancesDetach(self,part_list: EntityList, options: hwString ):
		pass

	def ME_ModuleOccurrenceInstancesSyncContents(self,source_part_entity: Entity, target_occurence_list: EntityList, options: hwString ):
		pass

	def ME_ModuleOccurrenceMoveContents(self,source_part_entity: Entity, target_part_entity: Entity, purge_target: int  = 1):
		pass

	def ME_ModuleOccurrencePurge(self,*args, **kwargs):
		"""
		ME_ModuleOccurrencePurge(HMAPI self, Entity part_entity, int const recursive=1, int const reset_representation=0, hwString const & udm_id="", _EntityFullTypeList_vector excluded_entity_types=std::vector< hwDescriptor::EntityFullType >())
		"""
		pass

	def ME_ModuleOccurrenceReparent(self,child_part_entity: Entity, parent_part_entity: Entity, options: hwString ):
		pass

	def ME_ModuleOccurrenceRepresentationLoad(self,part_entity: Entity, options: hwString ):
		pass

	def ME_ModuleOccurrenceRepresentationReset2(self,*args, **kwargs):
		"""
		ME_ModuleOccurrenceRepresentationReset2(HMAPI self, Entity part_entity, hwString const & udm_rep_ref_id="")
		"""
		pass

	def ME_ModuleOccurrenceRepresentationSet2(self,part_entity: Entity, key: hwString ):
		pass

	def ME_ModuleOccurrencesCreateByAssemblyMark(self,collection: Collection, options: hwString ):
		pass

	def ME_ModuleOccurrencesCreateByComponentMark(self,component_collection: Collection, options: hwString ):
		pass

	def ME_ModuleOccurrencesDelete(self,occurences: EntityList, options: hwString ):
		pass

	def ME_ModuleOccurrencesDeleteByMark(self,*args, **kwargs):
		"""
		ME_ModuleOccurrencesDeleteByMark(HMAPI self, Collection collection, hwString const & options=s_defaultString)
		"""
		pass

	def ME_ModuleOccurrencesLink(self,main_id: Entity, ids: EntityList, options: hwString ):
		pass

	def ME_ModuleOccurrencesPurge(self,*args, **kwargs):
		"""
		ME_ModuleOccurrencesPurge(HMAPIBase self, EntityList occurences, _EntityFullTypeList_vector excluded_entity_types=std::vector< hwDescriptor::EntityFullType >(), int const reset_representation=0, int const recursive=1)
		"""
		pass

	def ME_ModuleOccurrencesRealize(self,options: hwString ):
		pass

	def ME_ModuleOccurrencesReparent(self,child_entity_list: EntityList, parent_part_entity: Entity, options: hwString ):
		pass

	def ME_ModulePosition(self,part_entity: Entity, position: int =" 0", reserved: int =" 0"):
		pass

	def ME_ModulePrototypeCreate(self,tbd: hwString , name: hwString , options: hwString ):
		pass

	def ME_ModulePrototypeInstanceCreate(self,tbd: hwString , child_proto_name: hwString , name: hwString , r1c1: float, r1c2: float, r1c3: float, r1c4: float, r2c1: float, r2c2: float, r2c3: float, r2c4: float, r3c1: float, r3c2: float, r3c3: float, r3c4: float, r4c1: float, r4c2: float, r4c3: float, r4c4: float, options: hwString ):
		pass

	def ME_ModulePrototypeInstanceCreateByID(self,parent_proto_part_entity: Entity, child_proto_part_entity: Entity, name: hwString , options: hwString ):
		pass

	def ME_ModuleRepresentationAdd2(self,*args, **kwargs):
		"""
		ME_ModuleRepresentationAdd2(HMAPI self, Entity part_entity, hwString const & key, hwString const & type, hwString const & udm_rep_ref_id="")
		"""
		pass

	def ME_ModuleRepresentationAddFile2(self,part_entity: Entity, key: hwString , fileformat: hwString , filename: hwString ):
		pass

	def ME_ModuleRepresentationChangeKey(self,*args, **kwargs):
		"""
		ME_ModuleRepresentationChangeKey(HMAPI self, Entity part_entity, hwString const & key, hwString const & old_key, hwString const & udm_rep_ref_id="")
		"""
		pass

	def ME_ModuleRepresentationDetailAction(self,*args, **kwargs):
		"""
		ME_ModuleRepresentationDetailAction(HMAPI self, Entity part_entity, hwString const & key, hwString const & action, hwString const & metadata_name, hwString const & metadata_value, hwString const & metadata_type, hwString const & type="")
		"""
		pass

	def ME_ModuleRepresentationRemove2(self,part_entity: Entity, key: hwString ):
		pass

	def ME_ModuleRepresentationRemoveFile2(self,part_entity: Entity, key: hwString , filename: hwString ):
		pass

	def ME_ModuleUpdateOnRepresentationLoad(self,tbd: int):
		pass

	def ME_ModulesHierarchyLibrarySync(self,part_entity: Entity, options: hwString ):
		pass

	def ME_ModulesMoveContents(self,*args, **kwargs):
		"""
		ME_ModulesMoveContents(HMAPIBase self, EntityList src_parts, EntityList dst_parts, hwString const & options="")
		"""
		pass

	def ME_SingleEntityParametersChangedEmit(self,tbd: hwString , id: int):
		pass

	def ME_TransformationMatrixSet(self,part_entity: Entity, r1c1: float, r1c2: float, r1c3: float, r1c4: float, r2c1: float, r2c2: float, r2c3: float, r2c4: float, r3c1: float, r3c2: float, r3c3: float, r3c4: float, r4c1: float, r4c2: float, r4c3: float, r4c4: float, is_relative: int):
		pass

	def MethodUserInputUpdate(self,entityid: var0):
		pass

	def ModifySectionHandle(self,xold_coord: Entity, yold_coord: float, zold_coord: float, xnew_coord: float):
		pass

	def PenetrationCheckSummary(self,filename: hwString , sort_intersections: int, sort_penetrations: int):
		pass

	def RemoveToolMotion(self,part: hwString ):
		pass

	def Replace(self,newEntity: Entity, oldEntity: Entity):
		pass

	def Save(self,*args):
		pass

	def SetupToolMotion(self,part: hwString , velocity: float, travel: float, startingTime: float, risingTime: float, fallingTime: float, direction: int, setupOption: int, curveOption: int):
		pass

	def UpdateBinderSections(self,collection_1: Collection, collection_2: Collection, collection_3: Collection, collection_4: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, rotate_flag: int, blend_flag: int, method_flag: int, sym_flag: int, con_flag: int, type_fit: int =" 0"):
		pass

	def UpdateBinderSectionsLinesToLines(self,type_fit: int):
		pass

	def UpdateLatitudeLineDrag(self,int_type: int):
		pass

	def WriteBlankShapeToHyperNest(self,collection: Collection, resfile: hwString , state: hwString , outfile: hwString , flag: int =" 0"):
		pass

	def WriteMainConnectionSetupFile(self,ce_collection: CollectionSet, options: hwStringList):
		pass

	def WriteNXYDataToHyperNest(self,collection: Collection, resfile: hwString , state: hwString , outfile: hwString , flag: int =" 0"):
		pass

	def absoluterotatedummyjoint(self,collectorentity: Entity, xRot: float, yRot: float, zRot: float, arentChild: int):
		pass

	def absorbbeamsections(self,*args, **kwargs):
		"""
		absorbbeamsections(HMAPIBase self, Entity entity=hwDescriptor::Entity(), Collection collection=hwDescriptor::Collection(), int const deleteunused=1, int const option=0, double const tolerance=0.01)
		"""
		pass

	def absorbentities(self,collection: Collection, value_rule: var0, tolerance: float, location_unit_rule: var0, topology_rule: var0, face_angle: float =" 30_module.0", edge_angle: float =" 180_module.0", preserve_flag: var0 = 1, max_cluster_count: var0 = 4):
		pass

	def absorbloads(self,collection: Collection, disable_value_comparison: var0, renumber_flag: var0, compression_status: var0):
		pass

	def absorbmember(self,*args, **kwargs):
		"""
		absorbmember(HMAPI self, Collection collection=hwDescriptor::Collection(), double const break_angle=1.000000, int const create_legs=0, hwString const & prefix="")
		"""
		pass

	def absorbrigidbodiesfromproperties(self):
		pass

	def accepteditedsurface_with_user_tolerance(self,auto_stitch: int, tolerance: float):
		pass

	def acm_create_mpc(self,main_collection: Collection, secondary_collection: Collection, interface_collection: Collection, tolerance: float, behavior: float):
		pass

	def acousticmeshcreate(self,fixed_nodes_collection: Collection, mesh_type: int, max_structural_cavities: int, min_jacobian: float, min_tet_collapse: float, create_comp_collection: Collection, create_cavity_faces: int, reserved1: int, reserved2: float):
		pass

	def acousticmeshend(self):
		pass

	def acousticmeshinit(self,structural_collection: Collection, seats_collection: Collection, cell_size: float, seat_coupling: int, topo_patch_size: float, semantic_patch_size: float, create_hole_elements: int, flag: int, reserved: float):
		pass

	def acousticmeshinterface(self,collection: Collection, wetted_node_output_collection: Collection, interface_node_output_collection: Collection, wetted_element_output_collection: Collection, interface_element_output_collection: Collection, wetted_component_output_collection: Collection, acmodl_normal: float, acmodl_intol: float, acmodl_dskneps: float, reserved1: int, reserved2: float):
		pass

	def acousticmeshinterface_2(self,collection_cavity: Collection, collection_structural: Collection, wetted_node_output_collection: Collection, interface_node_output_collection: Collection, wetted_element_output_collection: Collection, interface_element_output_collection: Collection, wetted_component_output_collection: Collection, acmodl_normal: float, acmodl_intol: float, acmodl_dskneps: float, reserved1: int, reserved2: float):
		pass

	def activatetransformations(self,collection: Collection, flag: int):
		pass

	def adaptive_triangle_mesh(self,collection: Collection, options: hwString , graphicsDB: int =" 0"):
		pass

	def adaptive_wrapper_build(self):
		pass

	def adaptive_wrapper_end(self):
		pass

	def adaptive_wrapper_init(self,collection: Collection, clean_intersection: int, wrap_type: int):
		pass

	def adaptive_wrapper_leak_check(self,elem_collection: Collection, node_collection: Collection, min_size: float):
		pass

	def adaptive_wrapper_leak_check_mc(self,mc_collection: Collection, collection: Collection):
		pass

	def adaptive_wrapper_mesh(self,*args, **kwargs):
		"""
		adaptive_wrapper_mesh(HMAPI self, int mesh_type, int const OrganizeWrapElemsByBaseComps=0, int const DoRemesh=0, double const RemeshGrowthRate=0.000000, int const IncludeVolumeForLargestCavityIndex=0, Collection IncludeVolumeSeedNodeCollection=hwDescriptor::Collection(), Collection ExcludeVolumeSeedNodeCollection=hwDescriptor::Collection(), Collection ConsiderCavityByCompsCollection=hwDescriptor::Collection(), int const MaxSmoothIterations=0, int const ConformalMesh=0, int const SplitAtFeatures=0, double const SpanAngle=0.000000, hwString const & AcousticResponceNodes="", unsigned int const AcousticMeshType=1, double const AcousticMeshQualityTetCollapse=0.000000, double const AcousticMeshQualityHexJacobian=0.000000)
		"""
		pass

	def adaptive_wrapper_mesh_mc(self,mc_collection: Collection, collection: Collection):
		pass

	def adaptive_wrapper_mesh_reject(self):
		pass

	def adaptive_wrapper_preview(self,num_cavities: int):
		pass

	def adaptive_wrapper_preview_clear(self):
		pass

	def adaptive_wrapper_preview_reject(self):
		pass

	def adaptive_wrapper_proximity_params(self_proximity_for_all: int, prox_lower_bound: float, string_array: hwStringList):
		pass

	def adaptive_wrapper_reject_clear(self):
		pass

	def adaptive_wrapper_set_features(self,feature_type: int, collection: Collection, feature_angle: float, clean_features: int, cleanup_tol: float):
		pass

	def adaptive_wrapper_set_params(self,max_elem_size: float, min_elem_size: float, string_array: hwStringList):
		pass

	def add_multi_washer_elements(self,node_collection: Collection, feature_angle: float, string_array: hwStringList, periphery_node_collection: Collection, background_elem_collection: Collection, rigid_spider: int, local_cordinate_system: int):
		pass

	def add_remove_distance_manipulator(self,mode: int, point_entity1: Entity, point_entity2: Entity, lock_turnover: int, reserved: int):
		pass

	def add_rib(self,plane_normal: hwTriple, plane_base: hwTriple, surface_entity1: Entity, surface_entity2: Entity, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, width: float, draft_angle: float, plane_position: var0, options: var0):
		pass

	def addedgesorfaces(self,*args, **kwargs):
		"""
		addedgesorfaces(HMAPI self, Entity entity, Collection collection=hwDescriptor::Collection(), EntityList list=s_defaultEntityList, hwIntListList face_indices=hwIntListList(), hwIntListList edge_indices=hwIntListList(), unsigned int const reversenormal=0, unsigned int const main=1)
		"""
		pass

	def addfacestocontactsurf(self,name: hwString , elem_collection: Collection, node_collection: Collection, break_angle: float, reverse_normals: int, face_or_edge: int):
		pass

	def addfacestocontactsurfusingfacenumber(self,name: hwString , collection: Collection, face_number: int, reverse_normals: int, element_id: int, use_element_id: int):
		pass

	def addicconnectivity(self,entity: Entity, inode_entity: Entity, dependency_array: hwIntList2 ):
		pass

	def addincludetodisplay(self,id: var0, shortname: hwString ):
		pass

	def addposition(self,collection1: Collection, collection2: Collection):
		pass

	def addshellstocontactsurf(self,name: hwString , elemcollection: Collection, reversenormals: int):
		pass

	def addtransformation(self,collection1: Collection, collection2: Collection):
		pass

	def adjustcontactsurfacenormal(self,name: hwString , collection: Collection, elem_flag: int, orientation_element: var0, reverse_normal: int):
		pass

	def adjustgroupsnormal(self,name: hwString , main_flag: int, collection: Collection, elem_flag: int, orientation_element: var0, reverse_normal: int):
		pass

	def adjustnodes(self,collection: Collection, reduction: float, scale: float, segment: int, magnitude_mode: int):
		pass

	def admasconnectivityupdatemultentselectwithvisnod(self,mass_elem_entity: Entity, collection: Collection, additional_node_collection: Collection, vis_node_entity: Entity):
		pass

	def admasconnectivityupdatesingentselect(self,admaselemptr: Entity, grnodEntityType: EntityFullType, grnodId: int, addnodlistcollection: Collection):
		pass

	def admascreatemultentselectwithsets(self,collection: Collection, additional_node_collection: Collection, vis_node_entity: Entity, type: int, magnitude: float, attach_sets_flag: int):
		pass

	def admascreatesingentselect(self,grnodEntityType: EntityFullType, grnodId: int, addnodlistcollection: Collection, visnodptr: Entity, admasType: int, admasMag: float):
		pass

	def admasvisualizationnodeupdate(self,admaselemptr: Entity, visnodptr: Entity):
		pass

	def aggressive_tria_reduction(self,collection: Collection, qi_smooth: int, feature_angle: float, criteria_file_name: hwString , keep_surf_edges: int, qi_target: float):
		pass

	def alignnode(self,end_node1: Entity, end_node2: Entity, node: Entity):
		pass

	def alignnode2(self,end_node1: Entity, end_node2: Entity, node: Entity, ratio: float):
		pass

	def alignnode3(self,end_node1: Entity, end_node2: Entity, collection: Collection):
		pass

	def aligntoedges(self,line_collection: Collection, node_collection: Collection, FailureCountTolerance: float  =" 0_module.1", FailureIndexTolerance: float  =" 0_module.05", GlobalFailureCountTolerance: float  =" 0_module.1", GlobalFailureIndexTolerance: float  =" 0_module.05", OrientationMismatchPenalty: float  =" 0_module.0", LengthDistortionPenalty: float  =" 0_module.0", EdgeDeviationPenalty: float  =" 0_module.0", WigglePenalty: float  =" 0_module.0", NumIterations: float  =" 0_module.0"):
		pass

	def allsuppressactive(self,state: int):
		pass

	def allsuppressoutput(self,state: int):
		pass

	def alternatefejointcreate(self,type: int, node1: Entity, node2: Entity, system1: Entity, system2: Entity):
		pass

	def alternatefejointupdate(self,collection: Collection, type: var0, node1: Entity, node2: Entity, system1: Entity, system2: Entity, type_flag: int, node_flag: int, system1_flag: int, system2_flag: int):
		pass

	def alternatejointcreate(self,*args, **kwargs):
		"""
		alternatejointcreate(HMAPIBase self, int type, Entity n1, Entity n2, double orient1_x, double orient1_y, double orient1_z, double orient2_x, double orient2_y, double orient2_z, Entity orient1_node=hwDescriptor::Entity(), Entity orient2_node=hwDescriptor::Entity(), Entity set1=hwDescriptor::Entity(), Entity set2=hwDescriptor::Entity())
		"""
		pass

	def alternatejointupdate(self,collection: Collection, type: var0, n1: Entity, n2: Entity, orient1_node: Entity, orient2_node: Entity, orient1_x: float, orient1_y: float, orient1_z: float, orient2_x: float, orient2_y: float, orient2_z: float, set1: Entity, set2: Entity, typeflag: int, nodeflag: int, orient1flag: int, orient2flag: int, setflag: int):
		pass

	def altgapelement(self,node1: Entity, node2: Entity, propertyname: hwString , vector: Entity, orientnode: Entity, x1: float, x2: float, x3: float, coords: int, orientsys: Entity):
		pass

	def altgapelementupdate(self,collection: Collection, propertyname: hwString , vector: Entity, orientnode: Entity, x1: float, x2: float, x3: float, coords: int, orientsys: Entity, useprop: int, useorient: int):
		pass

	def altjointcreate(self,type: var0, n1: Entity, n2: Entity, orient1_node: Entity, orient2_node: Entity, orient1_x: float, orient1_y: float, orient1_z: float, orient2_x: float, orient2_y: float, orient2_z: float):
		pass

	def altjointupdate(self,collection: Collection, type: var0, n1: Entity, n2: Entity, orient1_node: Entity, orient2_node: Entity, orient1_x: float, orient1_y: float, orient1_z: float, orient2_x: float, orient2_y: float, orient2_z: float, typeflag: int, nodeflag: int, orient1flag: int, orient2flag: int):
		pass

	def ameshclearsurface(self):
		pass

	def analysiscurve_setsimulationrange(self,lbound: int, ubound: int):
		pass

	def analysiscurvecreate(self,collection: Collection, x_data_type: hwString , y_data_type: hwString , x_component: hwString , y_component: hwString ):
		pass

	def analysiscurvecreatecomplex(self,collection: Collection, x_data_type: hwString , y_data_type: hwString , x_component: hwString , y_component: hwString ):
		pass

	def analysisfileset(self,filename: hwString ):
		pass

	def analysisfilesetwithsolverids(self,filename: hwString ):
		pass

	def animatelegendsetrange(self,mindef: int, minimum: float, maxdef: int, maximum: float):
		pass

	def animation(self):
		pass

	def animationframenext(self):
		pass

	def animationframeprevious(self):
		pass

	def animationstart(self):
		pass

	def animationstop(self):
		pass

	def appendmarkelemsfromhcpool(self,collection: Collection, poolString: hwString , hcElementIdStart: int, hcElementIdEnd: int, uncollection: int, flag: int):
		pass

	def applydisplayattributes(self,style: int, colortype: int):
		pass

	def applyresults(self,collection: Collection, scale: float, component: hwString ):
		pass

	def applyresultsasloads(self,collection: Collection, multiplier: float, datatype: hwString , loadtype: hwString , loadcomp: hwString ):
		pass

	def applyscenario(self,scenario_name: hwString , entity_type: hwString , overwrite_attrib: int , realize: int ):
		pass

	def assemblyaddmark(self,assemblyptr: Entity, type: Collection):
		pass

	def assemblymodify(self,assemblyname: hwString , collection_set: CollectionSet, color: int):
		pass

	def assemblymodifyhierarchy(self,assemblyname: hwString , collection_set: CollectionSet, color: int):
		pass

	def assemblyremovemark(self,assemblycollection: Collection, entitycollection: Collection):
		pass

	def assigncardimagetosetswithnocardimage(self):
		pass

	def assignedplot(self,title: hwString , legend_min: int, legend_min_value: float, legend_max: int, legend_max_value: float, mesh_color: int, scale_factor: float, full_size: int, reserved: int, vector_comp: hwString , mult: float, min_max_titles: int, plot_info_title: int):
		pass

	def assignidpooltocweldelements(self):
		pass

	def assignsystem(self,collection: Collection, system_entity: Entity, axis: int, only_orient: int, normal_size: float, color: int):
		pass

	def assignsystem_fromcurves(self,collection: Collection, geom_collection: Collection, size: float, color: int, only_orient: var0, rebar: var0 =" 0", table_id: int =" 0", reverse_flag: var0 =" 0"):
		pass

	def assignsystem_option(self,collection: Collection, system_entity: Entity, axis: int, only_orient: int, normal_size: float, color: int, option: int):
		pass

	def associate_nodes_to_geom(self,*args, **kwargs):
		"""
		associate_nodes_to_geom(HMAPI self, Collection mesh_entity_collection, int const manual_association, double const assoc_tol, double const snap_tol, int const snap_nodes, int const override_assoc, EntityFullType geom_entity=hwDescriptor::EntityFullType((unsigned int)0))
		"""
		pass

	def attributedelete(self,entity: Entity, attribute_name_or_id: hwString , solver: int):
		pass

	def attributescopybymark(self,collection: Collection, sameasptr: Entity):
		pass

	def attributeupdate_entityidarray2d(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, target_entity: EntityList2):
		pass

	def attributeupdate_entityidarray2d_mark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, target: EntityList2):
		pass

	def attributeupdatecoupledouble(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, value1: float, value2: float):
		pass

	def attributeupdatecoupledoublearray(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def attributeupdatecoupledoublearraymark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def attributeupdatecoupledoublemark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, value1: float, value2: float):
		pass

	def attributeupdatecoupleint(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, value1: int, value2: int):
		pass

	def attributeupdatecoupleintmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, value1: int, value2: int):
		pass

	def attributeupdatedouble(self,entities: EntityFullType, type: var0, id: int, identifier: int, solver: int, status: int, behavior: float):
		pass

	def attributeupdatedoublearray(self,entities: EntityFullType, type: var0, id: int, identifier: int, solver: int, status: int, behavior: hwDoubleList):
		pass

	def attributeupdatedoublearray2d(self,entities: EntityFullType, type: var0, id: int, identifier: int, solver: int, status: int, behavior: hwDoubleList2 ):
		pass

	def attributeupdatedoublearray2delementmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, row: int, col: int, value: float):
		pass

	def attributeupdatedoublearray2dmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: hwDoubleList2 ):
		pass

	def attributeupdatedoublearrayelementmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, index: int, value: float):
		pass

	def attributeupdatedoublearraymark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def attributeupdatedoublemark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, value: float):
		pass

	def attributeupdateentity(self,entities: EntityFullType, type: var0, id: int, identifier: int, solver: int, status: int, targetentity: Entity):
		pass

	def attributeupdateentityidarray(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, targetentity: EntityFullType, data: hwUIntList):
		pass

	def attributeupdateentityidarray2delementmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, target_entity: EntityFullType, row: int, col: int, value: var0):
		pass

	def attributeupdateentityidarrayelementmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, target_entity: EntityFullType, index: int, value: var0):
		pass

	def attributeupdateentityidarraymark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: EntityList):
		pass

	def attributeupdateentitymark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, targetentityentity: Entity):
		pass

	def attributeupdateint(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, value: int):
		pass

	def attributeupdateintarray(self,entity: Entity, dentifier: int, solver: int, status: int, behavior: int, data: hwIntList):
		pass

	def attributeupdateintarray2d(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, data: hwIntList2 ):
		pass

	def attributeupdateintarray2delementmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, row: int, col: int, value: int):
		pass

	def attributeupdateintarray2dmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: hwIntList2 ):
		pass

	def attributeupdateintarrayelementmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, index: int, value: int):
		pass

	def attributeupdateintarraymark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: hwIntList):
		pass

	def attributeupdateintmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, value: int):
		pass

	def attributeupdatesolverid(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, solver_id: var0, pool_id: int):
		pass

	def attributeupdatestring(self,entities: EntityFullType, type: var0, id: int, identifier: int, solver: int, status: int, behavior: hwString ):
		pass

	def attributeupdatestringarray(self,entities: EntityFullType, type: var0, id: int, identifier: int, solver: int, status: int, behavior: hwStringList):
		pass

	def attributeupdatestringarrayelementmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, index: int, value: hwString ):
		pass

	def attributeupdatestringarraymark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: hwStringList):
		pass

	def attributeupdatestringmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, value: hwString ):
		pass

	def attributeupdatetripledouble(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, value1: float, value2: float, value3: float):
		pass

	def attributeupdatetripledoublearray(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def attributeupdatetripledoublearraymark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def attributeupdatetripledoublemark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, value1: float, value2: float, value3: float):
		pass

	def attributeupdatetripleint(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, value1: int, value2: int, value3: int):
		pass

	def attributeupdatetripleintmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, value1: int, value2: int, value3: int):
		pass

	def attributeupdateunsignedchar(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, val: var1):
		pass

	def attributeupdateunsignedcharmark(self,collection: Collection, identifier: int, solver: int, status: int, behavior: int, val: var1):
		pass

	def attributeupdateunsignedint(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, value: var0):
		pass

	def attributeupdateunsignedintarray(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, data: hwUIntList):
		pass

	def attributeupdateunsignedintarray2d(self,entity: Entity, identifier: int, solver: int, status: int, behavior: int, data: hwIntList2 ):
		pass

	def auto_elem_cleanup_new(self,elem_collection: Collection, node_collection: Collection, feature_angle: float, criteria_file: hwString , string_array: hwStringList):
		pass

	def autocolor(self,entity_type: EntityFullType):
		pass

	def autocolorwithmark(self,collection: Collection, option: int =" 0"):
		pass

	def automesh(self,face_index: var0, algorithm: int, elem_type: int):
		pass

	def automesh_mc(self,entity_collection: Collection, mesh_control_collection: Collection, mode: int):
		pass

	def automesh_params(self,*args, **kwargs):
		"""
		automesh_params(HMAPIBase self, int const mapmethod=0, int const smoothmethod=0, int const mindensity=1, double const mindensitycurvratio=0.0, double const mindensitylength=0.0, int const triamapflow=-2, Entity triamapflow_entity=hwDescriptor::Entity())
		"""
		pass

	def autotopocleanup(self,surfcollection: Collection, criteria_filename: hwString , param_filename: hwString ):
		pass

	def autotopocleanup2(self,surface_collection: Collection, criteria_file_name: hwString , param_file_name: hwString , do_midmesh: int  =" 0", extract_midsurface: int  =" 0"):
		pass

	def autotopocleanuplimited(self,surface_collection: Collection, elsize: float, min_elsize: float, prox_suppr_thresh: float, sharp_steps_width_suppr_thresh: float, flat_feat_suppr_level: int, adj_surfs_layers: int  = 1):
		pass

	def autoupdate1delems(self,*args, **kwargs):
		"""
		autoupdate1delems(HMAPI self, Collection collection, hwString const & adjustoffset="", int const allshells=0, double const angletol=0.000000, hwString const & offsetends="", hwString const & offsetlateral="", hwString const & offsetnormal="", int const orient=0, double const rotate=0.000000, hwString const & thickness="")
		"""
		pass

	def axisymmetry(self,*args, **kwargs):
		"""
		axisymmetry(HMAPI self, double const axisptx=0.000000, double const axispty=0.000000, double const axisptz=0.000000, double const axisx=0.000000, double const axisy=0.000000, double const axisz=0.000000, int const AxiSymmId=0, int const CrossSectionId=0, int const Delete=0, Collection ImprintGeomCollection=hwDescriptor::Collection(), int const MainCrossSectionId=0, int const MainSurfaceCreate=0, int const MainSurfaceId=0, int const Modify=0, int const NumGeomInstances=0, int const SecondaryImprint=0, Collection UserSurfaceCollection=hwDescriptor::Collection(), Collection VolumeSurfaceCollection=hwDescriptor::Collection())
		"""
		pass

	def bagdeleteall(self,collection: Collection):
		pass

	def bar3element(self,node1: Entity, node2: Entity, node3: Entity, vector: hwTriple, orientation_node: Entity, y_dir: int, pin_flags_a: hwBoolList, pin_flags_b: hwBoolList, property_name: hwString ):
		pass

	def bar3elementcreatewithoffsets(self,node1: Entity, node2: Entity, node3: Entity, vector: hwTriple, orientation_node: Entity, y_dir: int, pin_flags_a: hwBoolList, pin_flags_b: hwBoolList, property_name: hwString , offset_system_a: int, offset_x_a: float, offset: float, y_a: float, offset_z_a: int, offset_system_b: float, offset_x_b: float, offset_y_b: float):
		pass

	def bardirectionupdate(self,collection: Collection, orientation_node: Entity, y_dir: int):
		pass

	def barelement(self,node1: Entity, node2: Entity, vector: hwTriple, orientation_node: Entity, y_dir: int, pin_flags_a: hwBoolList, pin_flags_b: hwBoolList, property_name: hwString ):
		pass

	def barelementcreatewithoffsets(self,node1: Entity, node2: Entity, vector: hwTriple, orientation_node: Entity, y_dir: int, pin_flags_a: hwBoolList, pin_flags_b: hwBoolList, property_name: hwString , offset_system_a: int, offset_x_a: float, offset: float, y_a: float, offset_z_a: int, offset_system_b: float, offset_x_b: float, offset_y_b: float):
		pass

	def barelementorientbysystem(self,collection: Collection, vector: hwTriple, system_id: var0):
		pass

	def barelementrotatebyangle(self,collection: Collection, angle: float):
		pass

	def barelementupdate(self,collection: Collection, update_vector: int, vector: hwTriple, update_pins: int, pin_flags_a: hwBoolList, pin_flags_b: hwBoolList, update_property: int, property_name: hwString ):
		pass

	def barelementupdatelocal(self,collection: Collection, update_vector: int, vector: hwTriple, update_pins: int, pin_flags_a: hwBoolList, pin_flags_b: hwBoolList, update_property: int, property_name: hwString ):
		pass

	def barelementupdatewithoffsets(self,collection: Collection, update_vector: int, vector_option: int, vector: hwTriple, update_pins: int, pin_flags_a: hwBoolList, pin_flags_b: hwBoolList, update_property: int, property_name: hwString , update_orientation: int, orientation_node: int, y_dir: int, update_offset_a: int, offset_system_a: int, offset_x_a: float, offset: float, y_a: float, offset_z_a: int, update_offset_b: int, offset_system_b: float, offset_x_b: float, offset_y_b: float):
		pass

	def baroffset(self,element_entity: Entity, offset_x_a: float, offset_y_a: float, offset_z_a: float, offset_x_b: float, offset_y_b: float, offset_z_b: float):
		pass

	def baroffsetupdate(self,collection: Collection, update_offset_a: int, offset_x_a: float, offset_y_a: float, offset_z_a: float, update_offset_b: int, offset_x_b: float, offset_y_b: float, offset_z_b: float):
		pass

	def baroffsetupdatelocal(self,collection: Collection, update_offset_a: int, offset_x_a: float, offset_y_a: float, offset_z_a: float, update_offset_b: int, offset_x_b: float, offset_y_b: float, offset_z_b: float):
		pass

	def barpinsupdate(self,collection: Collection, update_pinsa: int, pinsa: int, update_pinsb: int, pinsb: int):
		pass

	def batchmesh(self,collection: Collection, criteria_file_name: hwString , batch_params_file_name: hwString ):
		pass

	def batchmesh2(self,*args, **kwargs):
		"""
		batchmesh2(HMAPI self, Collection collection, hwString const & criteria_file, hwString const & param_file, double const elemSize=-1.000000, int const elemType=2, int const elemOrder=-1, double const minElemSize=DBL_MAX, double const maxElemSize=DBL_MAX, double const elemFeatureAngle=25.000000, int const noGeomCleanup=0, int const noNodeMoveAcrossEdges=0, int const noRemoveHoles=0, int const noSeedHoles=0, int const noWasher=0, int const noAdvKeepFeatures=0, hwString const & paramsGenerateMode="", int const batchTempFilesMode=-1, int const saveModel=-1, int const breakConnectivity=0, int const keepPlotElems=1, int const keepPreservedEdges=0)
		"""
		pass

	def batchmesh_mc(self,collection: Collection, entity_collection: Collection, options: int):
		pass

	def batchmesh_steps(self,collection: Collection, criteria_file_name: hwString , batch_params_file_name: hwString , steps: hwIntList):
		pass

	def batchmesh_validate_geom(self,*args, **kwargs):
		"""
		batchmesh_validate_geom(HMAPI self, Collection modelcollection, Collection referencemodelcollection, int checks=15, int detailLevel=0, hwString const & user_filepath=s_defaultString)
		"""
		pass

	def batchmodifynodesandedges(self,workcollection: Collection, keep_structure: int):
		pass

	def batchparams_write(self,filename: hwString ):
		pass

	def batchremeshelems(self,collection: Collection, elemsize: float, elemtype: int, feature_angle: float, tria_seeds: int, max_iters: int):
		pass

	def beam_calculateproperties(self,datacollection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, y_axis: hwTriple, useplane: int, basenode: Entity, order: int, saveelems: int, choice: int, Sh: int, Cnt: int):
		pass

	def beamdiagramfromdisplacement(self,*args, **kwargs):
		"""
		beamdiagramfromdisplacement(HMAPI self, EntityFullType entityType, Collection collection, Entity simulation_entity, int const samplingpoints=0, unsigned int const modelsubcase=0, hwString const & skipdeform="", hwString const & tablename="")
		"""
		pass

	def beams_to_surfaces(self,*args, **kwargs):
		"""
		beams_to_surfaces(HMAPI self, Collection collection=hwDescriptor::Collection(), int const convert1DToSolid=0, bool const domesh=True, bool const meshextension=False, double const meshsize=0.000000, int const meshtype=2, hwString const & referencepoint="shearcenter", hwString const & shellsectiondestination="sortbycurrent", bool const smoothcurves=False, double const stitchtol=0.000000, hwString const & surfacecreationtype="surfacebyguidelines", double const tobeamcomponent=0.000000, double const x_breakangle=0.000000, double const y_breakangle=0.000000)
		"""
		pass

	def beamsectionautoconnectshell(self,beam_section_id: var0, connection_type: int, connection_tolerance: float, connection_thickness: float):
		pass

	def beamsectioncalculateresults(self,collection: Collection):
		pass

	def beamsectioncreateatplane(self,collection: Collection, float_array: hwDoubleList, merge_tol: float, plane_normal: hwTriple, plane_normal_base: hwTriple, vector_id: hwTriple, center_option: int, create_method: int, create_centroid_node: int, create_shear_node: int, beam_type: int, keep_lines: int):
		pass

	def beamsectioncreatefromentities(self,*args, **kwargs):
		"""
		beamsectioncreatefromentities(HMAPI self, Collection collection, int const allowshellparts=1, int const allowsolidparts=1, unsigned int const center=2, hwTriple centerposition=hwTriple(0.000000, 0.000000, 0.000000), unsigned int const config=4, double const contactdistance=0.000000, int const createsketch=0, unsigned int const defaultmaterial=1, double const mergetol=0.000000, hwTriple normal=hwTriple(0.000000, 0.000000, 0.000000), unsigned int const order=1, unsigned int const usermaterial=5, double const vertexangle=60.000000, hwTriple yaxis=hwTriple(0.000000, 0.000000, 0.000000), double const welddistance=0.000000)
		"""
		pass

	def beamsectioncreatefromsectioncut(self,*args, **kwargs):
		"""
		beamsectioncreatefromsectioncut(HMAPI self, Collection collection, int const allowshellparts=1, int const allowsolidparts=1, unsigned int const center=2, hwTriple centerposition=hwTriple(0.000000, 0.000000, 0.000000), unsigned int const config=4, double const contactdistance=0.000000, int const createsketch=0, unsigned int const defaultmaterial=1, double const mergetol=0.000000, hwTriple normal=hwTriple(0.000000, 0.000000, 0.000000), unsigned int const order=1, hwDoubleList planebase=hwDoubleList(), hwDoubleList planenormal=hwDoubleList(), hwDoubleList planesize=hwDoubleList(), unsigned int const usermaterial=5, double const vertexangle=60.000000, hwTriple yaxis=hwTriple(0.000000, 0.000000, 0.000000), double const welddistance=0.000000, double const consolidationtol=0.000000)
		"""
		pass

	def beamsectioncreategeneric(self):
		pass

	def beamsectioncreateshell(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, vector_id: hwTriple, project: int, base_node_entity: Entity, part_generation: int):
		pass

	def beamsectioncreateshelldirect(self,collection: Collection, merge_tol: float, use_normal_vector: int, normal_vector: hwTriple, use_orient_vector: int, orient_vector: hwTriple, center_option: int, x_loc: float, y_loc: float, z_loc: float, part_generation: int, create_centroid_node: int, create_shear_node: int):
		pass

	def beamsectioncreatesolid(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, vector_id: hwTriple, use_plane: int, base_node: Entity, elem_order: int):
		pass

	def beamsectioncreatesoliddirect(self,collection: Collection, merge_tol: float, use_normal_vector: int, normal_vector: hwTriple, use_orient_vector: int, orient_vector: hwTriple, center_option: int, x_loc: float, y_loc: float, z_loc: float, elem_order: int, create_centroid_node: int, create_shear_node: int):
		pass

	def beamsectioncreatesolidfrompoints(self,*args, **kwargs):
		"""
		beamsectioncreatesolidfrompoints(HMAPIBase self, hwDoubleList points, int order, int writetobeamsect, int flag, int choosebase, Entity beam_ptr=hwDescriptor::Entity())
		"""
		pass

	def beamsectioncreatestandardsolver(self,type: int, solver: int, type_name: hwString , orient: int):
		pass

	def beamsectionsetdatageneric(self,float_array: hwDoubleList, string_array: hwStringList, beam_sect_id: var0):
		pass

	def beamsectionsetdataroot(self,beam_sect_id: var0, collector_id: var0, solver: var0, beam_config: int, line_color: var1, fill_color: var1, flags: var1, torsion_factor: float, warping_factor: float, orient_vector1: float, orient_vector2: float, orient_origin1: float, orient_origin2: float):
		pass

	def beamsectionsetdatashell(self,vertex_array: hwDoubleList, connectivity_array: hwIntList, part_name_array: hwStringList, beam_sect_id: var0, part_count: int, vertex_count: int):
		pass

	def beamsectionsetdatasolid(self,point_array: hwDoubleList, elem_order: int, is_hollow: int, beam_sect_id: var0):
		pass

	def beamsectionsetdatasolidelems(self,vertices_float_array: hwDoubleList, elemverts_int_array: hwIntList, beam_sect_id: var0):
		pass

	def beamsectionsetdatastandard(self,parameter_array: hwDoubleList, beam_sect_id: var0, beam_sect_type: int, orientation_angle: int, beam_sect_subtype: hwString ):
		pass

	def beamsectiontranslate(self,beam_sect_id: var0, translate_option: int, translation_y: float, translation_z: float):
		pass

	def beamsectionupdateshellpartname(self,beam_sect_id: int, part_index: int, new_name: hwString ):
		pass

	def beamxs_calculateproperties(self,datacollection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, y_axis: hwTriple, useplane: int, basenode: Entity, order: int, saveelems: int):
		pass

	def belttensioning(self,seatbelt_entity: Entity, beltEndToPull: hwString , tension: float , friction: float , beltExtension: float , beltCutEnd: hwString ):
		pass

	def binder_auto(self,collection: Collection, node_list: EntityList, domaintype: int, offsetvalue: float, domain: Entity, exact: int):
		pass

	def binder_auto_withouttrim(self,collection: Collection, node_list: EntityList, domaintype: int, offsetvalue: float, exact: int):
		pass

	def blmesh2d_mc(self,collection: Collection):
		pass

	def blmesh_2d(self,*args, **kwargs):
		"""
		blmesh_2d(HMAPI self, Collection base_collection, Collection bl_collection, int num_layers, double first_layer_thickness, double growth_rate, double const element_size=0.000000, hwString const & element_type="")
		"""
		pass

	def blmesh_2d2(self,*args, **kwargs):
		"""
		blmesh_2d2(HMAPI self, Collection base_collection, int num_layers, double first_layer_thickness, double growth_rate, double const element_size=0.000000, hwString const & element_type="", int const BL_reduction=0, hwString const & DefaultBLSelection="With_BL", int const Auto_BL_reduction=0, double const CoreToBLThicknessRatio=0.000000, double const CornerFactor=0.000000, int const ElemsToSurfComp=0)
		"""
		pass

	def blmesh_2d_computeblthickness(self,base_collection: Collection, num_layers: int, first_layer_thickness: float, growth_rate: float, core_to_BL_ratio: float, corner_factor: float):
		pass

	def blmesh_2d_computeblthickness1(self,*args, **kwargs):
		"""
		blmesh_2d_computeblthickness1(HMAPI self, Collection base_collection, int num_layers, double first_layer_thickness, double growth_rate, double core_to_BL_ratio, double corner_factor, hwString const & DefaultBLSelection="")
		"""
		pass

	def blmesh_2d_input_bl(self,fixed_collection: Collection, float_collection: Collection):
		pass

	def blmesh_2d_input_nonbl(self,fixed_collection: Collection, float_collection: Collection, float_mode: int):
		pass

	def blockcontrollines(self,index: int, on: int):
		pass

	def blockcontrolplanes(self,index: int, on: int):
		pass

	def blocknodeupdate(self,name: hwString , function: int, type: int, start: float, end: float, number: int, factor: float):
		pass

	def blocksetcurrent(self,name: hwString ):
		pass

	def blockvisualize(self,name: hwString , iplane: int, jplane: int, kplane: int, icolor: int, jcolor: int, kcolor: int, usewallcolor: int):
		pass

	def blockwallcreate(self,blockname: hwString , wallname: hwString , color: int):
		pass

	def blockwalldelete(self,blockname: hwString , wallname: hwString ):
		pass

	def blockwalleditrange(self,blockname: hwString , wallname: hwString , imin: float, imax: float, jmin: float, jmax: float, kmin: float, kmax: float, _del: int):
		pass

	def blockwallfindintersect(self,blockname: hwString , wallname: hwString , type: Collection):
		pass

	def blockwallremove(self,blockname: hwString , wallname: hwString ):
		pass

	def blockwallreset(self,name: hwString ):
		pass

	def blockwallupdate(self,blockname: hwString , wallname: hwString , color: int):
		pass

	def bm_cleansurfacestopoinfo(self,surfscollection: Collection, cleanflgs: int):
		pass

	def bm_createauxfeaturesurfs(self,surfscollection: Collection, width: float, compname: hwString , compcolor: int):
		pass

	def bm_markpreservedcompsboundary(self,collection: Collection, common_bound: int, free_edges: int):
		pass

	def bm_setnotouchcomps(self,compscollection: Collection, on: int):
		pass

	def body_split_with_lines(self,collection: Collection, linecollection: Collection, options: int):
		pass

	def body_split_with_morphed_lines(self,collection: Collection, list: EntityList, coords: hwDoubleList, target_type: int, options: int):
		pass

	def body_split_with_points(self,collection: Collection, splinepoints: hwDoubleList, options: int):
		pass

	def body_split_with_swept_lines(self,collection: Collection, line_collection: Collection, vector: hwTriple, back_dist: float, options: int):
		pass

	def body_split_with_templine(self,collection: Collection, vector: hwTriple, linepts: hwDoubleList):
		pass

	def body_splitmerge_with_plane(self,collection: Collection, planeptr_normal: hwTriple, planeptr_normal_base: hwTriple):
		pass

	def body_trim_with_templine(self,collection: Collection, vector: hwTriple, coords: hwDoubleList, options: int):
		pass

	def bodycreate(self,name: hwString , collection: CollectionSet, type: var1, color: int, cmsmethod: int, freq_ub: float, nmodes: int):
		pass

	def bodyflexnodesupdate(self,name: hwString , collection: Collection, dof1: int, dof2: int, dof3: int, dof4: int, dof5: int, dof6: int, updateflag: int):
		pass

	def bodymesh(self,surfaceptr: Entity, elementsize: float, forcing: int):
		pass

	def bodyparametersreset(self,name: hwString ):
		pass

	def bodyparametersupdate(self,name: hwString , mass: float, ixx: float, iyy: float, izz: float, ixy: float, ixz: float, iyz: float, systemid: var0, cog_x: float, cog_y: float, cog_z: float):
		pass

	def bodyupdate(self,name: hwString , collection: CollectionSet, type: var1, color: int, cmsmethod: int, freq_ub: float, nmodes: int):
		pass

	def boolean_merge_bodies(self,ent_collection1: Collection, ent_collection2: Collection, bool_opcode: int, options: int):
		pass

	def boolean_merge_solids(self,entitycollectiona: Collection, entitycollectionb: Collection, opcode: int, options: int):
		pass

	def boolean_solids(self,*args, **kwargs):
		"""
		boolean_solids(HMAPI self, Collection SolidMarkA, Collection SolidMarkB=hwDescriptor::Collection(), int const OpCode=14, int const Option=3, double const BooleanTolerance=DBL_MAX)
		"""
		pass

	def buildfetopology(self,filepath: hwString ):
		pass

	def cadwrapper(self,ety: EntityFullType, mask_main: Collection, param_str: hwString , graphicsDB: int =" 0"):
		pass

	def calc_autotipping(self,collection: Collection, vector: hwTriple, plane_normal: hwTriple, plane_normal_base: hwTriple, angle: hwDoubleList, basenode: Entity):
		pass

	def calculateElemDrapingAngles(self,collection: Collection, result_file: hwString , table_name: hwString , fiber_vector: hwTriple, stamping_vector: hwTriple, ply_id: int):
		pass

	def calculateproximityelements(input_collection: Collection, output_collection: Collection, dim_type: int, calc_type: int, self_interference: int, check_method: int, proximity_dist: float, pair_angle: float, threshold_depth: float):
		pass

	def carddelete(self,name: hwString ):
		pass

	def carddisable(self,name: hwString ):
		pass

	def carddisablebyid(self,name: hwString , id: var0):
		pass

	def cardenable(self,name: hwString ):
		pass

	def cardenablebyid(self,name: hwString , id: var0):
		pass

	def cell_splitter(self,collection10: Collection, gr: float, minSize: float, maxSize: float, tetCollapse: float, reMeshing: int, wrapper: int):
		pass

	def cfdoutput(self,*args, **kwargs):
		"""
		cfdoutput(HMAPI self, hwString const & output_file, hwString const & format, hwString const & solver, int use_existing, hwString const & existing_file, hwStringList string_array=s_defaultStringList)
		"""
		pass

	def change_edgedensities(self,collection: Collection, mode: int, density: int, refedge: Entity):
		pass

	def change_edgedensities_advanced(self,edges_collection: Collection, density: int, mode: int  = 1, layers: int  =" 0"):
		pass

	def check_symmetric_mesh(self,source_collection: Collection, target_collection: Collection, param_strs: hwStringList):
		pass

	def check_symmetric_surfaces(self,source_collection: Collection, target_collection: Collection, param_strs: hwStringList):
		pass

	def checkpenetration(collection: Collection, dim_type: int, penetrations: int, self_interference: int, thickness_adjust: int, thickness_param: float, threshold_depth: float, reserved: int):
		pass

	def cleangeometry(self,operation: int):
		pass

	def cleanmember(self,*args, **kwargs):
		"""
		cleanmember(HMAPI self, CollectionSet members=hwDescriptor::CollectionSet(), double const min_length=-1.000000, double const tolerance=-1.000000, double const break_angle=1.000000, bool const merge_members=False, bool const offset_legs=True, bool const allow_member_destruction=True, bool const erase_duplicated_members=False)
		"""
		pass

	def cleanup_unoffsetable_nodes(self,collection: Collection, angle_threshold: float, layers: int, iters: int):
		pass

	def cleanupmodelfile(self,collection_set: CollectionSet, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, operation: hwString ):
		pass

	def clearallidranges(self,id_or_type: hwString , mode: hwString ):
		pass

	def clearallpreservednodes(self):
		pass

	def clearallunresolvedids(self,entity_type: EntityFullType):
		pass

	def clearclipboard(self):
		pass

	def clearentitymanipulators(self):
		pass

	def clearlock(self,entity_type: EntityFullType, dataname: hwString ):
		pass

	def clearlock2(self,pool_entity: Entity, dataname: hwString ):
		pass

	def clearpreservednodes(self,collection: Collection):
		pass

	def clearunresolvedid(self,entity: Entity):
		pass

	def clearunusedunresolvedids(self,entity_type: EntityFullType):
		pass

	def cmdUpdateAnalysisType(self,analysisType1: int, analysisType2: int, analysisType3: int, friction: float, cb_include: hwString , collection1: Collection, collection2: Collection):
		pass

	def coarsen_and_decimate_mesh2(self,comps_collection: Collection, nodes_collection: Collection, failed_comps_collection: Collection, elem_size: float, elem_type: int, feature_angle: float, max_diameter: float, options: int, delete_comp_size: float  =" 0_module.0", max_compsize_factor: float  =" 0_module.0", elsize_autoreduce_factor: float  =" 0_module.0", area_compare_factor: float  =" 1_module.1", area_low_factor: float  =" 0_module.5", feat_angle_area_compare: float  =" 0_module.0", area_low_factor_min: float  =" 0_module.25", delete_isolated_small_parts: float  =" 0_module.0", max_adjust_iters: int  = 4, delete_duplicated: int  =" 0", mesh_by_connected_parts: int  =" 0", delete_smallparts_after_mesh: int  =" 0", delete_small_t_con_shells: int  =" 0", generate_plotel_for_orphan_fixed_nodes: bool  = False, area_compare_factor_max: float  =" 1_module.25", big_part_elems_count: int  = 30, small_feat_angle: float  =" 30_module.0", small_feat_angle_big_parts: float  =" 9_module.0", coarsen_to_different_comp: bool  = False, max_node_count_per_comp: int  =" 0"):
		pass

	def coarsening_mesh(self,comps_collection: Collection, nodes_collection: Collection, failed_comps_collection: Collection, elem_size: float, elem_type: int, feature_angle: float, max_diameter: float, update_rigids: int):
		pass

	def collectionmovetoinclude(self,collection: Collection, file: var0, writeform: var0):
		pass

	def collectormarkmove(self,collection: Collection, move_to_front: int, sort: int):
		pass

	def collisioncheck2_temp(self,collection: Collection, config: int, thickness: float, allowable_depth: float, tolerance: float, pair_angle: float, minimum_penetration_depth: float =" 0_module.0"):
		pass

	def collisioncheck_temp(self,*args, **kwargs):
		"""
		collisioncheck_temp(HMAPI self, Collection collection_int_elems=s_defaultCollection, Collection collection_pene_elems=s_defaultCollection, Collection collection_int_surfs=s_defaultCollection, Collection collection_pene_surfs=s_defaultCollection, Collection collection_pene_nodes=s_defaultCollection, int self_check=0, int reserved1=0, double pair_angle=0.0, int store_segments=1, int mark_adjoining=0, double topo_feature_angle=0.0, int pair_results=0, int flag=0, double arg=0.0)
		"""
		pass

	def collisionfix_temp(self,reserved: int, collection: Collection, smooth: int):
		pass

	def collisionimportresults(self,*args, **kwargs):
		"""
		collisionimportresults(HMAPIBase self, hwString const & solveroutputpath, EntityList entityids=s_defaultEntityList, unsigned int const collisionType=0, double const minpendepth=0.000000, unsigned int const createsets=0)
		"""
		pass

	def collisionimportresults_temp(self,entityType: EntityFullType, id: int, filePath: hwString ):
		pass

	def collisionmanualfix_temp(self,elemcollection: Collection, nodecollection: Collection, distance: float, mode: int, i1: int, i2: int, i3: int):
		pass

	def collisionrecheck_temp(self,entity_type: EntityFullType, collection: Collection):
		pass

	def collisionsetoutdated(self,outdatedcompids: hwIntList):
		pass

	def colormapedit(self,color: int, red: int, green: int, blue: int):
		pass

	def colormark(self,collection: Collection, color: int):
		pass

	def combine_targets_of_many_vertices(self,face: Entity, collection: Collection, mode: int, offsetpoint_x: float, offsetpoint_y: float, offsetpoint_z: float):
		pass

	def combineelements(self,collection: Collection, tolerance: float, angle: float):
		pass

	def combineplotels(self,collection: Collection):
		pass

	def compactsubmodelids(self,submodel_id: hwString , id: var0, entity_type: hwString , pool_id: var0):
		pass

	def complexanimatemodal(self,title: hwString , max_deflection: float, frames: int, display_mode: int):
		pass

	def compute_gap_thickness(self,collection: Collection):
		pass

	def compute_midmesh_thickness(self,*args, **kwargs):
		"""
		compute_midmesh_thickness(HMAPI self, Collection mesh_collection, Collection geom_collection, double const AbsoluteGroupingTolerance=0.000000, int const AppendToTable=0, int const AssignMidIntervalAsThickness=0, hwString const & CardImage="", double const ConnectionInterpolationFactor=0.000000, double const CornerThicknessCorrectionThreshold=1.500000, double const FeatureAngle=30.000000, double const FixedInterval=0.000000, int const GroupThickness=0, double const GroupingTolerance=0.200000, int const HighlightCorrected=0, hwString const & LogFile="", double const MaxInclinationOfMidMeshWithSolid=35.000000, double const MaxRelativeChordalDeviation=0.100000, double const MaxSearchDistance=0.000000, double const MaxThickness=0.000000, double const MaxThicknessGradient=2.000000, double const MinThickness=0.000000, int const NeedOffset=0, hwString const & NewPropertyPrefix="thickness", int const NumDecimals=1, double const RegroupThicknessVariationFactor=0.200000, int const RenameRetainedComponents=0, hwString const & SampleProperty="", int const SkipOutsideMeshFromCorrection=0, double const StartThickness=0.000000, hwString const & ThicknessAssignMethod="Average", hwString const & ThicknessCorrectionMethod="Interpolation", hwString const & ThicknessOutputOption="", int const WriteToInclude=0)
		"""
		pass

	def computeboundarylayerthickness(self,*args, **kwargs):
		"""
		computeboundarylayerthickness(HMAPIBase self, Collection bl_collection, Collection non_bl_collection, double const first_layer_thicknessconst, double number_of_layersconst, double layer_growth_rateconst, double minimum_core_to_boundary_layer_thickness_ratioconst, double corner_thickness_scaling_factorconst, double check_for_closure_flag, hwString const & logfile="")
		"""
		pass

	def computedirectionnode(self,collection: Collection):
		pass

	def configedit(self,collection: Collection, config: hwString ):
		pass

	def connect(self,connection: hw_module.mdi.adaptors.datasource.DataSource):
		pass

	def connect_surfaces_11(self,source_collection: Collection, target_collection: Collection, extend_mode: int, trim_mode: int, distance: float, min_angle_to_target_surf: float, max_angle_edge_to_surf: float, lines_to_extend_over: Collection, guide_mode: int, ignore_guide_edges: Collection, guide_angle: float, advanced_options: int, reserved: int):
		pass

	@property
	def connections(self):
		pass
	@connections.setter
	def connections(self):
		pass

	def connector_realization_validate(self,connectorcollection: Collection, refconnectorcollection: Collection, checks: int, detailLevel: int, param_strs: hwStringList):
		pass

	def contactsurfcreatewithfaces(self,name: hwString , color: int, elem_collection: Collection, node_collection: Collection, break_angle: float, reverse_normals: int, on_face: int):
		pass

	def contactsurfcreatewithfacesusingfacenumber(self,name: hwString , color: int, collection: Collection, face_number: int, reverse_normals: int, element_id: int, use_element_id: int):
		pass

	def contactsurfcreatewithshells(self,name: hwString , color: int, collection: Collection, reverse_normals: int):
		pass

	def contourplot(self,title: hwString , legend_min: int, legend_min_value: float, legend_max: int, legend_max_value: float, mesh_color: int, scale_factor: float, full_size: int, reserved: int, vector_comp: hwString , mult: float, min_max_titles: int, plot_info_title: int):
		pass

	def control_sum_print(self,*args, **kwargs):
		"""
		control_sum_print(HMAPI self, hwString const & file_name="", hwString const & comment="", hwString const & output_format="scientific", hwString const & method="from_surface_geom", int const shift_to_center=1)
		"""
		pass

	def controlvolcreatesameas(self,collection: Collection, name: hwString , sameasname: hwString ):
		pass

	def convertbeamsection(self,collection: Collection, source_solver_id: int, target_solver_id: int):
		pass

	def convertcompoundtononorderedset(self,action: var0):
		pass

	def convertcontactelements(self,srcSolverName: hwString , destSolverName: hwString , srcType: hwString , destType: hwString ):
		pass

	def convertcord3rtocord1r(self):
		pass

	def convertelements(self,source_solver: hwString , destination_solver: hwString , source_element_type: hwString , destination_element_type: hwString ):
		pass

	def convertinclude(self,id: var0, shortname: hwString , flag: var0):
		pass

	def convertlegacyentities(self,source_entity_type: EntityFullType, target_entity_type: EntityFullType):
		pass

	def convertnodalthickness(self,srcSolverName: hwString , destSolverName: hwString ):
		pass

	def convertpressureloads(self,srcSolverName: hwString , destSolverName: hwString , srcLoadType: hwString , destLoadType: hwString ):
		pass

	def convertthermalloads(self,source_solver: hwString , target_solver: hwString , source_card: hwString , target_card: hwString ):
		pass

	def convertthickness(self,collection: Collection, source_solver_id: int, target_solver_id: int):
		pass

	def convertunit(self,source_unit_system: hwString , target_unit_system: hwString ):
		pass

	def convertunit_bycollection(self,collection: Collection, source_unit_system: hwString , target_unit_system: hwString ):
		pass

	def convertunit_bytype(self,entity_type: EntityFullType, source_unit_system: hwString , target_unit_system: hwString ):
		pass

	def convex_hull(self,mesh_mark: Collection):
		pass

	def copy_feature(self,*args, **kwargs):
		"""
		copy_feature(HMAPI self, Collection collection, int const NumCopies=1, int const ToOriginalComponent=1, int const NumLayers=2, hwString const & MappingMethod="auto", int const Rebuild=1, hwIntList StitchBoundary=hwIntList(), hwMatrix44 TransformByMatrix=hwMatrix44(1.0), hwIntList TransformByNodes=hwIntList())
		"""
		pass

	def copymark(self,collection: Collection, name: hwString , disable_fe_geom_duplicate: int, copy_elems_with_surf: int):
		pass

	def copymarkgroup(self,collection: Collection, name: hwString ):
		pass

	def copysegments(self,set_ids: hwIntList, elem_ids: hwIntList, face_indices: hwIntList, to_segment: hwString ):
		pass

	def copytoclipboard(self,*args, **kwargs):
		"""
		copytoclipboard(HMAPI self, CollectionSet collection, hwString const & componentrule="COMP_ONLY", hwString const & holderrule="", hwIntList includefileids=hwIntList(), hwString const & includefilerule="IGNORE", hwString const & referencerule="RESET")
		"""
		pass

	def correct_fillet_mesh(self,collection: Collection, elemsize: float, minsize: float, maxsize: float, splitsize: float, code: int, color: int):
		pass

	def correctalloverflowsubmodelentityids(self,submodel_type: hwString , id: hwString , entity_type: hwStringList, renum_option: hwUIntList, poolid: var0):
		pass

	def correctoverflowsubmodelentityids(self,submodel_type: hwString , id: var0, entity_type: hwString , option: hwString , renum_option: hwString , pool_id: var0):
		pass

	def create(self,cls, uid: str|hwdescriptor_module.uint_ptr|hwdescriptor_module.Uid, connection: str = None, owner: hw_module.mdi.base.MDIObject = None, ownership_attribute: hwdescriptor_module.Identifier = None, **kwargs):
		"""
		Create Metaobject

        Parameters
        ----------
        cls : str
            Is the type of the object being created. Can be passed as str with the meaning of a named EntityFulltype, as an EntityFulltype 
        owner : MDIObject, optional
            The parent object if any (default is None)
        ownership_attribute: Identifier
            Identifier which defines ownership. It's mandatory to proved it if there are different identifiers defining Ownership to same given type (default is None)
        
        Returns
        -------
        MDIObject
            created MDIObject
        
		"""
		pass

	def createCAERO1(self,*args, **kwargs):
		"""
		createCAERO1(HMAPI self, int start_id, int n_span, int n_chord, hwString const & coordinates, int mode=0, int table_id_1=0, int table_id_2=0, int createproperty=1, hwString const & propname=s_defaultString)
		"""
		pass

	def createCAERO2card(self,start_id: int, system_id: int, origin_coordinate: hwString , length: float, n_int: int, n_slend: int, radii: hwString , theta: hwString , axis: int = 1):
		pass

	def createEdgeBH(self,name: hwString , value: float, color: int, n0: Entity, n1: Entity, edgetype: int, friction: float):
		pass

	def createProfileNode(self,x: float, y: float, z: float, parentId: int):
		pass

	def create_batch_file(self,element_size: float =" 0_module.0", element_type: int =" 0", feature_angle: float =" 0_module.0", pinholes_diameter: float =" 0_module.0", layers_around_holes: int =" 0", nodes_around_holes: int =" 0", beads_suppr_height: float =" 0_module.0", max_edge_fillets_radius: float =" 0_module.0"):
		pass

	def create_bead_elements(self,collection: Collection, radius: float, height: float, make_sharp: int, feature_angle: float):
		pass

	def create_lines_by_mesh_plane_intersection(self,collection: Collection, edge_break_angle: float, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float):
		pass

	def create_octree_dual_surface_mesh(self,mesh_collection: Collection, dual_mesh_size: float):
		pass

	def create_parametric_feature(self,surf_collection: Collection, flag1: int, flag2: int):
		pass

	def create_shell_mesh_features(self,collection: Collection, feature_angle: float, reserved: float):
		pass

	def create_solid_from_eight_points(self,Point1: hwTriple, Point2: hwTriple, Point3: hwTriple, Point4: hwTriple, Point5: hwTriple, Point6: hwTriple, Point7: hwTriple, Point8: hwTriple):
		pass

	def create_springs(self,*args, **kwargs):
		"""
		create_springs(HMAPI self, Collection nodesCollection, int const DestinationComp, hwString const & SBushName="", hwString const & SBushPropName="", hwString const & SBushType="", int const ConnectType=0, int const ElemType=0, int const Config=0, double const Tolerance=0.000000, int const PropertyMode=0, int const Property=0, int const SystemMode=0, int const System=0, double const K1=0.000000, double const K2=0.000000, double const K3=0.000000, double const K5=0.000000, double const Pten=0.000000, double const Pshr=0.000000, double const Ppar=0.000000, double const Pprp=0.000000, double const Pm=0.000000, double const FF=0.000000, int const ReverseCoordYFlag=0, int const SwapCoordXFlag=0, int const AxialCompFlag=0)
		"""
		pass

	def create_surf_from_mesh(self,elemcollection: Collection, stype: int, tol: float):
		pass

	def create_thin_solid_midline(self,*args, **kwargs):
		"""
		create_thin_solid_midline(HMAPI self, Collection solid_collection, Collection node_collection=hwDescriptor::Collection(), Collection point_collection=hwDescriptor::Collection(), hwDoubleList plane_by_point_coords=hwDoubleList(), hwDoubleList plane_base=hwDoubleList(), hwDoubleList plane_normal=hwDoubleList(), hwString const & dest_comp="midline")
		"""
		pass

	def create_tube_midline(self,*args, **kwargs):
		"""
		create_tube_midline(HMAPI self, Collection collection, int const copy_metadata=0, hwString const & dest_comp="", Collection tube_ends_collection=hwDescriptor::Collection(), hwString const & dest_part="", hwString const & dest_comp_prefix="Midline_")
		"""
		pass

	def create_voxel_lattice_hex_mesh(self,mesh_collection: Collection, hex_mesh_size: float, num_buffer_layers: int):
		pass

	def create_voxel_lattice_mesh(self,collection_2d: Collection, collection_1d: Collection, origin_x: float, origin_y: float, origin_z: float, voxel_size_x: float, voxel_size_y: float, voxel_size_z: float, mesh_extent_x: int, mesh_extent_y: int, mesh_extent_z: int):
		pass

	def createairbag(self,entities: EntityFullType, markmask: int, name: hwString ):
		pass

	def createandadjustmass(self,*args, **kwargs):
		"""
		createandadjustmass(HMAPI self, Collection components, double const targetmass, double const targetcogx, double const targetcogy, double const targetcogz, Collection outputCollection=s_defaultCollection, double const tolerance=0.000000, bool const usestructuralmass=False, bool const addnumericalmass=False, int const nodalmass=1, int const iterations=1, bool const optimizetargetflag=False)
		"""
		pass

	def createandassignstructuralproperty(self,*args, **kwargs):
		"""
		createandassignstructuralproperty(HMAPI self, int iStructuralElemID, Collection collection, hwString const & data1=s_defaultString, hwString const & data2=s_defaultString, hwString const & data3=s_defaultString, hwString const & data4=s_defaultString)
		"""
		pass

	def createandmanagesetsandcontents(self,*args, **kwargs):
		"""
		createandmanagesetsandcontents(HMAPI self, CollectionSet setCollection, hwString const & file, hwString const & condense="none", bool const create_setsegment_by_topology=False, bool const force_rename=False, int const id=0, bool const keep_unused=False, hwString const & name="", bool const reversenormal=False, double const topology_face_angle=30.000000)
		"""
		pass

	def createautoddp(self,entities: Collection, autoddptype: int  =" 0", groupid: int  =" 0"):
		pass

	def createbatchparamsfromstrings(self,strings: hwStringList):
		pass

	def createbead(self,*args, **kwargs):
		"""
		createbead(HMAPI self, Collection elements=hwDescriptor::Collection(), hwDoubleList centerpoints=hwDoubleList(), Entity centerline=hwDescriptor::Entity(), int const opposite_mesh_normal=0, double const topwidth=0.000000, double const bottomwidth=0.000000, double const height=0.000000, hwString const & captype="", double const caplength=0.000000, double const trapezoidcapendwidth=0.000000, int const num_centerpoints=0, int const count=0, hwString const & centerlinetype="")
		"""
		pass

	def createbeamsectionfromstructuralproperty(self,*args, **kwargs):
		"""
		createbeamsectionfromstructuralproperty(HMAPI self, hwString const & data1=s_defaultString, hwString const & data2=s_defaultString, hwString const & data3=s_defaultString, hwString const & data4=s_defaultString)
		"""
		pass

	def createbestcirclecenternode(self,collection: Collection, point_flag: int, any_tol: int, make_circle: int):
		pass

	def createblankholder(self,name: hwString , bhpressure: float, tonnage: float, friction: float, color: int, collection: Collection):
		pass

	def createboundingboxes(self,compcollection: Collection):
		pass

	def createcaero1panelmeshing(self,*args, **kwargs):
		"""
		createcaero1panelmeshing(HMAPI self, Entity component, hwDoubleList locations, int const tableid1=0, int const tableid2=0, int const span=0, int const chord=0, int const igid=0, int const createproperty=1, int const mode=0, hwString const & panelname="", hwString const & propertyname="", int const systemid=0)
		"""
		pass

	def createcaero2bodymeshing(self,*args, **kwargs):
		"""
		createcaero2bodymeshing(HMAPI self, int const componentid, hwDoubleList halfwidths, int const igid, hwDoubleList interferenceangles, double const length, hwTriple location, int const systemid, hwString const & bodyname="", int const mode=0, int const nint=0, int const nsb=0, int const tableid1=0, int const tableid2=0)
		"""
		pass

	def createcenternode(self,node_entity1: Entity, node_entity2: Entity, node_entity3: Entity):
		pass

	def createcirclecenterpoint(self,point_entity1: Entity, point_entity2: Entity, point_entity3: Entity):
		pass

	def createcirclefromcenterradius(self,list: EntityList, vector: hwTriple, radius: float, angle: float, offset: float):
		pass

	def createcirclefrompointplane(self,list: EntityList, plane_normal: hwTriple, plane_normal_base: hwTriple, angle: float, offset: float):
		pass

	def createcirclefrompoints(self,list: EntityList, circle_flag: int):
		pass

	def createcollectorforpartiallycontained(self,collection: Collection, name: hwString , config: int =" 0", type: int =" 0", reserved: int =" 0"):
		pass

	def createconnectionelements(self,*args, **kwargs):
		"""
		createconnectionelements(HMAPIBase self, hwString const & elem_type, Collection nodes, double const tolerance, Collection collection=hwDescriptor::Collection())
		"""
		pass

	def createcontrolvol(self,collection: Collection, name: hwString ):
		pass

	def createcrbrelation(self,main_component_id: var0, secondary_component_id: var0):
		pass

	def createdoubler(self,*args, **kwargs):
		"""
		createdoubler(HMAPI self, Collection elements, Collection domElements, hwTriple normal, hwTriple plane_point, double const length, double const mesh_elem_size, double const offset, double const thickness, double const flange_width, Entity material=hwDescriptor::Entity(), Entity connectorControl=hwDescriptor::Entity(), bool const realizeconnectors=True, hwIntList seperation_edges=hwIntList())
		"""
		pass

	def createdrawbead(self,drawbeadname: hwString , list: EntityList, color: int, db_force: float, lockbead: int):
		pass

	def createdummytargetpoints(self,*args, **kwargs):
		"""
		createdummytargetpoints(HMAPI self, hwIntList outputblockids=hwIntList(), hwString const & nodenamepattern="", hwIntList nodeids=hwIntList(), hwString const & designpointnameprefix="Dummy_Point")
		"""
		pass

	def createdummytargetpointsfromcsv(self,*args, **kwargs):
		"""
		createdummytargetpointsfromcsv(HMAPI self, hwString const & filename, hwString const & skiplines="")
		"""
		pass

	def createdynamicdataname(self,*args, **kwargs):
		"""
		createdynamicdataname(HMAPI self, Collection collection, hwString const & dataname, int const basictype=0, hwString const & displayname="", hwString const & defaultvalue="", bool const visible=True, bool const editable=True)
		"""
		pass

	def createelement(self,config: int, type: int, list: EntityList, auto_order: int):
		pass

	def createelements(self,config: int, type: int, integer_array: hwIntList):
		pass

	def createelementsbetweennodes(self,surf1_collection: Collection, surf2_collection: Collection, collection: Collection, tol: float, createplot: int, configval: int, syst: int, code: int, property: hwString ):
		pass

	def createelementsbetweenpoints(self,surf1_collection: Collection, surf2_collection: Collection, collection: Collection, tol: float, createplot: int, configval: int, syst: int, code: int, property: hwString ):
		pass

	def createentitiesfromsource(self,entitytype: EntityFullType, source: hwString ):
		pass

	def createentitysameas(self,*args, **kwargs):
		"""
		createentitysameas(HMAPIBase self, Entity entities, hwString const & entityname="yes")
		"""
		pass

	def createexoskeletonlattice(self,*args, **kwargs):
		"""
		createexoskeletonlattice(HMAPI self, Collection entities, Collection nodes, double const exoskeletonsize, double const radius=0.000000, double const minelemsize=0.000000, double const tol=0.000000, unsigned int const matid=0, unsigned int const symmetryid=0, hwString const & desvaropt="size", hwString const & designopt="tight", hwString const & filepath="")
		"""
		pass

	def createfacesonfreeboundaries(self):
		pass

	def createfbddisplacementtable(self,*args, **kwargs):
		"""
		createfbddisplacementtable(HMAPIBase self, EntityList set_ids, hwTripleIList subcase_ids, int const freenode, Entity result_entity, unsigned int const displacement=0, unsigned int const resolvein_sys=0, unsigned int const rotation=0, double const tolerance=0.00001, Entity user_system=hwDescriptor::Entity())
		"""
		pass

	def createfbdfilefromfbdsummarytable(self,filepath: hwString , summPt_systemId: Entity, summaryTable_name: hwString ):
		pass

	def createfbdgroupfortraceplot(self,*args, **kwargs):
		"""
		createfbdgroupfortraceplot(HMAPIBase self, hwString const & name, EntityList node_ids, EntityFullType entType, int num_cuts, int path_dir, hwTriple userDir=hwTriple(0.000000, 0.000000, 0.000000), hwString const & sys_def="", Entity system=Entity(), hwTriple sys_ref_dir=hwTriple(0.000000, 0.000000, 0.000000))
		"""
		pass

	def createfbdreport(self,report_type: hwString , collection: Collection, subcase_ids: hwTripleIList, resultid: Entity, envelope: int  =" 0", gpf: int  =" 0", tolerance: float  = 1e-05):
		pass

	def createfbdsummarytable(self,*args, **kwargs):
		"""
		createfbdsummarytable(HMAPIBase self, EntityList freebodysection_ids, hwTripleIList subcase_ids, double const arrLen=25.000000, int const arrowOrigin=0, unsigned int const colorfx=3, unsigned int const colorfy=4, unsigned int const colorfz=5, unsigned int const colorfxy=1, unsigned int const colorfyz=2, unsigned int const colorfxz=7, unsigned int const colorfxyz=6, unsigned int const colormx=3, unsigned int const colormy=4, unsigned int const colormz=5, unsigned int const colormxy=1, unsigned int const colormyz=2, unsigned int const colormxz=7, unsigned int const colormxyz=6, int const createField=1, int const createLoad=1, int const decLim=2, int const display=1, int const displacement=0, int const freenode=2, int const fx=0, int const fxy=0, int const fxyz=0, int const fxz=0, int const fy=0, int const fyz=0, int const fz=0, int const mx=0, int const mxy=0, int const mxyz=0, int const mxz=0, int const my=0, int const myz=0, int const mz=0, int const resFileID=INT_MAX, int const resolveInSys=0, Entity resultID=hwDescriptor::Entity(), int const rotation=0, int const scID=0, int const scientific=0, int const showValue=0, int const sizeScale=0, int const stepID=0, double const tolerance=0.001000, Entity userSysID=hwDescriptor::Entity(), int const vecStyle=0, int const gpf=0, int const intf=0, int const mpcf=0, int const sumAt=0, int const sysProj=0, int const spcf=0, int const appf=0, int const absolute=0, int const color=0, int const createTable=0, int const displayAt=0, int const envelope=0, hwString const & fieldName="", int const interpolate=0, double const maxVal=0.000000, int const midArrow=0, int const minMax=0, int const normalLoad=0, int const oneLems=0, int const onNodes=0, int const plotDir=0, int const range=0, hwString const & reportTablename="", int const resultant=0, int const summf=0, int const tangentialLoad=0)
		"""
		pass

	def createfillet(self,line1_entity: Entity, line2_entity: Entity, radius: float, trim: int, quadselected: int):
		pass

	def createfilletmidlines(self,collection: Collection, max_radius: float, min_radius: float, max_width: float, min_width: float, suppress_rib: int):
		pass

	def createflattenfold(self,*args, **kwargs):
		"""
		createflattenfold(HMAPI self, Collection airbag_collection, hwString const & exportdir="")
		"""
		pass

	def createfldplot(self,name: hwString ):
		pass

	def createfldplots(self,collection: Collection):
		pass

	def createfmvss201u(self,*args, **kwargs):
		"""
		createfmvss201u(HMAPI self, int const side, int const vehicledir, hwIntList exteriorpartsids, hwIntList interiorpartsids, hwIntList windshieldpartsids, hwTriple sgrp, hwTriple sgrprear, double const seattraveldist=127.000000, double const wsoffset=0.000000, double const weatherstrippingoffset=0.000000, int const method=0, hwIntList apillarpartsids=hwIntList(), hwIntList bpillarpartsids=hwIntList(), hwIntList opillarpartsids=hwIntList(), hwIntList rpillarpartsids=hwIntList(), hwIntList interiorroofpartsids=hwIntList(), Entity ippointid=hwDescriptor::Entity(), Entity bp2pointid=hwDescriptor::Entity(), Entity bphighestpointid=hwDescriptor::Entity(), Entity bplowestpointid=hwDescriptor::Entity(), Entity bpn1pointid=hwDescriptor::Entity(), Entity bpn2pointid=hwDescriptor::Entity(), Entity op1pointid=hwDescriptor::Entity(), Entity ophighestpointid=hwDescriptor::Entity(), Entity oplowestpointid=hwDescriptor::Entity(), Entity opn1pointid=hwDescriptor::Entity(), Entity opn2pointid=hwDescriptor::Entity(), Entity rp2pointid=hwDescriptor::Entity(), Entity sr3pointid=hwDescriptor::Entity(), hwIntList fhsunroofids=hwIntList(), int const apbool=0, int const urbool=0, int const bpbool=0, int const opbool=0, int const rpbool=0, int const rhbool=0, int const fhbool=0, int const srbool=0, int const ap1=0, int const ap2=0, int const ap3=0, int const bp1=0, int const bp2=0, int const bp3=0, int const bp4=0, int const op1=0, int const op2=0, int const opanchorage=0, int const rp1=0, int const rp2=0, int const fh1=0, int const fh2=0, int const rh1=0, int const sr1=0, int const sr2h=0, int const sr2v=0, int const sr3=0)
		"""
		pass

	def createfmvss201u_createpoints(self,*args, **kwargs):
		"""
		createfmvss201u_createpoints(HMAPI self, int const pointtype, hwIntList apillarpartsids=hwIntList(), hwIntList bpillarpartsids=hwIntList(), hwIntList opillarpartsids=hwIntList(), hwIntList rpillarpartsids=hwIntList(), hwIntList interiorroofpartsids=hwIntList(), Entity ippointid=hwDescriptor::Entity(), Entity bp2pointid=hwDescriptor::Entity(), Entity bphighestpointid=hwDescriptor::Entity(), Entity bplowestpointid=hwDescriptor::Entity(), Entity bpn1pointid=hwDescriptor::Entity(), Entity bpn2pointid=hwDescriptor::Entity(), Entity op1pointid=hwDescriptor::Entity(), Entity ophighestpointid=hwDescriptor::Entity(), Entity oplowestpointid=hwDescriptor::Entity(), Entity opn1pointid=hwDescriptor::Entity(), Entity opn2pointid=hwDescriptor::Entity(), Entity rp2pointid=hwDescriptor::Entity(), Entity sr3pointid=hwDescriptor::Entity(), hwIntList fhsunroofids=hwIntList(), int const apbool=0, int const urbool=0, int const bpbool=0, int const opbool=0, int const rpbool=0, int const rhbool=0, int const fhbool=0, int const srbool=0, int const ap1=0, int const ap2=0, int const ap3=0, int const bp1=0, int const bp2=0, int const bp3=0, int const bp4=0, int const op1=0, int const op2=0, int const opanchorage=0, int const rp1=0, int const rp2=0, int const fh1=0, int const fh2=0, int const rh1=0, int const sr1=0, int const sr2h=0, int const sr2v=0, int const sr3=0)
		"""
		pass

	def createfmvss201u_end(self,deleteentities: int  =" 0"):
		pass

	def createfmvss201u_start(self,*args, **kwargs):
		"""
		createfmvss201u_start(HMAPI self, int const vehicledir, int const method, double const seattraveldist=127.000000, double const wsoffset=0.000000, double const weatherstrippingoffset=0.000000, hwIntList exteriorpartsids=hwIntList(), hwIntList interiorpartsids=hwIntList(), hwIntList windshieldpartsids=hwIntList(), hwTriple sgrp=hwTriple(0.000000, 0.000000, 0.000000), hwTriple sgrprear=hwTriple(0.000000, 0.000000, 0.000000), hwString const & testlabcsv="", int const side=0)
		"""
		pass

	def createfoldingtable(self,*args, **kwargs):
		"""
		createfoldingtable(HMAPI self, Collection airbagComponents, Entity originnode, Entity xaxisnode, Entity planenode, Entity fabricnode, double const gap=0.000000, bool const righthanded=False, hwString const & exportdir="")
		"""
		pass

	def createhfmaterial(self,name: hwString , k: float, e: float, epsilon0: float, r: float, n: float, id: int):
		pass

	def createhfsummaryfile(self,filename: hwString , dynafile: hwString ):
		pass

	def createidrange(self,submodel_type: hwString , id: var0, shortname: hwString , entity_type: hwString , min_id: var0, max_id: var0, pool_id: var0, integer_array: hwIntList):
		pass

	def createinclude(self,id: var0, shortname: hwString , fullname: hwString , parentid: var0):
		pass

	def createincludeperpart(self,collection: Collection):
		pass

	def createinflatorinsertfold(self,*args, **kwargs):
		"""
		createinflatorinsertfold(HMAPI self, Collection aribagComponents, Collection inflatorComponents, Collection holesElements, hwTriple translate, double const thickness, hwString const & exportdir="")
		"""
		pass

	def createintersectionsegments(self,collector: int, flag: int =" 0", param: float =" 0_module.0"):
		pass

	def createipimpact(self,*args, **kwargs):
		"""
		createipimpact(HMAPI self, int const regulation, hwIntList instrumentpanelids, hwIntList steeringwheelids, hwIntList windscreenids, hwIntList headerpartsids, hwTriple vehiclefrontaxis, hwTriple leftsrp, hwTriple rightsrp, hwTriple offsetvec=hwTriple(0.000000, 0.000000, 0.000000), double const targetpointsdistance=0.000000, double const armlenstepsize=0.000000, double const lhsarealimit=0.000000, double const rhsarealimit=0.000000, double const armlenmin=0.000000, double const armlength=0.000000, double const armlenmax=0.000000, double const headformdia=0.000000, double const rotationstep=0.000000, int const targetpointsmethod=0, int const ysectionpoints=0, int const driverside=0)
		"""
		pass

	def createjointelement_twonoded(self,type: int, node1: Entity, node2: Entity, orientation: int, o_node1: Entity, o_node2: Entity, o_system1: Entity, o_system2: Entity, property: hwString ):
		pass

	def createmembersectionfrommember(self,*args, **kwargs):
		"""
		createmembersectionfrommember(HMAPI self, Entity member_entity, hwString const & intersectingentitytype="elements", hwString const & planetype="infinite", unsigned int const numcontrollocs=0, hwTriple planenormal=hwTriple(0.000000, 0.000000, 0.000000), double const planelength=300.000000, double const planewidth=300.000000, bool const realize=False, hwString const & sectiontype="real", bool const createsketch=False, bool const autoweld=False, bool const auto_detect_thin_solids=False, bool const alongline=False, double const vertexangle=0.000000)
		"""
		pass

	def createmeshfromrData(self,resultfilepaths: hwString ):
		pass

	def createmultiplespotwelds(self,nodecol1_collection: Collection, nodecol2_collection: Collection, tolerance: float, length_given: int, length: float, systems: int, movenode: int, remesh: int, configval: int, property: hwString ):
		pass

	def createnodesandspotweldelems(self,surf1_collection: Collection, surf2_collection: Collection, tol: float, createplot: int, configval: int, syst: int, code: int, num_nodes: int, entities: EntityFullType, collection: Collection, biasstyle: int, biasingintensity: float, spacing: float, offset_type: int, endoffset: float, property: hwString ):
		pass

	def createnodesbetweennodelist(self,nodelist: EntityList, numberofnodes: int, biasstyle: int, biasingintensity: float):
		pass

	def createnodesbetweennodes(self,node1: Entity, node2: Entity, number: int):
		pass

	def createnodesbetweenpositions(self,x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, count: int, option: int, systemid: Entity):
		pass

	def createorthotropicdirection(self):
		pass

	def createpoint(self,x: float, y: float, z: float, system: Entity):
		pass

	def createpointsbetweenpoints(self,point_entity1: Entity, point_entity2: Entity, count: int):
		pass

	def createpointsbetweenpositions(self,x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, count: int, end_points: int, system_id: Entity):
		pass

	def createpositionformech(self,name: hwString ):
		pass

	def createreferencegeometry(self,collection: Collection, name: hwString ):
		pass

	def createrollfold(self,*args, **kwargs):
		"""
		createrollfold(HMAPI self, Collection airbagComponents, Collection nodesCollection, hwTriple linestart, hwTriple lineend, double const tooldimension=0.000000, int const rotationnums=0, int const tooltype=0, int const bcsmovingside=0, int const bcsfixedside=0, hwString const & exportdir="")
		"""
		pass

	def createsectioncut(self,*args, **kwargs):
		"""
		createsectioncut(HMAPIBase self, hwString const & sectionmethod, int const beamoffset=0, int const createbeamelems=0, int const createbeamsect=0, unsigned int const beamElemsAtPos=1, int const createelemsets=0, int const createsectiondata=0, int const detaileddata=0, unsigned int const elemscomp=0, int const includebeams=1, Collection includeCollection=hwDescriptor::Collection(), int const includerods=1, int const includeshells=1, hwString const & inertiaat="", int const keepintersectlines=0, unsigned int const linescomp=0, int const nodeatcentroid=0, int const nodeatneutralaxis=1, int const numcuts=0, double const offset=0.000000, EntityList ref_list=s_defaultEntityList, hwTriple sectionbase=hwTriple(0.000000, 0.000000, 0.000000), hwTriple sectionnormal=hwTriple(0.000000, 0.000000, 0.000000), int const shelloffset=0, hwTriple verticalaxis=hwTriple(0.000000, 0.000000, 0.000000), int const createelemsat=1)
		"""
		pass

	def createsensor(self,name: hwString ):
		pass

	def createsimexcomponent(self,name: hwString , type_flag: int, material_id: var0, thickness: float, friction: float, id: int, color: int, fld_comp_flag: int, curve_name: hwString , curvebinder: int):
		pass

	def createsimexmaterial(self,name: hwString , k: float, e: float, epsilon0: float, r: float, n: float):
		pass

	def createsimplefold(self,*args, **kwargs):
		"""
		createsimplefold(HMAPI self, Collection airbagComponents, Collection node, hwTriple linestart, hwTriple lineend, double const angle, hwTriple linestart2=hwTriple(0.000000, 0.000000, 0.000000), hwTriple lineend2=hwTriple(0.000000, 0.000000, 0.000000), double const interfriction=0.500000, double const envelopelementsize=0.000000, double const numsideelems=0.000000, double const heightratioenvelopelems=0.000000, bool const createvoidcomp=False, double const heightratiovoidelems=0.000000, hwString const & exportdir="")
		"""
		pass

	def createsinglewallbulkhead(self,*args, **kwargs):
		"""
		createsinglewallbulkhead(HMAPI self, Collection elementsCollection, Collection domElementsCollection, hwTriple normal, hwTriple plane_point, double const flange_width, double const mesh_elem_size, double const thickness, double const offset, bool const realizeconnectors=True, Entity material=hwDescriptor::Entity(), Entity connectorControl=hwDescriptor::Entity())
		"""
		pass

	def createsketchfrombeamsection(self,*args, **kwargs):
		"""
		createsketchfrombeamsection(HMAPI self, Collection beamsections, bool const assignsketch=True, bool const computeproperties=False, hwDoubleList offset=hwDoubleList())
		"""
		pass

	def createsketchfromentities(self,collection: Collection, includeInputForRealize: var0 =" 0"):
		pass

	def createsketchfromline(self,linerecordptr: Entity, includeInputForRealize: var0 =" 0"):
		pass

	def createsolidsfromshells(self,input_collection: Collection, output_collection: Collection, comp_create_option: int =" 0", solid_layers: int =" 0", fill_gaps: int =" 0", delete_shells: int =" 0", property_create: int =" 0", reserved1: var0 =" 0", reserved2: float =" 0_module.0", reserved3: float =" 0_module.0"):
		pass

	def createspotweld(self,independent: Entity, dependent: Entity, length_given: int, length: float, systems: int, movenode: int, remesh: int, configval: int, property: hwString ):
		pass

	def createtemporallock(self,entity: Entity, logic: hwString ):
		pass

	def createtemporallockbymark(self,collection: Collection, logic: hwString ):
		pass

	def createtuckfold(self,*args, **kwargs):
		"""
		createtuckfold(HMAPI self, Collection airbagComponents, Collection nodes, hwTriple linestart, hwTriple lineend, double const zdist=2.000000, hwString const & exportdir="")
		"""
		pass

	def createweldelemsfromalinelist(self,surf1_collection: Collection, surf2_collection: Collection, tol: float, createplot: int, configval: int, syst: int, code: int, num_nodes: int, linelist1: EntityList, nodelist1: EntityList, biasstyle: int, biasingintensity: float, spacing: float, offset_type: int, endoffset: float, property: hwString ):
		pass

	def createweldsbetweencompsusingnodes(self,comp1_collection: Collection, comp2_collection: Collection, single_col: int, node_collection: Collection, tol: float, syst: int, configval: int, property: hwString , remesh: int, forced_length: int, DTfile: hwString ):
		pass

	def createweldsbetweencompsusingpoints(self,comp1_collection: Collection, comp2_collection: Collection, single_col: int, point_collection: Collection, tol: float, syst: int, configval: int, property: hwString , null: int, forced_length: int, DTfile: hwString ):
		pass

	def createweldsbetweenelemsusingnodes(self,elem1_collection: Collection, elem2_collection: Collection, single_col: int, node_collection: Collection, tol: float, syst: int, configval: int, property: hwString , remesh: int):
		pass

	def createweldsbetweenelemsusingpoints(self,elem1_collection: Collection, elem2_collection: Collection, single_col: int, point_collection: Collection, tol: float, syst: int, configval: int, property: hwString , remesh: int):
		pass

	def createzigzagfold(self,*args, **kwargs):
		"""
		createzigzagfold(HMAPI self, Collection airbagComponents, Collection nodes, hwTriple linestart, hwTriple lineend, int const method=1, int const nplies=10, double const distplates=50.000000, double const fixedsidewidth=50.000000, hwString const & exportdir="")
		"""
		pass

	def criteria_write(self,filename: hwString ):
		pass

	def currentcollector(self,entity_type: EntityFullType, name: hwString ):
		pass

	def curveaddpoint(self,curve_id: var0, index: int, xvalue: float, yvalue: float):
		pass

	def curvedeletepoint(self,curve_id: var0, point_number: int):
		pass

	def curvemathexternalfilter(self,outputcurve: hwString , xbased: int, filter: hwString , parameter: hwString ):
		pass

	def curvemodifypointcords(self,curve_id: var0, point_number: int, xstring: hwString , xvalue: float, ystring: hwString , yvalue: float):
		pass

	def cut_hole(self,*args, **kwargs):
		"""
		cut_hole(HMAPI self, Collection base_collection, hwString const & type, int const count, hwDoubleList planenormal, hwDoubleList centerpoints=hwDoubleList(), hwIntList num_centerpoints=hwIntList(), Entity centerlines=hwDescriptor::Entity(), hwDoubleList radius=hwDoubleList(), hwDoubleList radius1=hwDoubleList(), hwDoubleList radius2=hwDoubleList(), int const cappedends=0, hwIntList num_vertices=hwIntList(), hwDoubleList vertexpoints=hwDoubleList(), hwDoubleList origin=hwDoubleList(), hwDoubleList x_axis=hwDoubleList(), hwDoubleList y_axis=hwDoubleList(), hwDoubleList length=hwDoubleList(), hwDoubleList width=hwDoubleList(), int const dorebuild=0, int const scaleparams=0)
		"""
		pass

	def cuttingplanereverse(self,id: int):
		pass

	def deactivatelegacynasoselementidpools(self,state: int):
		pass

	def decimate_mesh(self,comps_collection: Collection, nodes_collection: Collection, failed_comps_collection: Collection, size_or_factor: float, feature_angle: float, options: int):
		pass

	def defaultmeshelems(self,collection: Collection, elem_size: float, elem_type: int, elem_type_2: int, comp_mode: int, size_control: int, skew_control: int, edge_mesh_type: int, min_size: float, max_size: float, max_deviation: float, max_angle: float, previous_settings: int, vertex_angle: float):
		pass

	def defaultmeshsurf(self,collection: Collection, elem_size: float, elem_type: int, elem_type_2: int, previous_settings: int, comp_mode: int, size_control: int, skew_control: int, mesh_type: int, min_size: float, max_size: float, chordal_dev: float, max_angle: float):
		pass

	def defaultmeshsurf_growth(self,collection: Collection, elem_size: float, elem_type: int, elem_type_2: int, previous_settings: int, comp_mode: int, size_control: int, skew_control: int, mesh_type: int, keep_mesh: int, min_size: float, max_size: float, chordal_dev: float, max_angle: float, growth_rate: float, id_array: hwIntList, size_array: hwDoubleList):
		pass

	def defaultremeshelems(self,collection: Collection, elem_size: float, elem_type: int, elem_type_2: int, comp_mode: int, size_control: int, skew_control: int, edge_mesh_type: int, min_size: float, max_size: float, max_deviation: float, max_angle: float, previous_settings: int, vertex_angle: float):
		pass

	def defaultremeshsurf(self,collection: Collection, elem_size: float, elem_type: int, elem_type_2: int, previous_settings: int, comp_mode: int, size_control: int, skew_control: int, mesh_type: int, min_size: float, max_size: float, chordal_dev: float, max_angle: float):
		pass

	def deformedshape(self,title: hwString , undeformed_color: int, deformed_color: int, scale_factor: float, hidden_line: int, full_size: int):
		pass

	def delaunay_2d_3d(self,type: int, collection: Collection, reserved: hwString ):
		pass

	def delete(self,obj: hw_module.mdi.base.MDIObject|hwdescriptor_module.Collection|hwdescriptor_module.CollectionSet):
		pass

	def deleteEdgeBH(self,name: hwString , flag: int):
		pass

	def delete_logo(self,collection: Collection, max_height: float, max_size: float, concavity_factor: float):
		pass

	def delete_small_parts(self,collection: Collection, minsize: float, method: int):
		pass

	def deleteblankholder(self,name: hwString , collection: Collection):
		pass

	def deleteboundingboxes(self,num_of_comps: int):
		pass

	def deleteedges(self):
		pass

	def deletefeatures(self):
		pass

	def deletefile(self,name: hwString ):
		pass

	def deletefillet(self,line: Entity):
		pass

	def deleteidrange(self,submodel_type: hwString , id: var0, shortname: hwString , entity_type: hwString , pool_id: var0):
		pass

	def deletemark(self,type: Collection):
		pass

	def deletemodel(self):
		pass

	def deletesolids(self,collection: Collection, keepshell: int):
		pass

	def deletesolidswithelems(self,collection: Collection, keep_shell: int, keep_elems: int):
		pass

	def deletetemporallock(self,entities: EntityFullType, logic: hwString ):
		pass

	def dependencycheck(self,collection: Collection):
		pass

	def depthcue(self,on: int):
		pass

	def derigidpart(self,partname: hwString ):
		pass

	def descriptormove(self,xmin: float, ymin: float, xmax: float, ymax: float):
		pass

	def descriptorsetcolor(self,color: int):
		pass

	def descriptorsetfont(self,font: int):
		pass

	def descriptorsettext(self,text: hwString ):
		pass

	def destroy(self):
		pass

	def detach_fromelements(self,elements: Collection, from_collection: Collection, offset: float):
		pass

	def detach_fromwall(self,elements: Collection, from_collection: Collection, offset: float, detach_ends: int):
		pass

	def detach_geom(self,*args, **kwargs):
		"""
		detach_geom(HMAPI self, Collection collection0, Collection collection1=hwDescriptor::Collection(), bool const organize=False)
		"""
		pass

	def detach_solids(self,collection: Collection, options: int):
		pass

	def detachallelements(self,collection: Collection, offset: float):
		pass

	def detachelements(self,collection: Collection, offset: float):
		pass

	def detect_surface_notches(self,surf_collection: Collection, max_fillet_radius: float, debug_collection: Collection, flag1: int, flag2: int):
		pass

	def detectandcreateface2facecontacts(collection: Collection, tolerance: float, reverse_angle: float, use_shell_thickness: var0, consolidate_surfaces: var0, run_intersection_check: var0, contact_type: var0, main_entity_type: var0, secondary_entity_type: var0, property_option: var0, contact_property_id: var0, static_friction_value: float, contact_material_id: var0, contact_main_sensor_id: var0, contact_secondary_sensor_id: var0, skip_preview: var0, consider_self: var0, thickness_type: var0, thickness_value: float, friction_direction: hwString , set_name_prefix: hwString , csurf_name_prefix: hwString , include_whole_components: var0, copy_tolerance_to_contact: var0):
		pass

	def detectandcreatefeatures(self,*args, **kwargs):
		"""
		detectandcreatefeatures(HMAPI self, int const hole2d_detection=0, int const hole3d_detection=0, int const fillet_detection=0, int const flange2d_detection=0, int const logo_detection=0, Collection surface_collection=hwDescriptor::Collection(), Collection element_collection=hwDescriptor::Collection(), double const hole2d_minradius=0.000000, double const hole2d_maxradius=0.000000, int const hole3d_stephole=0, double const hole3d_minradius=0.000000, double const hole3d_maxradius=0.000000, double const hole3d_maxdepth=0.000000, double const fillet_minradius=0.000000, double const fillet_maxradius=0.000000, double const flange2d_maxwidth=0.000000, double const logo_maxwidth=0.000000, double const logo_maxheight=0.000000, double const logo_concavityfactor=1.000000)
		"""
		pass

	def disconnect(self,connection):
		pass

	def displayBlankShape(self,resfile: hwString , state: hwString ):
		pass

	def displayStampedPartProfile(self,resfile: hwString , state: hwString ):
		pass

	def displayStampedPartProfile_withcircles(self,resfile: hwString , state: hwString , collection2: Collection, pointscoords: hwDoubleList):
		pass

	def displayTrimLineAtPartProfile(self,resfile: hwString , state: hwString , flag3d: int, flagpoint: int):
		pass

	def display_thickness(self,collection: Collection, thickness: float, update: int):
		pass

	def displayall(self):
		pass

	def displayallgeometry(self,on: int):
		pass

	def displaycollector(self,entity_type: EntityFullType, mode: hwString , name: hwString , elements: int, geometry: int):
		pass

	def displaycollectorsall(self,mode: hwString , elements: int, geometry: int):
		pass

	def displaycollectorsallbymark(self,collection_set: CollectionSet, mode: hwString , elements: int, geometry: int):
		pass

	def displaycollectorsbymark(self,collection: Collection, mode: hwString , elements: int, geometry: int):
		pass

	def displaycollectorwithfilter(self,entity_type: EntityFullType, mode: hwString , name: hwString , elements: int, geometry: int):
		pass

	def displayelementsbyproperty(self,mode: hwString , type: int):
		pass

	def displayelementsbypropertybymark(self,collection: Collection, mode: hwString , type: int):
		pass

	def displayincludeonly(self,id: var0, shortname: hwString ):
		pass

	def displaynone(self):
		pass

	def do_afcstep(self,collection: Collection, stepname: hwString , dbllistsize: int, str_dblparamlist: hwString ):
		pass

	def do_markrejectclear(self,update: int):
		pass

	def double_collector_test(self,collection1: Collection, collection2: Collection, the_float: float, the_int: int):
		pass

	def draglinetoformsurface(self,linelist: EntityList, list: EntityList, direction_vector: hwTriple, distance: float):
		pass

	def dragnodestoformsurface(self,list: EntityList, direction_vector: hwTriple, distance: float):
		pass

	def drawlistresetstyle(self):
		pass

	def drawlisttexmapmode(self,mode: int):
		pass

	def dummyautomaticpositioner(self,*args, **kwargs):
		"""
		dummyautomaticpositioner(HMAPI self, int const dummyid, hwIntList designpointids, hwIntList bodiestomove, hwIntList bodydofs=hwIntList(), hwIntList bodyweights=hwIntList(), int const targetspriority=1)
		"""
		pass

	def dummyplacerootbodytopoint(self,name: hwString , sx: float, sy: float, sz: float, tx: float, ty: float, tz: float, tolerance: float):
		pass

	def duplicateandreflectskeletonentities(self,collection: Collection, symmetryid: int  =" 0", duplicatemembersections: bool  = False):
		pass

	def duplicateentities(self,input_collection: Collection, output_collection: Collection, destcomponent: var0 , destloadcol: var0 , transformloads: int  =" 0", reverseloads: int  =" 0"):
		pass

	def duplicatemark(self,collection: Collection, current_collector: int):
		pass

	def dynamicrotatemode(self,mode: int):
		pass

	def dynamicviewbegin(self):
		pass

	def dynamicviewend(self):
		pass

	def edgerelease(self,edge: Entity):
		pass

	def edgerestore(self,edge: Entity):
		pass

	def edgesmarkaddmidpoint(self,collection: Collection):
		pass

	def edgesmarkaddpoints(self,collection: Collection, num_points: int):
		pass

	def edgesmarkrelease(self,collection: Collection):
		pass

	def edgesmarkrestore(self,collection: Collection):
		pass

	def edgesmarkrestorejoints(self,collection: Collection):
		pass

	def edgesmarksuppress(self,collection: Collection, break_angle: float):
		pass

	def edgesmarkuntrim(self,collection: Collection):
		pass

	def edgesmerge(self,edge1: Entity, edge2: Entity, edge_tolerance: float):
		pass

	def edgesuppress(self,edge: Entity):
		pass

	def edgeuntrim(self,theline: Entity):
		pass

	def editcollectorcard(self,entities: EntityFullType, name: hwString ):
		pass

	def element1dswitch(self,collection: Collection):
		pass

	def element2Dalign(self,collection_2d: Collection, collection_1d: Collection, propagate: int):
		pass

	def element2Dshiftnodes(self,element_entity: Entity, mode: int, shift_value: int, first_node_entity: Entity, second_node_entity: Entity, direction_vector: hwTriple):
		pass

	def element3Dalign(self,collection_3d: Collection, collection_2d: Collection, propagate: int):
		pass

	def element3Dshiftnodes(self,element_entity_3d: Entity, mode: int, shift_value: int, first_node_entity: Entity, last_node_entity: Entity, second_node_entity: Entity, element_entity_2d: Entity):
		pass

	def element_smooth_nodes(self,*args, **kwargs):
		"""
		element_smooth_nodes(HMAPI self, Collection elementsCollection, Collection nodeCollection, int const anchorFreeEdgeNodes=0, int const iterations=0, hwString const & smoothmethod="", int const timelimit=0)
		"""
		pass

	def elementcheck_timestepshells(self,badnews: float, badelemlist: Collection):
		pass

	def elementchecksettings(self,solver: int, jacobian_2d: int, jacobian_3d: int, min_len_2d: int, min_len_3d: int, aspect_2d: int, aspect_3d: int, skew_2d: int, skew_3d: int, angle: int, warpage: int, taper: int, chord_dev: int, tetra_collapse: int, cell_squish_2d: int, equi_skew_2d: int, cell_squish_3d: int, equi_skew_3d: int, time_step: int, reserved_1: int, reserved_2: int, reserved_3: int, reserved_4: int):
		pass

	def elementconfigcolor(self,config: hwString , color: int):
		pass

	def elementmarksplit(self,collection: Collection, crosscode: hwIntList):
		pass

	def elementmarksplitwith1D(self,collection: Collection, crossingmasks: hwIntList):
		pass

	def elementquality_move_node(self,nodeId: int, movelength: float , x: float , y: float , z: float ):
		pass

	def elementqualitycollapseedge(self,element: Entity, edge_index: int , optimize: bool  = False):
		pass

	def elementqualitycollapseelems(self,elem_id1: int, elem_id2: int):
		pass

	def elementqualitydragtriaelem(self,elem_id: int, px: float, py: float, pz: float, merge_tria: int = 1, end: int = 1):
		pass

	def elementqualitymodifyhole(self,node_index: Entity, move_option: int, x: float, y: float, z: float, string_array: hwStringList):
		pass

	def elementqualityoptimizeelement_2(self,id: int, midnodes: int = 1, optimize: int = 1):
		pass

	def elementqualityoptimizeelementnew(self,element_id: int, midnodes_flag: int = 1):
		pass

	def elementqualityoptimizenodenew(self,node_id: int, midnodes_flag: int = 1, optimize_flag: int = 1):
		pass

	def elementqualityplacenodenew(self,node_id: int, x: float, y: float, z: float, normal_flag: int =" 0", boundary_flag: int =" 0", midnodes_flag: int = 1):
		pass

	def elementqualityredoaction(self):
		pass

	def elementqualityreplacenode(self,node1: Entity, node2: Entity, nodePosScheme: int = 1):
		pass

	def elementqualitysetup(self,elementcollection: Collection):
		pass

	def elementqualitysetup_new(self,collection: Collection):
		pass

	def elementqualityshutdown(self,dontsaveflag: int):
		pass

	def elementqualitysmoothnodesnew(self,elem_collection: Collection, nodes_collection: Collection, algorithm: int, target_qi: float, max_iterations: int, time_limit: int):
		pass

	def elementqualitysplitedge(self,element: Entity, edge_index: int , optimize: bool  = False):
		pass

	def elementqualitysplitelem(self,element: Entity, swap: bool ):
		pass

	def elementqualityswapedgenew(self,element_id: int, edge_index: int):
		pass

	def elementqualityundoaction(self):
		pass

	def elements_cleanup(self,collection: Collection, file_name: hwString , elemsize: float, elem_type: int, feature_angle: float, elements_to_surface_component: int):
		pass

	def elementsaddelemsfixed(self,collection: Collection):
		pass

	def elementsaddnodesfixed(self,elements_collection: Collection, nodes_collection: Collection):
		pass

	def elementsettypes(self,collection: Collection):
		pass

	def elementtestaltitudeaspect(self,collection: Collection, aspectratio: float, outputcollection: Collection, contour: int, title: hwString ):
		pass

	def elementtestaspect(self,collection: Collection, aspect: float, output_collection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestcellsquish(self,collection: Collection, cell_squish: float, output_collection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestchordaldeviation(self,collection: Collection, maxdeviation: float, outputcollection: Collection, contour: int, title: hwString ):
		pass

	def elementtestconnectivity(self,collection: Collection, outputcollection: Collection, dimension: int):
		pass

	def elementtestdependancy(self,collection: Collection, outputcollection: Collection):
		pass

	def elementtestduplicates(self,collection: Collection, outputcollection: Collection, dimension: int):
		pass

	def elementtestequiaskew(self,collection: Collection, equiangle_skew: float, output_collection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestfree1d(self,entity_type: EntityFullType, collection: Collection, output_collection_set: CollectionSet):
		pass

	def elementtestinterangle(self,collection: Collection, testangle: float, trias: int, outputcollection: Collection, wantmin: int, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestjacobian(self,collection: Collection, jacobian: float, outputcollection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestlength(self,collection: Collection, length: float, outputcollection: Collection, wantmin: int, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestorthogonality(self,input_collection: Collection, orthogonality: float, output_collection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestrigidloops(self,collection: Collection, outputcollection: Collection):
		pass

	def elementtestsizeratio(self,input_collection: Collection, size_ratio: float, output_collection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestskew(self,collection: Collection, skewangle: float, outputcollection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtesttaper(self,collection: Collection, taperval: float, outputcollection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtesttetracollapse(self,collection: Collection, collapseval: float, outputcollection: Collection, contour: int, title: hwString ):
		pass

	def elementtesttimestep(self,collection: Collection, time_beam: float, time_spring: float, time_shell: float, time_solid: float, time_tshell: float, output_collection: Collection, dimension: int, contour: int, added_mass: int, title: hwString ):
		pass

	def elementtestvolumeareaskew(self,collection: Collection, skew: float, output_collection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtestvolumetricskew(self,collection: Collection, skew: float, outputcollection: Collection, contour: int, title: hwString ):
		pass

	def elementtestwarpage(self,collection: Collection, angle: float, outputcollection: Collection, dimension: int, contour: int, title: hwString ):
		pass

	def elementtype(self,config: hwString , type: hwString ):
		pass

	def elemoffset(self,collection: Collection, density: int, bias_style: int, bias: float, initial_offset: float, corner_type: int, thickness_type: int, thickness: float, shells_only: int, offset_type: int, component_flag: int):
		pass

	def elemoffset_thinsolid(self,entity_type_source: EntityFullType, collection_source: Collection, entity_type_target: EntityFullType, collection_target: Collection, entity_type_along: EntityFullType, collection_along: Collection, modes: int, density: int, bias: float, string_array: hwStringList, batchmesh_source: int =" 0"):
		pass

	def elempatchdecraction(self):
		pass

	def elempatchincraction(self):
		pass

	def elempatchnextaction(self):
		pass

	def elempatchprevaction(self):
		pass

	def elempatchstartaction(self,patch_type: int, threshold: float):
		pass

	def elempatchstopaction(self):
		pass

	def elemswarpagefix(self,collection: Collection, criteria_file_path: hwString , max_move: float, break_mode: int, feature_angle: float):
		pass

	def elemtestdependwithinodes(self,collection: Collection, outputcollection: Collection):
		pass

	def enabledirtinessdetectionforentitytype(self,entity_type: EntityFullType, enable_flag: int):
		pass

	def encryptentity(self,entity: Entity, key: var0):
		pass

	def end_batch_import(self):
		pass

	def endnotehistorystate(self,name: hwString ):
		pass

	def endtimecheck(self,title: hwString ):
		pass

	def engine(self,*args):
		pass

	def engine_types(self,*args):
		pass

	def entitybundleaddid(self,name: hwString , data_item: var0, id: var0):
		pass

	def entitybundleaddmark(self,name: hwString , data_item: var0, collection: Collection):
		pass

	def entitybundleclear(self,name: hwString , data_item: int):
		pass

	def entitybundleregister(self,name: hwString , entity_type_list: hwString , also_delete_instance: int):
		pass

	def entitybundleremoveid(self,name: hwString , data_item: var0, id: var0):
		pass

	def entitybundleremovemark(self,name: hwString , data_item: var0, collection: Collection):
		pass

	def entitydisplaywithattached(self,collection: Collection, attached_entity_type: EntityFullType, display_flag: int =" 0"):
		pass

	def entitysetdirty(self,entity: Entity, dirtiness_aspect: hwString , dirty_flag: int):
		pass

	def equationcreate(self,collection: Collection, independent_dofs: hwIntList, independent_weights: hwDoubleList, dependent: Entity, dof: hwBoolList, weight: float, ant: float):
		pass

	def equationcreatebylist(self,list: EntityList, independent_dofs: hwIntList, independent_weights: hwDoubleList, dependent: Entity, dof: hwBoolList, weight: float, ant: float):
		pass

	def equationupdatemeshconnectivity(self,collection: Collection, tolerance: float):
		pass

	def equivalence(self,collection: Collection, tolerance: float, mode: int, location: int, numbering: int, equivalence_to_meshnodes: int =" 0"):
		pass

	def equivalence2(self,collection: Collection, tolerance: float, location: int, numbering: int):
		pass

	def equivalencesubsystems(self,input_collection: Collection, enableHistory: int):
		pass

	def equivalencesurfaces(self,collection: Collection, options: int):
		pass

	def estimate_geom_thickness(self,ecollection: Collection, param_strs: hwStringList):
		pass

	def evaltclscript(self,filename: hwString , flag: int):
		pass

	def evaltclstring(self,string: hwString , flag: int):
		pass

	def exclusiveidrange(self,submodel_type: hwString , id: var0, shortname: hwString , entity_type: hwString , pool_id: var0):
		pass

	def exists(self,entity: hwdescriptor_module.Entity):
		"""
		
            Check if Entity exists
        
		"""
		pass

	def export_cdm(self,path: str):
		pass

	def export_designtable(self,design_table_name: hwString , file_name: hwString ):
		pass

	def export_radioss_iga(self,filename: hwString , entity_collection: Collection, options: int):
		pass

	def exportbif(self,filename: hwString ):
		pass

	def exportbom(self,file_name: hwString , options: hwString ):
		pass

	def exportfbdsectstobdf(self,filePath: hwString , freebodysection_ids: EntityList):
		pass

	def exportfbdsectstocsv(self,filePath: hwString , freebodysection_ids: EntityList):
		pass

	def exportparmfile(self,parmfile: hwString ):
		pass

	def exportshapes(self,analysiscode: hwString , subcode: hwString , outputfile: hwString ):
		pass

	def exportuserdefinedshapes(self,header: hwString , keyword: hwString , delimiter1: hwString , delimiter1_value: hwString , nodeid_width: int, delimiter2: hwString , delimiter2_value: hwString , x_coord_width: int, x_coord_precision: int, y_coord_width: int, y_coord_precision: int, z_coord_width: int, z_coord_precision: int, delimiter3: hwString , delimiter3_value: hwString , outputfile: hwString ):
		pass

	def extend_elements(self,collection_source: Collection, collection_target: Collection, options: hwString ):
		pass

	def external_skin_extraction(self,collection: Collection, mode: int, min_size: float, max_size: float, extraction_mode: int, seed_point_coordinates: hwString , target_point_coordinates: hwString , baffle_detection: int, min_surface_area: float, mc_collection: Collection, graphicsDB: int =" 0"):
		pass

	def external_skin_extraction_ctrl(self,mark10: Collection, ctrl: hwString , mc_mark: Collection, graphicsDB: int =" 0"):
		pass

	def facedeleteduplicates(self,collection: Collection, tol: float):
		pass

	def facemap(self,elemSizeI: float, elemSizeJ: float, surfcollection: Collection, vertcollection: Collection):
		pass

	def facemap_preview(self,elemSize: float):
		pass

	def facepreviewduplicates(self,collection: Collection, tol: float):
		pass

	def facesdelete(self):
		pass

	def facesmarktosurface(self,collection: Collection, surface: Entity):
		pass

	def facetdisplayedsurfaces(self):
		pass

	def failed_elements_cleanup(self,collection: Collection, elem_type: int, min_elemsize: float, max_feature_angle: float, max_reverse_angle: float):
		pass

	def fatiguewrite(self,collection: Collection, filename: hwString , datagroup: hwString , filetype: int, analysistype: int, simulationtype: int, sim1: hwStringList):
		pass

	def fbdcrosssectdisplaytobbox(self,cs_id: Entity, pos_factor: float, calc_new_basenode: int, update_cs: int, clear: int, bboxOrder: int, bInterpolate: int):
		pass

	def fbddisplacement(self,*args, **kwargs):
		"""
		fbddisplacement(HMAPIBase self, EntityList set_ids, double const arrLen=25.000000, int const arrowOrigin=0, unsigned int const colorfx=3, unsigned int const colorfy=4, unsigned int const colorfz=5, unsigned int const colorfxy=1, unsigned int const colorfyz=2, unsigned int const colorfxz=7, unsigned int const colorfxyz=6, unsigned int const colormx=3, unsigned int const colormy=4, unsigned int const colormz=5, unsigned int const colormxy=1, unsigned int const colormyz=2, unsigned int const colormxz=7, unsigned int const colormxyz=6, int const createField=1, int const createLoad=1, int const decLim=2, int const display=1, int const displacement=0, int const freenode=2, int const fx=0, int const fxy=0, int const fxyz=0, int const fxz=0, int const fy=0, int const fyz=0, int const fz=0, int const mx=0, int const mxy=0, int const mxyz=0, int const mxz=0, int const my=0, int const myz=0, int const mz=0, int const resFileID=INT_MAX, int const resolveInSys=0, Entity resultID=hwDescriptor::Entity(), int const rotation=0, int const scID=0, int const scientific=0, int const showValue=0, int const sizeScale=0, int const stepID=0, double const tolerance=0.001000, Entity userSysID=hwDescriptor::Entity(), int const vecStyle=0, int const gpf=0, int const intf=0, int const mpcf=0, int const sumAt=0, int const sysProj=0, int const spcf=0, int const appf=0, int const absolute=0, int const color=0, int const createTable=0, int const displayAt=0, int const envelope=0, hwString const & fieldName="", int const interpolate=0, double const maxVal=0.000000, int const midArrow=0, int const minMax=0, int const normalLoad=0, int const oneLems=0, int const onNodes=0, int const plotDir=0, int const range=0, hwString const & reportTablename="", int const resultant=0, int const summf=0, int const tangentialLoad=0)
		"""
		pass

	def fbdforce(self,*args, **kwargs):
		"""
		fbdforce(HMAPIBase self, EntityList freebodysection_ids, double const arrLen=25.000000, int const arrowOrigin=0, unsigned int const colorfx=3, unsigned int const colorfy=4, unsigned int const colorfz=5, unsigned int const colorfxy=1, unsigned int const colorfyz=2, unsigned int const colorfxz=7, unsigned int const colorfxyz=6, unsigned int const colormx=3, unsigned int const colormy=4, unsigned int const colormz=5, unsigned int const colormxy=1, unsigned int const colormyz=2, unsigned int const colormxz=7, unsigned int const colormxyz=6, int const createField=1, int const createLoad=1, int const decLim=2, int const display=1, int const displacement=0, int const freenode=2, int const fx=0, int const fxy=0, int const fxyz=0, int const fxz=0, int const fy=0, int const fyz=0, int const fz=0, int const mx=0, int const mxy=0, int const mxyz=0, int const mxz=0, int const my=0, int const myz=0, int const mz=0, int const resFileID=INT_MAX, int const resolveInSys=0, Entity resultID=hwDescriptor::Entity(), int const rotation=0, int const scID=0, int const scientific=0, int const showValue=0, int const sizeScale=0, int const stepID=0, double const tolerance=0.001000, Entity userSysID=hwDescriptor::Entity(), int const vecStyle=0, int const gpf=0, int const intf=0, int const mpcf=0, int const sumAt=0, int const sysProj=0, int const spcf=0, int const appf=0, int const absolute=0, int const color=0, int const createTable=0, int const displayAt=0, int const envelope=0, hwString const & fieldName="", int const interpolate=0, double const maxVal=0.000000, int const midArrow=0, int const minMax=0, int const normalLoad=0, int const oneLems=0, int const onNodes=0, int const plotDir=0, int const range=0, hwString const & reportTablename="", int const resultant=0, int const summf=0, int const tangentialLoad=0)
		"""
		pass

	def fbdtraceplot(self,*args, **kwargs):
		"""
		fbdtraceplot(HMAPI self, Entity freebodygroup_id, double const arrLen=25.000000, int const arrowOrigin=0, int const colorfx=3, int const colorfy=4, int const colorfz=5, int const colorfxy=1, int const colorfyz=2, int const colorfxz=7, int const colorfxyz=6, int const colormx=3, int const colormy=4, int const colormz=5, int const colormxy=1, int const colormyz=2, int const colormxz=7, int const colormxyz=6, int const createField=1, int const createLoad=1, int const decLim=2, int const display=1, int const displacement=0, int const freenode=2, int const fx=0, int const fxy=0, int const fxyz=0, int const fxz=0, int const fy=0, int const fyz=0, int const fz=0, int const mx=0, int const mxy=0, int const mxyz=0, int const mxz=0, int const my=0, int const myz=0, int const mz=0, int const resFileID=INT_MAX, int const resolveInSys=0, Entity resultID=hwDescriptor::Entity(), int const rotation=0, int const scID=0, int const scientific=0, int const showValue=0, int const sizeScale=0, int const stepID=0, double const tolerance=0.001000, Entity userSysID=hwDescriptor::Entity(), int const vecStyle=0, int const gpf=0, int const intf=0, int const mpcf=0, int const sumAt=0, int const sysProj=0, int const spcf=0, int const appf=0, int const absolute=0, int const color=0, int const createTable=0, int const displayAt=0, int const envelope=0, hwString const & fieldName="", int const interpolate=0, double const maxVal=0.000000, int const midArrow=0, int const minMax=0, int const normalLoad=0, int const oneLems=0, int const onNodes=0, int const plotDir=0, int const range=0, hwString const & reportTablename="", int const resultant=0, int const summf=0, int const tangentialLoad=0)
		"""
		pass

	def feature_replace(self,source_collection: Collection, target_collection: Collection, float_array: hwDoubleList, tolerance: float, keep_source: int):
		pass

	def features(self,collection: Collection, feature_angle: float, ignorenormals: int, created_entity: int, break_angle: float, smooth: int):
		pass

	def features_add(self,node_list: EntityList, lines: int, smooth: int):
		pass

	def features_advanced(self,collection: Collection, feature_angle: float, type: int, break_angle: float, created_entity: int, smooth: int, IgnoreNormal: int  =" 0", MergeSmallArea: int  =" 0", MergeSmallAreaRatio: int  =" 0", ElementSize: int  =" 0"):
		pass

	def features_move_all_opened(self):
		pass

	def features_remove_selected(self,collection: Collection):
		pass

	def feexportcustom(self,outputname: hwString , dllpath: hwString , paramStrs: hwStringList):
		pass

	def feinputinteractive(self,programname: hwString , filename: hwString , overwrite: int, min_edge_length: float, cleanup_tolerance: float, blanked_component: int, offsetflag: var1):
		pass

	def feinputinteractive2(self,transfilename: hwString , inputfilename: hwString , overwrite: int, min_edge_length: float, cleanuptol: float, blanked_component: int, offsetflag: var1, data_strings: hwStringList, interactive: var1, scale_factor: float, splitbylayer: int):
		pass

	def feinputmerge(self,*args, **kwargs):
		"""
		feinputmerge(HMAPI self, hwString const & reader, hwString const & inputfilename, hwStringList importoptions=hwStringList(), hwString const & mergemode_comps="keepboth", hwString const & mergemode_geometryandmesh="keepboth", hwString const & mergemode_mats="keepboth", hwString const & mergemode_props="keepboth", hwString const & mergemode_sensors="keepboth", hwString const & mergemode_sections="keepboth")
		"""
		pass

	def feinputoffsetid(self,entity_type: EntityFullType, offsetvalue: int):
		pass

	def feinputomitincludefiles(self):
		pass

	def feinputpreserveincludefiles(self):
		pass

	def feinputwithdata2(self,import_reader: hwString , filename: hwString , overwrite_flag: int, reserved1: float, cleanup_tolerance: float, blanked_component: int, offset_flag: var1, string_array: hwStringList, scale_factor: float, name_comps_by_layer: int):
		pass

	def feoutput_select(self,templateName: hwString , outputFileName: hwString , select_collection: CollectionSet, lines: int, autoprops: int):
		pass

	def feoutput_singleinclude(self,*args, **kwargs):
		"""
		feoutput_singleinclude(HMAPI self, unsigned int id, hwString const & shortname, hwString const & export_template, hwString const & filename, int reserved1, int reserved2, int export_type, hwStringList string_array=s_defaultStringList)
		"""
		pass

	def feoutputincludes(self,template_path: hwString , filename: hwString , includeids: hwIntList, type: int , options: hwStringList):
		pass

	def feoutputmergeincludefiles(self,code: int):
		pass

	def feoutputwithdata(self,export_template: hwString , filename: hwString , reserved1: int, reserved2: int, export_type: int, string_array: hwStringList):
		pass

	def feoutputwithdata_PI(self,export_template: hwString , filename: hwString , reserved1: int, reserved2: int, export_type: int, string_array: hwStringList):
		pass

	def fetosurfs(self,collection_2d: Collection, collection_1d: Collection, options: int, complexity: int, tolerance: float, reserved: int):
		pass

	def filewrite_components_geometry(self,comps_collection: Collection, filename: hwString , compressed_format: int):
		pass

	def filewritecomponentgeometry(self,filename: hwString , component: hwString , compression: int):
		pass

	def filewriteentities(self,collection: Collection, filename: hwString , reserved: int, ce_realizedflag: int =" 0"):
		pass

	def fill_circular_holes(self,collection: Collection, radius_limit: float):
		pass

	def fill_fe_gaps_elems(self,*args, **kwargs):
		"""
		fill_fe_gaps_elems(HMAPIBase self, int mode, Collection collection1, Collection collection2, double max_width, unsigned int const AdjacentComp=0, unsigned int const ByFeature=0, unsigned int const CurvedFill=0, unsigned int const DefineMaxWidth=0, EntityList2 GuideNodePairs=s_defaultEntityList2, unsigned int const Remesh=0)
		"""
		pass

	def fill_fe_gaps_lines(self,*args, **kwargs):
		"""
		fill_fe_gaps_lines(HMAPI self, Collection collection1, Collection collection2, double max_width, int const ByFeature=0, int const Remesh=0, int const DefineMaxWidth=0, int const AdjacentComp=0, int const CurvedFill=0, hwIntList GuideNodePairs=hwIntList(), int const DetectNodeClusters=0, int const DoOverlapCleanup=0)
		"""
		pass

	def fill_fe_gaps_nodeid(self,*args, **kwargs):
		"""
		fill_fe_gaps_nodeid(HMAPIBase self, Entity node_id1, Entity node_id2, double max_width, unsigned int const AdjacentComp=0, unsigned int const ByFeature=0, unsigned int const CurvedFill=0, unsigned int const DefineMaxWidth=0, EntityList2 GuideNodePairs=s_defaultEntityList2, unsigned int const Remesh=0)
		"""
		pass

	def fill_fe_gaps_nodelist(self,*args, **kwargs):
		"""
		fill_fe_gaps_nodelist(HMAPIBase self, EntityList list1, EntityList list2, double max_width, unsigned int const AdjacentComp=0, unsigned int const ByFeature=0, unsigned int const CurvedFill=0, unsigned int const DefineMaxWidth=0, unsigned int const DetectNodeClusters=0, EntityList2 GuideNodePairs=s_defaultEntityList2, unsigned int const Remesh=0)
		"""
		pass

	def fill_fe_holes(self,*args, **kwargs):
		"""
		fill_fe_holes(HMAPIBase self, int mode, Collection collection, double max_width, unsigned int const AdjacentComp=0, unsigned int const ByFeature=0, unsigned int const CurvedFill=0, unsigned int const DefineMaxWidth=0, EntityList2 GuideNodePairs=s_defaultEntityList2, unsigned int const Remesh=0)
		"""
		pass

	def fill_fe_holes_lines(self,*args, **kwargs):
		"""
		fill_fe_holes_lines(HMAPI self, Collection collection, double max_width, int const ByFeature=0, int const Remesh=0, int const DefineMaxWidth=0, int const AdjacentComp=0, int const CurvedFill=0, hwIntList GuideNodePairs=hwIntList(), int const DetectNodeClusters=0, int const DoOverlapCleanup=0, int const CheckForDuplicate=0)
		"""
		pass

	def fill_fe_holes_nodelist(self,*args, **kwargs):
		"""
		fill_fe_holes_nodelist(HMAPIBase self, EntityList list, double max_width, unsigned int const AdjacentComp=0, unsigned int const ByFeature=0, unsigned int const CurvedFill=0, unsigned int const DefineMaxWidth=0, EntityList2 GuideNodePairs=s_defaultEntityList2, unsigned int const Remesh=0)
		"""
		pass

	def fillet_surface_edges(self,collection: Collection, fillet_radius: float, stitching_tol: float, unfold_angle_limit: float, fillet_option: int, trim_mode: int, reserved: int):
		pass

	def filletmesh(self,collection: Collection, feature: float, radius: float):
		pass

	def fillplot(self,title: hwString , mesh_color: int, fill_color: int, full_size: int, blocks: int):
		pass

	def filtertable(self,keycolumns: hwStringList, keystring: hwStringList, table: hwString , targettable: hwString , valuecolumns: hwStringList):
		pass

	def find_holes_in_3d_body(self,input_collection: Collection, output_collection: Collection, mode: int, flags: int, min_diam: float, max_diam: float, max_lensize: float):
		pass

	def findandremovethreads(self,collection: Collection, max_depth: float, replacement_type: int, flags: int, reserved1: float, reserved2: float):
		pass

	def findattachedelementfaces(self,collection: Collection, table_id: int):
		pass

	def findbetween(self,between_collection: Collection, function: var0 , numbers: int , output_collection: Collection):
		pass

	def findedges(self,*args, **kwargs):
		"""
		findedges(HMAPI self, Collection collection, hwString const & edgetype="free", bool const createlines=False, bool const smoothlines=False, bool const ignorefeatures=False, double const breakangle=30.000000, unsigned int const chainid=UINT_MAX, hwString const & componentprefix="", hwString const & componentname="^edges", hwString const & color="#FF0000")
		"""
		pass

	def findedges1(self,collection: Collection, edge_type: int, created_entity: int, smooth: int, break_angle: float):
		pass

	def findfaces(self,*args, **kwargs):
		"""
		findfaces(HMAPI self, Collection collection, hwString const & componentname="^faces", hwString const & componentprefix="", unsigned int const cluster_index=UINT_MAX, hwString const & color="#FF0000")
		"""
		pass

	def findloops(self,collection: Collection, by_component: int):
		pass

	def findmark(self,collection: Collection, function: int, adjacent: int, adjacent_entity_type: EntityFullType, numbers: int, output_collection: Collection, recursive: int =" 0"):
		pass

	def fix_2d_mesh(self,collection: Collection, fix_type: int, aspect_ratio: float, node_movement_tol: float, fix_method: int, failed_collection: Collection):
		pass

	def fix_degenerated_faces(self,collection: Collection, tol: float):
		pass

	def fix_overlaped_faces(self,collection: Collection, tol: float):
		pass

	def fix_surfaces_orientation(self,surfaces: Collection, orientation: int):
		pass

	def fixnarrowstrips(self,collection: Collection, width_threshold: float, width_sharp_edge_threshold: float, target_elem_size: float, min_elem_size: float, angular_tol: float, geometry_fix_tol: float, fix_flags: int):
		pass

	def fixnarrowsurfaces(self,collection: Collection, width_threshold: float, mesh_type: int, fix_flag: int, string_options: hwString ):
		pass

	def flangecreateline(self,collection1: Collection, collection2: Collection, list: EntityList, lineflag: int):
		pass

	def flanges_detect(self,comp_collection: Collection, max_width: float, min_width: float, flange_collection: Collection):
		pass

	def flattenpartmodel(self,reserved: int):
		pass

	def flexiblebodyparametersupdate(self,name: hwString , auto_flex: int, dtype: int, dval: float):
		pass

	def fmvss201u_autoposition(self,*args, **kwargs):
		"""
		fmvss201u_autoposition(HMAPI self, int const method, double const offset=0.000000, double const velocity=0.000000, int const sectioncut=0, hwIntList foreheadpartsids=hwIntList(), hwIntList headformpartsids=hwIntList(), hwIntList outertrimpartsids=hwIntList(), hwIntList designpointids=hwIntList(), hwIntList exportdpids=hwIntList(), Entity headformsystemid=hwDescriptor::Entity(), hwIntList exportheadformids=hwIntList(), hwString const & exportpath="", hwString const & mainfilepath="", hwString const & headformfilepath="", int const dpnamesfordirandincludes=0, int const folderforeachdp=0, int const transformationtype=0, int const vehicledir=-1)
		"""
		pass

	def formulaallclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, flag: int, clause_index: int):
		pass

	def formulaclause(self,entity: Entity, identifier: hwString , formulaentitytype: EntityFullType):
		pass

	def formulacolorclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, color: var0, flag: int, clause_index: int):
		pass

	def formulalistclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, data: hwUIntList, flag: int, clause_index: int):
		pass

	def formulanameclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, name: hwString , flag: int, clause_index: int):
		pass

	def formularangeclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, start: var0, end: var0, incr: var0, flag: int, clause_index: int):
		pass

	def formulasetreview(self,name: hwString , collection: CollectionSet):
		pass

	def formulaupdateallclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, flag: int, clause_index: int):
		pass

	def formulaupdatecolorclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, color: var0, flag: int, clause_index: int):
		pass

	def formulaupdatelistclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, data: hwUIntList, flag: int, clause_index: int):
		pass

	def formulaupdatenameclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, name: hwString , flag: int, clause_index: int):
		pass

	def formulaupdaterangeclause(self,entity: Entity, identifier: hwString , clauseEntitytype: EntityFullType, additionType: int, start: var0, end: var0, incr: var0, flag: int, clause_index: int):
		pass

	def frame_field_hex_meshing(self,collection10: Collection):
		pass

	def freebodysectiondisplacement(self,*args, **kwargs):
		"""
		freebodysectiondisplacement(HMAPIBase self, EntityList freebodysection_ids, int const freenode, double const arrlen=75.0, unsigned int const arroworigin=0, unsigned int const colorfx=3, unsigned int const colorfy=4, unsigned int const colorfz=5, unsigned int const colorfxy=1, unsigned int const colorfyz=2, unsigned int const colorfxz=7, unsigned int const colorfxyz=6, unsigned int const colormx=3, unsigned int const colormy=4, unsigned int const colormz=5, unsigned int const colormxy=1, unsigned int const colormyz=2, unsigned int const colormxz=7, unsigned int const colormxyz=6, unsigned int const createfield=0, unsigned int const createload=0, int const declim=2, unsigned int const display=1, unsigned int const displacement=0, unsigned int const fx=0, unsigned int const fxy=0, unsigned int const fxyz=0, unsigned int const fxz=0, unsigned int const fy=0, unsigned int const fyz=0, unsigned int const fz=0, unsigned int const mx=0, unsigned int const mxy=0, unsigned int const mxyz=0, unsigned int const mxz=0, unsigned int const my=0, unsigned int const myz=0, unsigned int const mz=0, int const resFileID=INT_MAX, unsigned int const resolvein_sys=0, Entity resultID=hwDescriptor::Entity(), unsigned int const rotation=0, unsigned int const scid=0, unsigned int const scientific=0, unsigned int const showvalue=0, unsigned int const sizescale=0, unsigned int const stepid=0, double const tolerance=0.0001, Entity userSysID=hwDescriptor::Entity(), unsigned int const vecstyle=0)
		"""
		pass

	def freebodysectiondisplacementtable(self,*args, **kwargs):
		"""
		freebodysectiondisplacementtable(HMAPIBase self, EntityList freebodysection_ids, hwTripleIList subcase_ids, int const freenode, unsigned int const displacement=0, unsigned int const resolvein_sys=0, Entity resultID=hwDescriptor::Entity(), unsigned int const rotation=0, double const tolerance=0.0001, Entity userSysID=hwDescriptor::Entity())
		"""
		pass

	def freebodysectionforce(self,*args, **kwargs):
		"""
		freebodysectionforce(HMAPIBase self, EntityList freebodysection_ids, unsigned int const appf=0, double const arrlen=75.0, unsigned int const arroworigin=0, unsigned int const colorfx=3, unsigned int const colorfy=4, unsigned int const colorfz=5, unsigned int const colorfxy=1, unsigned int const colorfyz=2, unsigned int const colorfxz=7, unsigned int const colorfxyz=6, unsigned int const colormx=3, unsigned int const colormy=4, unsigned int const colormz=5, unsigned int const colormxy=1, unsigned int const colormyz=2, unsigned int const colormxz=7, unsigned int const colormxyz=6, unsigned int const createfield=0, unsigned int const createload=0, int const declim=2, unsigned int const display=1, unsigned int const freenode=0, unsigned int const fx=0, unsigned int const fxy=0, unsigned int const fxyz=0, unsigned int const fxz=0, unsigned int const fy=0, unsigned int const fyz=0, unsigned int const fz=0, unsigned int const gpf=0, unsigned int const intf=0, unsigned int const mpcf=0, unsigned int const mx=0, unsigned int const mxy=0, unsigned int const mxyz=0, unsigned int const mxz=0, unsigned int const my=0, unsigned int const myz=0, unsigned int const mz=0, int const resFileID=INT_MAX, unsigned int const resolvein_sys=0, unsigned int const resultant=0, Entity resultID=hwDescriptor::Entity(), unsigned int const scid=0, unsigned int const scientific=0, unsigned int const showvalue=0, unsigned int const sizescale=0, unsigned int const spcf=0, unsigned int const stepid=0, double const tolerance=0.0001, Entity userSysID=hwDescriptor::Entity(), unsigned int const vecstyle=0)
		"""
		pass

	def freeshapedesvarcreatewithmethod(self,collection: Collection, name: hwString , method: var0):
		pass

	def freeshapedesvarupdatewithmethod(self,collection: Collection, name: hwString , method: var0):
		pass

	def fuse_shell_mesh(self,*args, **kwargs):
		"""
		fuse_shell_mesh(HMAPI self, Collection source_collection, Collection target_collection, double proximity, hwString const & options=s_defaultString)
		"""
		pass

	def gapelement(self,node1: Entity, node2: Entity, property: hwString , name: Entity):
		pass

	def gapelementupdate(self,collection: Collection, property: hwString , name: Entity, vectorid: int, Update: int):
		pass

	def gda_export(self,mesh_collection: Collection, outputFileName: hwString ):
		pass

	def gda_import(self,gdaInputFileName: hwString ):
		pass

	def geom_repair(self,*args, **kwargs):
		"""
		geom_repair(HMAPI self, Collection surf_collection=hwDescriptor::Collection(), hwString const & method="", double const width=0.000000, bool const optimize_geom=True)
		"""
		pass

	def geom_simplify(self,*args, **kwargs):
		"""
		geom_simplify(HMAPIBase self, Collection collection, hwString const & primitive_type="box", hwString const & cover="per_body", int const simplify=0, int const delete_original=0, hwString const & dest_comp="current", hwString const & comp_name="")
		"""
		pass

	def geomexport(self,translator_type: hwString , input_file_name: hwString , options: hwStringList):
		pass

	def geomimport(self,translator_type: hwString , input_file_name: hwString , options: hwStringList):
		pass

	def geommatchtopology(self,collection: Collection, stitch_tol: float):
		pass

	def geomnormalignmentmode(self,mode: int):
		pass

	def geomupdate(self,*args, **kwargs):
		"""
		geomupdate(HMAPI self, Collection collection, hwString const & DataToUpdate="", hwString const & FileVersionSameAsCAD="", hwString const & MetadataPrefixFilter="", hwString const & OutputFolder="", hwString const & OverWriteRepresentation="", hwString const & RemoveMetadataPrefix="", hwString const & UpdateColorFrom="", hwString const & UpdateMetaDataAsColor="", hwString const & UpdateMetaDataAsName="", hwString const & UpdateNameFrom="")
		"""
		pass

	def geomvectorcreate(self,geom_collection: Collection, node_collection: Collection, node_tol: float, magnitude: float, parlen: int, reverse: int):
		pass

	def geomvectorupdate(self,vector_collection: Collection, geom_collection: Collection, node_tol: float, magnitude: float, parlen: int, reverse: int, update_geom: int, update_mag: int, update_reverse: int):
		pass

	def get(self,entity: hwdescriptor_module.Entity):
		pass

	def get_from_metaobject(self,metaobject: hwdescriptor_module.Metaobject, **kwargs):
		pass

	def getnodesinsidedomaintomark(self,nodes_collection: Collection, element_id: var0, tolerance: float, calcminlen: int):
		pass

	def getqualitysummary(self,elementcollection: Collection, summary_file: hwString , failedcollection: Collection, criteria_use_mode: int):
		pass

	def getunmeshedsurfstomark(self,collection: Collection):
		pass

	def getunmeshedsurfstomark2(self,collection: Collection):
		pass

	def graphexport_file(self,fname: hwString ):
		pass

	def graphicactivationmode(self,mode: int):
		pass

	def graphicfont(self,size: int):
		pass

	def graphicsfilecolor(self,mode: int):
		pass

	def graphimport(self,fname: hwString , options: int, solid_flags: int, shell_flags: int):
		pass

	def graphimport_file(self,filename: hwString ):
		pass

	def graphimport_file_with_quality(self,fname: hwString , solid_flags: int, shell_flags: int):
		pass

	def graphpick(self,ent_type: EntityFullType, x: int, y: int, flags: int):
		pass

	def graphremove_file(self,fname: hwString ):
		pass

	def graphuserwindow_byXYZandR(self,x: float, y: float, z: float, r: float):
		pass

	def graphuserwindow_to_XYZ(self,x: float, y: float, z: float, n: int):
		pass

	def group_matches(self,*args, **kwargs):
		"""
		group_matches(HMAPIBase self, Collection collection, Collection reference_collection=s_defaultCollection, int const areaCalcMethod=1, int const compareType=0, double const deformationTolerance=0.000000, int const encoding_algorithm=INT_MAX, double const matchingPercentThreshold=0.000000, hwString const & parentpartsetname="", hwString const & partsetname="", bool const partsetforunmatched=False, hwString const & searchMethod="ByEncoding", int const sphhar_bandwidth=16, double const sphhar_fallof=2.828427, int const sphhar_radii=32, int const resolution=64, hwString const & unmatchedpartsetname="")
		"""
		pass

	def groupchangetype(self,name: hwString , config: int, type: int):
		pass

	def groupcreatesameas(self,newname: hwString , existingname: hwString , color: int):
		pass

	def groupdeleteunused(self,f_displayed: int):
		pass

	def grouppreviewunused(self,collection_set: CollectionSet, displayed: int):
		pass

	def groupsetconfigtype(self,collection: Collection, destConfig: var0, destType: var0):
		pass

	def hex_meshing(self,collection10: Collection, minOctantSize: float, maxOctantSize: float):
		pass

	def hex_refinement(self,collection1: Collection, collection2: Collection, refinement_level: int):
		pass

	def hfCreateFlatBinder(self,type: int, control: int, use_symmetry: int, plane_normal: hwTriple, plane_normal_base: hwTriple, offsetdist: float):
		pass

	def hfCreateSingleCurveBinder(self,type: int, control: int, use_symmetry: int, plane_normal: hwTriple, plane_normal_base: hwTriple, offsetdist: float):
		pass

	def hf_AddBinderSectionHandle(self,lineptr: Entity, x: float, y: float, z: float, dx: float, dy: float, dz: float):
		pass

	def hf_AddSectionHandle(self,line_entity: Entity, x_coord: float, y_coord: float, z_coord: float, dx_coord: float, dy_coord: float, dz_coord: float):
		pass

	def hf_Addendum_ActiveEditor(self,type: int, trimline: Collection, binder: Entity):
		pass

	def hf_Addendum_AddAddendumSections(self,model: Entity, collection: Collection):
		pass

	def hf_Addendum_AddBatchSeeds(self,lineptr: Entity, collection: Collection):
		pass

	def hf_Addendum_AddBinderTrack(self,seed1: Entity):
		pass

	def hf_Addendum_AddFreeRibbyInterpolating(self,n1: Entity, n2: Entity, rib1: Entity, rib2: Entity):
		pass

	def hf_Addendum_AddOldFixedRibs(self,linelist: EntityList):
		pass

	def hf_Addendum_AddOldRibs(self,linelist: EntityList):
		pass

	def hf_Addendum_AddPOLHandle(self,x: float, y: float, z: float, dx: float, dy: float, dz: float):
		pass

	def hf_Addendum_AddSeedByInterpolate(self,seed1: Entity, seed2: Entity, rib1: Entity, rib2: Entity):
		pass

	def hf_Addendum_AddSeeds(self,seed1: Entity, seed2: Entity, flag: int):
		pass

	def hf_Addendum_AddSingleSeed(self,seed1: Entity, flag: int):
		pass

	def hf_Addendum_AddTrackHandle(self,x: float, y: float, z: float, dx: float, dy: float, dz: float):
		pass

	def hf_Addendum_CastAddendumSections(self,model: Entity, collection: Collection):
		pass

	def hf_Addendum_CastBinderTracks(self,linelist1: EntityList, collection: Collection):
		pass

	def hf_Addendum_CastRibs_line(self,model: Entity, collection: Collection):
		pass

	def hf_Addendum_CreateRefElem(self,seed1: Entity, seed2: Entity):
		pass

	def hf_Addendum_DeleteAddendumSections(self,collection: Collection):
		pass

	def hf_Addendum_DeleteBinderTracks(self,collection: Collection):
		pass

	def hf_Addendum_DeleteRib(self,collection: Collection):
		pass

	def hf_Addendum_EvaluateRib(self,part_collection: Collection, rib: Entity, neutral: Entity, value: hwDoubleList):
		pass

	def hf_Addendum_ExtendSurface(self,collection: Collection, distance1: float, radius: float, distance2: float, sym_flag: int, x_sym: float, y_sym: float, z_sym: float, bx_sym: float, by_sym: float, bz_sym: float):
		pass

	def hf_Addendum_GetBasicRibInfo(self,n1: Entity, n2: Entity):
		pass

	def hf_Addendum_GetBinderTrackHandle(self,lineptr: Entity):
		pass

	def hf_Addendum_GetHandelsAtRibEnd(self,collection: Collection):
		pass

	def hf_Addendum_GetPOLhandles(self,surfptr: Entity, collection: Collection):
		pass

	def hf_Addendum_GetParamRibInfo(self,lineptr: Entity):
		pass

	def hf_Addendum_GetParamRibInfoFromScratch(self,lineptr: Entity):
		pass

	def hf_Addendum_MeasureDistanceFromBinder(self,base: Entity, collection: Collection):
		pass

	def hf_Addendum_ModifyPOL(self,n1: Entity, x: float, y: float, z: float, dx: float, dy: float, dz: float):
		pass

	def hf_Addendum_ModifyTrack(self,n1: Entity, x: float, y: float, z: float, dx: float, dy: float, dz: float):
		pass

	def hf_Addendum_MorphAddenumSectionEnd(self,nodeptr: Entity):
		pass

	def hf_Addendum_MorphAddenumSectionEnds(self,dummy: int):
		pass

	def hf_Addendum_PrepareLatitudeLine(self,int_flag: int):
		pass

	def hf_Addendum_RemovePOLhandles(self,collection: Collection):
		pass

	def hf_Addendum_RemoveSingleTrackHandle(self,x: float, y: float, z: float, dx: float, dy: float, dz: float):
		pass

	def hf_Addendum_RotateBinderSurf(self,planeptr_normal: hwTriple, planeptr_normal_base: hwTriple, angle: float, collection: Collection):
		pass

	def hf_Addendum_ScaleBinderSurf(self,base: Entity, sx: float, sy: float, sz: float, collection: Collection):
		pass

	def hf_Addendum_SlideHandleOnBinder(self,handleptr: Entity, mousex: int, mousey: int, tolerance: float):
		pass

	def hf_Addendum_SmoothPartialTLwithRollingCylinder(self,lineptr: Entity, smoothval: float, n1: Entity, n2: Entity, type: int):
		pass

	def hf_Addendum_SyncronizeWithBinder(self,dummy: int):
		pass

	def hf_Addendum_TranslateBinderSurf(self,planeptr_normal: hwTriple, planeptr_normal_base: hwTriple, distance: float, collection: Collection):
		pass

	def hf_Addendum_TweakRibEnd(self,rib: Entity, newend: Entity):
		pass

	def hf_Addendum_UpdateAddendumWithNewSection(self,lineptr: Entity):
		pass

	def hf_Addendum_UpdateBinder(self,dummy: float):
		pass

	def hf_Addendum_UpdateGlobalSet(self,symm_flag: int, symm_plane_normal: hwTriple, symm_plane_normal_base: hwTriple, dummy1: int, dummy2: int):
		pass

	def hf_Addendum_UpdateParamRib(self,lineptr: Entity):
		pass

	def hf_Addendum_UpdateSlide(self,handle_entity: Entity, x_coord: float, y_coord: float, z_coord: float, tol: float):
		pass

	def hf_Addendum_Updatewithparams(self,plus_value: float, entry_value: float, wall_value: float, smooth_value: float, fixed_value: int, split_value: int, first_constrain: int, cornerrib: int):
		pass

	def hf_CallEventManager(self,profile: var0, profile_obj: var0, prifile_event: var0):
		pass

	def hf_CastBinderSections(self,lineptr: Entity, lcollection: Collection):
		pass

	def hf_ClearFromWorkingSection(self,int_flag: int):
		pass

	def hf_ClearLLHandles(self,int_flag: int):
		pass

	def hf_ClearSectionHandles(self):
		pass

	def hf_CreateBinderSectionAndHandles(self,plane_flag: int, plane_normal: hwTriple, plane_normal_base: hwTriple, node_collection: Collection, line_entity: Entity, multiple: int):
		pass

	def hf_CreateInitialSectionHandles(self,section: Entity):
		pass

	def hf_CreateLineOffsetPreview(self,lines_list_collection: Collection, surfs_collection: Collection, plane_ptr_normal: hwTriple, plane_ptr_normal_base: hwTriple, extension_type: int, distance1: float, radius: float, distance2: float):
		pass

	def hf_CreatePol(self,offset: float):
		pass

	def hf_CreateSection(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, flag: int):
		pass

	def hf_Create_DieCadSys(self,reserved: int):
		pass

	def hf_DeleteBinderSectionHandle(self,handle_ptr: Entity):
		pass

	def hf_DeleteSection(self,lineptr: Entity):
		pass

	def hf_DeleteSectionHandle(self,handle_entity: Entity):
		pass

	def hf_DiePartPositioning(self,collection: Collection, vector: hwTriple, symmetry_flag: int, plane_id: hwTriple, plane_id_base: hwTriple, reduce_depth: int, reduce_undercut: int, alignment_flag: int, reposition_stamping: int, reposition_CAD: int = -1):
		pass

	def hf_DrawThickRibs(self):
		pass

	def hf_EditPol(self,reserved: int):
		pass

	def hf_EditSection(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, flag: var0):
		pass

	def hf_FeatureFromSurfaces(self,collection: Collection):
		pass

	def hf_FillDoubleAttachedPart(self,creation_flag: int, x_coord: float, y_coord: float, z_coord: float, gap: float, n1: Entity, n2: Entity):
		pass

	def hf_LevelElementsOnOff(self,state: int):
		pass

	def hf_LineModifyByControlPoint(self,lineptr1: Entity, base: Entity, n1: Entity, n2: Entity, imode: int, dx: float, dy: float, dz: float):
		pass

	def hf_LineOffset(self,flag: int, lineptr1: Entity, lineptr2: Entity, vector: hwTriple, surfptr: Entity, dist: float):
		pass

	def hf_LineOffsetprojectoffset(self,flag: int, lineptr1: Entity, lineptr2: Entity, vector: hwTriple, surfptr: Entity, dist: float, smoothrad: float):
		pass

	def hf_ModifyBinderSectionHandle(self,original_handle: Entity, new_x: float, new_y: float, new_z: float):
		pass

	def hf_ModifyRibwithPoint(self,lineptr: Entity, x: float, y: float, z: float, dirx: float, diry: float, dirz: float):
		pass

	def hf_RejectDragDeleteHandle(self,int_flag: int):
		pass

	def hf_ResetDFRibs(self,int_flag: int):
		pass

	def hf_RevertBinderSections(self,lcollection: Collection):
		pass

	def hf_RibPreviewActivate(self,preview_flag: int):
		pass

	def hf_RotateBinderSurf(self,plane_normal: hwTriple, plane_normal_base: hwTriple, angle: float):
		pass

	def hf_SaveRibData(self,rib_data: hwDoubleList, options: int, param1: int, param2: float):
		pass

	def hf_ScaleBinderSurf(self,base_point_entity: Entity, scale_factor_x: float, scale_factor_y: float, scale_factor_z: float):
		pass

	def hf_SetSurfaceLikeBinder(self,surf_ptr: Entity):
		pass

	def hf_ShutdownAddendumEngine(self,special: int):
		pass

	def hf_SlideHandleptrOnSectionPlane(self,handle_entity: Entity, x_mouse: int, y_mouse: int, reserved: float):
		pass

	def hf_TranslateBinderSurf(self,plane_normal: hwTriple, plane_normal_base: hwTriple, distance: float):
		pass

	def hf_TrimBinderOrAddendumWithAddDbeadDbar(self,collection_surf: Collection, collection_line: Collection):
		pass

	def hf_TrimElementsOnOff(self,state: int):
		pass

	def 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(self,collection1: Collection, collection2: Collection):
		pass

	def hf_UpdateExportSection(self,section_data: hwDoubleList, options: int, param1: int, param2: float):
		pass

	def hf_createdoubleattachedparams(self,line_collection: Collection, nodes_collection: Collection, gap: float, x_sym: float, y_sym: float, z_sym: float, x_draw: float, y_draw: float, z_draw: float, creation_flag: int):
		pass

	def hf_extendsurface(self,collection: Collection, dist: float, sym_flag: int, x_sym: float, y_sym: float, z_sym: float, bx_sym: float, by_sym: float, bz_sym: float):
		pass

	def hf_setTLPOL(self,suffix: hwString , color: int, line_entity: Entity, flag_TL: int, flag_POL: int):
		pass

	def hf_setdiecomponent(self,name: hwString , color: int, collection: Collection):
		pass

	def hf_setdieline(self,collection: Collection, flag: int):
		pass

	def hf_setdiestampingdirection(self,x_coord: float, y_coord: float, z_coord: float, reserved: int):
		pass

	def hf_setdiesymmetry(self,normal_x: float, normal_y: float, normal_z: float, origin_x: float, origin_y: float, origin_z: float, shape_flag: int, node_1: Entity, node_2: Entity):
		pass

	def hf_setformingdirection(self,x_coord: float, y_coord: float, z_coord: float, axisType: int =" 0"):
		pass

	def hf_setformingdirectionx(self,x: float, y: float, z: float):
		pass

	def hf_setpartcomponent(self,collection: Collection):
		pass

	def hf_setpartflangecomponent(self,suffix: hwString , color: int, collection: Collection, flag_FL: int, flag_part: int):
		pass

	def hf_trim_multi(self,collection: Collection, line_list: EntityList, vector: hwTriple, node_list: EntityList, trim_flag: int, reserved: float):
		pass

	def hfdeleteloadcol(self,loadcolname: hwString ):
		pass

	def hfsolverdeletedbset(self,db_setname: hwString ):
		pass

	def hiddenlinemethod(self,method: int):
		pass

	def hideall(self,*args, **kwargs):
		"""
		hideall(HMAPI self, hwStringList string_array=s_defaultStringList)
		"""
		pass

	def hideentity(self,entity: Entity, showcomps: bool  = False, elements_off: bool  = False, geometry_off: bool  = False):
		pass

	def hideentity_byname(self,entity_type: EntityFullType, entity_name: hwString , showcomps: bool  = False, elements_off: bool  = False, geometry_off: bool  = False):
		pass

	def hideentitybymark(self,*args, **kwargs):
		"""
		hideentitybymark(HMAPI self, CollectionSet collection_set, hwString const & showComps="", hwString const & refFlag="", hwString const & elementsOff="", hwString const & geometryOff="", hwString const & plotsOff="")
		"""
		pass

	def hideview(self,name: hwString , entity_type_id: int):
		pass

	def hm_ae_findattachmentsfromFEs(self,collection: Collection, select: bool ):
		pass

	def hm_ae_get_partson(self,attatchments: Collection):
		pass

	def hm_ae_getfe(self,id: int , entity_type: EntityFullType):
		pass

	def hm_ae_state(self,entity: Entity):
		pass

	def hm_answernext(self,*args, **kwargs):
		"""
		hm_answernext(HMAPI self, hwString const & answer="")
		"""
		pass

	def hm_attributeentitytype(self,entity_type: EntityFullType, entity_id: int , attribute_name_or_id: hwString ):
		pass

	def hm_attributeentitytype_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_name_or_id: hwString ):
		pass

	def hm_attributeidentifier(self,entity_type: EntityFullType, entity_id: int , attribute_name_or_id: hwString ):
		pass

	def hm_attributeidentifier_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_name_or_id: hwString ):
		pass

	def hm_attributeidfromname(self,attribute_name: hwString ):
		pass

	def hm_attributeindexentitytype(self,entity_type: EntityFullType, entity_id: var0 , attribute_index: int ):
		pass

	def hm_attributeindexentitytype_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_index: int ):
		pass

	def hm_attributeindexentitytypename(self,entity_type: EntityFullType, entity_id: var0 , attribute_index: int ):
		pass

	def hm_attributeindexentitytypename_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_index: int ):
		pass

	def hm_attributeindexidentifier(self,entity_type: EntityFullType, entity_id: var0 , attribute_index: int ):
		pass

	def hm_attributeindexidentifier_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_index: int ):
		pass

	def hm_attributeindexsolver(self,entity_type: EntityFullType, entity_id: var0 , attribute_index: int ):
		pass

	def hm_attributeindexsolver_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_index: int ):
		pass

	def hm_attributeindexstatus(self,entity_type: EntityFullType, entity_id: var0 , attribute_index: int ):
		pass

	def hm_attributeindexstatus_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_index: int ):
		pass

	def hm_attributeindextype(self,entity_type: EntityFullType, entity_id: var0 , attribute_index: int ):
		pass

	def hm_attributeindextype_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_index: int ):
		pass

	def hm_attributeindextypename(self,entity_type: EntityFullType, entity_id: var0 , attribute_index: int ):
		pass

	def hm_attributeindextypename_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_index: int ):
		pass

	def hm_attributelist(self,entity_type: EntityFullType, entity_id: var0 , value: hwString ):
		pass

	def hm_attributelist_byentityname(self,entity_type: EntityFullType, entity_name: hwString , value: hwString ):
		pass

	def hm_attributelistall(self,value: hwString ):
		pass

	def hm_attributenamefromid(self,attribute_id: int ):
		pass

	def hm_attributereferencecount_byentity(self,entity: Entity):
		pass

	def hm_attributereferencecount_byentityname(self,entity_type: EntityFullType, entity_name: hwString ):
		pass

	def hm_attributesolverarrayvalues_byentityid(self,entity_id: Entity, attribute_id: int , extend_search: int  =" 0"):
		pass

	def hm_attributesolverarrayvalues_byentityname(self,entity_type: EntityFullType, entity_name: hwString , attribute_name: hwString ):
		pass

	def hm_attributetype(self,attribute_id: int ):
		pass

	def hm_attributetype_byentityname(self,attribute_name: hwString ):
		pass

	def hm_attributetypename(self,attribute_id: int ):
		pass

	def hm_attributetypename_byentityname(self,attribute_name: hwString ):
		pass

	def hm_batchexportenginefile(self,type: int , filename: hwString , export_template: hwString ):
		pass

	def hm_blockbrowserupdate(self,mode: int ):
		pass

	def hm_cardassignedtoentity(self,entities: Collection):
		pass

	def hm_ce_checkprojection(self,ce_collection: Collection, tolerance: float ):
		pass

	def hm_ce_close_mcf(self):
		pass

	def hm_ce_datalist(self,ce_collection: Collection):
		pass

	def hm_ce_errorreport(self,connector: Entity, report_type: int ):
		pass

	def hm_ce_findduplicates(self,tolerance: float , connectors: Collection, location_type: hwString ):
		pass

	def hm_ce_generatenamefrominclude(self,connector_entity: Entity, base_name: hwString ):
		pass

	def hm_ce_generatenamefromsubsystem(self,connector: Entity, base_name: hwString ):
		pass

	def hm_ce_getconfigfromconnectorcontrol(self,entity_type: EntityFullType, name: hwString ):
		pass

	def hm_ce_getconnectorcontrollist(self,solver: hwString , style: hwString , option: int ):
		pass

	def hm_ce_getdefaultconnectorcontrolfromconfig(self,solver: hwString , style: hwString , feconfig: hwString ):
		pass

	def hm_ce_gethmholes(self,collection: Collection, upbound: float , lowbound: float , outerFlag: int , elementFlag: int , reserved: int  =" 0"):
		pass

	def hm_ce_getlinkentities(self,connector_entity: Entity, ent_type: EntityFullType):
		pass

	def hm_ce_getprojectiondata(self,collection1: Collection, collection2: Collection, numproj: int , tolerance: float , order: int , output: int , projFlag: int , projFlag2: int ):
		pass

	def hm_ce_linkprojectionorderget_bycollection(self,collection: Collection, option: var0 ):
		pass

	def hm_ce_linkprojectionorderget_byentity(self,entity: Entity, option: var0 ):
		pass

	def hm_ce_read_mcf(self,mcfName: hwString ):
		pass

	def hm_ce_tooclosetoedgecheck(self,collection1: Collection, collection2: Collection, distance: float , feature_angle: float , edge_option: int , auto_fix: int ):
		pass

	def hm_clearmarker(self,*args, **kwargs):
		"""
		hm_clearmarker(HMAPI self, EntityFullType entity_type=hwDescriptor::EntityFullType((unsigned int)0))
		"""
		pass

	def hm_clearmarker_bycollection(self,*args, **kwargs):
		"""
		hm_clearmarker_bycollection(HMAPI self, Collection collection, hwString const & dataname="")
		"""
		pass

	def hm_clearmarker_byentity(self,*args, **kwargs):
		"""
		hm_clearmarker_byentity(HMAPI self, Entity entity, hwString const & dataname="")
		"""
		pass

	def hm_clearshape(self,*args, **kwargs):
		"""
		hm_clearshape(HMAPI self, EntityFullType entity_type=hwDescriptor::EntityFullType((unsigned int)0))
		"""
		pass

	def hm_clearshape_bycollection(self,*args, **kwargs):
		"""
		hm_clearshape_bycollection(HMAPI self, Collection collection, hwString const & shape="")
		"""
		pass

	def hm_clearshape_byentity(self,*args, **kwargs):
		"""
		hm_clearshape_byentity(HMAPI self, Entity entity, hwString const & shape="")
		"""
		pass

	def hm_collisioncheck(self,*args, **kwargs):
		"""
		hm_collisioncheck(HMAPI self, Collection intersected_elements=s_defaultCollection, Collection penetrated_elements=s_defaultCollection, Collection intersected_surfaces=s_defaultCollection, Collection penetrated_surfaces=s_defaultCollection, Collection penetrated_nodes=s_defaultCollection, bool const self_check=False, int const reserved1=0, double const pair_angle=90.000000, bool const store_segments=False, int const mark_adjoining=0, double const topo_feature_angle=0.000000, bool const pair_results=False)
		"""
		pass

	def hm_collisionend(self):
		pass

	def hm_collisionentitycreate(self,collection: Collection, dimension: int , thickness_type: int , thickness: float , edge_penetration: int , midside_nodes: int , split_quads: int , used_topology: int , grouping_identifier: bool , offset: int ):
		pass

	def hm_collisiongetcomponententitypair(self,collision_type: int , component_index: int , entity_index: int , include_ignored: bool  = False):
		pass

	def hm_collisiongetcomponententitypaircount(self,collision_type: int , component_index: int , include_ignored: bool  = False):
		pass

	def hm_collisiongetcomponentlinesegment(self,component_index: int , linesegment_index: int , include_ignored: bool  = False):
		pass

	def hm_collisiongetcomponentlinesegmentcount(self,comp_index: int , include_ignored: bool  = False):
		pass

	def hm_collisiongetcomponentpair(self,collisionType: int , componentIndex: int , includeIgnored: bool  = False):
		pass

	def hm_collisiongetcomponentpaircount(self,collisionType: int , includeIgnored: bool  = False):
		pass

	def hm_collisiongetconfig(self,options: hwStringList):
		pass

	def hm_collisioninit(self,config: int  =" 0", tolerance: float  =" 0_module.0", allowable_depth: float  =" 0_module.0", min_overlap: float  =" 0_module.0"):
		pass

	def hm_collisionvisualizebymark(self,mark_collection: Collection, node_collection: Collection, review_type: int , fit_view: bool , display_type: int ):
		pass

	def hm_collisionwriteresultsfile(self,filename: hwString , include_ignored: bool  = False):
		pass

	def hm_compareend(self):
		pass

	def hm_compareentities(self,source_surfaces: Collection, target_surfaces: Collection, tolerance: float , result_type: int  = 1, review_results: bool  = True):
		pass

	def hm_compareentitiesposition(self,source_entities: Collection, target_entities: Collection, tolerance: float , n1_source: Entity, n2_source: Entity, n3_source: Entity, n1_target: Entity, n2_target: Entity, n3_target: Entity, result_type: int  = 1, review_results: bool  = True):
		pass

	def hm_compareentitiesrecursive(self,source_surfaces: Collection, target_surfaces: Collection, tolerance: float , result_type: int  = 1, review_results: bool  = True):
		pass

	def hm_compareentitiesrotate(self,source_entities: Collection, target_entities: Collection, tolerance: float , vec_x: float , vec_y: float , vec_z: float , base_x: float , base_y: float , base_z: float , angle: float , steps: int , result_type: int  = 1, review_results: bool  = False):
		pass

	def hm_compareentitiessameside(self,source_entities: Collection, target_entities: Collection, tolerance: float , result_type: int  =" 0", review_results: bool  = False):
		pass

	def hm_compareentitiessymmetry(self,source_entities: Collection, target_entities: Collection, tolerance: float , normal_x: float , normal_y: float , normal_z: float , base_x: float , base_y: float , base_z: float , result_type: int  = 1, review_results: bool  = True):
		pass

	def hm_compareentitiestranslate(self,source_entities: Collection, target_entities: Collection, tolerance: float , vec_x: float , vec_y: float , vec_z: float , distance: float , steps: int , result_type: int  = 1, review_results: bool  = True):
		pass

	def hm_comparefinddistances(self,max_distance: float , review_results: bool  = True):
		pass

	def hm_comparegetarea(self,max_distance: float , review_results: bool  = True):
		pass

	def hm_comparegetcomparea(self,match_type: int , match_location: int , component_id: int  =" 0", transformation_index: int  =" 0"):
		pass

	def hm_comparegetdistance(self,distance_index: int ):
		pass

	def hm_comparegetdistancecount(self):
		pass

	def hm_comparegetdistanceentityid(self,distance_index: int ):
		pass

	def hm_comparegetdistanceentitytype(self,distance_index: int ):
		pass

	def hm_comparegetdistancetransformid(self,distance_index: int ):
		pass

	def hm_comparegettransformationcount(self):
		pass

	def hm_comparegettransformationmatchcount(self,transformation_index: int ):
		pass

	def hm_comparegettransformationmatchentities(self,transformation_index: int , match_index: int , match_location: int ):
		pass

	def hm_comparegettransformationmatchentitycount(self,transformation_index: int , match_index: int , match_location: int ):
		pass

	def hm_comparegettransformationmatchentitytype(self,transformation_index: int , match_index: int , match_location: int ):
		pass

	def hm_comparegettransformationmatchstate(self,transformation_index: int , match_index: int ):
		pass

	def hm_comparegettransformationmatchtype(self,transformation_index: int , match_index: int ):
		pass

	def hm_comparegettransformationmatrix(self,transformation_index: int ):
		pass

	def hm_compareinit(self):
		pass

	def hm_comparereadfile(self,filename: hwString , overwrite: bool ):
		pass

	def hm_comparesetanalysismode(self,mode: int  =" 0"):
		pass

	def hm_comparesetelemsurfmode(self,mode: int  =" 0"):
		pass

	def hm_comparesetflags(self,flag: int  =" 0"):
		pass

	def hm_comparesetignoreholes(self,mode: int  =" 0", diameter: float  =" 0_module.0", length: float  =" 0_module.0"):
		pass

	def hm_comparesetrefacetmode(self,*args, **kwargs):
		"""
		hm_comparesetrefacetmode(HMAPI self, int const mode, double const max_size=DBL_MAX, double const max_angle=DBL_MAX)
		"""
		pass

	def hm_comparesetreview(self,type: int , min_legend: float  =" 0_module.0", max_legend: float  =" 0_module.0"):
		pass

	def hm_comparesetreviewcolor(self,match_type: int , match_location: int , color: int ):
		pass

	def hm_comparesetreviewcolordefault(self):
		pass

	def hm_comparesetreviewmode(self,mode: int  =" 0"):
		pass

	def hm_comparesetreviewtypes(self,match_types: hwIntList):
		pass

	def hm_comparesettransparentmode(self,mode: int , color: int  =" 0"):
		pass

	def hm_comparewritefile(self,filename: hwString ):
		pass

	def hm_comparewritepairedcomps(self,filename: hwString , match_type: int ):
		pass

	def hm_comparewriteresults(self,filename: hwString , source_component_id: int  =" 0", target_component_id: int  =" 0"):
		pass

	def hm_controlcardattributedefined(self,cardName: hwString , attribute: hwString ):
		pass

	def hm_convertFromOutFileToDatFile(self,file_name: hwString ):
		pass

	def hm_convertmarktorange(self,collection: Collection):
		pass

	def hm_defaultstatus_byentity(self,entity: Entity, attribute_name: hwString ):
		pass

	def hm_defaultstatus_byname(self,entity: EntityFullType, entityName: hwString , attributeName: hwString ):
		pass

	def hm_detectmeshpatterns(self,input_collection: Collection, output_collection: Collection, define_topology_by_1d: int  = 1, detect_singularity: int  = 1, smoothness: int  = 1, threshold_index: float  =" 0_module.5", tria_cluster: int  = 1, tria_on_edge: int  = 1):
		pass

	def hm_detectselfsymmetry(self,collection: Collection):
		pass

	def hm_diffencodings(self,encodings1: hwString , encodings2: hwString , encoding_algorithm: int  =" 0", sphhar_bandwidth: int  = 16, sphhar_falloff: float  =" 2_module.828427", sphhar_radii: int  = 32, sphhar_resolution: int  = 64):
		pass

	def hm_editcard(self,*args, **kwargs):
		"""
		hm_editcard(HMAPI self, Collection collection, int const config=0, int const type=0, hwString const & card_image="")
		"""
		pass

	def hm_edittextcard(self,card: Entity):
		pass

	def hm_encodeshape(self,entity_collection: Collection, encoding_algorithm: int  =" 0", sphhar_bandwidth: int  = 16, sphhar_falloff: float  =" 2_module.828427", sphhar_radii: int  = 32, sphhar_resolution: int  = 64):
		pass

	def hm_entityincollector_byentity(self,collector_entity: Entity, entity_type: EntityFullType, config_num: int , type_num: int ):
		pass

	def hm_entityincollector_byname(self,collector: EntityFullType, collector_name: hwString , entity_type: EntityFullType, config_num: int , type_num: int ):
		pass

	def hm_entityisdirty(self,*args, **kwargs):
		"""
		hm_entityisdirty(HMAPI self, Entity entity, hwString const & dirtinessAspect="dirty_for_export")
		"""
		pass

	def hm_entitylist(self,*args, **kwargs):
		"""
		hm_entitylist(HMAPI self, EntityFullType entity, hwString const & listType, hwString const & mode="active")
		"""
		pass

	def hm_entitymaxid(self,entity_type: EntityFullType, recalculate: int  = 1):
		pass

	def hm_entitymaxsolverid(self,*args, **kwargs):
		"""
		hm_entitymaxsolverid(HMAPI self, EntityFullType entity_type, hwString const & id_pool_name="")
		"""
		pass

	def hm_entityminid(self,entity_type: EntityFullType, recalculate: int  = 1):
		pass

	def hm_entityminsolverid(self,*args, **kwargs):
		"""
		hm_entityminsolverid(HMAPI self, EntityFullType entity_type, hwString const & id_pool_name="")
		"""
		pass

	def hm_entityrecorder(self,entity_type: EntityFullType, option: hwString ):
		pass

	def hm_entityrecorder_switch(self,entity_type: EntityFullType, option: hwString ):
		pass

	def hm_estimategeomthicknesslimits(self,entityCollection: Collection, elemSize: float  =" 0_module.0"):
		pass

	def hm_exportdummytargetpointstocsv(self,designPoints: Collection, file_path: hwString ):
		pass

	def hm_exportentitydefaults(self):
		pass

	def hm_exportidmgr(self,filename: hwString , format: int  =" 0", option: int  =" 0"):
		pass

	def hm_exportoptimizationcards(self,type: int , filename: hwString , export_template: hwString ):
		pass

	def hm_exportplyorientation(self,plysCollection: Collection, filename: hwString ):
		pass

	def hm_fbdplot(self,plot_type: hwString , collection: Collection, subcase_ids: hwTripleIList, resultid: Entity, absolute: var0  =" 0", arrlen: float  =" 25_module.0", arroworigin: int  =" 0", colorfx: int  = 3, colorfy: int  = 4, colorfz: int  = 5, colormx: int  = 3, colormy: int  = 4, colormz: int  = 5, declim: int  = 2, envelope: bool  = False, fx: bool  = False, fy: bool  = False, fz: bool  = False, gpf: int  =" 0", midarrow: bool  = False, minmax: int  =" 0", mx: bool  = False, my: bool  = False, mz: bool  = False, normalload: bool  = False, onelems: bool  = False, onenodes: bool  = False, plotdir: int  =" 0", scientific: bool  = False, showvalue: bool  = False, sizescale: int  =" 0", tangentialload: bool  = False, tolerance: float  = 1e-05, vecstyle: int  =" 0"):
		pass

	def hm_fbdplot_clear(self):
		pass

	def hm_fe_getWvsTfile(self,connector: Entity):
		pass

	def hm_fe_getconfigfile(self):
		pass

	def hm_fe_getdiameter(self):
		pass

	def hm_fe_getdvstfile(self,connector: Entity):
		pass

	def hm_fe_setWvsTfile(self,connector: Entity, wvstfile: hwString ):
		pass

	def hm_fe_setconfigfile(self,configfile: hwString ):
		pass

	def hm_fe_setdvstfile(self,connector: Entity, dvstfile: hwString ):
		pass

	def hm_findadvancedselectiongroups(self,*args, **kwargs):
		"""
		hm_findadvancedselectiongroups(HMAPI self, Collection collection, hwString const & method="by attached", double const angle=DBL_MAX)
		"""
		pass

	def hm_findclosestpointonline(self,x: float , y: float , z: float , line: Entity, return_type: int  =" 0"):
		pass

	def hm_findclosestpointonsurface(self,x: float , y: float , z: float , surface: Entity):
		pass

	def hm_findconnectedpatches(self,collection: Collection):
		pass

	def hm_finddeviation(self,source_collection: Collection, target_collection: Collection, tolerance_value: float ):
		pass

	def hm_findnarrowsurfaces(self,collection: Collection, width_threshold: float , output_surfs_flag: int  =" 0", sharp_angle_threshold: float  =" 10_module.0", reserved: int  =" 0"):
		pass

	def hm_findpolygonselection(self,elements: EntityList):
		pass

	def hm_findprojected(self,*args, **kwargs):
		"""
		hm_findprojected(HMAPI self, Collection project_collection, Collection target_collection, int const use_actual_thickness, double const thickness, double const tolerance, int const project_normal, double const project_x, double const project_y, double const project_z, int const mark_target, CollectionSet output_collection, bool const plot_results=False, int const legend_red=0, int const legend_yellow=0, hwString const & results_file="", hwString const & output_file="")
		"""
		pass

	def hm_findtangentpointoncircle(self,px: float , py: float , pz: float , cx: float , cy: float , cz: float , cnx: float , cny: float , cnz: float , radius: float ):
		pass

	def hm_findthinsolidproximity(self,solidCollection: Collection):
		pass

	def hm_flangedetectionend(self):
		pass

	def hm_flangedetectionfindflanges(self,find: int ):
		pass

	def hm_flangedetectionfindmates(self,max_search_dist: float , min_search_dist: float , mode: int  =" 0", percent_mate_area_tol: float  =" 0_module.1", search_scope: int  =" 0"):
		pass

	def hm_flangedetectiongetflangedetails(self,index: int ):
		pass

	def hm_flangedetectiongetflangemates(self,index: int ):
		pass

	def hm_flangedetectiongetflangemidline(self,index: int , offset_distance: float , max_chordal_deviation: float  =" 0_module.1"):
		pass

	def hm_flangedetectiongetmatingentities(self,index1: int , index2: int ):
		pass

	def hm_flangedetectiongetmatinggroupdetails(self,index: int ):
		pass

	def hm_flangedetectiongetnumberofflanges(self):
		pass

	def hm_flangedetectiongetnumberofmatinggroups(self):
		pass

	def hm_flangedetectioninit(self,*args, **kwargs):
		"""
		hm_flangedetectioninit(HMAPI self, Collection collection, int const consider_geom=INT_MAX)
		"""
		pass

	def hm_flangedetectionsetparams(self,*args, **kwargs):
		"""
		hm_flangedetectionsetparams(HMAPI self, double const max_width, double const min_width=0.000000, double const feature_angle=DBL_MAX)
		"""
		pass

	def hm_formnodelistsfrommark(self,*args, **kwargs):
		"""
		hm_formnodelistsfrommark(HMAPI self, Collection collection, Collection error_collection=s_defaultCollection, unsigned int const use_edge_topo=1)
		"""
		pass

	def hm_geomfindsymmetry(self,*args, **kwargs):
		"""
		hm_geomfindsymmetry(HMAPI self, Collection collection1, Collection collection2, double const tolerance=0.000000, hwMatrix44 transformation=hwMatrix44(1.0))
		"""
		pass

	def hm_getactiveplotcontrol(self,plot_type: hwString ):
		pass

	def hm_getactivesimstep(self):
		pass

	def hm_getadjfacesfromface(self,face_id: int ):
		pass

	def hm_getadjsurfacesfromsurface(self,surface: Entity):
		pass

	def hm_getangle(self,entityType: EntityFullType, id1: var0 , id2: var0 , id3: var0 ):
		pass

	def hm_getareaofsurface(self,entity_id: Entity):
		pass

	def hm_getattachedsolidelemfaces(self,collection: Collection, normal_flag: int ):
		pass

	def hm_getaverageelemsize(self,elems_collection: Collection, panel_sensitive_deprecated: int  = 1, round_to: int  =" 0", size_mode: int  =" 0", limit_range_percent: float  =" 0_module.0"):
		pass

	def hm_getaxisymmetricvolumereduced(self,solids: Collection, elems: Collection, rotal_axis: hwTriple, reference_point: hwTriple, num_samples: int  = 1, result_per_elem: var0  = 1):
		pass

	def hm_getbestcirclecenter(self,entityCollection: Collection, anyTol: int  =" 0"):
		pass

	def hm_getboundingbox(self,entityCollection: Collection, entityFlag: int  =" 0", systemID: int  =" 0", boxType: int  =" 0"):
		pass

	def hm_getboundingbox_predefined(self,collection: Collection, predefined_cut: hwString , limit: float ):
		pass

	def hm_getcardimageoptions(self,entityType: EntityFullType, cardImage: hwString , option: hwString ):
		pass

	def hm_getcentroid(self,entityCollection: Collection):
		pass

	def hm_getclosestnode(self,*args, **kwargs):
		"""
		hm_getclosestnode(HMAPI self, double const x, double const y, double const z, Collection elemCollection=hwDescriptor::Collection(), Collection nodeCollection=hwDescriptor::Collection())
		"""
		pass

	def hm_getclosestpointsbetweenlinesurface(self,line: Entity, surf: Entity):
		pass

	def hm_getclosestpointsbetweentwolines(self,line1: Entity, line2: Entity):
		pass

	def hm_getcog(self,collection: Collection, reserved_1: int  =" 0", reserved_2: int  =" 0", lumpedmassflag: int  =" 0", system_id: int  =" 0"):
		pass

	def hm_getconfigtypecountincol_byentity(self,entity_type: EntityFullType, collector_entity: Entity):
		pass

	def hm_getconfigtypecountincol_byname(self,collector_type: EntityFullType, entity_type: EntityFullType, name: hwString ):
		pass

	def hm_getconfigtypeincol_byentity(self,collector: Entity, entity_type: EntityFullType):
		pass

	def hm_getconfigtypeincol_byname(self,collector: EntityFullType, entity: EntityFullType, name: hwString ):
		pass

	def hm_getcoordinatesfromnearestsurface(self,x: float , y: float , z: float , surfaceIDs: hwIntList):
		pass

	def hm_getcoordinatesofpointsonline(self,line: Entity, paramList: hwDoubleList):
		pass

	def hm_getcrossreferencedentities(self,*args, **kwargs):
		"""
		hm_getcrossreferencedentities(HMAPI self, Entity entity, int const reference_flag, CollectionSet outputCollection, int const string_array=0, int const number_of_strings=0, hwString const & search_type="-byid", int const exclude_regions=0)
		"""
		pass

	def hm_getcrossreferencedentities_byname(self,*args, **kwargs):
		"""
		hm_getcrossreferencedentities_byname(HMAPI self, EntityFullType entity_type, hwString const & entity_name, int const reference_flag, CollectionSet outputCollection, int const string_array=0, int const number_of_strings=0, hwString const & search_type="-byname", int const exclude_regions=0)
		"""
		pass

	def hm_getcrossreferencedentitiesmark(self,collection: Collection, reference_flag: int , outputCollection: CollectionSet, string_array: int  =" 0", number_of_strings: int  =" 0", exclude_regions: int  =" 0"):
		pass

	def hm_getcurrentframe(self):
		pass

	def hm_getcurrenttime(self):
		pass

	def hm_getcurrentview(self):
		pass

	def hm_getdatatypeaveraginglist(self,subcase_id: int , data_type_name: hwString ):
		pass

	def hm_getdatatypecomponents(self,subcase_id: int , data_type_name: hwString ):
		pass

	def hm_getdatatypelayers(self,subcase_id: var0 , data_type_name: hwString ):
		pass

	def hm_getdatatyperesolvedinlist(self,subcase_id: int , data_type_name: hwString ):
		pass

	def hm_getdefaultcardimage(self,entity_type: EntityFullType):
		pass

	def hm_getdiameterfromfile(self,thickness: float , dvstfile: hwString ):
		pass

	def hm_getdistance(self,entityType: EntityFullType, id1: var0 , id2: var0 , localCoordSystemId: var0 ):
		pass

	def hm_getdistancefromnearestline(self,points: hwDoubleList, lineList: hwIntList):
		pass

	def hm_getdistancefromnearestsurface(self,points: hwTriple, surf_ids: hwIntList):
		pass

	def hm_getduplicateelements(self,elements: Collection, outputCollection: Collection, options: int  =" 0"):
		pass

	def hm_getedgeloops(self,*args, **kwargs):
		"""
		hm_getedgeloops(HMAPI self, Collection collection, int const looptype=255, Collection surf_collection=hwDescriptor::Collection(), double const featureangle=0.000000, int const restricttoinput=0)
		"""
		pass

	def hm_getedgeloops2(self,collection: Collection, looptype: int  = 63):
		pass

	def hm_getedgesfromvertex(self,point: Entity):
		pass

	def hm_getelemcheckbounds(self,elements: Collection, dimension: int , check_type: hwString , time_failure: float  =" 0_module.0005"):
		pass

	def hm_getelemcheckelems(self,elementsCollection: Collection, dimension: int , check_type: hwString , check_mode: hwString , threshold: float  =" 0_module.0", tolerance: float  =" 0_module.0", time_failure: float  =" 0_module.005"):
		pass

	def hm_getelemcheckvalues(self,elements: Collection, dimension: int , check_type: hwString , time_failure: float  =" 0_module.0005"):
		pass

	def hm_getelementcheckmethod(self,check_name: hwString , get_method_mode: int  = 2):
		pass

	def hm_getelementchecksettings(self):
		pass

	def hm_getelementnormal(self,elementID: int , queryType: hwString , queryIndex: int ):
		pass

	def hm_getelementsqualityinfo(self,*args, **kwargs):
		"""
		hm_getelementsqualityinfo(HMAPI self, Collection elements, int const criteria_use_mode=1, Collection failedElements=s_defaultCollection)
		"""
		pass

	def hm_getentities_dirty(self,*args, **kwargs):
		"""
		hm_getentities_dirty(HMAPI self, EntityFullType entity_type, hwString const & dirtiness_aspect="dirty_for_export")
		"""
		pass

	def hm_getentityalias(self,entity_type: hwString ):
		pass

	def hm_getentitybasename(self,*args, **kwargs):
		"""
		hm_getentitybasename(HMAPIBase self, EntityFullType entity_type, int const style=INT_MAX)
		"""
		pass

	def hm_getentitycardimagedictionary(self,*args, **kwargs):
		"""
		hm_getentitycardimagedictionary(HMAPI self, EntityFullType entity_type, hwString const & type="")
		"""
		pass

	def hm_getentitycreationid(self,entity_type: EntityFullType, pool_id: int , entity: Entity):
		pass

	def hm_getentityname(self,entity_type_id: var0 , style: var0  =" 0"):
		pass

	def hm_getentityroot(self,entity_type_name: hwString ):
		pass

	def hm_getentitytype(self,entity_type: hwString ):
		pass

	def hm_getentitytypealiasname(self,entity_type: EntityFullType):
		pass

	def hm_getentitytypedictionary(self,entity_type: EntityFullType):
		pass

	def hm_getentitytypedisplayname(self,EntityTypeName: hwString , singular: var0  = 1):
		pass

	def hm_getentitytypes(self,option: hwString ):
		pass

	def hm_getexistingentitytypes(self):
		pass

	def hm_getfacesbyarea(self,area: float ):
		pass

	def hm_getfacesbyedgelength(self,length: float ):
		pass

	def hm_getfacesfromedge(self,line: Entity):
		pass

	def hm_getfacesfromsurface(self,surface: Entity):
		pass

	def hm_getfacesfromvertex(self,point: Entity):
		pass

	def hm_getfilletfaces(self,radius_min: float , radius_max: float ):
		pass

	def hm_getfilletfaces_fromcollection(self,entities: Collection, min_radius: float , max_radius: float ):
		pass

	def hm_getfilletfacesbyprofile(self,collection: Collection):
		pass

	def hm_getgeometricthinsolidinfo(self,*args, **kwargs):
		"""
		hm_getgeometricthinsolidinfo(HMAPI self, Collection collection, double const feature_angle=0.000000, double const max_thickness=0.000000, hwString const & mode="simple", double const thinsolid_ratio=0.500000)
		"""
		pass

	def hm_getgeomwithlargestitch(self,tolerance: float  =" -1_module.0"):
		pass

	def hm_getguientityname(self,entity_type_id: var0 ):
		pass

	def hm_gethistorylimit(self):
		pass

	def hm_gethistorymemorylimit(self):
		pass

	def hm_gethistorymemoryusage(self):
		pass

	def hm_gethmfileuserprofile(self,filename: hwString ):
		pass

	def hm_gethmfileversion(self,filename: hwString ):
		pass

	def hm_getidpools(self,*args, **kwargs):
		"""
		hm_getidpools(HMAPI self, EntityFullType entity_type, hwString const & return_type="id")
		"""
		pass

	def hm_getidpoolsforidrange(self,entity_type: EntityFullType, solver_id_range: hwString ):
		pass

	def hm_getincludeisolationentitiesmark(self,comps_collection: Collection, output_collection_set: CollectionSet, isolate_special: bool , reserved: bool ):
		pass

	def hm_getincludes(self,*args, **kwargs):
		"""
		hm_getincludes(HMAPIBase self, hwString const & mode="")
		"""
		pass

	def hm_getincludes_modified_since_last_export(self):
		pass

	def hm_getincludesentities_byids(self,include_ids: hwIntList, collection_set: CollectionSet):
		pass

	def hm_getincludesentities_bynames(self,include_names: hwStringList, collection_set: CollectionSet):
		pass

	def hm_getincrementalname(self,*args, **kwargs):
		"""
		hm_getincrementalname(HMAPIBase self, _EntityFullTypeList_vector entity_type_list, hwString const & base_name, int const start_num=-1, int const num_digits=0, hwString const & separator="")
		"""
		pass

	def hm_getinputoffsetid(self,entity_type: EntityFullType):
		pass

	def hm_getinternalid_bypoolid(self,id_pool: int , solver_id: int ):
		pass

	def hm_getinternalid_bypoolname(self,pool_name: hwString , solver_id: int ):
		pass

	def hm_getinternalidlist_bypoolid(self,id_pool: int , solver_id_list: hwIntList):
		pass

	def hm_getinternalidlist_bypoolname(self,pool_name: hwString , solver_id_list: hwIntList):
		pass

	def hm_getinternalname_bypoolid(self,id_pool: int , solver_name: hwString ):
		pass

	def hm_getinternalname_bypoolname(self,pool_name: hwString , solver_name: hwString ):
		pass

	def hm_getlinearclenpoint(self,line_entity: Entity, dist: float , x: float , y: float , z: float ):
		pass

	def hm_getlinelineangle(self,line_entity1: Entity, line_entity2: Entity, x: float , y: float , z: float ):
		pass

	def hm_getlinepointsatdistance(self,line: Entity, dist: float , x: float , y: float , z: float ):
		pass

	def hm_getlinetangentatcoordinate(self,line: Entity, x: float , y: float , z: float ):
		pass

	def hm_getloadplotstate(self):
		pass

	def hm_getlockedentities(self,entity_type: EntityFullType, data_name: hwString ):
		pass

	def hm_getmass(self,collection: Collection, mass_type: int  = 1):
		pass

	def hm_getmatching(self,*args, **kwargs):
		"""
		hm_getmatching(HMAPI self, Collection collection, hwString const & areaCalcMethod="ByLowestId", int const compareType=0, double const deformationTolerance=0.000000, int const encodingAlgorithm=0, double const matchingPercentThreshold=0.000000, Collection referenceCollection=hwDescriptor::Collection(), hwString const & searchMethod="ByArea", double const sphharBandwidth=16.000000, double const sphharFallof=2.828427, double const sphharRadii=32.000000, double const sphharResolution=64.000000)
		"""
		pass

	def hm_getmatrixdifference(self,matrix_1: hwDoubleList, matrix_2: hwDoubleList):
		pass

	def hm_getmaxgapwidth(self,entity_list1: EntityList, entity_list2: EntityList):
		pass

	def hm_getmemoryinfo(self):
		pass

	def hm_getmeshedgeparams(self,line: Entity):
		pass

	def hm_getmeshfaceparams(self,surface: Entity):
		pass

	def hm_getmeshvolumesinfo(self,collection: Collection, mode: int  =" 0"):
		pass

	def hm_getmethodinfo(self,type: hwString ):
		pass

	def hm_getmidsurfaceinfo(self,*args, **kwargs):
		"""
		hm_getmidsurfaceinfo(HMAPI self, hwString const & query_type, Collection input_collection, EntityFullType output_entity_type=hwDescriptor::EntityFullType((unsigned int)5))
		"""
		pass

	def hm_getmodelcheckcheckname(self,check_display_name: hwString ):
		pass

	def hm_getmodelcheckcheckresult(self,check_display_name: hwString ):
		pass

	def hm_getmodelcheckcheckstatus(self,check_display_name: hwString ):
		pass

	def hm_getmodelcheckconcernentityidresultentityid(self,display_name: hwString , contact_id: int ):
		pass

	def hm_getmodelcheckcorrectiondisplayname(self,check_display_name: hwString ):
		pass

	def hm_getmodelcheckcorrectionname(self,correction_display_name: hwString ):
		pass

	def hm_getmodelcheckcorrectvalue(self,correction_display_name: hwString ):
		pass

	def hm_getmodelcheckdefaultconfigfile(self,*args, **kwargs):
		"""
		hm_getmodelcheckdefaultconfigfile(HMAPI self, hwString const & profile="")
		"""
		pass

	def hm_getmodelcheckdisplaynames(self,*args, **kwargs):
		"""
		hm_getmodelcheckdisplaynames(HMAPI self, hwString const & check_type="ALL", EntityFullType entity_type=hwDescriptor::EntityFullType((unsigned int)0))
		"""
		pass

	def hm_getmodelcheckenttype(self,display_name: hwString ):
		pass

	def hm_getmodelcheckfailedcount(self,check_name: hwString ):
		pass

	def hm_getmodelcheckresultentids(self,display_name: hwString ):
		pass

	def hm_getmodelchecksupportedentities(self):
		pass

	def hm_getmodelchkvaluelevellimitcriteriaattribute(self,display_name: hwString ):
		pass

	def hm_getmoi(self,*args, **kwargs):
		"""
		hm_getmoi(HMAPI self, Collection collection, int const location_flag=0, Entity node_entity=hwDescriptor::Entity(), int const axes_flag=0, int const system_id=0, int const reserved_1=0, int const reserved_2=0, int const reserved_3=0, int const reserved_4=0, int const lumpedmassflag=0)
		"""
		pass

	def hm_getmoiofsolid(self,*args, **kwargs):
		"""
		hm_getmoiofsolid(HMAPI self, Entity solid, double const density=DBL_MAX)
		"""
		pass

	def hm_getmultilevelreferenceentities(self,input_entities: Collection, output_entities: Collection):
		pass

	def hm_getnearbyentities(self,*args, **kwargs):
		"""
		hm_getnearbyentities(HMAPI self, Collection input_entity_collection, CollectionSet output_entity_collection, double const radius, _EntityFullTypeList_vector outputentitytypes=std::vector< hwDescriptor::EntityFullType >(), hwString const & nearby_search_method="sphere")
		"""
		pass

	def hm_getnodegeometry(self,*args, **kwargs):
		"""
		hm_getnodegeometry(HMAPI self, Entity node_entity, hwString const & geom_type="")
		"""
		pass

	def hm_getnodessharedbyothercomps(self,components: Collection, nodes: Collection, exclude: bool ):
		pass

	def hm_getoccupiedentitiesinrange(self,entity_type: EntityFullType, pool_id: int , range: hwString ):
		pass

	def hm_getorientation(self,*args, **kwargs):
		"""
		hm_getorientation(HMAPI self, Collection entityCollection, int const comparetype=0, hwString const & samplingFile="")
		"""
		pass

	def hm_getplanarfaces(self):
		pass

	def hm_getprincipalaxes(self,collection: Collection, location_flag: int  =" 0"):
		pass

	def hm_getprojceid(self,index: int ):
		pass

	def hm_getqephtimestep(self,name: hwString ):
		pass

	def hm_getqualitycriteriaelementsizeinfo(self,criteria_file: hwString , check_element_size: float  =" 0_module.0"):
		pass

	def hm_getqualitycriteriastatus(self,elementsize: float ):
		pass

	def hm_getredoactions(self):
		pass

	def hm_getreferencedentities(self,*args, **kwargs):
		"""
		hm_getreferencedentities(HMAPI self, Entity entity, int const reference_flag, Collection outputCollection, int const string_array=0, int const number_of_strings=0, hwString const & search_type="-byid", int const exclude_regions=0)
		"""
		pass

	def hm_getreferencedentities_byname(self,*args, **kwargs):
		"""
		hm_getreferencedentities_byname(HMAPI self, EntityFullType entity_type, hwString const & entity_name, int const reference_flag, CollectionSet outputCollectionSet, int const string_array=0, int const number_of_strings=0, hwString const & search_type="-byname", int const exclude_regions=0)
		"""
		pass

	def hm_getreferencedentitiesmark(self,collection: Collection, reference_flag: int , outputCollection: Collection, string_array: int  =" 0", number_of_strings: int  =" 0", exclude_regions: int  =" 0"):
		pass

	def hm_getreplacecomponentpairing(self,existing_component_collection: Collection, incoming_component_collection: Collection, pairing_mode: int ):
		pass

	def hm_getscreenvector(self,vector: hwString ):
		pass

	def hm_getshelloverlapinfo(self,source_collection: Collection, target_collection: Collection, maxproximitydistance: float ):
		pass

	def hm_getsketchdata(self,*args, **kwargs):
		"""
		hm_getsketchdata(HMAPI self, int const entity_id=0, hwString const & entity_type="none", int const id=0, hwString const & sketchdata="", hwString const & name="", hwString const & file_name="")
		"""
		pass

	def hm_getsketchlastcreated(self):
		pass

	def hm_getsolidboundsforsurfaces(self,surfaces: Collection, exclude_solids: int  = 1, find_baffles: int  =" 0"):
		pass

	def hm_getsolidsfromsurface(self,surface: Entity):
		pass

	def hm_getsolidshelloverlapinfo(self,source_collection: Collection, target_collection: Collection, maxproximitydistance: float ):
		pass

	def hm_getsolver(self,*args, **kwargs):
		"""
		hm_getsolver(HMAPI self, hwString const & value="name")
		"""
		pass

	def hm_getsolverfileprofilename(self,filename: hwString ):
		pass

	def hm_getsolverids_byentity(self,entity_list: EntityList, groupbypoolname: bool  = False):
		pass

	def hm_getsolverids_byname(self,entity_type: EntityFullType, entity_names: hwStringList, groupbypoolname: bool  = False):
		pass

	def hm_getsolverusessegmentsets(self):
		pass

	def hm_getsubcasedatatypes(self,subcase_id: int ):
		pass

	def hm_getsurfacecurvatureforedges(self,*args, **kwargs):
		"""
		hm_getsurfacecurvatureforedges(HMAPI self, hwString const & curv_method="by_chord", Collection collection=hwDescriptor::Collection(), double const min_edgepts_span=-1.000000, hwString const & offset="autodefined", hwString const & offset_method="in_surface", int const straight_edge_max_pts=0)
		"""
		pass

	def hm_getsurfaceedges(self,surface: Entity):
		pass

	def hm_getsurfacefromface(self,faceID: var0 ):
		pass

	def hm_getsurfacenormal(self,entity: Entity):
		pass

	def hm_getsurfacenormalatcoordinate(self,surface: Entity, x: float , y: float , z: float ):
		pass

	def hm_getsurfacesbyedgelength(self,length: float ):
		pass

	def hm_getsurfacesfromedge(self,line: Entity):
		pass

	def hm_getsurfacesfromsolid(self,*args, **kwargs):
		"""
		hm_getsurfacesfromsolid(HMAPI self, Entity solid, hwString const & type="all")
		"""
		pass

	def hm_getsurfacesfromvertex(self,point: Entity):
		pass

	def hm_getsurfacesurfaceangle(self,surf1: Entity, surf2: Entity, x: float , y: float , z: float ):
		pass

	def hm_getsurfacethicknessvalues_bycollection(self,collection: Collection, element_method: var0 , ambiguous_values: var0  =" 0"):
		pass

	def hm_getsurfacethicknessvaluesbyentity(self,entity: Entity):
		pass

	def hm_getsurfaceuvatcoordinate(self,surface_entity: Entity, x: float , y: float , z: float ):
		pass

	def hm_gettablecolumndata_byentity(self,table: Entity, column_id: int , eval_flag: bool  = False):
		pass

	def hm_gettablecolumndata_byname(self,table_name: hwString , column_id: int , eval_flag: bool  = False):
		pass

	def hm_gettgofpointsonline(self,line_entity: Entity, u_parameter_list: hwString ):
		pass

	def hm_gettiedentities(self,input_collection: Collection, output_collection: Collection, projection: int  = 1):
		pass

	def hm_gettotalcog(self):
		pass

	def hm_gettotalmass(self):
		pass

	def hm_gettotalmoi(self):
		pass

	def hm_gettypefromidpoolnumber(self,solvercode: int , poolnumber: int ):
		pass

	def hm_gettypesenabledfornamepools(self):
		pass

	def hm_gettypeswithunresolvedids(self):
		pass

	def hm_getundoactions(self):
		pass

	def hm_getunmeshedsurfstomark(self,inputSurfCollection: Collection, outputSurfCollection: Collection):
		pass

	def hm_getunoffsetablenodes(self,collection: Collection, angle_threshold: float ):
		pass

	def hm_getunresolvedidcrossreferences(self,entity: Entity, id_pool_id: var0  =" 0"):
		pass

	def hm_getunresolvedids(self,entity_type: EntityFullType, id_pool_id: int  =" 0"):
		pass

	def hm_getunusedoremptyentities_bycollection(self,mode: hwString , outputCollection: CollectionSet, inputCollection: Collection):
		pass

	def hm_getunusedoremptyentities_byentity(self,mode: hwString , outputCollection: CollectionSet, entity: Entity):
		pass

	def hm_getunusedoremptyentities_byname(self,mode: hwString , outputCollection: CollectionSet, type: EntityFullType, name: hwString ):
		pass

	def hm_getunusedoremptyentities_forall(self,mode: hwString , outputCollection: CollectionSet):
		pass

	def hm_getuvbounds(self,surface: Entity, scalar: bool  = False):
		pass

	def hm_getuvcoordinates(self,surface_entity: Entity, node_entity: Entity, scaled: int  =" 0"):
		pass

	def hm_getuvvectors_bynode(self,surf_entity: Entity, node_entity: Entity, scaled: int  =" 0"):
		pass

	def hm_getuvvectors_bypoint(self,surf_entity: Entity, point_entity: Entity, scaled: int  =" 0"):
		pass

	def hm_getuvvectors_byxyz(self,surf_entity: Entity, xyz: hwTriple, scaled: int  =" 0"):
		pass

	def hm_getverticesfromedge(self,line: Entity):
		pass

	def hm_highlightlist(self,list: EntityList, highlight: hwString , panel_sensitive: var0  =" 0"):
		pass

	def hm_highlightmark(self,collection: Collection, highlight: hwString , panelSensitive: int  =" 0"):
		pass

	def hm_holedetectionend(self):
		pass

	def hm_holedetectionfindholes(self,find: int ):
		pass

	def hm_holedetectionfindmates(self,*args, **kwargs):
		"""
		hm_holedetectionfindmates(HMAPI self, double const max_angle=1.000000, double const max_distance=10.000000, double const max_lateral_distance=1.000000, double const max_lateral_factor=DBL_MAX, int const allow_hole_to_tube=0, int const allow_mismatched_shapes=0, int const allow_self=0)
		"""
		pass

	def hm_holedetectiongetholedetailsdata(self,index: int , query_key: hwString ):
		pass

	def hm_holedetectiongetmatedetails(self,index: int ):
		pass

	def hm_holedetectiongetnumberofholes(self):
		pass

	def hm_holedetectiongetnumberofmates(self):
		pass

	def hm_holedetectiongetwasherelementslist(self,index: int ):
		pass

	def hm_holedetectionidentifyhole(self,id: int ):
		pass

	def hm_holedetectioninit(self):
		pass

	def hm_holedetectionsetentities(self,collection: Collection):
		pass

	def hm_holedetectionsetholeparams(self,hole_shape: int , hole_type: int  =" 0", min_planar_dim: float  =" 0_module.0", max_planar_dim: float  =" 0_module.0", max_big_planar_dim: float  =" 0_module.0", max_offset_plane_dev: float  =" 0_module.0", max_geom_dev_percent: float  =" 0_module.0", max_smooth_edge_angle: float  =" -1_module.0", max_geom_dev_abs: float  =" -1_module.0", max_geom_angle_dev_abs: float  =" -1_module.0", max_straightness_dev_percent: float  =" -1_module.0", max_avg_adj_surf_angle: float  =" 0_module.0", max_geom_dist: float  =" 0_module.0", break_angle: float  =" 0_module.0", inspect_non_manifold_loops: float  =" 0_module.0"):
		pass

	def hm_holedetectionsettubeparams(self,tube_shape: int , tube_type: int , feature_angle: float  =" 0_module.0", max_geom_dev_percent: float  =" -1_module.0", max_height: float  =" 0_module.0", max_offset_angle: float  =" 0_module.0", max_offset_plane_dev: float  =" 0_module.0", max_planar_dim: float  =" 0_module.0", max_smooth_edge_angle: float  =" -1_module.0", merge_connected_barrels: int  = 1, min_cone_angle: float  =" 0_module.0", min_planar_dim: float  =" 0_module.0", min_height: float  =" 0_module.0"):
		pass

	def hm_includeisdirty(self,*args, **kwargs):
		"""
		hm_includeisdirty(HMAPI self, unsigned int const includeId, hwString const & dirtinessAspect="dirty_for_export")
		"""
		pass

	def hm_intersectlineline(self,segment1Start: hwTriple, segment1End: hwTriple, segment2Start: hwTriple, segment2End: hwTriple):
		pass

	def hm_is_dirtiness_detection_enabled_for_entitytype(self,entity_type: hwString ):
		pass

	def hm_is_dirtiness_detection_enabled_for_includes(self):
		pass

	def hm_isentitydatanameparameterized(self,entity: Entity, data_name_or_attribute: hwString , row: int  = -1, column: int  = -1):
		pass

	def hm_isentitydatanameparameterized_byentity(self,entity: Entity, attribute_id: int , row: int  = -1, column: int  = -1):
		pass

	def hm_isentitysupportedforaction(self,entity_type: EntityFullType, action: hwString ):
		pass

	def hm_ispointinsidesolid(self,x: float , y: float , z: float , solidEntity: Entity):
		pass

	def hm_ispointinsidesolidelem(self,x: float , y: float , z: float , element: Entity):
		pass

	def hm_issurfacemappable(self,surface: Entity, element_size: float ):
		pass

	def hm_istextcard(self,entity: Entity):
		pass

	def hm_latestentityid(self,entity_type: EntityFullType, num: int  =" 0"):
		pass

	def hm_linegetorderelems(self,lineCollection: Collection, tolerance: float  =" -1_module.0"):
		pass

	def hm_linegetordernodes(self,lines: Collection, tolerance: float  =" -1_module.0"):
		pass

	def hm_mapelementstoplane(self,collection_id: Collection):
		pass

	def hm_markbyfeature(self,input_collection: CollectionSet, output_collection: CollectionSet, feature_mode: int , min_radius: float  =" 0_module.0", max_radius: float  =" 0_module.0", internal_only: int  =" 0", closed_cylinder: int  =" 0", valve_output: int  = 1):
		pass

	def hm_me_childrenget(self,id: int ):
		pass

	def hm_me_entitiesall(self,id: int ):
		pass

	def hm_me_entitiesget(self,module_id: int , search_entity_type: EntityFullType):
		pass

	def hm_me_moduleget(self,entity_id: Entity):
		pass

	def hm_me_modulesgetFromUid(self,uid: hwString ):
		pass

	def hm_me_occrepkeyget(self,part: Entity):
		pass

	def hm_me_parentsget(self,moduledID: int ):
		pass

	def hm_me_protoreplistget(self,*args, **kwargs):
		"""
		hm_me_protoreplistget(HMAPI self, unsigned int const prototypeID, hwString const & repType="")
		"""
		pass

	def hm_me_protoreptypeget(self,prototypeID: var0 , repKey: hwString ):
		pass

	def hm_me_repdetailget(self,moduleID: var0 , repKey: hwString , metadataAttributeName: hwString ):
		pass

	def hm_me_repfiledataget(self,moduleID: var0 , repKey: hwString ):
		pass

	def hm_me_rootget(self):
		pass

	def hm_measureshortestdistance(self,entityCollection1: Collection, reserved1: int , entityCollection2: Collection, reserved2: int , systemID: int ):
		pass

	def hm_measureshortestdistance2(self,x: float , y: float , z: float , entity: Collection, reserved: int , systemCoord: int ):
		pass

	def hm_metadata_all(self):
		pass

	def hm_metadata_bycollection(self,collection: Collection):
		pass

	def hm_metadata_byentitytype(self,entity_type: EntityFullType):
		pass

	def hm_metadata_byname(self,*args, **kwargs):
		"""
		hm_metadata_byname(HMAPI self, hwString const & name, EntityFullType entity_type=hwDescriptor::EntityFullType((unsigned int)0))
		"""
		pass

	def hm_modelcheckneedscorrection(self,check_display_name: hwString ):
		pass

	def hm_modelchecksavetoxml(self,filename: hwString ):
		pass

	def hm_modent_getchildren(self,entity: Entity, outputModules: Collection, recursive: bool ):
		pass

	def hm_modent_getconstraintruleoptions(self):
		pass

	def hm_morph_getdomainangle(self,*args, **kwargs):
		"""
		hm_morph_getdomainangle(HMAPI self, Entity domain1, Entity domain2, double const x=DBL_MAX, double const y=DBL_MAX, double const z=DBL_MAX)
		"""
		pass

	def hm_morph_getdomainarcangle_bybaseandaxis(self,domainID: Entity, base: hwTriple, axis: hwTriple):
		pass

	def hm_morph_getdomainarcangle_byentity(self,*args, **kwargs):
		"""
		hm_morph_getdomainarcangle_byentity(HMAPIBase self, Entity domain, Entity line_or_node_entity=hwDescriptor::Entity())
		"""
		pass

	def hm_morph_getdomainlength(self,*args, **kwargs):
		"""
		hm_morph_getdomainlength(HMAPI self, Entity domain, double const x=DBL_MAX, double const y=DBL_MAX, double const z=DBL_MAX)
		"""
		pass

	def hm_morph_getdomainradius_bybaseandaxis(self,domain: Entity, base: hwTriple, axis: hwTriple):
		pass

	def hm_morph_getdomainradius_byentity(self,*args, **kwargs):
		"""
		hm_morph_getdomainradius_byentity(HMAPIBase self, Entity domain, Entity line_or_node_entity=hwDescriptor::Entity())
		"""
		pass

	def hm_morph_gethandledomains(self,handle: Entity):
		pass

	def hm_morph_gethandlenode(self,handle: Entity):
		pass

	def hm_morph_getinfo_domaincount(self,domain_type: int ):
		pass

	def hm_morph_getinfo_excludedelements_list(self,keywordList: hwString ):
		pass

	def hm_morph_getinfo_excludedelements_mark(self,keyword1: hwString , collection: Collection):
		pass

	def hm_morph_getinfo_parameter(self,parameter_name: hwString ):
		pass

	def hm_morph_getinfo_testlimits(self,elem_type: int , test_id: int ):
		pass

	def hm_morph_getinfo_undolist(self,option: hwString ):
		pass

	def hm_morph_getmvoledge(self,node1: Entity, node2: Entity):
		pass

	def hm_morph_getmvoledgenodes(self,edge_id: int ):
		pass

	def hm_morph_getmvolface(self,mvol: Entity, node1: Entity, node2: Entity, node3: Entity):
		pass

	def hm_morph_getnodehandle(self,node: Entity):
		pass

	def hm_morphupdatecheck(self):
		pass

	def hm_nodeismidnode(self,node_entity: Entity):
		pass

	def hm_plotentity(self,collection: Collection, dataname: hwString , plottype: int ):
		pass

	def hm_plotloads_bycollection(self,collection: Collection, dataname: hwString , plottype: int ):
		pass

	def hm_plotloads_byentity(self,id: Entity, dataname: hwString , plottype: int ):
		pass

	def hm_plotmarker_bycollection(self,*args, **kwargs):
		"""
		hm_plotmarker_bycollection(HMAPI self, Collection collection, hwString const & dataname="", hwString const & inputmarker="", int const color=1, hwString const & location="centroid", int const display=0, int const precision=6)
		"""
		pass

	def hm_plotmarker_byentity(self,*args, **kwargs):
		"""
		hm_plotmarker_byentity(HMAPI self, Entity id, hwString const & dataname="", hwString const & inputmarker="", int const color=1, hwString const & location="centroid", int const display=0, int const precision=6)
		"""
		pass

	def hm_plotshape_bycollection(self,collection: Collection, shape: hwString , height: float  =" 1_module.0", L1: float  =" 1_module.0", L2: float  =" 1_module.0", L3: float  =" 1_module.0", r1: float  =" 3_module.0", r2: float  =" 3_module.0", r3: float  =" 3_module.0", color: int  = 1, drawmode: int  = 1, transparency: float  =" 0_module.0", system: int  =" 0"):
		pass

	def hm_plotshape_byentity(self,id: Entity, shape: hwString , height: float  =" 1_module.0", L1: float  =" 1_module.0", L2: float  =" 1_module.0", L3: float  =" 1_module.0", r1: float  =" 3_module.0", r2: float  =" 3_module.0", r3: float  =" 3_module.0", color: int  = 1, drawmode: int  = 1, transparency: float  =" 0_module.0", system: int  =" 0"):
		pass

	def hm_posteeforentity(self,*args, **kwargs):
		"""
		hm_posteeforentity(HMAPI self, Entity entity, hwString const & title="Entity Editor", int const modal=0, hwString const & defaultParentWindow=".")
		"""
		pass

	def hm_posteeformarkmask(self,*args, **kwargs):
		"""
		hm_posteeformarkmask(HMAPI self, Collection mark_id, hwString const & title="Entity Editor", int const modal=1, int const disable_create_edit=0)
		"""
		pass

	def hm_projectpointonsegment(self,px: float , py: float , pz: float , sx1: float , sy1: float , sz1: float , sx2: float , sy2: float , sz2: float ):
		pass

	def hm_projectpointtosegment(self,px: float , py: float , pz: float , sx1: float , sy1: float , sz1: float , sx2: float , sy2: float , sz2: float ):
		pass

	def hm_projectpointtosegmentwithangle(self,px: float , py: float , pz: float , sx1: float , sy1: float , sz1: float , sx2: float , sy2: float , sz2: float , angle: float ):
		pass

	def hm_proximityend(self):
		pass

	def hm_proximitygetcomponentelementpair(self,component_pair_index: var0 , element_pair_index: var0 ):
		pass

	def hm_proximitygetcomponentelementpaircount(self,component_pair_index: var0 ):
		pass

	def hm_proximitygetcomponentpair(self,component_pair_index: var0 ):
		pass

	def hm_proximitygetcomponentpaircount(self):
		pass

	def hm_proximitygetelementdistance(self,element_entity: Entity):
		pass

	def hm_proximityinit(self,collection: Collection, max_distance: float , mode: var0  = 1, check_side: var0  = 3, proximity_scheme: var0  = 1, proximity_by_edge: var0  =" 0", min_angle_limit: float  =" 0_module.0", max_angle_limit: float  =" 180_module.0"):
		pass

	def hm_proximityinitwithtarget(self,source_collection: Collection, target_collection: Collection, max_proximity_distance: float , check_side: var0  = 3, proximity_scheme: var0  = 1, proximity_by_edge: var0  =" 0", min_angle_limit: float  =" 0_module.0", max_angle_limit: float  =" 180_module.0"):
		pass

	def hm_proximitymarkcomponentallelementpairs(self,component_pair_index: var0 , collection1: Collection, collection2: Collection):
		pass

	def hm_proximitymarksourceproximityelements(self,collection: Collection):
		pass

	def hm_proximitymarktargetproximityelements(self,collection: Collection):
		pass

	def hm_redraw(self):
		pass

	def hm_registerredraw(self,mode: int ):
		pass

	def hm_setmodelcheckcheckstatus(self,display_name: hwString , status: var0 ):
		pass

	def hm_setmodelcheckresultentids(self,display_name: hwString , collection_id: CollectionSet):
		pass

	def hm_setsolver(self,name: hwString ):
		pass

	def hm_triplecos(self,start: hwTriple, end: hwTriple):
		pass

	def hm_undefinedmatchingcriteria(self,entity_type: EntityFullType):
		pass

	def hm_updatemodelcheckresultvalues(self,display_name: hwString ):
		pass

	def hm_visualizeloads(self,*args, **kwargs):
		"""
		hm_visualizeloads(HMAPI self, Collection entities, int const config, int const plottype, int const showlabel=0, EntityFullType locationentitytype=hwDescriptor::EntityFullType((unsigned int)0))
		"""
		pass

	def hm_visualizeloads_clearall(self):
		pass

	def hm_wadlinescheckentities(self):
		pass

	def hm_wadlinesend(self):
		pass

	def hm_wadlinesgetadulttestzone(self):
		pass

	def hm_wadlinesgetchildtestzone(self):
		pass

	def hm_wadlinesgetdebugtracelines(self,line_type: int , offset_distance: float  =" 0_module.0", protocol_method: int  =" 0"):
		pass

	def hm_wadlinesgetgridpoints(self,wad_child_min: float , wad_child_max: float , wad_adult_min: float , wad_adult_max: float , side_tolerance: float , protocol_method: int  =" 0", protocol_version: float  =" 7_module.0", grid_spacing: float  =" 100_module.0", vertical_spacing: float  =" 100_module.0"):
		pass

	def hm_wadlinesgetgridpointsleg(self,*args, **kwargs):
		"""
		hm_wadlinesgetgridpointsleg(HMAPI self, int const height, double const spacing=100.000000, double const version=DBL_MAX, double const end_gap=50.000000, double const clearance=75.000000, double const height_option=DBL_MAX, double const max_depth=10.000000, int const method=0)
		"""
		pass

	def hm_wadlinesgetinternalbumperline(self,spacing: float , max_depth: float  =" 10_module.0", max_height: float  =" 520_module.0"):
		pass

	def hm_wadlinesgetleggridline(self):
		pass

	def hm_wadlinesgetreferenceline(self,line_location: int , offset: float  =" 0_module.0", method: int  =" 0"):
		pass

	def hm_wadlinesgetsectionmax(self,origin: hwTriple, plane_normal: hwTriple, direction: hwTriple):
		pass

	def hm_wadlinesgetwadline(self,distance: float ):
		pass

	def hm_wadlinesgetwadpointtapeline(self,lateral_location: float , distance: float ):
		pass

	def hm_wadlinesinit(self):
		pass

	def hm_wadlinesispointintestzone(self,testpoint: hwTriple, tolerance: float , normal: hwTriple, num_pts: int , points: hwDoubleList):
		pass

	def hm_wadlinessetaxes(self,origin: hwTriple, forwardvec: hwTriple, leftvec: hwTriple):
		pass

	def hm_wadlinessetbumper(self,entities: Collection):
		pass

	def hm_wadlinessetentities_bycollection(self,frontEntities: Collection, rearEntities: Collection):
		pass

	def hm_wadlinessetentities_bymode(self,mark_id_front: Collection, mode: hwString ):
		pass

	def hm_wadlinessetfrontentitiesforcollision(self,entities: Collection):
		pass

	def hm_wadlinessethood(self,hoodEntities: Collection):
		pass

	def hm_wadlinessetoptions(self,*args, **kwargs):
		"""
		hm_wadlinessetoptions(HMAPI self, bool const active_hood_method=False, double const blerl_height=600.000000, double const blerl_offset=82.500000, double const blerl_selen=1000.000000, double const brrl_offset=82.500000, double const corner_gauge_height=236.000000, double const corner_height_max=1003.000000, double const corner_height_min=75.000000, double const cycling_impact_angle=60.000000, double const cycling_zone_max=0.000000, double const cycling_zone_min=0.000000, double const groundz_cord=0.000000, double const headform_adult_impact_angle=65.000000, double const headform_child_impact_angle=50.000000, double const headform_forward_impact_angle=20.000000, double const horiz_proj_min_angle=60.000000, double const horiz_proj_min_dist=50.000000, double const impactor_mass=10.500000, double const impactor_mass_nominal=7.400000, double const init_velocity=11.110000, double const leg_offset=42.000000, int const protocol_method=0, double const protocol_version=8.400000, double const side_ref_wad_dist=1000.000000, double const side_reference_resolution=100.000000, double const srl_left_offset=82.500000, double const srl_right_offset=82.500000, double const upper_legform_max_energy=457.000000, double const upper_legform_min_energy=160.000000, double const upperlegbumper_lowerlimit=425.000000, double const upperlegbumper_upperlimit=500.000000, int const wad_method=1, double const zheight=75.000000)
		"""
		pass

	def hm_wadlinessetparameters(self,side_angle: float , front_angle: float , spacing: float  =" 0_module.0", rear_reference_radius: float  =" 0_module.0", reference_resolution: float  =" 0_module.0", upper_bumper_angle: float  =" 0_module.0", lower_bumper_angle: float  =" 0_module.0", corner_angle: float  =" 0_module.0"):
		pass

	def hm_wadlinessetwindscreen(self,entities: Collection):
		pass

	def hm_wadlinessetwipers(self,wiperEntities: Collection, use_for_reference_line: bool  = False, use_for_wad_line: bool  = False):
		pass

	def hm_xformnodetolocal(self,node: Entity, system: Entity):
		pass

	def hm_xformvectoratpointtoglobal(self,x: float , y: float , z: float , system: Entity, node: Entity):
		pass

	def hm_xformvectoratpointtolocal(self,x: float , y: float , z: float , system: Entity, node: Entity):
		pass

	def hm_xpointlocal(self,system: Entity, x: float , y: float , z: float ):
		pass

	def hm_xpointvectorlocal(self,system: Entity, x: float , y: float , z: float , vx: float , vy: float , vz: float ):
		pass

	def hm_ypointlocal(self,system: Entity, x: float , y: float , z: float ):
		pass

	def hm_ypointvectorlocal(self,system: Entity, x: float , y: float , z: float , vx: float , vy: float , vz: float ):
		pass

	def hm_zpointlocal(self,system: Entity, x: float , y: float , z: float ):
		pass

	def hm_zpointvectorlocal(self,system: Entity, x: float , y: float , z: float , vx: float , vy: float , vz: float ):
		pass

	def hmgquality(self,fname: hwString , solid_flags: int, shell_flags: int):
		pass

	def hmmeshdrag(self,quads: int):
		pass

	def hmmeshlinedrag(self,quads: int):
		pass

	def hmmeshskin(self,quads: int):
		pass

	def hmmeshspin(self,quads: int):
		pass

	def hmmeshspline(self,quads: int):
		pass

	def hmmeshsurfacecone(self,quads: int):
		pass

	def hmmeshsurfaceplane(self,quads: int):
		pass

	def hmmeshsurfacesphere(self,quads: int):
		pass

	def hmmeshsurfacetorus(self,quads: int):
		pass

	def hmplygeomsmoothing(self,collection: Collection, num_iters: int, tol: float, create_line: int, create_surface: int, mode: int):
		pass

	def hmplysmoothing(self,collection: Collection, num_iters: int, region_type: int, tol: float, split_ply: int):
		pass

	def hmshrinkwrap(self,entity_collection: Collection, elems_collection: Collection, wrap_type: int, elem_size: float, warpage_value: float):
		pass

	def hwCfdCreateMeshControlsFromSolverOptions(self,mesher: hwString ):
		pass

	def hwCfdSceneReverseAll(self,entity_type: EntityFullType, consider_geom: int = 1, consider_elems: int = 1):
		pass

	def hwCfdSceneShowAll(self,consider_geom: int = 1, consider_elems: int = 1):
		pass

	def hwCfdSceneShowHideIsolateEntity(self,function: hwString , collection: Collection, consider_geom: int = 1, consider_elems: int = 1, unhighlight: int = 1):
		pass

	def hwct_addrepsfromlibrary(self,collection: Collection, rep_alias_list: hwString , params: hwString ):
		pass

	def hwct_addselectedrepsfromlibrary(self,entity_type: EntityFullType, string_array: hwStringList, params: hwString ):
		pass

	def hwct_closelibrary(self,*args, **kwargs):
		"""
		hwct_closelibrary(HMAPI self, EntityFullType entity_type, hwString const & options=s_defaultString)
		"""
		pass

	def hwct_deleterepsfromlibrary(self,collection: Collection, params: hwString , options: hwString ):
		pass

	def hwct_openlibrary(self,entity_type: EntityFullType, params: hwString ):
		pass

	def hwct_savetolibrary(self,collection: Collection, rep_alias_list: hwString , params: hwString ):
		pass

	def hwct_synclibrary(self,collection: Collection, params: hwString ):
		pass

	def hyperbeamreadbmfile(self,bmfile: hwString ):
		pass

	def icelementcreate(self):
		pass

	def identify_circle_reachable_region(self,solidcollection: Collection, circlediameter: float):
		pass

	def idmgrshowhide(self,submodel_type: hwString , id: var0, short_name: hwString , show_hide_flag: int, show_hide_type: hwString ):
		pass

	def import_cdm(self,path: str):
		pass

	def importbom(self,file_name: hwString , options: hwString ):
		pass

	def importdummyfrompositioningfile(self,file: hwString ):
		pass

	def imprint_elements(self,collection_target: Collection, collection_source: Collection, options: hwString ):
		pass

	def imprint_geom(self,collection_target: Collection, collection_source: Collection, options: hwString ):
		pass

	def imprint_nodelist(self,list_source: EntityList, collection_target: Collection, options: hwString ):
		pass

	def imprint_pointchain(self,*args, **kwargs):
		"""
		imprint_pointchain(HMAPI self, Collection baseCollection, hwIntList isHard=hwIntList(), int const numChains=0, hwIntList numPoints=hwIntList(), hwDoubleList points=hwDoubleList(), bool const saveToUserList=False)
		"""
		pass

	def imprintingki(self,mesh_collection: Collection, _ctrls: hwString ):
		pass

	def improve_connectivity(self,collection: Collection, elem_type: int, max_feature_angle: float):
		pass

	def include(self,file: hwString ):
		pass

	def includemergingoffset(self,merging: int):
		pass

	def includesuppressactive(self,include_id: var0, include_shortname: hwString , state: int):
		pass

	def includesuppressoutput(self,include_id: var0, include_shortname: hwString , state: int):
		pass

	def inflate_surfaces(self,surf_collection: Collection, thickness: float, debug: int):
		pass

	def initialdelaunay(self,mesh_collection: Collection, _ctrls: hwString ):
		pass

	def initializeattributes(self,collector_type: EntityFullType, collector_name: hwString ):
		pass

	def inputsimulation(self,simulationname: hwString , datatypename: hwString ):
		pass

	def interactivemeshelems(self,collection: Collection, elementsize: float, elem_type: int, elem_type2: int, size_control: int, skew_control: int, break_connect: int, angle: float):
		pass

	def interactivemeshsurf(self,collection: Collection, elementsize: float, elem_type: int, elem_type2: int, forcing: int, size_control: int, skew_control: int):
		pass

	def interactiveremeshelems(self,collection: Collection, elementsize: float, elem_type: int, elem_type2: int, size_control: int, skew_control: int, break_connect: int, angle: float):
		pass

	def interactiveremeshsurf(self,collection: Collection, elementsize: float, elem_type: int, elem_type2: int, forcing: int, size_control: int, skew_control: int):
		pass

	def interfaceadd(self,name: hwString , main: int, collection: Collection, reverse: int):
		pass

	def interfaceaddelement(self,name: hwString , main: int, node1: Entity, node2: Entity, node3: Entity, node4: Entity, type: int):
		pass

	def interfaceaddlist(self,name: hwString , main: int, entities: EntityFullType, list: EntityList):
		pass

	def interfaceaddsolidface(self,name: hwString , main: int, element_collection: Collection, node_collection: Collection, break_angle: float):
		pass

	def interruptreturntohc(self,flag: int):
		pass

	def intersectmark(self,collection: Collection, plane_normal: hwTriple, plane_base: hwTriple, combine_flag: int, break_angle: float, smooth_flag: int):
		pass

	def intersectmark2(self,collection: Collection, plane_normal: hwTriple, plane_base: hwTriple, combine_flag: int, break_angle: float, smooth_flag: int, comp_mode: int):
		pass

	def isolateentitybymark(self,*args, **kwargs):
		"""
		isolateentitybymark(HMAPI self, CollectionSet collection_set, hwString const & elementsOff="", hwString const & geometryOff="", hwString const & showComps="", hwString const & refFlag="", hwString const & plotsOff="")
		"""
		pass

	def isolateonlyentity(self,entity: Entity, showcomps: bool  = False, elements_off: bool  = False, geometry_off: bool  = False):
		pass

	def isolateonlyentity_byname(self,entity_type: EntityFullType, entity_name: hwString , showcomps: bool  = False, elements_off: bool  = False, geometry_off: bool  = False):
		pass

	def isolateonlyentitybymark(self,*args, **kwargs):
		"""
		isolateonlyentitybymark(HMAPI self, CollectionSet collection_set, hwString const & showComps="", hwString const & refFlag="", hwString const & elementsOff="", hwString const & geometryOff="", hwString const & plotsOff="")
		"""
		pass

	def isolatesegments(self,*args, **kwargs):
		"""
		isolatesegments(HMAPI self, hwIntList set_ids, hwIntList elem_ids, hwIntList face_indices=hwIntList(), bool const consider_elems=False)
		"""
		pass

	def isosurface_wrapper(self,collection10: Collection, minOctantSize: float, maxOctantSize: float):
		pass

	def jacobian_calculate_cornerpts(self,mode: int):
		pass

	def jointelement_fournoded(self,type: int, n1: Entity, n2: Entity, n3: Entity, n4: Entity, orientation: int, system1: Entity, system2: Entity, property: hwString ):
		pass

	def jointelement_sixnoded(self,type: int, n1: Entity, n2: Entity, n3: Entity, n4: Entity, n5: Entity, n6: Entity, orientation: int, system1: Entity, system2: Entity, property: hwString ):
		pass

	def jointelement_twonoded(self,n1: Entity, n2: Entity, orientation: int, o_node1: Entity, o_node2: Entity, system1: Entity, system2: Entity, property: hwString ):
		pass

	def jpegfile(self):
		pass

	def jpegfilenamed(self,filename: hwString ):
		pass

	def laminaterealize(self,lamptr: Entity):
		pass

	def laminaterealizewithoptions(self,*args, **kwargs):
		"""
		laminaterealizewithoptions(HMAPI self, Entity laminate_entity, int drape_flag=1, double thickness_tol=0, double orientation_tol=0, hwString const & create_sequence=s_defaultString, int reserved2=0, int reserved3=0, double reserved4=0, double reserved5=0, unsigned int reserved6=0)
		"""
		pass

	def laminateunrealize(self,lamptr: Entity):
		pass

	def legendsetborderhwcolor(self,color: int):
		pass

	def lightswitch(self,on: int, plot: int):
		pass

	def line_mesh_decimator(self,collection: Collection, element_size: float, options: hwString ):
		pass

	def line_trim_ends(self,collection: Collection, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, keep_original_lines: int):
		pass

	def linear1delements(self,collection1: Collection, collection2: Collection, node11: Entity, node12: Entity, node13: Entity, node21: Entity, node22: Entity, node23: Entity, density: int, config: int):
		pass

	def linear1delements_byprojections(self,collection1: Collection, collection2: Collection, config: int, type: int, density: int):
		pass

	def linearmesh(self,quads: int):
		pass

	def linearsolids(self,collection1: Collection, collection2: Collection, align1: Entity, align2: Entity, align3: Entity, align4: Entity, align5: Entity, align6: Entity, number: int, biasstyle: int, biasing: float):
		pass

	def linearsolidsbynodelist(self,collection1: Collection, collection2: Collection, align1: Entity, align2: Entity, align3: Entity, align4: Entity, align5: Entity, align6: Entity, nodelist: EntityList):
		pass

	def linearsurfacebetweenlines(self,linelist1: EntityList, endpoints1: EntityList, linelist2: EntityList, endpoints2: EntityList, reverse: int):
		pass

	def linearsurfacebetweennodes(self,list1: EntityList, list2: EntityList, reverse: int):
		pass

	def linearsurfacebetweennodesandline(self,list1: EntityList, linelist1: EntityList, endpoints: EntityList, reverse: int):
		pass

	def linecombine(self,line_entity1: Entity, line_entity2: Entity, smooth: int):
		pass

	def linecombinemark(self,collection: Collection, tolerance: float, break_angle: float, smooth: int):
		pass

	def linecombinemarkall(self,collection: Collection, smooth: int, keep_original_lines: int):
		pass

	def linecreateatplanesintersection(self,plane1_normal: hwTriple, plane1_normal_base: hwTriple, plane2_normal: hwTriple, plane2_normal_base: hwTriple, length_option: int, length: float):
		pass

	def linecreateatsurfacefeatures(self,collection: Collection, reserved: int, radius: float):
		pass

	def linecreateatsurfparams(self,surf_entity: Entity, u1: float, u2: float, ucount: int, v1: float, v2: float, vcount: int, mode: int, comp_mode: int):
		pass

	def linecreateconic(self,sx: float, sy: float, sz: float, ex: float, ey: float, ez: float, tx: float, ty: float, tz: float, ratio: float):
		pass

	def linecreatedragnodealongvector(self,collection: Collection, vector: hwTriple, distance: float):
		pass

	def linecreatefromcoords(self,type: int, break_angle: float, aspect: float, linear_angle: float, float_array: hwDoubleList):
		pass

	def linecreatefromnodes(self,list: EntityList, type: int, break_angle: float, aspect: float, linear_angle: float):
		pass

	def linecreatefromnodesandprojecttobinder(self,list: EntityList, type: int, break_angle: float, aspect: float, linear_angle: float, proj_dir: hwTriple, binder_surf: Entity):
		pass

	def linecreatefromnodesonsurface(self,surf_entity: Entity, point_list: EntityList, curve_type: int, options: int):
		pass

	def linecreatenormal2d(self,line_entity: Entity, point_entity: Entity, plane_normal: hwTriple, plane_normal_base: hwTriple, length: float, mode: int):
		pass

	def linecreatenormalfromgeom(self,point_collection: Collection, geom_collection: Collection, length: float, mode: int):
		pass

	def linecreatenormaltogeom(self,point_collection: Collection, geom_collection: Collection, mode: int):
		pass

	def linecreatenurbs(self,degree: int, dimension: int, knot_count: int, pole_count: int, ratnl: int, float_array: hwDoubleList):
		pass

	def linecreateoffsetalongcurvature(self,line_list: EntityList, start_offset: float, end_offset: float, link_type: int, flags: int):
		pass

	def linecreatespline(self,point_list: EntityList, scond: int, econd: int, svector: hwTriple, evector: hwTriple):
		pass

	def linecreatestraight(self,x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):
		pass

	def linedragelements(self,collection: Collection, gue: EntityList, gueendpoints: EntityList, plane_normal: hwTriple, plane_normal_base: hwTriple, ondrag: int, biasstyle: int, biasing: float, using_default_vector: int):
		pass

	def linedraglinetoformsurface(self,sectionlinelist: EntityList, sectionnodelist: EntityList, draglinelist: EntityList, dragnodelist: EntityList, refplane_normal: hwTriple, refplane_normal_base: hwTriple, using_default_vector: int):
		pass

	def linedragnodestoformsurface(self,sectionnodelist: EntityList, draglinelist: EntityList, dragnodelist: EntityList, refplane_normal: hwTriple, refplane_normal_base: hwTriple, using_default_vector: int):
		pass

	def lineeditlength(self,entity: Entity, length: float, derivative: int, direction: int):
		pass

	def lineextenddistance(self,line: Entity, distance: float, derivative: int, direction: int):
		pass

	def lineextendtoline(self,line1: Entity, line2: Entity, capture_radius: float, derivative: int, direction: int):
		pass

	def lineextendtonode(self,line: Entity, node: Entity, capture_radius: float, derivative: int, direction: int):
		pass

	def lineextendtopoint(self,line: Entity, point: Entity, capture_radius: float, derivative: int, direction: int):
		pass

	def lineextendtosurf(self,line: Entity, surface: Entity, capture_radius: float, derivative: int, direction: int):
		pass

	def linefromsurfedgecomp(self,collection: Collection, comp_flag: int):
		pass

	def lineimprintpoints(self,collection: Collection, float_array: hwDoubleList, max_distance: float):
		pass

	def linelistbypath(self,line_entity1: Entity, line_entity2: Entity, list: EntityList, flag: int):
		pass

	def linemarkbypath(self,line_entity1: Entity, line_entity2: Entity, collection: Collection, flag: int):
		pass

	def linemarkremovepinholes(self,collection: Collection, exclude_point: int):
		pass

	def linemesh_preparedata1(self,collection: Collection, break_angle: float, config: int):
		pass

	def linemesh_preparenodeslist1(self,list: EntityList, config: int):
		pass

	def linemesh_savedata1(self,create_flag: int, config: int, property_id: int, organize: int):
		pass

	def linemesh_savedata_bar1(self,entity_type: EntityFullType, create_flag: int, config: int, property_id: int, vector: hwTriple, offset_x_a: float, offset_y_a: float, offset_z_a: float, offset_x_b: float, offset_y_b: float, offset_z_b: float, auto_flag: int, organize: int):
		pass

	def linemesh_saveparameters(self,segment: int, density: int, bias: float, bias_style: int):
		pass

	def lineplot(self,title: hwString , full_size: int):
		pass

	def linereverse(self,line_entity: Entity):
		pass

	def lines_approximate(self,collection: Collection, type: int, reserved1: int, reserved2: float):
		pass

	def linescombine(self,edge1: Entity, edge2: Entity, edge_tolerance: float):
		pass

	def linescreatemidline(self,linelist1: EntityList, trimnodelist1: EntityList, linelist2: EntityList, trimnodelist2: EntityList):
		pass

	def linesplitatangle(self,lineptr: Entity, angle: float):
		pass

	def linesplitatjoint(self,line: Entity, node: Entity):
		pass

	def linesplitatline(self,collection: Collection, cut: Entity):
		pass

	def linesplitatmultiplelines(self,target_collection: Collection, trim_collection: Collection, cross_trim: int  =" 0"):
		pass

	def linesplitatplane(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple):
		pass

	def linesplitatpoint(self,line: Entity, node: Entity):
		pass

	def linessmoothtoangle(self,collection: Collection, cosangle: float):
		pass

	def linessmoothtotol(self,collection: Collection, tol: float):
		pass

	def linestoelementsaddelemsfixed(self,collection: Collection, elem_size: float):
		pass

	def list_collector_test(self,list1: EntityList, list2: EntityList, the_float: float, the_int: int):
		pass

	def load(self,path: str, embed_connection_files: bool):
		pass

	def load_connection(self,connection_name: str, file_path: str):
		pass

	def load_hmg(self,fname: hwString ):
		pass

	def load_sl_gda(self,type: int, gda_fn: hwString ):
		pass

	def loadcreate(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float):
		pass

	def loadcreateonentity(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float):
		pass

	def loadcreateonentity_curve(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, x_loc: float, y_loc: float, z_loc: float, curve_id: var0, x_scale: float):
		pass

	def loadcreateonentity_function(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, xlocation: float, ylocation: float, zlocation: float, function: hwString ):
		pass

	def loadcreateonentitywithvars(self,collection: Collection, config: int, type: int, comp1_var: hwString , comp2_var: hwString , comp3_var: hwString , comp4_var: hwString , comp5_var: hwString , comp6_var: hwString ):
		pass

	def loadcreatewithsystem(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, system: Entity, transformflag: int):
		pass

	def loadcreatewithsystemonentity(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, system: Entity, transformflag: int):
		pass

	def loadcreatewithsystemonentity_curve(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, system_entity: Entity, transform_flag: int, x_loc: float, y_loc: float, z_loc: float, curve_id: var0, x_scale: float):
		pass

	def loadcreatewithsystemonentity_function(self,collection: Collection, config: int, type: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, sysptr: Entity, transform_flag: int, xlocation: float, ylocation: float, zlocation: float, function: hwString ):
		pass

	def loadcreatewithsystemonentitywithvars(self,collection: Collection, config: int, type: int, comp1_var: hwString , comp2_var: hwString , comp3_var: hwString , comp4_var: hwString , comp5_var: hwString , comp6_var: hwString , system_entity: Entity):
		pass

	def loaddefaultattributevaluesfromxml(self,xmlfilename: hwString ):
		pass

	def loadsettypes(self,collection_set: CollectionSet, entities: EntityFullType):
		pass

	def loadsupdate(self,collection: Collection, config: int, type: int, updatevector: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, updatemag: int, magnitude: float, update_system: int, system_id: var0, transform_flag: int):
		pass

	def loadsupdatecurve(self,collection: Collection, config: int, type: int, updatevector: int, comp1: float, comp2: float, comp3: float, comp4: float, comp5: float, comp6: float, updatemag: int, magnitude: float, update_system: int, system_id: var0, transform_flag: int, updatecurve: int, curve_id: var0, updatexscale: int, xscale: float, updatedisplaylocation: int, xlocation: float, ylocation: float, zlocation: float):
		pass

	def loadsupdatefixedvalue(self,collection: Collection, fixed_value: int):
		pass

	def loadtype(self,config: hwString , type: hwString ):
		pass

	def lockallentities(self,pool_entity: Entity, dataname: hwString ):
		pass

	def lockentities(self,collection: Collection, dataname: hwString ):
		pass

	def lockview(self):
		pass

	def makepreservednodes(self,collection: Collection):
		pass

	def makesecondarymodeleditable(self,model_name: hwString , edit_state: var0):
		pass

	def maketempfrompreservednodes(self,collection: Collection):
		pass

	def manualsplit_applypatterns(self,edge_split_count: int, triplets: hwString ):
		pass

	def map_symmetric_mesh(self,source_collection: Collection, target_collection: Collection, param_strs: hwStringList):
		pass

	def mapgroupelementsfromshellstosolids(self,collection: Collection):
		pass

	def maploadtomesh(self,collection: Collection):
		pass

	def mark_internal_mesh_elements(self,mesh_collection_input: Collection, mesh_collection_output: Collection, dTol: float):
		pass

	def mark_preserved_edges(self,hmlinescollection: Collection, highlight: int):
		pass

	def markcardnoneditable(self,selectcollection: Collection, editFlag: int):
		pass

	def markcombineelements(self,elements: Collection, tolerance: float  =" 1_module.0", quadstrias: int  =" 0", validity: bool  = False):
		pass

	def markdifference(self,collectiona: Collection, collectionb: Collection):
		pass

	def markercreate(self,name: hwString , node_entity: Entity, syst_entity: Entity, sys_flag: int, color: int):
		pass

	def markersupdate(self,collection: Collection, node_entity: Entity, syst_entity: Entity, sys_flag: int, color: int, update_node: int, update_syst: int, update_color: int):
		pass

	def markintersection(self,collectiona: Collection, collectionb: Collection):
		pass

	def markintersectplane(self,entitycollection: Collection, plane_normal: hwTriple, plane_base: hwTriple, elemoutcollection: Collection, nodeoutcollection: Collection):
		pass

	def markloadsteploads(self,name: hwString , collectionl: Collection):
		pass

	def markmovetoinclude(self,collection: Collection, include_id: var0):
		pass

	def markmovetoincludewithcontents(self,collection: Collection, include_id: var0, child_entity_types: hwString ):
		pass

	def markmovetomodule(self,collection: Collection, module_name: hwString ):
		pass

	def markmovetoskeleton(self,skeleton_id: var0, collection: Collection):
		pass

	def markmovetosubmodel(self,submodel_type: hwString , collection: Collection, parent_id: var0):
		pass

	def marknodenudge(self,collection: Collection, distance: float, vector: hwTriple):
		pass

	def marknotintersection(self,collectiona: Collection, collectionb: Collection):
		pass

	def markprojectnormallytoline(self,collection: Collection, projectlinelist: EntityList, projectnodelist: EntityList):
		pass

	def markprojectnormallytosurface(self,collection: Collection, surfptr: Entity):
		pass

	def markprojecttoline(self,collection: Collection, vector: hwTriple, projectlinelist: EntityList, projectnodelist: EntityList):
		pass

	def markprojecttosurface(self,collection: Collection, vector: hwTriple, surface: Entity):
		pass

	def marksmoothelements(self,tosmoothcollection: Collection, toanchorcollection: Collection, smoothmethod: int, iterations: int):
		pass

	def marksmoothsolids(self,collection: Collection, iterations: int):
		pass

	def marktousermark(self,collection: Collection):
		pass

	def maskall(self):
		pass

	def maskall2(self):
		pass

	def maskentitiesincollector(self,collection: Collection, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int, flag_6: int):
		pass

	def maskentitymark(self,collection: Collection, flag: int):
		pass

	def masknotshown(self):
		pass

	def masknotshown2(self):
		pass

	def maskreverse(self,entity_type: EntityFullType):
		pass

	def maskreverseall(self):
		pass

	def maskreverseall2(self):
		pass

	def masksegments(self,*args, **kwargs):
		"""
		masksegments(HMAPI self, hwIntList set_ids, hwIntList elem_ids, hwIntList face_indices=hwIntList(), bool const consider_elems=False)
		"""
		pass

	def masselement(self,collection: Collection, mass: float, property: hwString , name: Entity):
		pass

	def masselementwithvar(self,collection: Collection, mass_var: hwString ):
		pass

	def massmagnitudeupdate(self,collection: Collection, massMag: float, admasType: int):
		pass

	def mechadjustballjoint(self,name: hwString , x: float, y: float, z: float, tolerance: float, lock: var0, angle_step: float):
		pass

	def mechadjustjoint(self,name: hwString , direction: var0, value: float, tolerance: float, lock: var0, angle_step: float, hold_angles: var0 = 1):
		pass

	def mechapplybodymovements(self,bodies_array: hwStringList, matrices_array: hwDoubleList2 ):
		pass

	def mechapplybodytotargetpoints(self,bodies_array: hwStringList, point_pairs_array: hwDoubleList2 ):
		pass

	def mechapplyconfiguration(self,name: hwString ):
		pass

	def mechapplyediposition(self,mode: int, run_solver: int =" 0"):
		pass

	def mechapplyposition(self,name: hwString , asmove: int, tolerance: float):
		pass

	def mechcontructfromedi(self,mode: int, param: int):
		pass

	def mechconvertbodytomdl(self,name: hwString , flexible: var0 =" 0", cmsmethod: int = 1, freq_ub: float =" 0_module.0", nmodes: int =" 0"):
		pass

	def mechconvertjointtomdl(self,name: hwString ):
		pass

	def mechconvertmdlbodies(self,ecollection: Collection):
		pass

	def mechconvertmdljoints(self,ecollection: Collection):
		pass

	def mechcreatebody(self,ecollection: Collection, name: hwString , sysid: var0, rx: float, ry: float, rz: float, method: int, grounded: int, dbe: int, color: int, weight: float):
		pass

	def mechcreateconstraint(self,bodyname1: hwString , bodyname2: hwString , raintname: hwString , type: int, n1id: var0, n2id: var0, n3id: var0, n4id: var0, n5id: var0, n6id: var0, color: int, weight: float):
		pass

	def mechcreatejoint(self,bodyname1: hwString , bodyname2: hwString , jointname: hwString , sysid: var0, xloc: float, yloc: float, zloc: float, axis: int, type: int, color: int, elemid: var0):
		pass

	def mechcreatemechanism(self,name: hwString , color: int, bodyids: hwIntList):
		pass

	def mechcreatesubmechanism(self,name: hwString , color: int, mechname: hwString , parentname: hwString , bodyids: hwIntList):
		pass

	def mechdeleteall(self):
		pass

	def mechdeletebodies(self,bodyids: hwIntList):
		pass

	def mechdeletebody(self,bodyname: hwString ):
		pass

	def mechdeleteconfiguration(self,name: hwString ):
		pass

	def mechdeleteconstraint(self,constraintname: hwString ):
		pass

	def mechdeleteconstraints(self,constraintids: hwIntList):
		pass

	def mechdeletejoint(self,jointname: hwString ):
		pass

	def mechdeletejoints(self,jointids: hwIntList):
		pass

	def mechdeletemechanism(self,name: hwString ):
		pass

	def mechdeleteposition(self,positionname: hwString ):
		pass

	def mechdeletesubmechanism(self,name: hwString ):
		pass

	def mechexportdaf(self,filename: hwString ):
		pass

	def mechimportdaf(self,filename: hwString ):
		pass

	def mechjointlimits(self,limits: var0):
		pass

	def mechplacebodytobody(self,name1: hwString , px: float, py: float, pz: float, name2: hwString , tx: float, ty: float, tz: float, tolerance: float):
		pass

	def mechplacebodytopoint(self,name: hwString , sx: float, sy: float, sz: float, tx: float, ty: float, tz: float, tolerance: float):
		pass

	def mechplanetranslatebody(self,name: hwString , sx: float, sy: float, sz: float, tx: float, ty: float, tz: float, rx: float, ry: float, rz: float, tolerance: float):
		pass

	def mechreplicateposition(self,posname: hwString , newname: hwString , color: int, basebody: hwString , targetbody: hwString , mode: var0):
		pass

	def mechrotatebody(self,name: hwString , plane_normal: hwTriple, plane_normal_base: hwTriple, angle: float, method: var0, tolerance: float, angle_step: float):
		pass

	def mechsaveconfiguration(self,name: hwString , color: int, mechs: hwIntList):
		pass

	def mechsaveposition(self,name: hwString , color: int, ids: hwIntList, type: var0):
		pass

	def mechsetalllimits(self,option: int):
		pass

	def mechsetbodygrounded(self,name: hwString , on: int):
		pass

	def mechsetjointlimit(self,jointname: hwString , type: int, direction: int, on: int, value: float):
		pass

	def mechsetjointvalue(self,jointname: hwString , direction: var0, value: float):
		pass

	def mechtransformposition(self,posname: hwString , newname: hwString , color: int, bodyname: hwString ):
		pass

	def mechundoredo(self,option: int):
		pass

	def mechupdatebody(self,ecollection: Collection, name: hwString , sysid: var0, rx: float, ry: float, rz: float, grounded: int, color: int, weight: float):
		pass

	def mechupdateconstraint(self,bodyname1: hwString , bodyname2: hwString , raintname: hwString , type: int, n1id: var0, n2id: var0, n3id: var0, n4id: var0, n5id: var0, n6id: var0, color: int, weight: float, active: int):
		pass

	def mechupdatejoint(self,bodyname1: hwString , bodyname2: hwString , jointname: hwString , sysid: var0, xloc: float, yloc: float, zloc: float, axis: int, type: int, color: int):
		pass

	def mechupdatemechanism(self,name: hwString , color: int, bodyids: hwIntList):
		pass

	def mechupdateparameter(self,parameter: hwString , value: float):
		pass

	def mechupdateparameterstring(self,parameter: hwString , value: hwString ):
		pass

	def mechupdatesubmechanism(self,name: hwString , color: int, bodyids: hwIntList, parentname: hwString ):
		pass

	def memberpanelmesh(self,memberpanels: Collection, elemSize: float , elemtype: int ):
		pass

	def menufilterdisable(self):
		pass

	def menufilterenable(self):
		pass

	def menufilterset(self,string: hwString ):
		pass

	def menufont(self,size: int):
		pass

	def mergefile(self,filename: hwString , geom_merge: int, fe_merge: int):
		pass

	def mergefile2(self,*args, **kwargs):
		"""
		mergefile2(HMAPI self, hwString const & filename, bool const connectors_checkattribute=False, bool const connectors_layercheck=False, bool const connectors_thicknesscheck=False, double const connectors_tolerance=0.000000, hwString const & dropincomingmodulehierarchy="no", hwString const & mergemode_comps="keepboth", hwString const & mergemode_mats="keepboth", hwString const & mergemode_props="keepboth", hwString const & mergemode_sensors="keepboth", hwString const & mergemode_sections="keepboth", hwString const & respectincomingparentmodule="no", hwString const & mergemode_connectors="keepboth", hwString const & mergemode_geometryandmesh="keepboth")
		"""
		pass

	def mergehistorystate(self,statename: hwString , newstatename: hwString ):
		pass

	def mesh_create_size_ctrl(self,pars_str: hwString ):
		pass

	def mesh_fusing(self,destination_collection: Collection, target_collection: Collection, string_options: hwString ):
		pass

	def mesh_size_tree_setup(self,type: int, dbls_str: hwString ):
		pass

	def mesh_size_tree_teardown(self):
		pass

	def meshactiveface(self,faceindex: var0):
		pass

	def meshdragelements2(self,collection: Collection, vector: hwTriple, distance: float, on_drag: int, bias_style: int, biasing: float, organize: int):
		pass

	def meshflowevaluate(self,geom_collection: Collection, elem_collection: Collection, associate_tol: float, filename: hwString ):
		pass

	def meshflowfields(self,collection: Collection, line_collection: Collection, elemsize: float, str_params: hwString ):
		pass

	def meshline_create_from_plot_elements(self,collection: Collection, reserved1: int, reserved2: int, reserved3: int, reserved4: float, reserved5: float, reserved6: float):
		pass

	def meshline_create_from_points(self,list: EntityList, reserved1: int, reserved2: int, reserved3: float, reserved4: float):
		pass

	def meshline_delete(self,collection: Collection):
		pass

	def meshline_delete_surface(self,collection: Collection):
		pass

	def meshline_display_scaffold(self,flag: int, reserved: CollectionSet):
		pass

	def meshline_end(self,reserved: int):
		pass

	def meshline_initialize(self,reserved: int =" 0", mask_element: int =" 0", display_scaffold: int =" 0", reserve1: int =" 0", feature_angle: float =" 0_module.0", relative_tol: float =" 0_module.0", reserve2: float =" 0_module.0", reserve3: float =" 0_module.0"):
		pass

	def meshline_mark_entity_inside_class(self,collection1: Collection, collection2: Collection):
		pass

	def meshline_mark_plot(self,collection: Collection):
		pass

	def meshline_mask_class_element(self,flag: int, reserved: CollectionSet):
		pass

	def meshline_reject(self,reserved: int):
		pass

	def meshline_set_approximate_tol_factor(self,tol: float):
		pass

	def meshline_set_feature_angle(self,featureangle: float):
		pass

	def meshline_update_surface(self,flag: int, reserved: CollectionSet):
		pass

	def meshmode(self,displaylist: int, mode: int, plot: int):
		pass

	def meshspinelements2(self,collection: Collection, plane_normal: hwTriple, plane_base: hwTriple, angle: float, on_spin: int, bias_style: int, biasing: float, organize: int):
		pass

	def meshtopologyadjust(self,collection: Collection, flags: int):
		pass

	def meshutils_cutelements_2points(self,*args, **kwargs):
		"""
		meshutils_cutelements_2points(HMAPI self, Collection element_collection, double c1x, double c1y, double c1z, double c2x, double c2y, double c2z, hwString const & spc_collector_name, hwString const & box_collector_name, hwDoubleList dof_array=s_defaultDoubleList)
		"""
		pass

	def meshutils_cutelements_8points(self,element_collection: Collection, c1x: float, c1y: float, c1z: float, c2x: float, c2y: float, c2z: float, c3x: float, c3y: float, c3z: float, c4x: float, c4y: float, c4z: float, c5x: float, c5y: float, c5z: float, c6x: float, c6y: float, c6z: float, c7x: float, c7y: float, c7z: float, c8x: float, c8y: float, c8z: float, spc_collector_name: hwString , box_collector_name: hwString ):
		pass

	def meshutils_cutelements_predefined(self,*args, **kwargs):
		"""
		meshutils_cutelements_predefined(HMAPI self, Collection element_collection, hwString const & predefined_cut, double limit, hwString const & spc_collector_name, hwString const & box_collector_name, hwDoubleList dof_array=s_defaultDoubleList)
		"""
		pass

	def meshutils_cutjoints(self,element_collection: Collection, center_x: float, center_y: float, center_z: float, extent_x_n: float, extent_x_p: float, extent_y_n: float, extent_y_p: float, extent_z_n: float, extent_z_p: float, rigid_collector_name: hwString , spc_collector_name: hwString , rain: int):
		pass

	def messagefilefilter(self,type: hwString , filter: hwString ):
		pass

	def messagefileset(self,type: hwString , file: hwString ):
		pass

	def metadatamarkbool(self,collection: Collection, name: hwString , value: int):
		pass

	def metadatamarkdate(self,collection: Collection, name: hwString , value: int):
		pass

	def metadatamarkdouble(self,collection: Collection, name: hwString , value: float):
		pass

	def metadatamarkdoublearray(self,collection: Collection, name: hwString , float_array: hwDoubleList):
		pass

	def metadatamarkentityidtype(self,collection: Collection, name: hwString , entity_type_2: EntityFullType, value: var0):
		pass

	def metadatamarkentityidtypearray(self,collection: Collection, name: hwString , entity_array: EntityList):
		pass

	def metadatamarkint(self,collection: Collection, name: hwString , value: int):
		pass

	def metadatamarkintarray(self,collection: Collection, name: hwString , integer_array: hwIntList):
		pass

	def metadatamarkremove(self,collection: Collection, name: hwString ):
		pass

	def metadatamarkstring(self,collection: Collection, name: hwString , value: hwString ):
		pass

	def metadatamarkstringarray(self,collection: Collection, name: hwString , string_array: hwStringList):
		pass

	def midmesh_extract(self,*args, **kwargs):
		"""
		midmesh_extract(HMAPI self, Collection collection, double const CombineNonManifoldEdgesDistance=0.000000, double const CombineNonManifoldEdgesFactor=0.500000, double const DefeatureOpeningsFactor=0.500000, double const DefeatureOpeningsWidth=0.000000, double const DefeatureRibsWidth=0.000000, double const DefeatureRibsWidthFactor=0.500000, hwString const & DestinationComponent="Midmesh", hwString const & DestinationComponentName="Midmesh", double const ExtractionSize=2.000000, int const FlattenConnections=0, int const IgnoreFlatEdges=0, double const MidlineTrimFilletsFactor=0.500000, double const MinimumSize=2.000000, hwString const & StepOffsetMode="Automatic", double const SuppressProximityEdgesDistance=0.000000, double const SuppressProximityEdgesFactor=0.500000, double const SuppressProximityFilletsFactor=0.500000, double const TargetElementSize=2.000000, hwString const & DestinationComponentPrefix="Midmesh_", hwString const & DestinationPart="")
		"""
		pass

	def midmesh_extract_skeleton(self,thinsolidcollection: Collection, param_strs: hwStringList):
		pass

	def midmesh_inspect_delete_sets(self,mode: var0):
		pass

	def midmesh_inspect_end(self):
		pass

	def midmesh_inspect_init(self,SourceCollection: Collection, TargetCollection: Collection, CheckMinElemSize: int  = 1, MinEdgeOffEdgeDeviation: float  =" 0_module.1", MinElemCenterDeviation: float  =" 0_module.1", MinNodeOffMidDeviation: float  =" 0_module.1", MinNodeOffSolidEdgeDeviation: float  =" 0_module.1", MinNodeOutOfSolidDeviation: float  =" 0_module.1"):
		pass

	def midmesh_repair(self,mode: hwString , string_array: hwStringList):
		pass

	def midmesh_test(self,thinsolidcollection: Collection):
		pass

	def midmesh_validate(self,midmeshcomponentres: Collection, midmeshcomponentref: Collection, validation_options: int, output_options: int):
		pass

	def midsurface_accept_edge_target_by_number(self,face: Entity, e1_edge_number: int, e2_line: Entity, is_opposite: int):
		pass

	def midsurface_accept_point_target(self,face: Entity, offset_x: float, offset_y: float, offset_z: float, target_x: float, target_y: float, target_z: float, istarget: int):
		pass

	def midsurface_clear_plate_info(self,collection: Collection, reserved1: int, reserved2: int):
		pass

	def midsurface_collapse_lines(self,collection: Collection):
		pass

	def midsurface_combine_all_targets(self,face: Entity, display_only: int):
		pass

	def midsurface_display_plate_sides(self,plate_number: int, reserved1: int, reserved2: int):
		pass

	def midsurface_display_plates(self,use_base_surfaces: int, plate_type: int):
		pass

	def midsurface_edit_base_surfaces(self,collection: Collection, mode: int, distance: float, skip_drawing_duplicates: int):
		pass

	def midsurface_extract_10(self,collection: Collection, outbound_normals: int, thickness_bound: int, align_steps: int, extract_by_comp: int, rerun_type: int, stitch_tol_mode: int, max_R_t_ratio: float, reserved_1: float, reserved_2: float, max_thickness_ratio: float, min_thickness: float, max_thickness: float, mid_position: float, reserved_4: Collection, reserved_5: int, new_or_curr_comp: int):
		pass

	def midsurface_imprint(self,imprint_collection: Collection, target_collection: Collection, line_extend_option: int, surface_imprint_option: int, min_gap_size: float, reserved1: float, reserved2: float, reserved3: int, reserved4: int):
		pass

	def midsurface_merge_into_one_plate(self,collection: Collection, plate_type: int, use_base_surfaces: int, reserved: int):
		pass

	def midsurface_new_plate(self,collection: Collection, plate_type: int, use_base_surfaces: int, reserved: int):
		pass

	def midsurface_offset_by_targets_11(self,surface: Entity, mode: int):
		pass

	def midsurface_remove_display_plate_sides(self,plate_number: int, reserved1: int, reserved2: int):
		pass

	def midsurface_remove_display_plates(self,delete_plate_info: int, remove_from_all_comps: int, reserved1: int):
		pass

	def midsurface_remove_edge_target_by_number(self,face: Entity, e1_line_number: int):
		pass

	def midsurface_remove_edit_bodies(self):
		pass

	def midsurface_remove_new_target(self):
		pass

	def midsurface_remove_plate_base_conflicts(self,reserved1: int, reserved2: int):
		pass

	def midsurface_remove_target(self,face: Entity, offsetpoint_x: float, offsetpoint_y: float, offsetpoint_z: float, point_sel_code: int):
		pass

	def midsurface_set_not_a_plate_side(self,collection: Collection, use_base_surfaces: int, functionality: int):
		pass

	def midsurface_show_for_edit(self,surface: Entity):
		pass

	def midsurface_switch_sides_within_plate(self,collection: Collection, reserved1: int, reserved2: int):
		pass

	def midsurface_unsuppress_conflict_edges(self,reserved1: int, reserved2: int):
		pass

	def midsurface_update_from_plate_edit(self,collection: Collection, outbound_normals: int, thickness_bound: int, align_steps: int, extract_by_comp: int, rerun_type: int, stitch_tol_mode: int, max_R_t_ratio: float, reserved_1: float, reserved_2: float, max_thickness_ratio: float, min_thickness: float, max_thickness: float, mid_position: float, reserved_4: Collection, reserved_5: int, new_or_curr_comp: int):
		pass

	def midsurface_update_masks(self,selected_surface: Entity, on: int, displayedOnly: int):
		pass

	def midsurfaceextract(self,collection: Collection, mode: int, thickness_bound: int, min_thickness: float, max_thickness: float, reserved_2: Collection, reserved_3: int, new_or_curr_comp: int):
		pass

	def midsurfmesh(self,collection: Collection, criteria_file: hwString , param_file: hwString , elem_size: float  =" -1_module.0", elem_type: int  = -1, elem_order: int  = -1, min_elem_size: float  =" -1_module.0", max_elem_size: float  =" -1_module.0", elem_feature_angle: float  =" -1_module.0", no_geomcleanup: int  = -1, no_node_move_across_edges: int  = -1, no_remove_holes: int  = -1, no_seed_holes: int  = -1, do_washer: int  = -1, thickness_mode: int  = -1, thickness_min: float  =" -1_module.0", thickness_max: float  =" -1_module.0", midsurf_method: int  = -1, save_model: int  = -1, keep_midsurf_elems: int  = -1):
		pass

	def migrateloadcolcardstoanalysisparam(self):
		pass

	def migratetablecardstocurve(self):
		pass

	def migratetorigidwall(self):
		pass

	def min_size_node_movement(self,collection: Collection):
		pass

	def minmaxtitlemove(self,xmin: float, ymin: float, xmax: float, ymax: float, type: int, minmax: int):
		pass

	def minmaxtitlesetcolor(self,color: int, type: int, minmax: int):
		pass

	def minmaxtitlesetfont(self,font: int, type: int, minmax: int):
		pass

	def modelcheck_applyautocorrection_byallentitytypes(self,*args, **kwargs):
		"""
		modelcheck_applyautocorrection_byallentitytypes(HMAPIBase self, hwString const & check_display_name, hwString const & error_type, CollectionSet collection_set=hwDescriptor::CollectionSet())
		"""
		pass

	def modelcheck_applyautocorrection_bycollection(self,check_display_name: hwString , error_type: hwString , collection: Collection):
		pass

	def modelcheck_applyautocorrection_byentitytype(self,check_display_name: hwString , entity_type: EntityFullType, error_type: hwString ):
		pass

	def modelcheck_applyautocorrectiononmark(self,checkDisplayName: hwString , collection: CollectionSet, correctionDisplayName: hwString ):
		pass

	def modelcheck_applycorrection(self,check_display_name: hwString , correction_display_name: hwString ):
		pass

	def modelcheck_clearresults(self):
		pass

	def modelcheck_createchecks(self,filename: hwString , add: int):
		pass

	def modelcheck_loadconfigfile(self):
		pass

	def modelcheck_organizechecks(self,parent_name: hwString , collection: Collection):
		pass

	def modelcheck_runchecks_byallentitytypes(self,*args, **kwargs):
		"""
		modelcheck_runchecks_byallentitytypes(HMAPIBase self, hwString const & check_display_name, hwString const & error_type, CollectionSet collection_set=hwDescriptor::CollectionSet())
		"""
		pass

	def modelcheck_runchecks_bycollection(self,check_display_name: hwString , error_type: hwString , collection: Collection):
		pass

	def modelcheck_runchecks_byentitytype(self,check_display_name: hwString , entity_type: EntityFullType, error_type: hwString ):
		pass

	def modelcleanup(self,empty: bool  = True, unused: bool  = False, undefined: bool  = False):
		pass

	def modent_addcontentsbyids(self,*args, **kwargs):
		"""
		modent_addcontentsbyids(HMAPI self, Entity modular_entity, EntityFullType content_entity_type, hwString const & content_entity_ids, hwString const & representation_key=s_defaultString)
		"""
		pass

	def modent_addcontentsbymark(self,*args, **kwargs):
		"""
		modent_addcontentsbymark(HMAPI self, Entity modular_entity, Collection content_collection, hwString const & representation_key=s_defaultString)
		"""
		pass

	def modent_addrepresentations(self,entity: Entity, representation_key: hwString , representation_file: hwString , representation_file_format: hwString ):
		pass

	def modent_clonebymark(self,*args, **kwargs):
		"""
		modent_clonebymark(HMAPI self, Collection input_collection, Collection output_collection, bool const copy_contents=True, hwMatrix44 delta_matrix=hwMatrix44(1.0))
		"""
		pass

	def modent_deletebymark(self,collection: Collection, keep_contents: var0 =" 0"):
		pass

	def modent_deleterepresentation(self,collection: Collection, content_entity_type: hwString , representation_key: var0 =" 0"):
		pass

	def modent_export(self,entity: Entity, file_name: hwString , options: hwString ):
		pass

	def modent_realizerepresentation(self,entity: Entity, representation_key: hwString ):
		pass

	def modent_registerconstraintruleoptions(self,modular_entity_type: EntityFullType, modular_entity_action: int, independent_entity_type: EntityFullType, dependent_entity_type: EntityFullType, add_behavior_for_dependent_entity_type: int, add_behavior_for_shared_dependent_entity_type: int):
		pass

	def modent_removecontentsbyids(self,modular_entity: Entity, content_entity_type: EntityFullType, content_entity_ids: hwString ):
		pass

	def modent_removecontentsbymark(self,modular_entity: Entity, content_collection: Collection):
		pass

	def modent_reparentbymark(self,new_parent_part_entity: Entity, collection: Collection, options: hwString ):
		pass

	def modent_saverepresentation(self,entity: Entity, options: hwString ):
		pass

	def modent_saverepresentation2(self,*args, **kwargs):
		"""
		modent_saverepresentation2(HMAPI self, Entity entity, hwString const & repcomment="", hwString const & repkey="", hwString const & filepath="")
		"""
		pass

	def modent_unrealizerepresentation(self,*args, **kwargs):
		"""
		modent_unrealizerepresentation(HMAPI self, Entity entity, hwString const & representation_key, hwString const & etypesExcluded_unused=s_defaultString, int excludeOption_unused=0)
		"""
		pass

	def modifyicelement(self,entity: Entity, mode: int, node_entity: Entity):
		pass

	def morph_surfaces_by_nodes(self,nodes: hwIntList, moves: hwDoubleList, options: int):
		pass

	def morphalteranglevec(self,h1collection: Collection, h2collection: Collection, n1: Entity, n2: Entity, n3: Entity, hold: int, ang: float, sym: int, con: int, vec: hwTriple):
		pass

	def morphaltercurvectr(self,domcollection: Collection, holdnode: Collection, type: int, curve: float, sym: int, con: int, hold: int, mode: int, node: Entity, plane_normal: hwTriple, plane_normal_base: hwTriple, line: Entity, project: int, force: int, add: int):
		pass

	def morphalterdistancevec(self,h1collection: Collection, h2collection: Collection, n1: Entity, n2: Entity, hold: int, dist: float, sym: int, con: int, vec: hwTriple):
		pass

	def morphapplyfesolver(self):
		pass

	def morphapplylargedomains(self):
		pass

	def morphbeziershape(self,dcollection: Collection, ecollection: Collection, shapeid: int, sym: int, con: int, vvec: hwTriple, mag: float, type: int, meth: int, umark: int):
		pass

	def morphbiasstyle(self,style: int, con: int):
		pass

	def morphbiasupdate(self,hptr: Entity, bias: float):
		pass

	def morphbiasupdatemulti(self,hcollection: Collection, bias: float):
		pass

	def morphbiasupdateretroactive(self,hcollection: Collection, bias: float, con: int):
		pass

	def morphchecknodes(self,readfile: hwString , mode: int, reportfile: hwString ):
		pass

	def morphcombineedges(self,dcollection: Collection, rethand: int):
		pass

	def morphcombinemorphvolumes(self,h1: Entity, h2: Entity, hand: int, tangent: int):
		pass

	def morphcomparenodes(self,readfile: hwString ):
		pass

	def morphconnstodoms(self,collection: Collection, retain_handles: int, create_type: int):
		pass

	def morphconstraintapply(self):
		pass

	def morphconstraintcreateangle(self,scollection: Collection, type: int, name: hwString , n1: Entity, n2: Entity, n3: Entity, vec: hwTriple, angle: float, bound: int, color: int):
		pass

	def morphconstraintcreatearcrad(self,scollection: Collection, acollection: Collection, type: int, name: hwString , plane_normal: hwTriple, plane_normal_base: hwTriple, dptr: Entity, radius: float, bound: int, arc: int, color: int):
		pass

	def morphconstraintcreateavm(self,scollection: Collection, ecollection: Collection, type: int, name: hwString , target: float, bound: int, color: int):
		pass

	def morphconstraintcreatecomps(self,acollection: Collection, bcollection: Collection, type: int, name: hwString , vec: hwTriple, dist: float, nodedist: float, elemdist: float, ivec: int, color: int):
		pass

	def morphconstraintcreatedof(self,collection: Collection, dof1: int, dof2: int, dof3: int, system_entity: Entity, options: int, name: hwString , color: int):
		pass

	def morphconstraintcreateedge(self,name: hwString , dptr1: Entity, dptr2: Entity, end: Entity, type: int, vec: hwTriple, color: int):
		pass

	def morphconstraintcreateelems(self,ncollection: Collection, ecollection: Collection, type: int, name: hwString , p_vec: hwTriple, dist: float, ivec: int, color: int):
		pass

	def morphconstraintcreateeq(self,ncollection: Collection, type: int, name: hwString , vec: hwTriple, function: hwString , distance: float, ivec: int, meth: int, oid: var0, color: int):
		pass

	def morphconstraintcreatefc(self,ncollection: Collection, type: int, name: hwString , color: int):
		pass

	def morphconstraintcreatelayer(self,n_collection: Collection, e_collection: Collection, type: int, name: hwString , color: int):
		pass

	def morphconstraintcreatelength(self,scollection: Collection, type: int, name: hwString , nodes: EntityList, vec: hwTriple, length: float, bound: int, color: int):
		pass

	def morphconstraintcreateline(self,ncollection: Collection, type: int, name: hwString , vec: hwTriple, line: Entity, dist: float, ivec: int, color: int):
		pass

	def morphconstraintcreatematch(self,a_collection: Collection, b_collection: Collection, type: int, name: hwString , vec: hwTriple, dist: float, node_basea: Entity, node_xa: Entity, node_xya: Entity, node_baseb: Entity, node_xb: Entity, node_xyb: Entity, color: int):
		pass

	def morphconstraintcreateplane(self,ncollection: Collection, type: int, name: hwString , vec: hwTriple, plane_normal: hwTriple, plane_normal_base: hwTriple, dist: float, ivec: int, color: int):
		pass

	def morphconstraintcreatesmooth(self,nlist: EntityList, type: int, closed: int, name: hwString , color: int):
		pass

	def morphconstraintcreatesurf(self,ncollection: Collection, type: int, name: hwString , vec: hwTriple, surf: Entity, dist: float, ivec: int, color: int):
		pass

	def morphconstraintcreatevec(self,ncollection: Collection, type: int, name: hwString , vec: hwTriple, plane_normal: hwTriple, plane_normal_base: hwTriple, dist: float, color: int):
		pass

	def morphconstraintsetcolor(self,mcon: Entity, color: int):
		pass

	def morphconstraintupdateangle(self,scollection: Collection, type: int, mcon: Entity, n1: Entity, n2: Entity, n3: Entity, vec: hwTriple, angle: float, bound: int, color: int):
		pass

	def morphconstraintupdatearcrad(self,scollection: Collection, acollection: Collection, type: int, mcon: Entity, plane_normal: hwTriple, plane_normal_base: hwTriple, dptr: Entity, radius: float, bound: int, arc: int, color: int):
		pass

	def morphconstraintupdateavm(self,scollection: Collection, ecollection: Collection, type: int, mcon: Entity, target: float, bound: int, color: int):
		pass

	def morphconstraintupdatedof(self,collection: Collection, dof1: int, dof2: int, dof3: int, system_entity: Entity, options: int, entity: Entity, color: int):
		pass

	def morphconstraintupdateedge(self,mcon: Entity, dptr1: Entity, dptr2: Entity, end: Entity, type: int, vec: hwTriple, color: int):
		pass

	def morphconstraintupdateelems(self,ncollection: Collection, ecollection: Collection, type: int, name: Entity, p_vec: hwTriple, dist: float, ivec: int, color: int):
		pass

	def morphconstraintupdateeq(self,ncollection: Collection, type: int, mcon: Entity, vec: hwTriple, function: hwString , distance: float, ivec: int, meth: int, oid: var0, color: int):
		pass

	def morphconstraintupdatefc(self,ncollection: Collection, type: int, mcon: Entity, color: int):
		pass

	def morphconstraintupdatelayer(self,n_collection: Collection, e_collection: Collection, type: int, morphconstraint_entity: Entity, color: int):
		pass

	def morphconstraintupdatelength(self,scollection: Collection, type: int, mcon: Entity, nodes: EntityList, vec: hwTriple, length: float, bound: int, color: int):
		pass

	def morphconstraintupdateline(self,ncollection: Collection, type: int, mcon: Entity, vec: hwTriple, line: Entity, dist: float, ivec: int, color: int):
		pass

	def morphconstraintupdatematch(self,a_collection: Collection, b_collection: Collection, type: int, morphconstraint_entity: Entity, vec: hwTriple, dist: float, node_basea: Entity, node_xa: Entity, node_xya: Entity, node_baseb: Entity, node_xb: Entity, node_xyb: Entity, color: int):
		pass

	def morphconstraintupdateplane(self,ncollection: Collection, type: int, mcon: Entity, vec: hwTriple, plane_normal: hwTriple, plane_normal_base: hwTriple, dist: float, ivec: int, color: int):
		pass

	def morphconstraintupdatesmooth(self,nlist: EntityList, type: int, closed: int, mcon: Entity, color: int):
		pass

	def morphconstraintupdatesurf(self,ncollection: Collection, type: int, mcon: Entity, vec: hwTriple, surf: Entity, dist: float, ivec: int, color: int):
		pass

	def morphconstraintupdatevec(self,ncollection: Collection, type: int, mcon: Entity, vec: hwTriple, plane_normal: hwTriple, plane_normal_base: hwTriple, dist: float, color: int):
		pass

	def morphconvertmv(self,ccollection: Collection, han: int, ord: int, tan: int, mode: int, nauto: int):
		pass

	def morphconverttomlines(self,ecollection: Collection, nseg: int, tol: float, radtol: float):
		pass

	def morphcreatedomaindc(self,elemcollection: Collection, type: int, part: int, rethand: int, bydom: int, bycomp: int):
		pass

	def morphcreatedomainedge(self,nodes: EntityList):
		pass

	def morphcreatedomainglobalnodes(self,ncollection: Collection, mode: int):
		pass

	def morphcreateline(self,list: EntityList):
		pass

	def morphcreatemodelshape(self,type: int, mode: int, e_collection: Collection, node_list: EntityList, plane_normal: hwTriple, plane_normal_base: hwTriple, did: var0, lid: var0):
		pass

	def morphcreateresultsfile(self,collection: Collection):
		pass

	def morphcreatetempline(self,points: int):
		pass

	def morphdeleteall(self):
		pass

	def morphdeletehandlesanddomains(self):
		pass

	def morphdeletemvedgenodes(self,collection: Collection):
		pass

	def morphdisplayconstraints(self,collection: Collection):
		pass

	def morphdisplayconstraintvector(self,xp: float, yp: float, zp: float, xv: float, yv: float, zv: float, vv: float, op: int):
		pass

	def morphdisplaydependencies(self,collection: Collection):
		pass

	def morphdisplaysymmetries(self,collection: Collection):
		pass

	def morphdomainautocolor(self,collection: Collection):
		pass

	def morphdomainsetcolor(self,domain_entity: Entity, color: int):
		pass

	def morphdomainsupdatecolor(self,collection: Collection, color: int):
		pass

	def morphdoshape(self,option: int):
		pass

	def morphentitydelete(self,ecollection: Collection):
		pass

	def morphfitfaces(self,fmark: int, ecollection: Collection, offset: float, nproj: int, p_vec: hwTriple, nhand: int, mode: int, method: int, smooth: int, regnodes: int):
		pass

	def morphfittosurface(self,n_collection: Collection, e_collection: Collection, h_collection: Collection, s_collection: Collection, face: int, nhand: int, sym: int, con: int, mode: int, maxiter: var0):
		pass

	def morphhandlecreatenodes(self,collectionnode: Collection, dcollectionhandle: Collection, domain: Entity, name: hwString ):
		pass

	def morphhandlecreatenodesnodom(self,collectionnode: Collection, dcollectionhandle: Collection, name: hwString ):
		pass

	def morphhandlecreatexyz(self,dcollectionhandle: Collection, domain: Entity, name: hwString , xx: float, yy: float, zz: float, sys: int):
		pass

	def morphhandlepertnormal(self,collectionhandle: Collection, collectionelem: Collection, dist: float, sym: int, con: int, umark: int):
		pass

	def morphhandlepertxyz(self,collection: Collection, x_val: float, y_val: float, z_val: float, system_id: int, symmetry_flag: int, constraint_flag: int):
		pass

	def morphhandleprojectentity(self,h_collection: Collection, e_collection: Collection, p_collection: Collection, nproj: int, proj: hwTriple, sym: int, con: int):
		pass

	def morphhandleprojectentityoffset(self,h_collection: Collection, e_collection: Collection, extend: int, p_collection: Collection, nproj: int, proj: hwTriple, sym: int, con: int, offset: float):
		pass

	def morphhandleprojectline(self,h_collection: Collection, p_collection: Collection, line_list: EntityList, node_list: EntityList, nproj: int, proj: hwTriple, sym: int, con: int):
		pass

	def morphhandleprojectlineoffset(self,h_collection: Collection, p_collection: Collection, line_list: EntityList, node_list: EntityList, nproj: int, proj: hwTriple, sym: int, con: int, offset: float):
		pass

	def morphhandleprojectplane(self,h_collection: Collection, p_collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, nproj: int, proj: hwTriple, sym: int, con: int):
		pass

	def morphhandleprojectplaneoffset(self,h_collection: Collection, p_collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, nproj: int, proj: hwTriple, sym: int, con: int, offset: float):
		pass

	def morphhandlerotate(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, angle: float, sym: int, con: int, vari: int):
		pass

	def morphhandlescalexyz(self,h_collection: Collection, node_id: var0, x: float, y: float, z: float, system_id: var0, sym: int, con: int):
		pass

	def morphhandleupdatemulti(self,collectionhandle: Collection, dcollectionhandle: Collection):
		pass

	def morphhandleupdatesingle(self,handleptr: Entity, dcollectionhandle: Collection, xx: float, yy: float, zz: float, sys: int):
		pass

	def morphhypermorph(self,collectionhand: Collection, xi: int, yi: int, zi: int, xx: float, yy: float, zz: float, sys: int, sym: int, con: int):
		pass

	def morphhypermorphnormal(self,collection_hand: Collection, collection_elem: Collection, sym: int, con: int, mag: float, ucollection: int =" 0"):
		pass

	def morphhypermorphvector(self,collectionhand: Collection, vec: hwTriple, sym: int, con: int, mag: float):
		pass

	def morphhyperpreview(self,collectionhand: Collection, collectionelem: Collection, xi: int, yi: int, zi: int, xx: float, yy: float, zz: float, sys: int, sym: int, con: int, vvec: hwTriple, mag: float, type: int, ucollection: int):
		pass

	def morphhyperpreviewbezier(self,dcollection: Collection, shape: Entity):
		pass

	def morphinterpolatesurf(self,n_collection: Collection, e_collection: Collection, sizbld: float, buffer: float, ndens: int, mode: int, plane_normal: hwTriple, plane_normal_base: hwTriple, node_id: var0, system_id: var0, line_list: EntityList, node_list: EntityList, sym: int, con: int, covar: int, drift: int, nugget: int, nugval: float, symm: int, type: int, draw: float, offset: float, sym_plane_normal: hwTriple, sym_plane_normal_base: hwTriple, model_shape: int, node1_entity: Entity, node2_entity: Entity):
		pass

	def morphkrigmanual(self,mode: int):
		pass

	def morphlistupdate(self,mode: int, start: int, finish: int):
		pass

	def morphloaddata(self,morphdatafile: hwString , mode: int, hand: int, shape: int):
		pass

	def morphloadmvols(self,morphmvolfile: hwString , nauto: int):
		pass

	def morphloadshape(self,filename: hwString , apply_shapes: int, filetype: int, create_elems: int, tolerance: float):
		pass

	def morphmanageedgemark(self,edge_id: int, user_mark_id: int, mode: int):
		pass

	def morphmanagefacemark(self,mvol_entity: Entity, face_id: int, mlist: int, mode: int):
		pass

	def morphmanualapplyenvelope(self,e_collection: Collection, f_collection: Collection, mode: int, mbias: float, fbias: float, integ: int, envelope: float, undisplayed: int):
		pass

	def morphmanualinit(self):
		pass

	def morphmanualrestore(self):
		pass

	def morphmapdifference(self,m_collection: Collection, f_collection: Collection, i_line_list: EntityList, i_node_list: EntityList, f_line_list: EntityList, f_node_list: EntityList, r_plane_normal: hwTriple, r_plane_normal_base: hwTriple, rotate: int, axis: int, sym: int, con: int, blend: int, mbias: float, fbias: float):
		pass

	def morphmapdifferencesurf(self,m_collection: Collection, f_collection: Collection, i_collection: Collection, t_collection: Collection, r_plane_normal: hwTriple, r_plane_normal_base: hwTriple, rotate: int, axial: int, sym: int, con: int, blend: int, mbias: float, fbias: float):
		pass

	def morphmapedgestoequationoffset(self,user_mark_id: int, equation: hwString , origin: int, origin_id: var0, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, number_of_mid_handles: int, offset: float):
		pass

	def morphmapedgestoextendedoffset(self,user_mark_id: int, collection: Collection, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, number_of_mid_handles: int, offset: float):
		pass

	def morphmapedgestolineoffset(self,user_mark_id: int, line_list: EntityList, node_list: EntityList, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, number_of_mid_handles: int, offset: float):
		pass

	def morphmapedgestonodelistoffset(self,user_mark_id: int, node_list: EntityList, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, number_of_mid_handles: int, offset: float):
		pass

	def morphmapedgestoplaneoffset(self,user_mark_id: int, plane_normal: hwTriple, plane_normal_base: hwTriple, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, number_of_mid_handles: int, offset: float):
		pass

	def morphmapedgestosurfaceoffset(self,user_mark_id: int, collection: Collection, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, number_of_mid_handles: int, offset: float):
		pass

	def morphmapedgestotacitoffset(self,user_mark_id: int, collection: Collection, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, number_of_mid_handles: int, offset: float):
		pass

	def morphmaplinestolines(self,m_collection: Collection, t_collection: Collection, i_line_list: EntityList, f_line_list: EntityList, fixed_collection: Collection, r_plane_normal: hwTriple, r_plane_normal_base: hwTriple, rotate: int, blend: int, axis: int, sym: int, con: int):
		pass

	def morphmapnormaloffset(self,collectionelem: Collection, collectionfix: Collection, sym: int, con: int, blend: int, offset: float, umark: int):
		pass

	def morphmaprecalc(self,nlist: EntityList, nmark: int, collectionedge: Collection, collectionface: Collection, mode: int):
		pass

	def morphmapsections(self,collectionelem: Collection, collectionnode: Collection, collectionline: Collection, collectionfix: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, rotate: int, blend: int, axis: int, sym: int, con: int):
		pass

	def morphmaptoequationvecoffset(self,collection_nodes: Collection, collection_handles: Collection, equation: hwString , origin: int, origin_id: var0, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, mode: int, offset: float):
		pass

	def morphmaptoextendedvecoffset(self,collection_nodes: Collection, collection_handles: Collection, collection_map: Collection, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, mode: int, offset: float):
		pass

	def morphmaptolinenodesoffset(self,list_nodes: EntityList, collection_handles: Collection, line_list: EntityList, node_list: EntityList, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, offset: float):
		pass

	def morphmaptolinevecoffset(self,collection_nodes: Collection, collection_handles: Collection, line_list: EntityList, node_list: EntityList, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, mode: int, offset: float):
		pass

	def morphmaptonodelistvecoffset(self,collection_nodes: Collection, collection_handles: Collection, node_list: EntityList, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, mode: int, offset: float):
		pass

	def morphmaptonodesnodelistoffset(self,list_nodes: EntityList, collection_handles: Collection, node_list: EntityList, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, offset: float):
		pass

	def morphmaptoplanevecoffset(self,collection_nodes: Collection, collection_handles: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, mode: int, offset: float):
		pass

	def morphmaptosurfacevecoffset(self,collection_nodes: Collection, collection_handles: Collection, collection_surfaces: Collection, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, mode: int, offset: float):
		pass

	def morphmaptotacitvecoffset(self,collection_nodes: Collection, collection_handles: Collection, collection_elems: Collection, use_symmetry: int, use_constraints: int, project: int, vector: hwTriple, mode: int, offset: float):
		pass

	def morphmaptshp(self,hptr: Entity, x: float, y: float, z: float, clear: int, sym: int, con: int):
		pass

	def morphmaptshpedge(self,dcollection: Collection, ecollection: Collection, scollection: Collection, lline: Entity, plane_normal: hwTriple, plane_normal_base: hwTriple, line: EntityList, points: EntityList, niproj: int, iproj: hwTriple, clear: int, sym: int, con: int, type: int):
		pass

	def morphmaptshpface(self,d_collection: Collection, e_collection: Collection, s_collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, nproj: int, c_vec: hwTriple, clear: int, sym: int, con: int, type: int):
		pass

	def morphmaptshpoffset(self,pcollection: Collection, tcollection: Collection, tlines: int, tpoints: int, tplane_normal: hwTriple, tplane_normal_base: hwTriple, niproj: int, iproj: hwTriple, clear: int, sym: int, con: int, type: int, offset: float):
		pass

	def morphmvskinsolve(self):
		pass

	def morphnodesequaoffset(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, equation: hwString , ori: int, oid: var0, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphnodesextendedoffset(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, t_collection: Collection, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphnodeslineoffset(self,e_collection: Collection, f_collection: Collection, t_line_list: EntityList, t_node_list: EntityList, m_node_list: EntityList, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphnodesmatrixdiffenvelope(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, matrix_array: hwDoubleList, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int):
		pass

	def morphnodesmeshoffset(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, t_collection: Collection, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphnodesnodesoffset(self,e_collection: Collection, f_collection: Collection, t_node_list: EntityList, m_node_list: EntityList, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphnodesnormalenvelope(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, n_collection: Collection, dist: float, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int):
		pass

	def morphnodesplaneoffset(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, t_plane_normal: hwTriple, t_plane_normal_base: hwTriple, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphnodesrotateenvelope(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, r_plane_normal: hwTriple, r_plane_normal_base: hwTriple, angle: float, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int):
		pass

	def morphnodesshapeenvelope(self,e_collection: Collection, f_collection: Collection, a_shape: Entity, integ: int, mbias: float, fbias: float, mult: float, envelope: float, undisplayed: int):
		pass

	def morphnodessurfoffset(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, s_collection: Collection, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphnodestranslateenvelope(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, x: float, y: float, z: float, s_system: int, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int):
		pass

	def morphnodesvectoroffset(self,m_collection: Collection, e_collection: Collection, f_collection: Collection, a_node: Entity, b_node: Entity, nproj: int, c_vec: hwTriple, integ: int, mbias: float, fbias: float, envelope: float, undisplayed: int, offset: float):
		pass

	def morphorganizedomain(self,elemcollection: Collection, domain: Entity, type: int, rethand: int):
		pass

	def morphorganizedomainsplit(self,node: Entity, domain: Entity):
		pass

	def morphpartition(self,dcollection: Collection):
		pass

	def morphpositionshapemark(self,s_collection: Collection, a_collection: Collection, n1: Entity, n2: Entity, n3: Entity, n4: Entity, n5: Entity, n6: Entity, xs: float, ys: float, zs: float, mode: int, scale: int, tol: float, system_id: int, con: int):
		pass

	def morphrecalcmvhandles(self):
		pass

	def morphrecalculateconstraints(self,type: int):
		pass

	def morphreflectshapemark(self,s_collection: Collection, sym_collection: Collection, a_collection: Collection, mode: int, tol: float, con: int):
		pass

	def morphregistergeometry(self,collection: Collection, mode: var0, target: var0):
		pass

	def morphremeshedges(self,e_collection: Collection, starg: float, size: int, skew: int, mesh: int, preserve: int, qa: int):
		pass

	def morphremoveconstraint(self,collectionnode: Collection, option: int):
		pass

	def morphrenamehandle(self,nameold: hwString , namenew: hwString ):
		pass

	def morphreparam(self,collectiondomain: Collection):
		pass

	def morphrotatetrue(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, angle: float, sym: int, con: int, vari: int):
		pass

	def morphsavedata(self,morphdatafile: hwString ):
		pass

	def morphsavemvols(self,scollection: Collection, savefile: hwString , shapes: int):
		pass

	def morphsaveshape(self,scollection: Collection, savefile: hwString , filetype: int):
		pass

	def morphsculptmesh3(self,e_collection: Collection, s_collection: Collection, t_collection: Collection, n_collection: Collection, tool: int, t_vec: hwTriple, t_line_list: EntityList, t_node_list: EntityList, t_plane_normal: hwTriple, t_plane_normal_base: hwTriple, xbase: float, ybase: float, zbase: float, tsize: float, offset: float, path: int, p_line_list: EntityList, p_node_list: EntityList, p_xyz: hwDoubleList, s_vec: hwTriple, push: int, remesh: int, solver: int, con: int, comp: float, mode: int):
		pass

	def morphsetactive(self,ecollection: Collection):
		pass

	def morphsetsmoothignoredelems(self,collection: Collection):
		pass

	def morphsetsmoothtests(self,mode: int, active: int, elem_type: int, test_id: int, warning: float, error: float, invalid: float):
		pass

	def morphshapeapply(self,shcollection: Collection, mult: float):
		pass

	def morphshapeapplynodes(self,shcollection: Collection, ncollection: Collection, mult: float):
		pass

	def morphshapecreatecolor(self,shapename: hwString , option: int, color: int):
		pass

	def morphshapecreatecolorsystem(self,name: hwString , option: int, color: int, system_id: var0):
		pass

	def morphshapecreatelist(self,name: hwString , option: int, color: int):
		pass

	def morphshapecreateorthogonal(self,s_collection: Collection, md_collection: Collection, system_entity: Entity, method: int, prec: int, tol: float):
		pass

	def morphshapecreateorthogonalbound(self,s_collection: Collection, md_collection: Collection, system_entity: Entity, method: int, prec: int, tol: float, initial: float, l_bound: float, u_bound: float):
		pass

	def morphshapelinkedapply(self,n_collection: Collection):
		pass

	def morphshapelinkedpush(self,shape_entity: Entity, mult: float):
		pass

	def morphshapepreview(self,collection: Collection, mode: int):
		pass

	def morphshapesmooth(self,shape_collection: Collection, node_collection: Collection, option: int, autofix: int, constraints: int, feature_angle: float, report_file: hwString ):
		pass

	def morphshapeupdatecolor(self,shape: Entity, color: int):
		pass

	def morphshrinkmvols(self,ccollection: Collection, buffer: float, iface: int, itermax: int, uvec: int, vec: hwTriple):
		pass

	def morphsmooth(self,dcollection: Collection, method: int, iter: int):
		pass

	def morphsmoothmorphbased(self,d_collection: Collection, f_collection: Collection, iter: int, quality_level: int, fix_type: int, fix_angle: float):
		pass

	def morphsplitmorphvolumes(self,n1: Entity, n2: Entity, split: float, hand: int, tangent: int):
		pass

	def morphstoredomains(self,mode: int):
		pass

	def morphstorematch(self,domain_id: var0, surface_id: var0, mode: int):
		pass

	def morphstoremorphvolumes(self,mode: int):
		pass

	def morphsubdivide(self,dcollection: Collection, fcollection: Collection, rethand: int):
		pass

	def morphsurfaces(self,collectionsurf: Collection):
		pass

	def morphsymmetrycreateaxis(self,name: hwString , sysptr: Entity, collectiondomain: Collection, enforce: int, multilat: int, type: int, ucyc: int, orient: int, mv: int):
		pass

	def morphsymmetryrefresh(self):
		pass

	def morphsymmetryupdateaxis(self,symptr: Entity, sysptr: Entity, collectiondomain: Collection, enforce: int, multilat: int, type: int, ucyc: int, orient: int, mv: int):
		pass

	def morphsymmetryupdatebyd(self,dptr: Entity, collectionsym: Collection):
		pass

	def morphtranslateshapemark(self,s_collection: Collection, n_collection: Collection, a_collection: Collection, base_node_entity: Entity, mode: int, tol: float, con: int):
		pass

	def morphupdatedatabase(self):
		pass

	def morphupdatedisplay(self,type: int, mode: int):
		pass

	def morphupdatedomainmethod(self,dcollection: Collection, method: int):
		pass

	def morphupdatedomains(self,mode: int):
		pass

	def morphupdateendbymvol(self,acollection: Collection, bcollection: Collection, vec: hwTriple, sysid: int, mode: int):
		pass

	def morphupdateendcondition(self,n1: Entity, n2: Entity, n3: Entity, x: float, y: float, z: float, mode: int):
		pass

	def morphupdateendconditionmultiple(self,nodeList: EntityList, endVectors: hwTripleList, mode: int ):
		pass

	def morphupdatemodelcheck(self):
		pass

	def morphupdatemvedgenodes(self,nodes: EntityList, hand: int):
		pass

	def morphupdatemvedgenodesmultiple(self,nodeList: EntityList, nmidhandles: float , mode: int , hand: int ):
		pass

	def morphupdatemvnodes(self,ccollection: Collection, ncollection: Collection):
		pass

	def morphupdatemvols(self,ccollection: Collection, han: int, ord: int, tan: int):
		pass

	def morphupdateparameter(self,parameter: hwString , value: float):
		pass

	def morphupdateparameterstring(self,parameter: hwString , value: hwString ):
		pass

	def morphupdateshapes(self,collection: Collection, mode: int):
		pass

	def morphvolumeconnect(self,hcube1: Entity, hcube2: Entity, tan: int, mode: int, nauto: int):
		pass

	def morphvolumecreate(self,ecollection: Collection, xd: int, yd: int, zd: int, buff: float, sysid: int, han: int, ord: int, tan: int):
		pass

	def morphvolumecreateflex(self,e_collection: Collection, xd: int, yd: int, zd: int, buff: float, system_id: int, han: int, order: int, tan: int, m_collection: Collection, alines: EntityList, apoints: EntityList, mlines: EntityList, mpoints: EntityList, plane_normal: hwTriple, plane_normal_base: hwTriple, method: int, drag: float):
		pass

	def morphvolumecreatenodes(self,nodes: EntityList, ecollection: Collection, han: int, ord: int, tan: int, nauto: int):
		pass

	def morphvolumecreateplus(self,ecollection: Collection, xd: int, yd: int, zd: int, buff: float, sysid: int, han: int, ord: int, tan: int, options: int):
		pass

	def morphvolumedeleteempty(self):
		pass

	def morphvolumeequivalence(self,c_collection: Collection, tol: float, tan: int, nauto: int):
		pass

	def morphvolumereflect(self,c_collection: Collection, s_collection: Collection, nauto: int):
		pass

	def morphvolumereparameterize(self):
		pass

	def morphwritenodes(self,filename: hwString , mode: int):
		pass

	def move_clipping_sphere_to_XYZ_and_fit(self,x_center: float, y_center: float, z_center: float, radius: float, n_animation: int):
		pass

	def move_feature(self,*args, **kwargs):
		"""
		move_feature(HMAPI self, Collection collection, int const NumLayers=2, hwString const & MappingMethod="auto", int const Rebuild=1, hwIntList StitchBoundary=hwIntList(), hwMatrix44 TransformByMatrix=hwMatrix44(1.0), hwIntList TransformByNodes=hwIntList())
		"""
		pass

	def movecuttingplane(self,axis: int, distance: float):
		pass

	def moveinclude(self,filebeingmoved: hwString , newparent: hwString ):
		pass

	def moveincludecontents(self,source_id: var0, source_shortname: hwString , dest_shortname: hwString , delete_flag: int):
		pass

	def movemark(self,collection: Collection, name: hwString ):
		pass

	def movemarkgroup(self,collection: Collection, name: hwString ):
		pass

	def movesegments(self,set_ids: hwIntList, elem_ids: hwIntList, face_indices: hwIntList, to_segment: hwString ):
		pass

	def movesolvermasses(self,solvermass_collection: Collection, target_solvermass_id: var0):
		pass

	def movesubmodel(self,source_submodel_type: hwString , source_filename: hwString , target_submodel_type: hwString , target_filename: hwString ):
		pass

	def movevectorstodesvar(self,collection: Collection, collector: hwString ):
		pass

	def multi_surfs_lines_merge(self,surf_collection: Collection, line_collection: Collection, options: int):
		pass

	def multi_trim_by_offset_edges(self,surfaces: Collection, lines: Collection, offset_distance: float  =" 0_module.0", offset_count: int  = 1):
		pass

	@property
	def name(self):
		pass
	@name.setter
	def name(self):
		pass

	def nameview(self,number: int, name: hwString ):
		pass

	def new_failed_elements_cleanup(self,collection: Collection, elem_type: int, max_feature_angle: float):
		pass

	def newidoption(self,*args, **kwargs):
		"""
		newidoption(HMAPI self, hwString const & id, unsigned int option, hwString const & using_maxid=s_defaultString)
		"""
		pass

	def nodecleartempmark(self):
		pass

	def nodecreateatintersection(self,collection1: Collection, collection2: Collection, point_flag: int):
		pass

	def nodecreateatlinemarkparams(self,collection: Collection, params: hwDoubleList, insert_count: int, mode: int, point_flag: int):
		pass

	def nodecreateatlineparams(self,line_entity: Entity, float_array: hwDoubleList, insert_count: int, mode: int, point_flag: int):
		pass

	def nodecreateatplaneintersection(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, plane_use: int, point_flag: int):
		pass

	def nodecreateatpointmark(self,collection: Collection):
		pass

	def nodecreateatsurfparams(self,surf_entity: Entity, u1: float, u2: float, ucount: int, v1: float, v2: float, vcount: int, mode: int, point_flag: int):
		pass

	def nodecreateatvectorplaneintersection(self,vector: hwTriple, vector_base: hwTriple, plane_or_vector: hwTriple, plane_or_vector_base: hwTriple, vector_use: int, plane_use: int, point_flag: int):
		pass

	def nodecreatebetweennodes(self,entity: Entity, node_list: EntityList, num_intervals_array: hwIntList, biasstyle: int, biasintensity: float, options: int):
		pass

	def nodecreateonlines(self,collection: Collection, number: int, bias_style: int, bias_intensity: float):
		pass

	def nodelistbypath(self,node_entity1: Entity, node_entity2: Entity, list: EntityList):
		pass

	def nodelistbypath2(self,nodeA: Entity, nodeB: Entity, list: EntityList, ignoreEdgeFlag: int, search_factor: float  =" 1_module.0"):
		pass

	def nodemarkaddtempmark(self,collection: Collection):
		pass

	def nodemarkbypath(self,node_entity1: Entity, node_entity2: Entity, collection: Collection):
		pass

	def nodemarkclear(self,node_collection: Collection, clearTempNodes: int , clearPreservedNodes: int ):
		pass

	def nodemarkcleartempmark(self,collection: Collection):
		pass

	def nodemodify(self,nodeentity: Entity, x: float, y: float, z: float):
		pass

	def nodeplaceatxyz(self,node: Entity, surface: Entity, location: float, y: float, z: float):
		pass

	def nodesandelemsclear(self):
		pass

	def nodesassociatetogeometry(self,collection: Collection, entity: Entity, tolerance: float):
		pass

	def nodesassociatetogeometry2(self,nodecollection: Collection, ententity: Entity, reasso: int, snap_tol: float, prj_tol: float, xthr: float):
		pass

	def nodetoelementgapscreate(self,gaps_location: Collection, target_elems: Collection, face_nodes: Collection, break_angle: float, property_name: hwString , tolerance: float, vectorentity: Entity, nodeentity: Entity, orient_x: float, orient_y: float, orient_z: float, comps_flag: int, systementity: Entity):
		pass

	def nonstructuralmasscreate(self,name: hwString , color: int, type: var1, mass: float, collection: Collection):
		pass

	def nonstructuralmasscreateall(self,name: hwString , color: int, type: var1, mass: float, card_image: hwString ):
		pass

	def nonstructuralmassupdate(self,name: hwString , color: int, type: var1, mass: float, collection: Collection):
		pass

	def nonstructuralmassupdateall(self,name: hwString , color: int, type: var1, mass: float, card_image: hwString ):
		pass

	def normalsadjust2(self,collection: Collection, mode: int, orientation_element: Entity, size: float, display: int, vector: hwTriple, feature_angle: float):
		pass

	def normalsadjustbynodes(self,entity_type: EntityFullType, collection: Collection, node_collection: Collection, size: float, display: int):
		pass

	def normalsdisplay(self,collection: Collection, size: float):
		pass

	def normalsoff(self):
		pass

	def normalsreverse(self,collection: Collection, size: float):
		pass

	def numbers(self,on: int):
		pass

	def numbersclear(self):
		pass

	def numbersmark(self,type: Collection, mar: int):
		pass

	def offset_elements_to_middle(self,source_elements: Collection, target_elements: Collection, to_current_comp: int):
		pass

	def offset_surfaces_and_modify(self,collection: Collection, surf_collection: Collection, line_collection: Collection, offset_type: int, offset: float):
		pass

	def offset_surfaces_display_offset(self,collection: Collection, reserved_1: int):
		pass

	def offset_surfaces_edit_links(self,surfcollection: Collection, vert_collection1: Collection, vert_collection2: Collection, what_to_do: int, tol: float):
		pass

	def offset_surfaces_on_surfaces(self,surf_to_offset: Collection, base_surf: Collection, offset_limit: float, set_thickness: int, delete_base: int, debug_mode: int):
		pass

	def offset_surfaces_remove_links_display(self):
		pass

	def offset_surfaces_update_removable(self,surfcollection: Collection, what_to_do: int):
		pass

	def optimized_elements_remesh2(self,collection: Collection, criteria_file: hwString , elem_size: float, elem_type: int, feature_angle: float, vertex_angle: float, comp_mode: int, break_flag: int, algorithm: int):
		pass

	def optimized_mesh(self,collection: Collection, filename: hwString , elem_size: float, elem_type: int, smooth_across: int, feature_angle: float, algorithm: int, do_remesh: int, comp_mode: int):
		pass

	def optimsmooth(self,smoothcollection: Collection, anchorcollection: Collection, criteria_filename: hwString , feature_angle: float, target_QI: float, max_iterations: int, time_limit: int):
		pass

	def orderchangetofirst(self,collection: Collection):
		pass

	def orderchangetosecond(self,collection: Collection, doproject: int, tacitmode: int):
		pass

	def organizeRegionsAcrossModules(self,region_collection: Collection, source_part_name: hwString ):
		pass

	def orient_normals_outside_solid(self,collection: Collection, orientation: int):
		pass

	def ossmooth2(self,femfile: hwString , load_op: int, outputcode: int, tetrameshingcode: int, units: int, autobead: int, autobeadthreshold: float, autobeadlayer: int, isosurface: int, surfacecode: int, densitythreshold: float, distancecoefficient: float, optismoothboundary: int, lapiteration: int, lapfeatureangle: float, lapsmoothboundary: int, remesh: int, surfacereduction: int, reductionfeatureangle: float):
		pass

	def ossmooth_12(self,modelsel: int, exemode: int, load_op: int, outputcode: int, filepath_fem: hwString , filepath_sh: hwString , filepath_grid: hwString , isosurface: int, autobead: int, string_array: hwStringList):
		pass

	def ossmooth_createsurf_auto(self,feature_angle: float, options: int, complexity: int, tolerance: float, reserved: int):
		pass

	def ossmooth_geometry(self,modelsel: int, fem_filename: hwString , filepath_grid: hwString , filepath_sh: hwString , load_op: int, outputcode: int, tetrameshingcode: int, units: int, autobead: int, autobeadthreshold: float, autobeadlayer: int, isosurface: int, surfacecode: int, densitythreshold: float, detectbridge: int, lowthreshold: float, distancecoefficient: float, optismoothboundary: int, lapiteration: int, lapfeatureangle: float, lapsmoothboundary: int, remesh: int, surfacereduction: int, reductionfeatureangle: float, createplotel: int):
		pass

	def ossmooth_reanalysis(self,modelsel: int, filepath_fem: hwString , sh_filename: hwString , mode: int, densitythreshold: float, createplotel: int, detectbridge: int, lowthreshold: float):
		pass

	def ossmooth_savesurf(self,mode: int, filepath: hwString , units: int, output: int):
		pass

	def panelcreation(self,collection: Collection, name: hwString , findPanel: int):
		pass

	def parmtran(self,filename: hwString ):
		pass

	def parsesolveroutputfile(self,*args, **kwargs):
		"""
		parsesolveroutputfile(HMAPI self, hwString const & filename, hwString const & filetype="f06", hwString const & extractdata="fluttercurves")
		"""
		pass

	def partisolatesupressall(self,oldid: var0, newid: var0):
		pass

	def pastefromclipboard(self,*args, **kwargs):
		"""
		pastefromclipboard(HMAPI self, hwString const & targetmodel="", bool const connectors_checkattribute=False, bool const connectors_layercheck=False, bool const connectors_thicknesscheck=False, double const connectors_tolerance=0.000000, hwString const & dropincomingmodulehierarchy="", hwString const & mergemode_comps="", hwString const & mergemode_connectors="", hwString const & mergemode_geometryandmesh="", hwString const & mergemode_mats="", hwString const & mergemode_modules="", hwString const & mergemode_props="", hwString const & respectincomingparentmodule="")
		"""
		pass

	def pause_events(self):
		pass

	def penetrationcheck(self,collection: Collection, check_type: int):
		pass

	def penetrationcheckend(self):
		pass

	def penetrationchecktwo(self,collection1: Collection, collection2: Collection, segment_orientation: int, partscale_contthick_toggle: int, part_scale: float, cont_thick: float):
		pass

	def penetrationdisplay(self,contact_thickness: float, part_thickness_scale: float, display_mode: int, normal_scale: float, label: int, segment_orientation: int, magnitude_mode: int):
		pass

	def penetrationrecheck(self,collection: Collection, reduction: float, scale: float, display_mode: int, normal_scale: float, label: int, segment: int, magnitude_mode: int):
		pass

	def permutemark(self,collection: Collection, type: int):
		pass

	def perturbationshapecreate(self,name: hwString , vectorcolid: var0):
		pass

	def perturbationshapecreatecolor(self,name: hwString , vectorcolid: var0, color: int):
		pass

	def perturbationshapeupdate(self,name: hwString , vectorcolid: var0):
		pass

	def perturbationshapeupdatecolor(self,name: hwString , vectorcolid: var0, color: int):
		pass

	def plot(self):
		pass

	def plotaxisnodes(self,collection: Collection, axis: int):
		pass

	def plotinfotitlemove(self,xmin: float, ymin: float, xmax: float, ymax: float):
		pass

	def plotinfotitlesetcolor(self,color: int):
		pass

	def plotinfotitlesetfont(self,font: int):
		pass

	def plotinfotitlesettext(self,text: hwString ):
		pass

	def plotmassdistribution(self,solvermass_id: var0):
		pass

	def plotnodelist(self,list: EntityList):
		pass

	def plottitlemove(self,xmin: float, ymin: float, xmax: float, ymax: float):
		pass

	def plottitlesetcolor(self,color: int):
		pass

	def plottitlesetfont(self,font: int):
		pass

	def plottitlesettext(self,text: hwString ):
		pass

	def plyabsorb(self,collection: Collection):
		pass

	def plydrape(self,*args, **kwargs):
		"""
		plydrape(HMAPIBase self, Collection plies_collection, hwString const & application="", Entity ply_entity=hwDescriptor::Entity(), double const seed_point_x=0.000000, double const seed_point_y=0.000000, double const seed_point_z=0.000000, double const draping_direction_x=0.000000, double const draping_direction_y=0.000000, double const draping_direction_z=0.000000, double const draping_normal_x=0.000000, double const draping_normal_y=0.000000, double const draping_normal_z=0.000000, double const elem_size=0.000000, double const locking_angle=0.000000, double const relaxation_angle=0.000000, hwString const & quadrants="Yes", hwString const & continuations="Yes", int const directions=15, int const projection=0, Entity closest_elem=hwDescriptor::Entity(), hwString const & surface_approx="default")
		"""
		pass

	def plynormalsdisplay(self,ply_name: hwString , collection: Collection, size: float):
		pass

	def plynormalsreverse(self,ply_name: hwString , collection: Collection, size: float):
		pass

	def plyrealization_option(self,ply_collection: Collection, collection: Collection, project: int, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, reserved1: int, search_option: int, reserved2: int, shrinkage: float, table_id: int, float_array: hwDoubleList, reserved3: int, reserved4: float):
		pass

	def pointcreateatnodemark(self,collection: Collection):
		pass

	def pointmodify(self,point_entity: Entity, x: float, y: float, z: float):
		pass

	def positiondummy(self,collectorentity: Entity, x: float, y: float, z: float):
		pass

	def positionentity(self,*args, **kwargs):
		"""
		positionentity(HMAPIBase self, Entity entity, hwTripleList source_coords=hwTripleList(), hwTripleList target_coords=hwTripleList(), EntityList source_nodes=s_defaultEntityList, EntityList target_nodes=s_defaultEntityList)
		"""
		pass

	def positionentity_bycollection(self,*args, **kwargs):
		"""
		positionentity_bycollection(HMAPIBase self, Collection collection, hwTripleList source_coords=hwTripleList(), hwTripleList target_coords=hwTripleList(), EntityList source_nodes=s_defaultEntityList, EntityList target_nodes=s_defaultEntityList)
		"""
		pass

	def positionipimpact(self,*args, **kwargs):
		"""
		positionipimpact(HMAPI self, hwIntList instrumentpanelids=hwIntList(), hwIntList headformids=hwIntList(), Entity headformsystemid=hwDescriptor::Entity(), hwIntList designpointids=hwIntList(), Entity pivotnodeid=hwDescriptor::Entity(), hwTriple vehiclefrontaxis=hwTriple(1.000000, 0.000000, 0.000000), hwString const & mainfilepath="", hwString const & headformfilepath="", hwString const & exportpath="", int const dpnamefordirandincludes=1, int const folderforeachdp=0, int const mode=1, hwString const & csvfile="")
		"""
		pass

	def positionmark(self,collection: Collection, node1: Entity, node2: Entity, node3: Entity, node4: Entity, node5: Entity, node6: Entity):
		pass

	def postmesh_element_optimization(self,type: int, do_save: int):
		pass

	def pre_tesselation_cleanup(self,collection: Collection, min_size: float, max_size: float, max_chordal: float, max_angle: float):
		pass

	def prepare_solid_holes_for_meshing(self,input_collection: Collection, output_collection: Collection, string_array: hwStringList):
		pass

	def pressureonelement_curve(self,entity: Entity, face_index: int, x_comp: float, y_comp: float, z_comp: float, magnitude: float, curve_id: var0, x_scale: float):
		pass

	def pressures(self,collection: Collection, face_nodes: Collection, x_comp: float, y_comp: float, z_comp: float, magnitude: float, break_angle: float, on_face: int):
		pass

	def pressuresonentity(self,collection: Collection, nodes_collection: Collection, x: float, y: float, z: float, magnitude: float, breakangle: float, onface: int):
		pass

	def pressuresonentity_curve(self,collection: Collection, facenodes: Collection, x_comp: float, y_comp: float, z_comp: float, magnitude: float, breakangle: float, onface: int, xlocation: float, ylocation: float, zlocation: float, curve_id: var0, x_scale: float):
		pass

	def pressuresonentity_function(self,collection: Collection, facenodes: Collection, x: float, y: float, z: float, magnitude: float, breakangle: float, onface: int, xlocation: float, ylocation: float, zlocation: float, function: hwString , systemptr: Entity):
		pass

	def processflange(self,surf_collection: Collection, point_collection: Collection, distance_tol: float, angle_tol: float):
		pass

	def project_mesh_to_mesh(self,s_mesh_collection: Collection, t_mesh_collection: Collection, max_proj_distance: float, proj_clearance: float):
		pass

	def projectlinetomeshcomp(self,list: EntityList, collection: Collection):
		pass

	def projectmarktoplane(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, vector: hwTriple, toplane: int):
		pass

	def projectpointstoedges(self,edge_collection: Collection, point_collection: Collection, distance_tol: float, angle_tol: float):
		pass

	def projectsystem(self,collection: Collection, vectorptr: hwTriple, onlyorient: int, normal_size: float, color: int):
		pass

	def propagate_welds(self,surfscollection: Collection, max_proxim: float, min_edge_len: float, max_angle_dev: float, select_exten_flag: int, meshed_touch_flag: int):
		pass

	def propagatesplithexas(self,splittype: int, startelement: Entity, n1: Entity, n2: Entity):
		pass

	def pushtofront(self,entity_type: EntityFullType, mode: int):
		pass

	def putelemstorestore(self,collection: Collection, do_clean_restorelist: int):
		pass

	def qa_amesh_checkup(self,name: hwString ):
		pass

	def qa_amesh_header(self,name: hwString ):
		pass

	def qa_checklines(self):
		pass

	def qaclosereffile(self):
		pass

	def qaopenreffile(self,name: hwString ):
		pass

	def qawritegeometrycount(self,filename: hwString ):
		pass

	def qawritetopology(self,name: hwString ):
		pass

	def qi_result_summary(self,collection: Collection, criteria_file_name: hwString , result_file_name: hwString , mode: int):
		pass

	def qismoothconstrained(self,smoothcollection: Collection, anchorcollection: Collection, criteria_file: hwString , feature_angle: float, goal_qi: float, ignore_features: int, constr_flags: int, stifflimit: float, toughlimit: float, midlimit: float, looselimit: float, max_iteration: int, time_limit: int):
		pass

	def qismoothconstrained2(self,smoothcollection: Collection, anchorcollection: Collection, criteria_file: hwString , feature_angle: float, goal_qi: float, free_edges_moveoffemax: float, shared_featedges_moveoffemax: float, shared_notfeatedges_moveoffemax: float, algflags: int, max_iterations: int, time_limit: int):
		pass

	def qismoothfixfailed(self,smoothcollection: Collection, anchorcollection: Collection, criteria_file: hwString , feature_angle: float, ignore_features: int, freenodesmovelimit: float, breaknodesmovelimit: float, smoothedgenodesmovelimit: float, flgs: int, max_iterations: int):
		pass

	def quad_split(self,collection: Collection, _ctrls: hwString ):
		pass

	def quatrotate(self,q0: float, q1: float, q2: float, q3: float):
		pass

	def rbe3(self,collection: Collection, independent_dofs: hwIntList, independent_weights: hwDoubleList, dependent_node: Entity, dof: hwBoolList, weight: float):
		pass

	def rbe3withset(self,collection: Collection, indepdofsarray: hwIntList, indepwtsarray: hwDoubleList, dep_node: Entity, dofs: hwBoolList, wts: float, attach_set: int):
		pass

	def rbody_mesh(self,collection: Collection, min_size: float, max_size: float, max_chordal: float, max_angle: float, remesh: int, mesh_type: int, elem_comp: int, elem_order: int, shared_edge_flag: int):
		pass

	def readFldFile(self,filename: hwString ):
		pass

	def readMaterialFile(self,matfile: hwString ):
		pass

	def readbatchparamsfile(self,params_filename: hwString ):
		pass

	def readfile(self,filename: hwString , load_cad_geometry_as_graphics: int):
		pass

	def readfileautostitch(self,name: hwString , autostitch: int, cleanup_tol: float):
		pass

	def readfilesubst(self,name: hwString ):
		pass

	def readmeshcontroltemplate(self,filename: hwString , mode: int =" 0"):
		pass

	def readnodepositionsfromdynainfile(self,path: hwString , options: hwString ):
		pass

	def readnodepositionsfromh3dfile(self,*args, **kwargs):
		"""
		readnodepositionsfromh3dfile(HMAPI self, hwString const & path, unsigned int animation_number=0, unsigned int create_initial_xref_cards=0, Collection comps_collection=s_defaultCollection)
		"""
		pass

	def readqiviewsettings(self,file: hwString ):
		pass

	def readqualitycriteria(self,file_name: hwString ):
		pass

	def realizeabaqussurfacetogroups(self):
		pass

	def realizeabaqussurfacetosets(self):
		pass

	def realizecontactsurfstosets(self,card_image: hwString ):
		pass

	def realizecsfbdsectiontostdfbdsection(self,freebodysection_ids: EntityList):
		pass

	def realizedxentities(self,skipDelete: var0):
		pass

	def realizeengineeringentities(self,collection: Collection, reserved: int):
		pass

	def realizeengineeringentity(self,entity: Entity, reserved: int):
		pass

	def realizeengineeringentitymanagementbyid(self,entityptr_eng: Entity, action: int, entityptr: Entity, flag: int):
		pass

	def realizeengineeringentitymanagementbymark(self,entityptr_eng: Entity, action: int, collection: Collection, flag: int):
		pass

	def realizefieldloads(self,collection: Collection, skip_delete: var0):
		pass

	def realizehmentity(self,*args, **kwargs):
		"""
		realizehmentity(HMAPI self, Collection markmask, EntityFullType targetentitytype=hwDescriptor::EntityFullType((unsigned int)2))
		"""
		pass

	def realizemasselementstosolvermasses(self,collection: Collection):
		pass

	def realizerigidbodiestoproperties(self):
		pass

	def realizesetstocontactsurfs(self,card_image: hwString ):
		pass

	def realizesolvermassestomasselements(self,collection: Collection):
		pass

	def rebuild_mesh(self,collection: Collection):
		pass

	def rebuild_mesh_advanced(self,*args, **kwargs):
		"""
		rebuild_mesh_advanced(HMAPIBase self, Collection collection, hwTripleList flow_guides=hwTripleList(), hwString const & keep_selection="", hwString const & mode="")
		"""
		pass

	def recalculaterigidmainnode(self,collection: Collection):
		pass

	def redohistorystate(self,count: var0):
		pass

	def referencegeometrycreatesameas(self,collection: Collection, name: hwString , sameasname: hwString ):
		pass

	def refine_adaptive(self,collection: Collection, string_array: hwStringList):
		pass

	def refine_by_patterns(self,*args, **kwargs):
		"""
		refine_by_patterns(HMAPIBase self, Collection collection, Entity node, int const auto_transition, double const refine_zone_height, double const refine_zone_length, double const refine_zone_size, double const refine_zone_width, int const squeez, double const transition_zone_height, double const transition_zone_length, double const transition_zone_width, Entity system=hwDescriptor::Entity())
		"""
		pass

	def refine_by_patterns_multiple_points(self,collection: Collection, strings: hwString ):
		pass

	def refineelementsbydeviation(self,collection: Collection, deviation: float, minlength: float):
		pass

	def refineelementsbydeviationwith1D(self,collection: Collection, deviation: float, minlength: float):
		pass

	def refineelementsbysize(self,collection: Collection, maxlength: float):
		pass

	def refineelementsbysizewith1D(self,collection: Collection, maxlength: float):
		pass

	def reflectmark(self,collection: Collection, plane_normal: hwTriple, plane_base: hwTriple):
		pass

	def reflectmarkwithoption(self,collection: Collection, plane_normal: hwTriple, plane_base: hwTriple, option: int):
		pass

	def regionsetcreate(self,name: hwString , color: int):
		pass

	def rejectmesh(self,faceindex: var0):
		pass

	def relativerotatedummyjoint(self,collectorentity: Entity, axis: int, rotAngle: float, parentChild: int):
		pass

	def release_temp_fixed_vertices(self):
		pass

	def remap(self,nodelist: EntityList, linelist: EntityList, endpoints: EntityList):
		pass

	def remesh_element_intersection(self,collection: Collection, params: hwString ):
		pass

	def remesh_main_secondary_boolean(self,selected_collection: Collection, main_collection: Collection, strings: hwString ):
		pass

	def remesh_optistruct(self,*args, **kwargs):
		"""
		remesh_optistruct(HMAPI self, hwString const & fgrd="", hwString const & fsh="", hwString const & fdesvar="", hwString const & fhist="")
		"""
		pass

	def remove_coarsening(self):
		pass

	def remove_dynain(self):
		pass

	def remove_fe_cracks(self,collection: Collection, stitch_tol: float):
		pass

	def remove_gravity(self):
		pass

	def remove_implicitgravity(self):
		pass

	def remove_mapping(self):
		pass

	def remove_solid_holes(self,collection: Collection, max_diam: float, cross_sect_size_max: float, options: int, string_array: hwStringList):
		pass

	def remove_springback(self,ticon: int):
		pass

	def remove_trimming(self):
		pass

	def remove_volumes(self,ety: EntityFullType, collection: Collection, param_str: hwString ):
		pass

	def removeassembly(self,collection: Collection):
		pass

	def removecrbrelation(self,collection: Collection):
		pass

	def removecutbetweenlocations(self,location1: hwTriple, location2: hwTriple):
		pass

	def removeedgefillets(self,collection: Collection, min_radius: float, max_radius: float, min_angle: float, failed_elem_size: float):
		pass

	def removeelemsfromcontactsurf(self,name: hwString , elem_collection: Collection):
		pass

	def removeelemsfromcontactsurfusingnodes(self,name: hwString , elem_collection: Collection, node_collection: Collection):
		pass

	def removefeaturesbysurfacemark(self,collection: Collection, flags: int, stringinput: hwStringList):
		pass

	def removefilletbetweennodes(self,nodes: EntityList):
		pass

	def removeinclude(self,*args, **kwargs):
		"""
		removeinclude(HMAPIBase self, unsigned int id=0, hwString const & shortname="", int removecontents=0)
		"""
		pass

	def removeincludefromdisplay(self,id: var0, shortname: hwString ):
		pass

	def removeincludes(self,include_ids: hwIntList, remove_contents: bool  = False):
		pass

	def removeposition(self,collection1: Collection, collection2: Collection):
		pass

	def removesubmodel(self,submodel_type: hwString , id: var0, shortname: hwString , remove: int):
		pass

	def removetempcleanupfile(self):
		pass

	def removetransformation(self,collection1: Collection, collection2: Collection):
		pass

	def removeunnecessaryassemblies(self):
		pass

	def removeview(self,name: hwString ):
		pass

	def renamecollector(self,entity_type: EntityFullType, collector_name: hwString , new_name: hwString ):
		pass

	def renamecollectorbyid(self,entity: EntityFullType, type: hwString ):
		pass

	def renamefile(self,oldname: hwString , newname: hwString ):
		pass

	def renameviewmask(self,old_name: hwString , new_name: hwString ):
		pass

	def renumber(self,collection: Collection, start_id: var0, incr_val: var0, offset_val: int, offset_flag: int):
		pass

	def renumberall(self,start_id: var0, incr_val: var0, offset_val: int, offset_flag: int):
		pass

	def renumberelemsnodesasmapgrid(self,elem_collection: Collection, origin_node_id: int, x_ref_node_id: int, elem_start_id: int, node_start_id: int):
		pass

	def renumbersolverid(self,collection: Collection, start_id: var0, incr_val: var0, offset_val: int, offset_flag: int, reserved_1: int, reserved_2: int, reserved_3: float):
		pass

	def renumbersolveridall(self,start_id: var0, incr_val: var0, offset_val: int, offset_flag: int, reserved_1: int, reserved_2: int, reserved_3: float):
		pass

	def renumbersolveridlist(self,entity_list: EntityList, start_id: var0, incr_val: var0, offset_val: int, offset_flag: int, reserved_1: int, reserved_2: int, reserved_3: float):
		pass

	def reorderinclude(self,id_to_move: var0, id_of: var0, predecessor: int):
		pass

	def reorganizeindependentloads(self):
		pass

	def repair_midmesh_line_imprinter(self,*args, **kwargs):
		"""
		repair_midmesh_line_imprinter(HMAPI self, EntityList line_list, Collection GuideSurfaceCollection=hwDescriptor::Collection(), double const LineEndSnapTolerance=0.000000, hwTriple ProjectionDirection=hwTriple(0.000000, 0.000000, 0.000000), double const ProjectionType=2.000000, Collection ProjectOnElemsCollection=hwDescriptor::Collection())
		"""
		pass

	def reparammark(self,collection: Collection):
		pass

	def replacenodes(self,*args, **kwargs):
		"""
		replacenodes(HMAPI self, Entity source_node=hwDescriptor::Entity(), Entity target_node=hwDescriptor::Entity(), EntityList source_list=s_defaultEntityList, EntityList target_list=s_defaultEntityList, int const equiv=1, int const midpoint=0, int const collapse_check=1)
		"""
		pass

	def replacenodes_multiple(self,sourcelist: EntityList, targetlist: EntityList, equivalence: int, midpoint: int):
		pass

	def replacentitywithentity(self,*args, **kwargs):
		"""
		replacentitywithentity(HMAPIBase self, int mode, EntityFullType entity_type, int existing_id, int incoming_id, double const tolerance=0.01, int const keep_src_prop=0, int const keep_src_mat=0, int const keep_src_comp_cardimage=0, int const keep_src_include=0, hwString const & log_file="")
		"""
		pass

	def replacentitywithentitymark(self,*args, **kwargs):
		"""
		replacentitywithentitymark(HMAPI self, int mode, Collection existing_component_collection, Collection incoming_component_collection, double const tolerance=0.000000, double const customBBoxTolForEquivalencingIncomingIds=0.000000, unsigned int const keepSrcProp=0, unsigned int const keepSrcMat=0, unsigned int const keepSrcCompCardimage=0, unsigned int const logFile=0, unsigned int const keepSrcCompId=0, unsigned int const keepSrcInclude=0, unsigned int const replaceByFileImport=0, unsigned int const compsInFileImport=0, unsigned int const deleteSrcComp=0, unsigned int const autoPreserveConnections=0, unsigned int const mergeNodes=0, unsigned int const boxApproachNset=0, unsigned int const bvtRun=0, unsigned int const keepSrcEtType=0, unsigned int const incomingIncludeId=0, hwString const & componentPairingString="", unsigned int const retainPlotelElemNodeIdsFromSrcComp=0, unsigned int const prefixBasenameSuffixBasedNamePairing=0)
		"""
		pass

	def rescanunresolvedids(self):
		pass

	def resetFldList(self):
		pass

	def resetMaterialList(self):
		pass

	def reset_elemsize_criteria(self,elementsize: float):
		pass

	def reset_thickness_legend(self):
		pass

	def resetcuttingplanesbase(self,x: float, y: float, z: float):
		pass

	def resetfacets(self):
		pass

	def resetoptimizationattributes(self):
		pass

	def resetreview(self):
		pass

	def resize(self,on: int):
		pass

	def resolve_folded_facets(self,collection: Collection):
		pass

	def restoreoptimizationentitiesafterdelete(self):
		pass

	def restoresuppressededges(self,collection: Collection):
		pass

	def restoreviewmask(self,view_name: hwString , visible: int):
		pass

	def resume_events(self):
		pass

	def retainmarkselections(self,mode: int):
		pass

	def reversecontactsurfnormals(self,name: hwString , elemcollection: Collection, indelems: int):
		pass

	def reverseview(self,name: hwString , entity_type_id: int):
		pass

	def reviewairbag(self,collection: Collection, name: hwString ):
		pass

	def reviewclearall(self):
		pass

	def reviewclearbyid(self,entity: Entity, review_type: int):
		pass

	def reviewclearbymark(self,collection: Collection):
		pass

	def reviewcontactnormalinconsistency(self,entity_type: EntityFullType, name: hwString , flag: int =" 0", elements_3d_flag: int =" 0"):
		pass

	def reviewentity(self,entity: Entity, color: int, showcomps: bool  = False):
		pass

	def reviewentity_byname(self,entity_type: EntityFullType, entity_name: hwString , color: int, showcomps: bool  = False):
		pass

	def reviewentitybymark(self,*args, **kwargs):
		"""
		reviewentitybymark(HMAPI self, CollectionSet collection_set, int color=0, hwString const & showcomps="", hwString const & refflag="", hwString const & elements_off="", hwString const & geometry_off="", hwString const & plots_off="")
		"""
		pass

	def reviewmaterialorientation(self,collection: Collection, onlyorient: int, normal_size: float, color: int):
		pass

	def reviewmaterialorientation_option(self,collection: Collection, only_orient: int, normal_size: float, color: int, option: int):
		pass

	def reviewreferencegeometry(self,collection: Collection, name: hwString ):
		pass

	def reviewsystem(self,collection: Collection, onlyorient: int, normal_size: float, color: int):
		pass

	def reviewtwomark(self,collection_set1: CollectionSet, collection_set2: CollectionSet, color1: int, color2: int):
		pass

	def rigid(self,node1: Entity, node2: Entity, dofs: hwBoolList):
		pass

	def rigidlink(self,independent: Entity, collection: Collection, dofs: int):
		pass

	def rigidlinkbycollector(self,node_entity: Entity, collection: Collection, dofs: int):
		pass

	def rigidlinkinodecalandcreate(self,node_collection1: Collection, set_id: var0, attach_set_option: int, dof: hwBoolList):
		pass

	def rigidlinkupdatebycollector(self,element_entity: Entity, node_entity: Entity, collection_set: CollectionSet, entity_type: EntityFullType):
		pass

	def rigidlinkupdatecalcinodebycollector(self,element_entity: Entity, collection_set: CollectionSet, entity_type: EntityFullType):
		pass

	def rigidlinkwithset(self,independent: Entity, collection: Collection, dependent_set: var0, dof: hwBoolList):
		pass

	def rigidlinkwithset_twonodes(self,independent: Entity, dependent: Entity, dof: hwBoolList):
		pass

	def rigidpart(self,partname: hwString , fixed: int):
		pass

	def rigidscombine(self,collection: Collection, combine_common_inode: int):
		pass

	def rigidwall_geometry(self,name: hwString , geometrytype: var1, basenode: Entity, vectors: hwTriple, n1: Entity, n2: Entity, geomvar1: float, geomvar2: float, geomvar3: float):
		pass

	def rigidwallsize(self,size: float):
		pass

	def rlinkcalcinodeandcreateforcollector(self,collection: Collection, dof: hwBoolList):
		pass

	def rod(self,node1: Entity, node2: Entity, property: hwString ):
		pass

	def rotate(self,axis: float, angle: float):
		pass

	def rotateabout(self,overridedefault: int, x: float, y: float, z: float):
		pass

	def rotateandtransform(self,rx: float, ry: float, rz: float, tx: float, ty: float, tz: float):
		pass

	def rotatedummy(self,collectorentity: Entity, plane_normal: hwTriple, plane_normal_base: hwTriple, increment: float):
		pass

	def rotatedummyrootbodytoeulerangles(self,name: hwString , ax: float, ay: float, az: float, cx: float, cy: float, cz: float):
		pass

	def rotatemark(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, angle: float):
		pass

	def rundesignmethod(self,*args, **kwargs):
		"""
		rundesignmethod(HMAPI self, Entity entity, unsigned int const appendlogfile=0, hwString const & columnLabels="", unsigned int const debugInfo=1, hwString const & loadcaselist="", unsigned int const logfileInfo=1, unsigned int const tableInfo=0, unsigned int const tableperloadcase=0, Collection targetentityCollection=hwDescriptor::Collection())
		"""
		pass

	def save(self,path: str, embed_connection_files: bool, **connection_file_formats):
		pass

	def saveFldFile(self,filename: hwString ):
		pass

	def saveMaterialFile(self,filename: hwString ):
		pass

	def save_connection(self,connection_name: str, file_path: str, collection_set: hwdescriptor_module.CollectionSet = None, save_format: hwdescriptor_module.MDIFormat = None):
		pass

	def save_sl_gda(self,type: int, gda_fn: hwString ):
		pass

	def savefailednodesvectors(self,collection: Collection, reduction: float, scale: float, segment: int, magnitude_mode: int):
		pass

	def savefailedsurfstomark(self,surfs_collection: Collection):
		pass

	def saveviewmask(self,view_name: hwString , visible: int):
		pass

	def scale_thickness(self,collection: Collection, add: float  =" 0_module.0", multiply: float  =" 0_module.0", MaxThickness: float  =" 0_module.0", MinThickness: float  =" 0_module.0"):
		pass

	def scalemark(self,collection: Collection, scale_x: float, scale_y: float, scale_z: float, origin: Entity):
		pass

	def scalemarkwithsystem(self,collection: Collection, scale_x: float, scale_y: float, scale_z: float, system_entity: Entity, origin: Entity):
		pass

	def screencopy(self):
		pass

	def screenfile(self):
		pass

	def seatbelttensioning(self,*args, **kwargs):
		"""
		seatbelttensioning(HMAPI self, hwString const & seatbelth3dfile, Entity seatbelt_entity, hwString const & beltendtopull="", double const seatbeltextension=0.000000, hwString const & seatbeltcutend="")
		"""
		pass

	def secondorderfix2(self,collection: Collection, min_jacobian: float, max_midangle: float, min_midratio: float, jacobian_method: int, fix_method: int):
		pass

	def section_plane_mesh(self,collection: Collection, mesh_type: int, elem_size: float, connectivity: int, elem_collection: Collection, tol: float):
		pass

	def segmentsetaddfaces(self,name: hwString , elem_collection: Collection, node_collection: Collection, break_angle: float, reverse_normals: int, face_or_edge: int):
		pass

	def segmentsetaddfacesusingfacenumber(self,name: hwString , collection: Collection, face_number: int, reverse_normals: int, element_id: int, option: int):
		pass

	def segmentsetaddmixedfaces(self,name: hwString , elem_collection: Collection, node_collection: Collection, break_angle: float, reverse_normals: int):
		pass

	def segmentsetaddshells(self,name: hwString , collection: Collection, reverse_normals: int):
		pass

	def segmentsetadjustnormal(self,name: hwString , elem_collection: Collection, elem_flag: int, orientation_element: var0, reverse_normals: int):
		pass

	def segmentsetcreateusingfacenumber(self,name: hwString , color: int, collection: Collection, face_number: int, reverse_normals: int, element_id: int, option: int):
		pass

	def segmentsetcreatewithfaces(self,name: hwString , color: int, elem_collection: Collection, node_collection: Collection, break_angle: float, reverse_normals: int, face_or_edge: int):
		pass

	def segmentsetcreatewithmixedfaces(self,name: hwString , color: int, elem_collection: Collection, node_collection: Collection, break_angle: float, reverse_normals: int):
		pass

	def segmentsetcreatewithshells(self,name: hwString , color: int, collection: Collection, reverse_normals: int):
		pass

	def segmentsetremoveelems(self,name: hwString , collection: Collection):
		pass

	def segmentsetremoveelemsusingnodes(self,name: hwString , elem_collection: Collection, node_collection: Collection):
		pass

	def segmentsetreversenormals(self,name: hwString , collection: Collection, reverse_flag: int):
		pass

	def segregateByPatches(self,collection: Collection, component_name: hwString ):
		pass

	def segregateengineeringconstraints(self,collection: Collection):
		pass

	def select_polygonal_elem_region(self,collection: Collection, max_feature_angle: float, elem_type: int):
		pass

	def separate_fillets(self,input_collection: Collection, output_collection: Collection, string_array: hwStringList):
		pass

	def separate_holes_in_3d_body_new(self,input_collection: Collection, output_collection: Collection, flags: int, string_array: hwStringList):
		pass

	def serializepartnodeenggids(self,mainid: var0):
		pass

	def set_acousticmesh_options(self,NumElemPerWaveLength: int  = 6, WaveSpeed: float  =" 340000_module.0", DisplayCavities: int  =" 0"):
		pass

	def set_default_quality_criteria(self,elementsize: float):
		pass

	def set_meshedgeparams(self,edge_index: var0, elem_density: var0, alg_type: int, bias_style: int, bias: float, min_size: float, max_size: float, chordal_dev: float, max_angle: float):
		pass

	def set_meshfaceparams(self,face_index: var0, shape_type: int, elem_type: int, alg_type: int, elem_size: int, smooth_method: int, smooth_tol: float, size_control: int, skew_control: int):
		pass

	def set_midsurface_z_offset(self,collection: Collection, z_offset: float, reserved: int):
		pass

	def set_preserved_edges(self,hmlinescollection: Collection, new_stat: int):
		pass

	def setactiveplotcontrol(self,plot_type: hwString , plotcontrol_id: int):
		pass

	def setanimationframe(self,nFrame: int):
		pass

	def setanimationtime(self,dTime: float):
		pass

	def setautoupdatesets(self,mode: int):
		pass

	def setcleanupglobalflags(self,flags: int, mode: int):
		pass

	def setcolor(self,index: int, red: int, green: int, blue: int):
		pass

	def setcomponentdisplayattributes(self,name: hwString , style: int, colortype: int):
		pass

	def setcomptopologydisplay(self,compid: int, disp_type: int):
		pass

	def setcurrentinclude(self,id: var0, shortname: hwString ):
		pass

	def setcuttingplaneactive(self,axis: int, state: int):
		pass

	def setcuttingplanecolor(self,axis: int, mode: int, color: int):
		pass

	def setcuttingplanesbase(self,x: float, y: float, z: float):
		pass

	def setcuttingplanethickness(self,axis: int, thickness: float):
		pass

	def setcuttingplanethicknesson(self,axis: int, state: int):
		pass

	def setdisplayattributes(self,style: int, colortype: int):
		pass

	def setdosuppressvertices(self,on: int):
		pass

	def setedgeattractiontriared(self,edgeattr: int):
		pass

	def setedgedensitylink(self,method: int):
		pass

	def setedgedensitylinkbytypeandaspectratio(self,type: int, aspect_ratio: float):
		pass

	def setedgedensitylinkwithaspectratio(self,aspectratio: float):
		pass

	def setelementcheckmethod(self,check_name: hwString , method: int):
		pass

	def setelemparamcolor(self,param_id: int, color: int):
		pass

	def setelemparamscolors(self,float_array: hwDoubleList):
		pass

	def setelemparamsvisualpriorities(self,float_array: hwDoubleList):
		pass

	def setelemparamvisualpriority(self,param_id: int, priority: int):
		pass

	def setelemqualityparamactive(self,param_id: int, activ: int):
		pass

	def setelemqualityviewoption(self,tagname: hwString , option: float):
		pass

	def setelemqualityviewoptions(self,all_options: hwDoubleList):
		pass

	def setelemqualityviewsettings(self,strings: hwStringList):
		pass

	def setentitycolorsaturation(self,percentage: int, flag: int):
		pass

	def setentitytypesupportedbyenggid(self,string_array: hwStringList):
		pass

	def setentitytypesupportedbynamepool(self,num_types: hwStringList):
		pass

	def setfacetfactor(self,refine_max: int, deviation_factor: float, angle: float, total: int):
		pass

	def setgeometryfileversion(self,major_version: int, minor_version: int):
		pass

	def setglobal_meshrefineoptions(self,collection: Collection, param_strs: hwStringList, append_mode: int):
		pass

	def setglobalply(self,collection: Collection, ply_name: hwString , only_orient: int, normal_size: float, color: int):
		pass

	def setglobalply_option(self,collection: Collection, ply_name: hwString , only_orient: int, normal_size: float, color: int, option: int):
		pass

	def setgraphictranslation(self,entity: Entity, x: float, y: float, z: float):
		pass

	def sethistorylimit(self,count: int):
		pass

	def sethistorymemorylimit(self,memory: int):
		pass

	def sethistoryrecord(self,state: int):
		pass

	def setisosurfaceparameters(self,on: int, legendbased: int, value: float, addfacesabove: int, transparent: int, constantcolor: int, color: int):
		pass

	def setlegendbackgroundcolor(self,red: float, green: float, blue: float, alpha: float):
		pass

	def setlightsource(self,x: float, y: float, z: float):
		pass

	def setmarkdisplayattributes(self,collection: Collection, style: int, colortype: int):
		pass

	def setmarktopologydisplay(self,collection: Collection, style: int):
		pass

	def setmeshflowcontrols(self,meshsurf_algorithm: int, dirx: float, diry: float, dirz: float):
		pass

	def setmeshparams_byedgecollection(self,*args, **kwargs):
		"""
		setmeshparams_byedgecollection(HMAPIBase self, Collection edge_collection, int const EdgeAlgType=INT_MAX, double const EdgeBiasing=DBL_MAX, int const EdgeBiasStyle=INT_MAX, double const EdgeChordalDeviation=DBL_MAX, double const EdgeDensity=DBL_MAX, hwDoubleList EdgeDistribution=hwDoubleList(), double const EdgeElemSize=DBL_MAX, double const EdgeMaxAngle=DBL_MAX, double const EdgeMaxSize=DBL_MAX, double const EdgeMinSize=DBL_MAX)
		"""
		pass

	def setmeshparams_byentity(self,*args, **kwargs):
		"""
		setmeshparams_byentity(HMAPIBase self, Entity entity, int const EdgeAlgType=INT_MAX, double const EdgeBiasing=DBL_MAX, int const EdgeBiasStyle=INT_MAX, double const EdgeChordalDeviation=DBL_MAX, double const EdgeDensity=DBL_MAX, hwDoubleList EdgeDistribution=hwDoubleList(), double const EdgeElemSize=DBL_MAX, double const EdgeMaxAngle=DBL_MAX, double const EdgeMaxSize=DBL_MAX, double const EdgeMinSize=DBL_MAX, int const FaceAlgType=INT_MAX, int const FaceElemType=INT_MAX, int const FaceElemType2=INT_MAX, int const FaceMeshAlgorithm=INT_MAX, Entity FaceMeshMapPoint1=hwDescriptor::Entity(), Entity FaceMeshMapPoint2=hwDescriptor::Entity(), Entity FaceMeshMapPoint3=hwDescriptor::Entity(), Entity FaceMeshMapPoint4=hwDescriptor::Entity(), Entity FaceMeshMapPoint5=hwDescriptor::Entity(), int const FaceSizeControl=INT_MAX, int const FaceSkewControl=INT_MAX, int const FaceSmoothMethod=0, double const FaceSmoothTolerance=DBL_MAX)
		"""
		pass

	def setmeshparams_byfacecollection(self,*args, **kwargs):
		"""
		setmeshparams_byfacecollection(HMAPIBase self, Collection face_collection, int const FaceAlgType=INT_MAX, int const FaceElemType=INT_MAX, int const FaceElemType2=INT_MAX, int const FaceMeshAlgorithm=INT_MAX, Entity FaceMeshMapPoint1=hwDescriptor::Entity(), Entity FaceMeshMapPoint2=hwDescriptor::Entity(), Entity FaceMeshMapPoint3=hwDescriptor::Entity(), Entity FaceMeshMapPoint4=hwDescriptor::Entity(), Entity FaceMeshMapPoint5=hwDescriptor::Entity(), int const FaceSizeControl=INT_MAX, int const FaceSkewControl=INT_MAX, int const FaceSmoothMethod=0, double const FaceSmoothTolerance=DBL_MAX)
		"""
		pass

	def setmeshparams_bynodepair(self,*args, **kwargs):
		"""
		setmeshparams_bynodepair(HMAPIBase self, Entity node1, Entity node2, int const FaceAlgType=INT_MAX, int const FaceElemType=INT_MAX, int const FaceElemType2=INT_MAX, int const FaceMeshAlgorithm=INT_MAX, Entity FaceMeshMapPoint1=hwDescriptor::Entity(), Entity FaceMeshMapPoint2=hwDescriptor::Entity(), Entity FaceMeshMapPoint3=hwDescriptor::Entity(), Entity FaceMeshMapPoint4=hwDescriptor::Entity(), Entity FaceMeshMapPoint5=hwDescriptor::Entity(), int const FaceSizeControl=INT_MAX, int const FaceSkewControl=INT_MAX, int const FaceSmoothMethod=0, double const FaceSmoothTolerance=DBL_MAX)
		"""
		pass

	def setmode_compsfindloads(self,comp_loads_only: int):
		pass

	def setmode_surfsfindpoints(self,mode: int):
		pass

	def setnormalsdisplaytype(self,type: int):
		pass

	def setoffsetconflictoptionmessage(self,mode: int):
		pass

	def setply(self,collection: Collection, ply_number: int, only_orient: int, normal_size: float, color: int):
		pass

	def setply_option(self,collection: Collection, ply_number: int, only_orient: int, normal_size: float, color: int, option: int):
		pass

	def setqualitycriteria(self,string_array: hwStringList, mode: int):
		pass

	def setqualitythresholdcolor(self,range_id: int, color: int):
		pass

	def setqualitythresholdscolors(self,float_array: hwDoubleList):
		pass

	def setredoconnectparams(self,mesh_side: int, num_layers: int):
		pass

	def setreplacereportshowgui(self,option: int):
		pass

	def setreviewbyid(self,entity: Entity, color: int, review_type: int):
		pass

	def setreviewbymark(self,collection: Collection, color: int):
		pass

	def setreviewbymarkenhanced(self,collection: Collection, color: int, shaded: int, edges: int):
		pass

	def setreviewbyname(self,entity_type: EntityFullType, name: hwString , color: int, review_type: int):
		pass

	def setreviewcolormode(self,mode: int):
		pass

	def setreviewmode(self,mode: int):
		pass

	def setreviewtransparentmode(self,mode: int):
		pass

	def setsimulationstep(self,subcase_id: int, simulation_id: int):
		pass

	def setsketchtransformation(self,sketchId: var0, transform: hwDoubleList):
		pass

	def setsolver(self,solvername: hwString ):
		pass

	def setsolverusessegmentsets(self,flag: int):
		pass

	def setsphereclip(self,onoff: int):
		pass

	def setsubmodeltype(self,type: hwString ):
		pass

	def setsurfacenormalsdisplaytype(self,type: int):
		pass

	def setsystem(self,collection: Collection, setangle: float, onlyorient: int, normal_size: float, color: int):
		pass

	def settopologydisplaytype(self,type: int):
		pass

	def settransparency(self,onoff: int):
		pass

	def settrimcuttingplanes(self,state: int):
		pass

	def setup_coarsening(self,collection: Collection, list: EntityList, angle: float):
		pass

	def setup_dynain(self,collection: Collection, option: int):
		pass

	def setup_gravity(self,collection: Collection, axis_type: int, value: float, option1: int, option2: int, option3: int):
		pass

	def setup_implicitgravity(self,collection: Collection, axis_type: int, value: float, option1: int, option2: int, option3: int):
		pass

	def setup_mapping(self,file: hwString , part_id: int, n1s: int, n2s: int, n3s: int, n1c: int, n2c: int, n3c: int, opt1: int, opt2: int, opt3: int, opt4: int):
		pass

	def setup_springback(self,collection1: Collection, collection2: Collection, option: int, comp1: int, comp2: int, comp3: int, comp4: int, comp5: int, comp6: int):
		pass

	def setup_trimming(self,collection: Collection, list: EntityList, curve_dir: int, curve_flag: int, tolerence: float):
		pass

	def setusefeatures(self,mode: int):
		pass

	def setviewangles(self,thetax: float, thetay: float, thetaz: float):
		pass

	def shapevarcreate_xproduct(self,basenode: Entity, shape: Entity, variable: Entity, A: float):
		pass

	def shapevarupdate_xproduct(self,collection: Collection, basenode: Entity, shape_variable_a: Entity, shape_variable_b: Entity, baseflag: float, directionflag: int, magnitude: int):
		pass

	def shell_mesh_open_manifolds(self,mesh_collection: Collection, method: int, do_decimate: int):
		pass

	def shell_mesh_smoother(self,collection: Collection, fix_nodes_collection: Collection, mesh_shape_weight: float, node_displacement_weight: float, iterations: int):
		pass

	def shelloffset(self,collection: Collection, corner_type: int, distance_type: int, distance: float, offset_type: int):
		pass

	def show_new_edge_target_by_number(self,face: Entity, e1_edge_number: int, e2_line: Entity, is_opposite: int):
		pass

	def show_new_target(self,face: Entity, offsetpoint_x: float, offsetpoint_y: float, offsetpoint_z: float, target_x: float, target_y: float, target_z: float, code: int):
		pass

	def show_stlmesh(self,collection: Collection, minsize: float, maxsize: float, maxdeviation: float, maxfacetangle: float):
		pass

	def showall(self,*args, **kwargs):
		"""
		showall(HMAPI self, hwStringList string_array=s_defaultStringList)
		"""
		pass

	def showentity(self,entity: Entity, reviewentity: bool  = False, elements_off: bool  = False, geometry_off: bool  = False):
		pass

	def showentity_byname(self,entity_type: EntityFullType, entity_name: hwString , showcomps: bool  = False, elements_off: bool  = False, geometry_off: bool  = False):
		pass

	def showentitybymark(self,*args, **kwargs):
		"""
		showentitybymark(HMAPI self, CollectionSet collection_set, hwString const & showComps="", hwString const & refFlag="", hwString const & elementsOff="", hwString const & geometryOff="", hwString const & plotsOff="")
		"""
		pass

	def showfacets(self,mode: int):
		pass

	def showview(self,name: hwString , entity_type_id: int):
		pass

	def shrinkwrapmesh(self,entity_collection: Collection, feature_collection: Collection, mesh_size: float, feature_angle: float, mesh_type: int, projection_type: int, min_checkval: float, system_entity: Entity, create_hole_elements: int, hole_patch_size: float, gap_patch_size: float):
		pass

	def shrinkwrapmeshboolean(self,booleantype: int, collection1: Collection, collection2: Collection, featurecollection: Collection, cellsize: float, featureangle: float, meshtype: int, projtype1: int, projtype2: int, mincheckval: float, sysptr: Entity, flag: int, arg1: float, arg2: float):
		pass

	def signal(self,cls: EntityClass):
		pass

	def simexdrawbeadradii(self,setname: hwString , db_height: float, db_shoulder_radius: float, db_radius: float):
		pass

	def simplify_model_geometry(self,surf_collection: Collection, max_fillet_radius: float, debug_collection: Collection, flag1: int, flag2: int):
		pass

	def simplifygeometry(self,collection: Collection, option: int, mode: int, tol: float):
		pass

	def simulationsetangle(self,angle: float):
		pass

	def simulationtitleon(self,on: int):
		pass

	def single_collector_test(self,name: hwString , collection: Collection, the_float: float, the_int: int):
		pass

	def sizedesvarsupdate(self,name: hwString , upperbound: float, initialvalue: float, lowerbound: float, delxv: float):
		pass

	def sketchdisassociateentities(self,sketch_id: var0):
		pass

	def sketchedit(self,*args, **kwargs):
		"""
		sketchedit(HMAPIBase self, int const id=0, hwString const & operation="", hwString const & entity_type="", hwString const & creation_method="", hwCouple point_position=hwCouple(DBL_MAX, DBL_MAX), hwCoupleList position_list=hwCoupleList(), int const curve_id=0, hwCouple line_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple line_direction=hwCouple(0.000000, 0.000000), int const point_id=0, hwCouple start_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple end_position=hwCouple(DBL_MAX, DBL_MAX), int const start_point=0, int const end_point=0, double const angle=DBL_MAX, double const length=0.000000, hwCouple center_position=hwCouple(DBL_MAX, DBL_MAX), double const radius=0.000000, int const center_point=0, hwCouple curve_position=hwCouple(DBL_MAX, DBL_MAX), int const curve_point=0, hwCouple opposite_position=hwCouple(DBL_MAX, DBL_MAX), int const opposite_point=0, hwCouple first_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple second_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple third_position=hwCouple(DBL_MAX, DBL_MAX), int const first_point=0, int const second_point=0, int const third_point=0, int const is_periodic=-1, int const degree=0, hwIntList arc_direction=hwIntList(), hwIntList type_list=hwIntList(), hwIntList entity_list=hwIntList(), int const pattern_dir=0, double const pattern_distance=DBL_MAX, int const number_copies=0, int const is_symmetric=-1, int const dir1_copies_count=0, double const dir1_distance=DBL_MAX, int const dir1_is_symmetric=-1, int const pattern_dir1=0, int const dir2_copies_count=0, double const dir2_distance=DBL_MAX, int const dir2_is_symmetric=-1, int const pattern_dir2=0, double const pattern_angle=DBL_MAX, int const is_counterclockwise=-1, int const invert_tangent=-1, hwString const & name="", int const is_interpolated=-1, hwCouple corner_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple corner_position2=hwCouple(DBL_MAX, DBL_MAX), hwCouple length_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple width_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple lower_left=hwCouple(DBL_MAX, DBL_MAX), hwCouple lower_right=hwCouple(DBL_MAX, DBL_MAX), hwCouple upper_right=hwCouple(DBL_MAX, DBL_MAX), hwCouple circle_position=hwCouple(DBL_MAX, DBL_MAX), int const number_sides=0, int const midside_mode=-1, int const entity_id=0, hwString const & constraint_type="", int const first_entity=0, int const second_entity=0, hwCouple dim_position=hwCouple(DBL_MAX, DBL_MAX), int const is_fixed=-1, int const is_construction=-1, double const start_angle=DBL_MAX, double const end_angle=DBL_MAX, double const sweep_angle=DBL_MAX, double const major_radius=0.000000, double const minor_radius=0.000000, hwString const & variable_name="", double const dim_value=DBL_MAX, int const is_dimdriven=-1, hwString const & operation_method="", hwCouple split_position=hwCouple(DBL_MAX, DBL_MAX), hwIntList point_list=hwIntList(), hwCouple geom_position=hwCouple(DBL_MAX, DBL_MAX), double const offset_distance=0.000000, hwCouple trim_position=hwCouple(DBL_MAX, DBL_MAX), int const mirror_axis=0, hwCouple extend_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple translate_direction=hwCouple(0.000000, 0.000000), double const translate_distance=DBL_MAX, int const keep_relations=-1, double const rotate_angle=DBL_MAX, int const delete_original=-1, hwCouple major_axis=hwCouple(0.000000, 0.000000), int const majoraxis_line=0, int const minoraxis_line=0, hwCouple majoraxis_position=hwCouple(DBL_MAX, DBL_MAX), hwCouple minoraxis_position=hwCouple(DBL_MAX, DBL_MAX))
		"""
		pass

	def sketchintersect(self,sketch_id: var0, collection: Collection, create_entities: var0 =" 0", only_displayed: var0 = 1, planeDimension: float =" 0_module.0"):
		pass

	def sketchproject(self,sketch_id: var0, collection: Collection, create_entities: var0 =" 0"):
		pass

	def sketchupdateentity(self,sketcherID: var0, actionName: hwString , updateReason: hwString ):
		pass

	def sl_feature_mesh(self,surface_collection: Collection, meshcontrol_collection: Collection, mode: int):
		pass

	def sl_meshsurfaces(self,collection: Collection, file: hwString , reserved: int):
		pass

	def sliversfixfe(self,edge1: hwIntList, edge2: hwIntList, widthThreshold: float ):
		pass

	def slivertetrafix(self,collection: Collection, options: hwString ):
		pass

	def smooth3d(self,entity_type: EntityFullType, collection: Collection, options: hwString ):
		pass

	def smoothelements(self,faceindex: var0, smoothmethod: int, iterations: int):
		pass

	def solid_cavity_detect_end(self):
		pass

	def solid_cavity_detect_fill(self,collection: Collection, merge_flag: int):
		pass

	def solid_cavity_detect_local(self,collection: Collection, face_id: var0, fill_flag: var0):
		pass

	def solid_cavity_detect_modify_rims(self,add_collection: Collection, remove_collection: Collection, region_id: var0, add_surfs_flag: int):
		pass

	def solid_cavity_detect_modify_surfaces(self,collection: Collection, region_id: var0, add_surfs_flag: int):
		pass

	def solid_cavity_detect_start(self,collection: Collection, all_cavities: int, get_n_cavities: var0, max_radius: float, max_length: float, min_concavity: float):
		pass

	def solid_extrude_from_surfs(self,collection: Collection, vec_x: float, vec_y: float, vec_z: float, options: int, comp_mode: int):
		pass

	def solid_facesfind(self,compmask: Collection):
		pass

	def solid_fixedptsmaker(self,surf_collection: Collection, comp_collection: Collection, tol_rel: float):
		pass

	def solid_fixedptssuppressor(self,point_collection: Collection):
		pass

	def solid_map_split_guides(self,solidcollection: Collection, meshsize: float, param_strs: hwStringList):
		pass

	def solid_offset_from_surfs(self,collection: Collection, offset: float, options: int, comp_mode: int):
		pass

	def solid_prepare_entitylst(self,entity_type: EntityFullType, reserved: var0):
		pass

	def solid_prepare_nodeline(self,start: int):
		pass

	def solid_rotate(self,*args, **kwargs):
		"""
		solid_rotate(HMAPI self, Collection solid_collection, hwTriple axis, hwTriple base_point, int const projection_point=0, int const create_spunsolid=0, int const create_crosssection=0, int const create_spunoutline=0, int const offset_method=0, double const offset_dist=0.000000, hwString const & dest_component="current", hwString const & comp_name="")
		"""
		pass

	def solid_untrim(self,collection: Collection, force: int):
		pass

	def solidblock(self,base_x: float, base_y: float, base_z: float, ivec_x: float, ivec_y: float, ivec_z: float, jvec_x: float, jvec_y: float, jvec_z: float, kvec_x: float, kvec_y: float, kvec_z: float):
		pass

	def solidcone(self,base_x: float, base_y: float, base_z: float, mvec_x: float, mvec_y: float, mvec_z: float, nvec_x: float, nvec_y: float, nvec_z: float, base_radius: float, top_radius: float, aspect_ratio: float, start_angle: float, end_angle: float, height: float):
		pass

	def solidcreatedragsurfalongline(self,surfs_collection: Collection, lines_list: EntityList, method: int, options: int, comp_mode: int, node_entity: Entity, ref_plane_normal: hwTriple, ref_plane_normal_base: hwTriple):
		pass

	def solidcreateruled(self,surf_list: EntityList, link_coords_array: hwDoubleList, guide_collection_set: CollectionSet, ruled_type: int, options: int, comp_mode: int):
		pass

	def solidcreatespinsurfwithoffsetangle(self,surf_collection: Collection, rotation_plane_normal: hwTriple, rotation_plane_normal_base: hwTriple, start_angle: float, end_angle: float, options: int, comp_mode: int):
		pass

	def solidmap_begin(self,ordered: int):
		pass

	def solidmap_end(self,options: int, density_or_size: float, bias_style: int, biasing: float, elemDest: int):
		pass

	def solidmap_equivalence(self,tolerance: float, find_faces: int):
		pass

	def solidmap_equivalence2(self,tolerance: Collection, find_faces: float, isAlsoFindFaces: int):
		pass

	def solidmap_evaluate_mappable_count(self,solentity: Entity):
		pass

	def solidmap_initialize_edges(self,*args, **kwargs):
		"""
		solidmap_initialize_edges(HMAPI self, Collection solidcollection, double const elemsize, Collection dest_hint_collection=s_defaultCollection, unsigned int const elem_type=2, unsigned int const orthogonal_extrusion=0, Collection src_hint_collection=s_defaultCollection)
		"""
		pass

	def solidmap_prepare_usrdataptr(self,type: hwString , options: var0):
		pass

	def solidmap_set_source_size(self,size: float):
		pass

	def solidmap_solids_begin(self,collection: Collection, options: var0, elem_size: float):
		pass

	def solidmap_solids_begin2(self,solid_collection: Collection, source_surface_collection: Collection, destination_surface_collection: Collection, options: var0, elem_size: float):
		pass

	def solidmap_solids_end(self):
		pass

	def solidmap_solids_set_density(self,edge_collection: Collection, den: int):
		pass

	def solidmap_solids_set_elemsize(self,edge_collection: Collection, elemsize: float):
		pass

	def solidmap_solids_set_face_params(self,collection: Collection, options: var0):
		pass

	def solidmap_solids_set_mapface(self,point_id1: int, point_id2: int, point_id3: int, point_id4: int):
		pass

	def solidmesh12lines(self,lines: EntityList, density1: int, density2: int, density3: int):
		pass

	def solidmesh9lines(self,lines: EntityList, density1: int, density2: int, density3: int):
		pass

	def solidmeshwithsurfaces(self,type: int, source: Collection, dest: Collection, along: EntityList, genelems: int, elements: Collection, density: int, biasstyle: int, biasing: float):
		pass

	def solidrc(self,mesh_collection: Collection, _ctrls: hwString , graphicsDB: int =" 0"):
		pass

	def solidrc_fillhole_nodelist(self,nodeList: EntityList, graphicsDB: int =" 0"):
		pass

	def solids_create_from_surfaces(self,surfs_collection: Collection, depth_mode: int, depth_level: int, comp_mode: int):
		pass

	def solids_detach(self,solid_collection: Collection):
		pass

	def solidspherefull(self,xc: float, yc: float, zc: float, radius: float):
		pass

	def solidtorus(self,cx: float, cy: float, cz: float, majx: float, majy: float, majz: float, normx: float, normy: float, normz: float, tuberad: float, majrad: float, majamin: float, majamax: float, tubeamin: float, tubeamax: float):
		pass

	def solverconvert(self,source_solver: hwString , destination_solver: hwString , source_type: hwString , destination_type: hwString , batch: hwString , config_file_path: hwString ):
		pass

	def solverdeckcleanup(self,solver: hwString , collection_set: CollectionSet):
		pass

	def sort_midsurfaces(self,mode: int):
		pass

	def spatialrenumbering(self,*args, **kwargs):
		"""
		spatialrenumbering(HMAPI self, Collection collection, hwString const & type, unsigned int const renumbering_type=0, Entity system_entity=hwDescriptor::Entity(), unsigned int const start_id=0, int const primary_axis=0, double const primary_tolerance=0.000000, unsigned int const primaryid_increment=0, int const secondary_axis=0, double const secondary_tolerance=0.000000, unsigned int const secondaryid_increment=0, int const ternary_axis=0, double const ternary_tolerance=0.000000, unsigned int const ternaryid_increment=0, Entity start_entity=hwDescriptor::Entity(), Entity primary_entity=hwDescriptor::Entity(), Entity secondary_entity=hwDescriptor::Entity(), Entity ternary_entity=hwDescriptor::Entity())
		"""
		pass

	def spawn_solver(self,comm_opts: hwString , projdir: hwString , projroot: hwString , memory: hwString ):
		pass

	def sphereclipautofit(self,onoff: int):
		pass

	def sphereclipcenter(self,x: float, y: float, z: float):
		pass

	def sphereclipradius(self,radius: float):
		pass

	def sphgenerate_new(self,collection: Collection, string_array: hwStringList):
		pass

	def splinesurface(self,collection: Collection, plane_flag: int, plane_normal: hwTriple, plane_normal_base: hwTriple, options: int):
		pass

	def split1delements(self,*args, **kwargs):
		"""
		split1delements(HMAPI self, Collection collection, hwString const & meshingtype, bool const delorgelems, unsigned int const beamstartid, EntityList entity_list=s_defaultEntityList, unsigned int const numelems=0)
		"""
		pass

	def splitSurfaceRegions(self,collection: Collection, split_mode: hwString ):
		pass

	def split_elements_by_structure_pattern(self,refine_collection: Collection, transition_collection: Collection, refine_size: float, num_layers: int =" 0"):
		pass

	def split_elements_by_structure_pattern_freeselection(self,entity_type: EntityFullType, collection: Collection, refine_size: float, adjacent_layers: int):
		pass

	def split_hex_continuum(self,node_array: hwIntList, entity_type: EntityFullType, collection: Collection, layers: int, growth_rate: float, action: int, component: int):
		pass

	def splitcontactfromcontactgroup(self,id: var0):
		pass

	def splitelementbyelemselect(self,*args, **kwargs):
		"""
		splitelementbyelemselect(HMAPI self, Collection elem_collection, unsigned int const consider1ds=1, hwString const & dividequadsoptions="ShortestDiagonals", hwString const & midpointoptions="", unsigned int const reverseorientation=0, hwString const & splitallsidesoptions="Quads", unsigned int const splitnumberedges=1, hwString const & splitoptions="SplitAllSides", unsigned int const useinferredgeometry=0, unsigned int const useadjacentlayer=0)
		"""
		pass

	def splitelements(self,method: int, collection: Collection):
		pass

	def splitelementswith1D(self,inferred: int, collection: Collection):
		pass

	def splitsolidelements(self,collection: Collection, splittype: int):
		pass

	def spring(self,node_entity1: Entity, node_entity2: Entity, dof: hwBoolList, property_name: hwString , vector_entity: Entity):
		pass

	def springfournoded(self,node_entity1: Entity, node_entity2: Entity, node_entity3: Entity, node_entity4: Entity, dof: hwBoolList, property_name: hwString , vector_entity: Entity):
		pass

	def springos(self,node_entity1: Entity, node_entity2: Entity, property_name: hwString , vector_entity: Entity, direction_node_entity: Entity, orient_x: float, orient_y: float, orient_z: float, orient_comps_flag: int, system_entity: Entity):
		pass

	def springsosupdate(self,collection: Collection, property_flag: int, propery_name: hwString , vector_flag: int, vector_entity: Entity, direction_node_entity: Entity, orient_x: float, orient_y: float, orient_z: float, orient_comps_flag: int, system_entity: Entity, update_orient_flag: int):
		pass

	def springsupdate(self,collection: Collection, dofflag: int, dof: hwBoolList, propertyflag: int, property: hwString , vectorflag: int, vectorentity: Entity):
		pass

	def springthreenoded(self,node_entity1: Entity, node_entity2: Entity, node_entity3: Entity, dof: hwBoolList, property_name: hwString , vector_entity: Entity):
		pass

	def stackdisplay(self,collection: Collection, size: float):
		pass

	def stackreverse(self,collection: Collection, size: float):
		pass

	def start_batch_import(self,mode: var0):
		pass

	def startnotehistorystate(self,name: hwString ):
		pass

	def starttimecheck(self,title: hwString ):
		pass

	def stitch_mesh_nodes(self,inputlist1: EntityList, inputlist2: EntityList, postProcessingOption: int):
		pass

	def stitchsurfaces(self,collection: Collection):
		pass

	def stl_write(self,filename: hwString , all: int):
		pass

	def stl_write_mark(self,filename: hwString , collection: Collection):
		pass

	def stl_write_selected(self,filename: hwString ):
		pass

	def storemeshtodatabase(self,elemstosurfcomp: int):
		pass

	def submodleoffset(self,submodel: hwString , id: var0, shortname: hwString , entities: hwString , poolid: var0, offset: var0):
		pass

	def summary(self,template_file: hwString , output_file: hwString , _print: int, all: int):
		pass

	def superelementset(self,collection: Collection, super: int):
		pass

	def surface_patch(self,*args, **kwargs):
		"""
		surface_patch(HMAPI self, Collection line_collection, hwString const & tangency="nontangent", bool const stitch=True, bool const solid_stitch=True, hwString const & dest_component="original")
		"""
		pass

	def surface_rmesh(self,collection: Collection, min_length: float, max_length: float, chordal_deviation: float, fillet_angle: float, edge_accuracy: float, fix_edge_nodes_flag: int):
		pass

	def surface_showfacets(self,collection: Collection):
		pass

	def surfaceaddnodesfixed(self,surfacecollection: Collection, nodelist: EntityList, tolerance: float, createplot: int):
		pass

	def surfaceaddpoint(self,surfptr: Entity, x: float, y: float, z: float):
		pass

	def surfaceaddpointsfixed(self,surfacecollection: Collection, pointcollection: Collection, tolerance: float, createplot: int):
		pass

	def surfacecone(self,bottom_center: Entity, major_vector: Entity, normal_vector: Entity, base_radius: float, top_radius: float, aspect_ratio: float, start_angle: float, end_angle: float, height: float):
		pass

	def surfaceconefull(self,top_center: Entity, bottom_center: Entity, base_radius: float, top_radius: float, aspect_ratio: float, height: float):
		pass

	def surfacecopyedges(self,surface: Entity, list: EntityList, all_edges: int):
		pass

	def surfacecreatedraglinealongline(self,lines_collection: Collection, lines_list: EntityList, method: int, options: int, comp_mode: int, node_entity: Entity, replane_normal: hwTriple, replane_normal_base: hwTriple):
		pass

	def surfacecreatedraglinealongnormal(self,line_list: EntityList, start_offset: float, end_offset: float, link_type: int, comp_mode: int, reverse_dir: int):
		pass

	def surfacecreatedraglinealongvector(self,collection: Collection, vector: hwTriple, distance: float, options: int, comp_mode: int, node_ptr: Entity, scale: float, twistangle: float):
		pass

	def surfacecreatedragnodesalongline(self,sectionnodelist: EntityList, draglinelist: EntityList, method: int, options: int, comp_mode: int, node_entity: Entity, refplane_normal: hwTriple, refplane_normal_base: hwTriple):
		pass

	def surfacecreatenormalfromedges(self,collection: Collection, distance: float, reserved: int, comp_mode: int):
		pass

	def surfacecreatenurbs(self,udegree: int, vdegree: int, uk_count: int, vk_count: int, up_count: int, vp_count: int, ratnl: int, float_array: hwDoubleList):
		pass

	def surfacecreateruled(self,line_list: EntityList, link_coords_array: hwDoubleList, guide_collection_set: CollectionSet, ruled_type: int, options: int, comp_mode: int):
		pass

	def surfacecreatespinlinewithoffsetangle(self,collection: Collection, rotation_plane_normal: hwTriple, rotation_plane_normal_base: hwTriple, start_angle: float, end_angle: float, options: int):
		pass

	def surfacecreatespinnodeswithoffsetangle(self,nodelist: EntityList, rotplane_normal: hwTriple, rotplane_normal_base: hwTriple, start_angle: float, end_angle: float):
		pass

	def surfacecreatetangentfromedges(self,collection: Collection, distance: float, extend_mode: int, component: int):
		pass

	def surfacedisplaynormals(self,collection: Collection, size: float):
		pass

	def surfacefilletremove(self,entity_type: Collection, collection: Collection, size: Collection):
		pass

	def surfaceimprintpoints(self,collection: Collection, float_array: hwDoubleList, max_distance: float):
		pass

	def surfaceintersectmark(self,collection1: Collection, plane_flag: int, plane_normal: hwTriple, plane_base: hwTriple, collection2: Collection):
		pass

	def surfaceintersectmark2(self,collection1: Collection, plane_flag: int, plane_normal: hwTriple, plane_base: hwTriple, collection2: Collection, comp_mode: int):
		pass

	def surfacemark_duplicate_check(self,collection1: Collection, collection2: Collection, options: int, use_plane: int, plane_normal: hwTriple, plane_normal_base: hwTriple, tol: float):
		pass

	def surfacemark_find_organize_symmetry(self,surf_set_collection1: Collection, surf_set_collection2: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple, options: int, tolerance: float):
		pass

	def surfacemark_shellcombine(self,surf_collection: Collection, opts: int):
		pass

	def surfacemarkaddnodesfixed(self,surf_collection: Collection, node_collection: Collection, tol: float, reserved_1: int):
		pass

	def surfacemarkclipwithline(self,collection: Collection, line: Entity, tolerance: float):
		pass

	def surfacemarkclipwithlines(self,surf_collection: Collection, line_collection: Collection, tolerance: float):
		pass

	def surfacemarkcopyedges(self,surf_collection: Collection, list: EntityList, all_edges: int):
		pass

	def surfacemarkfeatures(self,collection: Collection, angle_surf: float, offset_surf: float, close_orphans: int, fillet_min: float, fillet_max: float, angle_vertex: float, edge_min: float, shape_discontinuity: float, update_only: int):
		pass

	def surfacemarkmerge(self,collection: Collection, breakangle: float, minradius: float, maxradius: float):
		pass

	def surfacemarkremoveallpinholes(self,collection: Collection, diameter: float):
		pass

	def surfacemarkremovelinefillets(self,collection: Collection, min_radius: float, max_radius: float, min_angle: float, float_array: hwDoubleList):
		pass

	def surfacemarkremovepinholes(self,collection: Collection, diameter: float, coords: hwDoubleList):
		pass

	def surfacemarksplitwithelemedges(self,surf_colllection: Collection, edge_list: hwString ):
		pass

	def surfacemarksplitwithline(self,collection: Collection, line_entity: Entity, vector: hwTriple, trim_flag: int, distance: float):
		pass

	def surfacemarksplitwithlines(self,surf_collection: Collection, line_collection: Collection, vector: hwTriple, trim_flag: int, distance: float):
		pass

	def surfacemarksplitwithnodes(self,collection: Collection, node_list: EntityList):
		pass

	def surfacemarksplitwithplane(self,collection: Collection, plane_normal: hwTriple, plane_normal_base: hwTriple):
		pass

	def surfacemarksplitwithsurface(self,collection: Collection, surface: Entity):
		pass

	def surfacemarkuntrim(self,surfacecollection: Collection):
		pass

	def surfacemode(self,mode: int):
		pass

	def surfaceplane(self,plane_normal: hwTriple, plane_normal_base: hwTriple, size: float):
		pass

	def surfaceprimitivefromlines(self,collection: Collection, surf_type: int, tol_mode: int, tol: float, options: int):
		pass

	def surfaceprimitivefrompoints(self,collection: Collection, surf_type: int, options: int, tol: float):
		pass

	def surfacereversenormals2(self,collection: Collection, size: float, adjust_fe: int):
		pass

	def surfaceskin(self,skin_linelist: EntityList, auto_reverse: int):
		pass

	def surfacespherefromfournodes(self,list: EntityList):
		pass

	def surfacespherefromthreepoints(self,center_node: Entity, radius: float, r_node: Entity, theta_start: float, theta_end: float, angle_node: Entity, phi_start: float, phi_end: float, angle_type: int):
		pass

	def surfacespherefull(self,center_node: Entity, radius: float):
		pass

	def surfacesplinefillholes(self,collection: Collection):
		pass

	def surfacesplinefillholes2(self,collection: Collection, options: int):
		pass

	def surfacesplinefrommesh(self,shellelemcollection: Collection, edgeelemcollection: Collection, tol: float):
		pass

	def surfacesplinefrommesh_ex(self,shellelemcollection: Collection, edgeelemcollection: Collection, tol: float, debug_value: int):
		pass

	def surfacesplinefrompoints(self,collection: Collection, options: int):
		pass

	def surfacesplineonlinesloop(self,collection: Collection, fill_gaps: int, use_surfs: int, options: int):
		pass

	def surfacesplineonnodesloop2(self,list: EntityList, options: int):
		pass

	def surfacesplinepatchforholes(self,collection: Collection, fill_gaps: int, options: int):
		pass

	def surfacesplitatscratches(self,collection: Collection, collection_points: Collection, minElemSize: float, out_surf_collection: Collection):
		pass

	def surfacesplitwithcoords(self,surf_entity: Entity, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):
		pass

	def surfacesplitwithline(self,surface: Entity, line: Entity, vector: hwTriple, entire_surf_flag: int, distance: float):
		pass

	def surfacesplitwithplane(self,surface: Entity, plane_normal: hwTriple, plane_normal_base: hwTriple):
		pass

	def surfacesplitwithsurface(self,surface1: Entity, surface2: Entity):
		pass

	def surfacetorus(self,center: Entity, major_vector: Entity, normal_vector: Entity, minor_radius: float, major_radius: float, major_start_angle: float, major_end_angle: float, minor_start_angle: float, minor_end_angle: float):
		pass

	def surfacetorusfromthreepoints(self,major: Entity, center: Entity, minor: Entity):
		pass

	def surfacetorusfull(self,center: Entity, normal: Entity, vector: float, minor: float):
		pass

	def surfaceuntrim(self,surfptr: Entity):
		pass

	def surfmark_trim_by_elemmark(self,input_surf_collection: Collection, ref_line_collection: Collection, trim_elem_collection: Collection):
		pass

	def surfmark_trim_by_surfmark(self,collection1: Collection, collection2: Collection, mode: int):
		pass

	def surfmarkoffsetplusminuswithtolerances(self,surf_collection: Collection, offset: float, offset_tol: float, preoffset_cleanup_tol: float):
		pass

	def swapcards(self,*args, **kwargs):
		"""
		swapcards(HMAPI self, Collection collection, hwString const & target_card_image=s_defaultString)
		"""
		pass

	def swapcontactmainsecondary(self,collection: Collection):
		pass

	def sweep_envelope(self,*args, **kwargs):
		"""
		sweep_envelope(HMAPI self, Collection collection, Entity line=hwDescriptor::Entity(), hwString const & path_rotation="MAX", bool const path_reverse=False, hwTriple axis_base=hwTriple(0.000000, 0.000000, 0.000000), hwTriple axis_direction=hwTriple(0.000000, 0.000000, 0.000000), hwDoubleList angle_range=hwDoubleList())
		"""
		pass

	def synchregionsrepresentations(self,collection: Collection, flag: int):
		pass

	def syncpropertybeamsectionvalues(self,collection: Collection):
		pass

	def systemcommand(self,command: hwString ):
		pass

	def systemcreate3nodes(self,type: int, origin: Entity, axisname: hwString , axispt: Entity, planename: hwString , planept: Entity):
		pass

	def systemorthobound(self,child_system_entity: Entity, parent_system_entity: Entity, xmin: float, xmax: float, ymin: float, ymax: float, zmin: float, zmax: float):
		pass

	def systemupdateangles(self,systemptr: Entity, origindefinition: int, originx: float, originy: float, originz: float, vectorsdefinition: int, axisname: hwString , axisx: float, axisy: float, axisz: float, planename: hwString , planex: float, planey: float, planez: float, parentsystemid: var0):
		pass

	def tableaddcolumn(self,name: hwString , data_type: hwString , column_label: hwString , string_array: hwStringList):
		pass

	def tableadddoublecolumn(self,name: hwString , datatype: hwString , columnlabel: hwString , values: hwDoubleList):
		pass

	def tableaddintegercolumn(self,name: hwString , datatype: hwString , columnlabel: hwString , values: hwIntList):
		pass

	def tableaddrow(self,name: hwString , string_array: hwStringList):
		pass

	def tablecontour(self,table_name: hwString , table_id_column: hwString , table_value_column: hwString , legend_title: hwString ):
		pass

	def tablecreate(self,name: hwString , color: var1, config: int, string_array: hwStringList, number_of_rows: var0):
		pass

	def tabledeletecolumn(self,name: hwString , column_index: var0):
		pass

	def tabledeleterow(self,name: hwString , row_index: int):
		pass

	def tableexport(self,name: hwString , filename: hwString , delimiter: hwString ):
		pass

	def tableinsertcolumn(self,name: hwString , data_type: hwString , column_label: hwString , string_array: hwStringList, column_index: var0):
		pass

	def tableinsertdoublecolumn(self,name: hwString , datatype: hwString , columnlabel: hwString , values: hwDoubleList, cindex: var0):
		pass

	def tableinsertintegercolumn(self,name: hwString , datatype: hwString , columnlabel: hwString , values: hwIntList, cindex: var0):
		pass

	def tableinsertrow(self,name: hwString , string_array: hwStringList, row_index: int):
		pass

	def tablepopulate(self,name: hwString , filename: hwString , delimiter: hwString ):
		pass

	def tableupdatecell(self,name: hwString , row_index: int, column_index: int, value: hwString ):
		pass

	def tableupdatecolumn(self,name: hwString , data_flag: var0, data_type: hwString , column_label_flag: var0, column_label: hwString , string_array: hwStringList, column_index: var0):
		pass

	def tableupdatedoublecolumn(self,name: hwString , dataflag: var0, datatype: hwString , columnlabelflag: var0, columnlabel: hwString , values: hwDoubleList, cindex: var0):
		pass

	def tableupdateintegercolumn(self,name: hwString , dataflag: var0, datatype: hwString , columnlabelflag: var0, columnlabel: hwString , values: hwIntList, cindex: var0):
		pass

	def tableupdatelabels(self,name: hwString , string_array: hwStringList):
		pass

	def tableupdaterow(self,name: hwString , string_array: hwStringList, row_index: int):
		pass

	def tangentbetweenlines(self,line1_entity: Entity, line2_entity: Entity, checkpoints: int, lineselected: int):
		pass

	def tangentbetweennodeandline(self,node_entity: Entity, line_entity: Entity, checkpoints: int, lineselected: int):
		pass

	def templatefileset(self,filename: hwString ):
		pass

	def tetmesh(self,collection1: Collection, mode1: int, collection2: Collection, mode2: int, string_array: hwStringList):
		pass

	def tetmesh_create_size_ctrl(self,string: hwString ):
		pass

	def tetmesh_set_input(self,collection1: Collection, mode1: int, collection2: Collection, mode2: int):
		pass

	def tetmesh_set_params(self,pars_str0: hwString ):
		pass

	def tetmeshlite(self,mesh_collection: Collection, _ctrls: hwString ):
		pass

	def thinsolid_extract(self,collection: Collection, thinsolid_ratio: float, max_thickness: float, feature_angle: float):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	def titlecreate(self,name: hwString , entity: Entity, pointindex: int, color: int, font: int, anchorpoint: int, x: float, y: float):
		pass

	def titledraw(self,titlename: hwString ):
		pass

	def titlepop(self,titlename: hwString ):
		pass

	def titlepush(self,titlename: hwString ):
		pass

	def titlesetcurrent(self,titlename: hwString ):
		pass

	def toggleincludefromdisplay(self,id: var0, shortname: hwString ):
		pass

	def topography_reanalysis(self,modelsel: int, filepath_fem: hwString , grid_filename: hwString , sh_filename: hwString , autobead: int, bead_threshold: float, layers: int, isosurface: int, mode: int, density_threshold: float, createplotel: int, detectbridge: int, lowthreshold: float):
		pass

	def transfertohypercrash(self,usecollection: int, collection: Collection, transfer: int, flag: int, arg: float, filepath: hwString ):
		pass

	def transformmark(self,collection: Collection, r1c1: float, r1c2: float, r1c3: float, r1c4: float, r2c1: float, r2c2: float, r2c3: float, r2c4: float, r3c1: float, r3c2: float, r3c3: float, r3c4: float, r4c1: float, r4c2: float, r4c3: float, r4c4: float):
		pass

	def translatemark(self,collection: Collection, vector: hwTriple, distance: float):
		pass

	def translatemarkwithsystem(self,collection: Collection, vector: hwTriple, distance: float, system_entity: Entity, origin: Entity):
		pass

	def translatewithreference(self,collection1: Collection, collection2: Collection, axis_type: int, drawbead_thickness: float, flag: int, total: hwDoubleList):
		pass

	def transparencymark(self,collection: Collection):
		pass

	def transparencyvalue(self,value: int):
		pass

	def triangle_clean_up(self,collection: Collection, criteria_string: hwString , graphicsDB: int =" 0"):
		pass

	def trim_by_offset_edges(self,surfs: Collection, lines: Collection, offset: float, break_mode: int, mode: int, break_angle: float):
		pass

	def trim_elements2(self,base_element_collection: Collection, trim_element_collection: Collection, mode: int, num_layers: int, feature_angle: float, base_component: int):
		pass

	def trim_elements_with_box(self,*args, **kwargs):
		"""
		trim_elements_with_box(HMAPI self, Collection trim_collection, Collection box_collection, hwString const & SPC_collector="", hwIntList DOF_array=hwIntList(), int const comp_remainder_elem_numb=-1, double const comp_remainder_area_rate=0.000000, bool const rebuild=False)
		"""
		pass

	def trim_elements_with_predefined_box(self,*args, **kwargs):
		"""
		trim_elements_with_predefined_box(HMAPI self, Collection collection, hwString const & cut_type, double limit, hwString const & spc_collector_name, hwString const & box_collector_name, hwString const & remesh_params, hwDoubleList dof_array=s_defaultDoubleList)
		"""
		pass

	def trim_elements_with_two_point_box(self,*args, **kwargs):
		"""
		trim_elements_with_two_point_box(HMAPI self, Collection collection, double x1, double y1, double z1, double x2, double y2, double z2, hwString const & spc_collector_name, hwString const & box_collector_name, hwString const & remesh_params, hwDoubleList dof_array=s_defaultDoubleList)
		"""
		pass

	def trim_elems_by_multi_circular_hole(self,node_collection: Collection, feature_angle: float, string_array: hwStringList, periphery_node_collection: Collection, background_elem_collection: Collection, rigid_spider: int):
		pass

	def trim_mesh_by_mesh(self,*args, **kwargs):
		"""
		trim_mesh_by_mesh(HMAPI self, Collection collection_source, Collection collection_target, int const ImprintOnMesh=2, Collection NodeCollection=hwDescriptor::Collection(), int const FetchImprintedEdges=1, int const ImprintedEdgesComp=0, int const RetainMarkedNodeCluster=0, double const SliverRatio=0.000000)
		"""
		pass

	def trim_shell_elems_by_shell_elems(self,collection: Collection, trimmer_collection: Collection, param_string: hwString ):
		pass

	def trim_solids_by_plane_normal_to_edge(self,solid_collection: Collection, line_collection: Collection, point_X: float, point_Y: float, point_Z: float, options: int):
		pass

	def trim_solids_by_surfaces(self,solid_collection: Collection, surf_collection: Collection, options: int):
		pass

	def trim_surfaces_with_nearby_lines(self,surf_to_trim: Collection, comps_from: Collection, max_distance: float, lines_from_selected_comps: int, only_with_edges: int, debug_mode: int):
		pass

	def trimcreateline(self,collection: Collection, lineflag: int):
		pass

	def trueview(self,plane_normal: hwTriple, plane_normal_base: hwTriple, id: int):
		pass

	def try_far_tria_reduction(self,smoothcollection: Collection, elemsize: float, minelemsize: float, maxelemsize: float, minangle: float, maxangle: float):
		pass

	def try_reverse_elements(self,smoothcollection: Collection, feature_angle: float, elem_type: int):
		pass

	def undercut_check(self,name: hwString , collection: Collection):
		pass

	def undohistorystate(self,count: var0):
		pass

	def unflange(self,collection: Collection, lineptr: Entity, angle: float):
		pass

	def unlockallentities(self,pool_entity: Entity, dataname: hwString ):
		pass

	def unlockentities(self,collection: Collection, dataname: hwString ):
		pass

	def unlockview(self):
		pass

	def unmaskall(self):
		pass

	def unmaskall2(self):
		pass

	def unmaskentitiesincollector(self,collection: Collection, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int, flag_6: int):
		pass

	def unmaskentitymark(self,collection: Collection, flag: int):
		pass

	def unmasksegments(self,set_ids: hwIntList, elem_ids: hwIntList, face_indices: hwIntList, consider_elems: bool  = False):
		pass

	def unmaskshown(self):
		pass

	def unmaskshown2(self):
		pass

	def unrealizeengineeringentities(self,collection: Collection, unrealize_mode: int):
		pass

	def unrealizeengineeringentity(self,entity: Entity, unrealize_mode: int):
		pass

	def unsmoothelements(self,faceindex: var0):
		pass

	def untrim_selected_edges(self,collection_lines: Collection, collection_surfs: Collection, untrim_option: int, keep_vertices: int, reserved1: float, reserved2: float):
		pass

	def updateEdgeBH(self,name: hwString , value: float, color: int, edgetype: int, friction: float):
		pass

	def updateairbag(self,collection: Collection, name: hwString ):
		pass

	def updateblankholder(self,name: hwString , bhpressure: float, tonnage: float, friction: float, color: int, collection: Collection):
		pass

	def updatecurvedatafromdtfile(self,fileName: hwString , curveId: var0):
		pass

	def updatedrawbead(self,drawbeadname: hwString , list: EntityList, color: int, db_force: float, lockbead: int):
		pass

	def updatefeatures(self,flag: int):
		pass

	def updatefree1delements(self,input_collection: Collection, output_collection: Collection, update_weight: int, summary_filename: hwString ):
		pass

	def updatehfconstraint(self,name: hwString , color: int, comp1: float, comp2: float, collection: Collection):
		pass

	def updatehfmaterial(self,name: hwString , k: float, e: float, epsilon0: float, r: float, n: float, id: int):
		pass

	def updatehfsolvermaterial(self,name: hwString , ys: float, nu: float, r0: float, r45: float, r90: float, ts: float):
		pass

	def updatehmdb(self,collection: Collection):
		pass

	def updateidrange(self,submodel_type: hwString , id: var0, shortname: hwString , entity_type: hwString , min_id: var0, max_id: var0, pool_id: var0, integer_array: hwIntList):
		pass

	def updateinclude(self,id: var0, shortname_flag: int, shortname: hwString , fullname_flag: int, fullname: hwString , parentid_flag: int, parentid: var0):
		pass

	def updateincludedata2(self,id: var0, shortname: hwString , do_not_export_flag: int, do_not_export: int, solver1_flag: int, solver1: int, solver2_flag: int, solver2: int, merge_flag: int, merge: int):
		pass

	def updateoffset(self,type: hwString , include_id: var0, shortname: hwString , entity_type: hwString , pool_id: var0, offset: var0):
		pass

	def updateoptimizationentitiesafterdelete(self):
		pass

	def updatepositions(self,collection: Collection):
		pass

	def updatepropertyfromstructuralproperty(self,*args, **kwargs):
		"""
		updatepropertyfromstructuralproperty(HMAPI self, hwString const & ddpgroupnames, hwString const & data1=s_defaultString, hwString const & data2=s_defaultString, hwString const & data3=s_defaultString, hwString const & data4=s_defaultString)
		"""
		pass

	def updatepropertyidforfejoints(self,collection: Collection, property_id: var0):
		pass

	def updatereferencegeometry(self,collection: Collection, name: hwString ):
		pass

	def updatesimexcomponent(self,name: hwString , type_flag: int, material_id: var0, thickness: float, friction: float, id: int, color: int, fld_comp_flag: int, curve_name: hwString , curvebinder: int):
		pass

	def updatesimexmaterial(self,name: hwString , k: float, e: float, epsilon0: float, r: float, n: float):
		pass

	def updatestackedentities(self,*args, **kwargs):
		"""
		updatestackedentities(HMAPIBase self, Entity id, hwEntityListList entitylist, hwString const & method="", unsigned int const index=0, bool const reorderinputbyindex=False)
		"""
		pass

	def updatesystemconstructiondata(self,systemptr: Entity, bForceUpdate: int =" 0"):
		pass

	def updatevalueboolrowcolumn(self,entity: Entity, identifier: hwString , value: int, row: hwString , column: var0):
		pass

	def updatevaluecoupledoublearray(self,entity: Entity, identifier: hwString , solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def updatevaluecoupledoublearraymark(self,collection: Collection, identifier: hwString , solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def updatevalueentityidarray2dmark(self,collection: Collection, identifier: hwString , solver: int, status: int, behavior: int, data: EntityList2):
		pass

	def updatevaluestringrowcolumn(self,entity: Entity, identifier: hwString , value: hwString , row: hwString , column: var0):
		pass

	def updatevaluetripledoublearray(self,entity: Entity, identifier: hwString , solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def updatevaluetripledoublearraymark(self,collection: Collection, identifier: hwString , solver: int, status: int, behavior: int, data: hwDoubleList):
		pass

	def updatevalueunsignedintrowcolumn(self,entity: Entity, identifier: hwString , value: var0, row: hwString , column: var0):
		pass

	def usercheck(self,template_file: hwString , output_file: hwString , all: int):
		pass

	def vabs(self,*args, **kwargs):
		"""
		vabs(HMAPI self, Collection collection, Collection beam_collection, int const exportvabs=0, hwString const & filepath="", int const createelements=0)
		"""
		pass

	def validate_mesh(self,inputcollection: Collection, filePath: hwString , param_strs: hwStringList):
		pass

	def validatefeatures(self,collection: Collection):
		pass

	def variablesimport(self,fileName: hwString ):
		pass

	def vectorcreate_xproduct(self,basenode: Entity, vector_a: Entity, vector_b: Entity, magnitude: float):
		pass

	def vectorplot(self,title: hwString , vector_size: float, mesh_color: int, full_size: int, constant_size: int):
		pass

	def vectorsoff(self):
		pass

	def vectorupdate_xproduct(self,collection: Collection, basenode: Entity, vector_a: Entity, vector_b: Entity, magnitude: float, baseflag: int, directionflag: int):
		pass

	def vertexrelease(self,vertex: Entity):
		pass

	def verticescombine(self,retained_point: Entity, collection: Collection):
		pass

	def verticesmarksuppress(self,collection: Collection, break_angle: float, save_as_points: int):
		pass

	def verticesrelease(self,collection: Collection):
		pass

	def view(self,view_name: hwString ):
		pass

	def view_restoreprevious(self):
		pass

	def viewset(self,a00: float, a01: float, a02: float, a03: float, a10: float, a11: float, a12: float, a13: float, a20: float, a21: float, a22: float, a23: float, a30: float, a31: float, a32: float, a33: float, minx: float, miny: float, maxx: float, maxy: float):
		pass

	def visualizemode(self,hiddenline: int, fillmode: int, meshmode: int, plot: int):
		pass

	def voxel_lattice_hex_mesh_add_box(self,collection: Collection, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, i1: float, j1: float, k1: float, i2: float, j2: float, k2: float):
		pass

	def voxel_lattice_hex_mesh_add_buffer_layers(self,num_buffer_layers: int):
		pass

	def voxel_lattice_hex_mesh_add_entities(self,collection: Collection, mode: int):
		pass

	def voxel_lattice_hex_mesh_add_entities_with_buffer(self,collection: Collection, num_buffer_layers: int):
		pass

	def voxel_lattice_hex_mesh_add_planar_constraint(self,base_x: float, base_y: float, base_z: float, normal_x: float, normal_y: float, normal_z: float, normal_side: int):
		pass

	def voxel_lattice_hex_mesh_add_volume(self,x: float, y: float, z: float):
		pass

	def voxel_lattice_hex_mesh_create(self):
		pass

	def voxel_lattice_hex_mesh_drag_faces(self,voxel_collection: Collection, face_node_collection: Collection, dx: float, dy: float, dz: float):
		pass

	def voxel_lattice_hex_mesh_end(self):
		pass

	def voxel_lattice_hex_mesh_fill_voids(self,mode: int):
		pass

	def voxel_lattice_hex_mesh_import(self,collection: Collection):
		pass

	def voxel_lattice_hex_mesh_init(self,voxel_size: float):
		pass

	def voxel_lattice_hex_mesh_remove_buffer_layers(self,num_buffer_layers: int):
		pass

	def voxel_lattice_hex_mesh_remove_constraints(self):
		pass

	def voxel_lattice_hex_mesh_remove_entities(self,collection: Collection, mode: int):
		pass

	def voxel_lattice_hex_mesh_remove_volume(self,x: float, y: float, z: float):
		pass

	def voxel_lattice_hex_mesh_renumber_to_grid_position(self):
		pass

	def wadlines_createfromresultsfile(self,file: hwString , title: hwString , color: int):
		pass

	def wadlines_createline(self,vertices: hwDoubleList, smooth: int):
		pass

	def wadlines_createlines(self,integer_array: hwIntList, float_array: hwDoubleList, line_type: int):
		pass

	def wadlines_createspheres(self,float_array: hwDoubleList, radius: float):
		pass

	def wadlines_hardpartzone(self,collection: Collection, float_array: hwDoubleList, vector: hwTriple, search_distance: float):
		pass

	def wadlines_windscreenperiphery(self,*args, **kwargs):
		"""
		wadlines_windscreenperiphery(HMAPI self, Collection windscreen_comps_collection, hwIntList line_list=hwIntList(), double const offset=165.000000, double const step_size=10.000000)
		"""
		pass

	def walldisplay(self,blockname: hwString , function: hwString , wallname: hwString ):
		pass

	def weld(self,independent: Entity, dependent: Entity, length: float, systems: int, movenode: int):
		pass

	def wind_tunnel_mesh(self,*args, **kwargs):
		"""
		wind_tunnel_mesh(HMAPIBase self, Collection collection, double elem_size, double interface_clearance, double front_space, double rear_space, double side_space, double top_space, double const tet_bl_first_layer_thickness=DBL_MAX, double const tet_bl_growth_rate=DBL_MAX, double const tet_bl_number_of_boundary_layers=DBL_MAX, double const bottom_bl_first_layer_thickness=DBL_MAX, double const bottom_bl_growth_rate=DBL_MAX, double const bottom_bl_number_of_boundary_layers=DBL_MAX)
		"""
		pass

	def window(self,function: int, xmin: float, ymin: float, xmax: float, ymax: float):
		pass

	def window_entitymark(self,collection: Collection):
		pass

	def wrap_mesh(self,srccollection: Collection, trgcollection: Collection, maxProximityDistance: float):
		pass

	def writeBlankShape(self,name: hwString , flag: int):
		pass

	def writeBlankShapePlusLine(self,name: hwString , lineflag: int):
		pass

	def writeFldToFile(self,filename: hwString , fld: hwString ):
		pass

	def writeMaterialToFile(self,filename: hwString , material: hwString ):
		pass

	def writecurrentqualitycriteria(self,file_name: hwString ):
		pass

	def writefile(self,filename: hwString , do_not_write_facets: int):
		pass

	def writeh3dwithoptions(self,*args, **kwargs):
		"""
		writeh3dwithoptions(HMAPI self, hwString const & filename, int const model=1, int const result=0, int const title=0, hwString const & orient="", int const overwrite=0)
		"""
		pass

	def writemodelcheckresultfile(self,filename: hwString , filetype: int):
		pass

	def writepart(self,file_path: hwString , collection: Collection):
		pass

	def writeqiviewsettings(self,file: hwString ):
		pass

	def writequalitysummary(self,applicable: hwIntList, data: hwDoubleList, name: hwString ):
		pass

	def xelem_bynodelist(self,node_list: EntityList, node_distance: float):
		pass

	def xelem_bysetid(self,node_set_id: int):
		pass

	def xyplotchangemode(self,plotname: hwString , mode: int):
		pass

	def xyplotcoloroverride(self,color: int):
		pass

	def xyplotcreate(self,plot: hwString , name: hwString ):
		pass

	def xyplotcreateandsize(self,plot_name: hwString , like_plot: hwString , xmin: float, xmax: float, ymin: float, ymax: float):
		pass

	def xyplotcreatecomplex(self,plot: hwString , name: hwString , mode: int):
		pass

	def xyplotcurvecreate(self,curve: hwString ):
		pass

	def xyplotcurvemodify(self,curve_name: hwString , item_name: hwString , string: hwString , value: float, plot: int):
		pass

	def xyplotcurvepermute(self,curve: hwString ):
		pass

	def xyplotdraw(self,plot: hwString ):
		pass

	def xyplotexpand(self,plot: hwString ):
		pass

	def xyplotfindcurves(self,plot: hwString ):
		pass

	def xyplotmodify(self,plot_name: hwString , item_name: hwString , string: hwString , value: float, plot: int):
		pass

	def xyplotmodifycurve(self,curvename: hwString , filename1: hwString , type1: hwString , req1: hwString , comp1: hwString , source1: int, filename2: hwString , type2: hwString , req2: hwString , comp2: hwString , source2: int):
		pass

	def xyplotonecurvemath(self,function: int, outputname: hwString , xbased: int, factor: float):
		pass

	def xyplotorganize(self):
		pass

	def xyplotpage(self):
		pass

	def xyplotpop(self,plot: hwString ):
		pass

	def xyplotpush(self,plot: hwString ):
		pass

	def xyplotreadcurve(self,filename: hwString ):
		pass

	def xyplotreadengineeringcurve(self,filename: hwString ):
		pass

	def xyplotregisterexternalreader(self,path: hwString ):
		pass

	def xyplotregisterimporttemplate(self,filename: hwString ):
		pass

	def xyplotsetcurrent(self,plot: hwString ):
		pass

	def xyplotsetcurve(self,curve: hwString ):
		pass

	def xyplotsetcurves(self,plotname: hwString , collection: Collection):
		pass

	def xyplotsetsecondcurve(self,curvename: hwString ):
		pass

	def xyplotstack(self):
		pass

	def xyplottwocurvemath(self,function: int, outputcurve: hwString , xbased: int):
		pass

	def xyplotwindow(self,plotname: hwString , xmin: float, xmax: float, ymin: float, ymax: float):
		pass

	def xyplotzoomout(self,plot: hwString ):
		pass

RELATIVE_LOCATION_INSIDE=0

RELATIVE_LOCATION_ONBOUNDARIES=2

RELATIVE_LOCATION_OUTSIDE=1

class Session:
	def __init__(self):
		"""
Get a list of models in session
    
    This custom override makes use of the optional list argument of instance().GetAllModels in order
    to return to its caller the list of models that contain at least one connection to an HM adaptor
    (e.g. HM or HMBatch adaptors)

    Returns
    -------
        A list of model names         
    
"""
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

	def get_current_model(self):
		pass

	def get_entityfulltype_from_classname(self,metaclass: str):
		pass

	def get_entityfulltype_from_metaclass(self,handle: int):
		pass

	def get_ownership(self,owner_handle: int, child):
		pass

	def get_uid_attributename(self,fulltype):
		pass

	def getclass(self,fulltype: hwdescriptor_module.EntityFullType|int):
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

	def remove_model(self,model: str|hwdescriptor_module.Model):
		pass

	def set_ownership(self,owner_handle: int, child, attribute_handle: int):
		pass

class TMDIObject:
	"""
Type variable.

    Usage::

      T = TypeVar('T')  # Can be anything
      A = TypeVar('A', str, bytes)  # Must be str or bytes

    Type variables exist primarily for the benefit of static type
    checkers.  They serve as the parameters for generic types as well
    as for generic function definitions.  See class Generic for more
    information on generic types.  Generic functions work as follows:

      def repeat(x: T, n: int) -> List[T]:
          '''Return a list containing n references to x.'''
          return [x]*n

      def longest(x: A, y: A) -> A:
          '''Return the longest of two strings.'''
          return x if len(x) >= len(y) else y

    The latter example's signature is essentially the overloading
    of (str, str) -> str and (bytes, bytes) -> bytes.  Also note
    that if the arguments are instances of some subclass of str,
    the return type is still plain str.

    At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError.

    Type variables defined with covariant=True or contravariant=True
    can be used to declare covariant or contravariant generic types.
    See PEP 484 for more details. By default generic types are invariant
    in all type variables.

    Type variables can be introspected. e.g.:

      T.__name__ == 'T'
      T.__constraints__ == ()
      T.__covariant__ == False
      T.__contravariant__ = False
      A.__constraints__ == (str, bytes)

    Note that only type variables defined in global scope can be pickled.
    
"""
	pass

class Type:
	def __init__(self,*args, **kwargs):
		"""
A special construct usable to annotate class objects.

    For example, suppose we have the following classes::

      class User: ...  # Abstract base for User classes
      class BasicUser(User): ...
      class ProUser(User): ...
      class TeamUser(User): ...

    And a function that takes a class argument that's a subclass of
    User and returns an instance of the corresponding class::

      U = TypeVar('U', bound=User)
      def new_user(user_class: Type[U]) -> U:
          user = user_class()
          # (Here we could write the user object to a database)
          return user

      joe = new_user(BasicUser)

    At this point the type checker knows that joe has type BasicUser.
    
"""
		pass

	def copy_with(self,params):
		pass

class Uid:
	def __init__(self,*args):
		pass

	def AsString(self):
		pass

	def IsValid(self):
		pass

	def Serialize(self,stream: ostream):
		pass

	@property
	def branch(self):
		pass
	@branch.setter
	def branch(self):
		pass

	@property
	def is_numeric(self):
		pass
	@is_numeric.setter
	def is_numeric(self):
		pass

	@property
	def number(self):
		pass
	@number.setter
	def number(self):
		pass

	@property
	def revision(self):
		pass
	@revision.setter
	def revision(self):
		pass

	@property
	def string(self):
		pass
	@string.setter
	def string(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class Union:
	def __init__(self,*args, **kwds):
		"""
Internal indicator of special typing constructs.
    See _doc instance attribute for specific docs.
    
"""
		pass

altair_home:str

class coreCollection:
	def __init__(self,*args, **kwargs):
		"""

    Constructor codepaths:
        __init__([metaobject])
        __init__(model, [entity])
        __init__(model, EntityList)
        __init__(model, Filter)
        __init__(model, FilterByCollection, source_collection)
        __init__(model, type)
        __init__(model, type, string)
        __init__(model, type, bool)
        __init__(model, type, [uid (int/string)])
        __init__(model, type, [entities from source collection], [Identifiers])
        __init__(model, type, [objects from source collection], [Identifiers])
        __init__(model, type, Collection, [Identifiers])
    
"""
		pass

	def TestValue(self,identifier: Identifier, value: Value):
		pass

	def add(self,rule: CollectionRule, source: Collection = None):
		pass

	def begin(self,forPython: bool = False):
		pass

	def complement(self):
		pass

	def contains(self,entity: Entity):
		pass

	def delete_items(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	def empty(self):
		pass

	def get_attribute_definition(self,identifier: str):
		pass

	def intersect(self,rule: CollectionRule, source: Collection = None):
		pass

	@property
	def mdimodel(self):
		pass
	@mdimodel.setter
	def mdimodel(self):
		pass

	def set_items(self,identifier: str, value):
		pass

	def subtract(self,rule: CollectionRule, source: Collection = None):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class coreFilterByCollection:
	def __init__(self,aclass: EntityClass, source_class: EntityClass, identifiers: list[str]|list[hwdescriptor_module.Identifier], *args):
		pass

	def DownCast(self,o: CollectionRule):
		pass

	def GetOperator(self,index: var0):
		pass

	def GetRule(self,index: var0):
		pass

	@property
	def aggregation(self):
		pass
	@aggregation.setter
	def aggregation(self):
		pass

	@property
	def eclass(self):
		pass
	@eclass.setter
	def eclass(self):
		pass

	@property
	def identifiers(self):
		pass
	@identifiers.setter
	def identifiers(self):
		pass

	@property
	def source(self):
		pass
	@source.setter
	def source(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

def hm_getcurrentmodel(*args, **kwargs):
	"""
hm_getcurrentmodel(hwString const & flag="False")
"""
	pass

def hm_getoption(option: hwString, defaultValue: int  = 0):
	pass

def hm_getoption_cad_reader(*args, **kwargs):
	"""
hm_getoption_cad_reader(hwString const & cad_reader, hwString const & option="")
"""
	pass

def hm_getoption_cad_writer(*args, **kwargs):
	"""
hm_getoption_cad_writer(hwString const & cad_writer, hwString const & option="")
"""
	pass

class hwBoolList:
	def __init__(self,*args):
		pass

	def append(self,x: bool):
		pass

	def assign(self,n: int, x: bool):
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

	def push_back(self,x: bool):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwBoolList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwCouple:
	def __init__(self,*args):
		pass

	def Add(self,*args):
		pass

	def Assign(self,*args):
		pass

	def Div(self,v: float):
		pass

	def Divide(self,v: float):
		pass

	def GetU(self):
		pass

	def GetV(self):
		pass

	def GetX(self):
		pass

	def GetY(self):
		pass

	def HasInfinity(self):
		pass

	def Len(self):
		pass

	def Len2(self):
		pass

	def Length(self):
		pass

	def Length2(self):
		pass

	def Mul(self,v: float):
		pass

	def Multiply(self,v: float):
		pass

	def Normalize(self,*args):
		pass

	def Set(self,*args):
		pass

	def SetMax(self,_in: hwCouple):
		pass

	def SetMin(self,_in: hwCouple):
		pass

	def SetNegInfinity(self):
		pass

	def SetPosInfinity(self):
		pass

	def SetU(self,v: float):
		pass

	def SetV(self,v: float):
		pass

	def SetX(self,v: float):
		pass

	def SetY(self,v: float):
		pass

	def SetZero(self):
		pass

	def Sub(self,*args):
		pass

	def Subtract(self,*args):
		pass

	def U(self,*args):
		pass

	def V(self,*args):
		pass

	def X(self,*args):
		pass

	def Y(self,*args):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwDoubleList:
	def __init__(self,*args):
		pass

	def append(self,x: float):
		pass

	def assign(self,n: int, x: float):
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

	def push_back(self,x: float):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwDoubleList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwDoubleListList:
	def __init__(self,*args):
		pass

	def append(self,x: hwDoubleList):
		pass

	def assign(self,n: int, x: hwDoubleList):
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

	def push_back(self,x: hwDoubleList):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwDoubleListList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwIntList:
	def __init__(self,*args):
		pass

	def append(self,x: int):
		pass

	def assign(self,n: int, x: int):
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

	def push_back(self,x: int):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwIntList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwIntListList:
	def __init__(self,*args):
		pass

	def append(self,x: hwIntList):
		pass

	def assign(self,n: int, x: hwIntList):
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

	def push_back(self,x: hwIntList):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwIntListList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwMatrix44:
	def __init__(self,*args):
		pass

	def Add(self,*args):
		pass

	def ApplyRotation(self,rotation_v: hwTriple, rotAngInRad: float):
		pass

	def ApplyScaling(self,*args):
		pass

	def ApplyTranslation(self,trans: hwTriple):
		pass

	def Assign(self,rhs: hwMatrix44):
		pass

	def Columns(self):
		pass

	def Data(self,*args):
		pass

	def Det(self):
		pass

	def Divide(self,*args):
		pass

	def GetCell(self,row: var0, col: var0):
		pass

	def HasReflection(self):
		pass

	def Invert(self):
		pass

	def InvertFast(self):
		pass

	def IsIdentity(self):
		pass

	def IsIsotropic(self):
		pass

	def MakeIdentity(self):
		pass

	def Multiply(self,*args):
		pass

	def Rows(self):
		pass

	def SetCell(self,row: var0, col: var0, value: float):
		pass

	def Subtract(self,*args):
		pass

	def Transform(self,xyz: hwTriple):
		pass

	def Transform33(self,xyz: hwTriple):
		pass

	def Transpose(self):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwString:
	def __init__(self,*args):
		pass

	def c_str(self):
		pass

	def compareTo(self,*args):
		pass

	def contains(self,*args):
		pass

	def first(self,*args):
		pass

	def hash(self):
		pass

	def hash_string(self,c: hwString):
		pass

	def index(self,*args):
		pass

	def isEmpty(self):
		pass

	def isNull(self):
		pass

	def last(self,*args):
		pass

	def length(self):
		pass

	def prepend(self,*args):
		pass

	def remove(self,*args):
		pass

	def reverse(self):
		pass

	def subString(self,*args):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	def tolower(self):
		pass

	def toupper(self):
		pass

class hwStringList:
	def __init__(self,*args):
		pass

	def append(self,x: hwString):
		pass

	def assign(self,n: int, x: hwString):
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

	def push_back(self,x: hwString):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwStringList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwTriple:
	def __init__(self,*args):
		pass

	def Add(self,*args):
		pass

	def Assign(self,*args):
		pass

	def Div(self,v: float):
		pass

	def Divide(self,v: float):
		pass

	def GetX(self):
		pass

	def GetY(self):
		pass

	def GetZ(self):
		pass

	def HasInfinity(self):
		pass

	def Len(self):
		pass

	def Len2(self):
		pass

	def Length(self):
		pass

	def Length2(self):
		pass

	def Mul(self,v: float):
		pass

	def Multiply(self,v: float):
		pass

	def Normalize(self,*args):
		pass

	def Set(self,*args):
		pass

	def SetMax(self,_in: hwTriple):
		pass

	def SetMin(self,_in: hwTriple):
		pass

	def SetNegInfinity(self):
		pass

	def SetPosInfinity(self):
		pass

	def SetX(self,v: float):
		pass

	def SetY(self,v: float):
		pass

	def SetZ(self,v: float):
		pass

	def SetZero(self):
		pass

	def Sub(self,*args):
		pass

	def Subtract(self,*args):
		pass

	def X(self,*args):
		pass

	def Y(self,*args):
		pass

	def Z(self,*args):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwTripleI:
	def __init__(self,*args):
		pass

	def Add(self,*args):
		pass

	def Assign(self,*args):
		pass

	def Div(self,v: int):
		pass

	def Divide(self,v: int):
		pass

	def GetX(self):
		pass

	def GetY(self):
		pass

	def GetZ(self):
		pass

	def HasInfinity(self):
		pass

	def Len(self):
		pass

	def Len2(self):
		pass

	def Length(self):
		pass

	def Length2(self):
		pass

	def Mul(self,v: int):
		pass

	def Multiply(self,v: int):
		pass

	def Normalize(self,*args):
		pass

	def Set(self,*args):
		pass

	def SetMax(self,_in: hwTripleI):
		pass

	def SetMin(self,_in: hwTripleI):
		pass

	def SetNegInfinity(self):
		pass

	def SetPosInfinity(self):
		pass

	def SetX(self,v: int):
		pass

	def SetY(self,v: int):
		pass

	def SetZ(self,v: int):
		pass

	def SetZero(self):
		pass

	def Sub(self,*args):
		pass

	def Subtract(self,*args):
		pass

	def X(self,*args):
		pass

	def Y(self,*args):
		pass

	def Z(self,*args):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwTripleIList:
	def __init__(self,*args):
		pass

	def append(self,x: hwTripleI):
		pass

	def assign(self,n: int, x: hwTripleI):
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

	def push_back(self,x: hwTripleI):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwTripleIList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwTripleList:
	def __init__(self,*args):
		pass

	def append(self,x: hwTriple):
		pass

	def assign(self,n: int, x: hwTriple):
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

	def push_back(self,x: hwTriple):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwTripleList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwUIntList:
	def __init__(self,*args):
		pass

	def append(self,x: var0):
		pass

	def assign(self,n: int, x: var0):
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

	def push_back(self,x: var0):
		pass

	def rbegin(self):
		pass

	def rend(self):
		pass

	def reserve(self,n: int):
		pass

	def resize(self,*args):
		pass

	def size(self):
		pass

	def swap(self,v: _hwUIntList_vector):
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

class hwx:
	pass

class initmdi:
	"""
 HyperMesh MDI Initialization

Methods to intitialize MDI HyperMesh Adaptor and Create MDI Model

"""
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

sessionCmd:str='setoption_cadwriter'

def setoption(*args, **kwargs):
	pass

def setoption_cadreader(cad_reader: hwString ,option_name: hwString , option_value: hwString ):
	pass

def setoption_cadwriter(cad_writer: hwString , option_name: hwString , option_value: hwString ):
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

unity_root:str

