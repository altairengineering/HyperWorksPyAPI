from typing import TypeVar
class size_t:
	pass
class hwMatrix44:
	pass
class hwBox3:
	pass

class AxisPoints:
	def __init__(self,iterable=()):
		"""
list[Point]: 2+ Points along a line
"""
		pass

	@property
	def center(self):
		pass
	@center.setter
	def center(self):
		pass

	@property
	def direction(self):
		pass
	@direction.setter
	def direction(self):
		pass

class Box:
	def __init__(self,position, x, y, z):
		"""
Position and x, y, z dimension lengths.
  
  APIs will always return non axis-aligned bounding boxes so:
    box.x >= box.y >= box.z
  
"""
		pass

	def Contains(self,*args):
		pass

	def GetAxis(self,i: size_t):
		pass

	def GetCenter(self):
		pass

	def GetExtent(self,i: size_t):
		pass

	def GetTransformedBy(self,transf: hwMatrix44):
		pass

	def GetVertices(self,*args):
		pass

	def GetVolume(self):
		pass

	def Grow(self,*args):
		pass

	def Intersects(self,box: hwBox3):
		pass

	def IsEmpty(self):
		pass

	def Transform(self,transf: hwMatrix44):
		pass

	@property
	def extents(self):
		pass
	@extents.setter
	def extents(self):
		pass

	def fromMinMax(self,minPoint, maxPoint):
		"""
		Create an axis-aligned box from corner points.
		"""
		pass

	@property
	def minMax(self):
		pass
	@minMax.setter
	def minMax(self):
		pass

	def sortAxes(self):
		"""
		Update axes so box.x >= box.y >= box.z.
		"""
		pass

	@property
	def thisown(self):
		pass
	@thisown.setter
	def thisown(self):
		pass

	@property
	def xyz(self):
		pass
	@xyz.setter
	def xyz(self):
		pass

class Matrix44:
	def __init__(self,values=None, origin=None, angles=None, degrees=False, scale=None, xv=None, yv=None, zv=None, xvyv=None, xvzv=None, yvxv=None, yvzv=None, zvxv=None, zvyv=None, xp=None, yp=None, zp=None, xpyp=None, xpzp=None, ypxp=None, ypzp=None, zpxp=None, zpyp=None, eulerParameters=None):
		"""
A 4x4 orthonormal Matrix.
"""
		pass

	@property
	def angles(self):
		pass
	@angles.setter
	def angles(self):
		pass

	def copy(self):
		"""
		Creates a copy of self.

    Returns:
      Matrix44: The newly created Matrix44.
    
		"""
		pass

	def divide(self,other):
		"""
		Returns the result of the multiplication with the inverse of other.

    Args:
      other (Matrix44): The Matrix44 to inverse and multiply with.

    Returns:
      Matrix44: The result of the multiplication with the inverse.
    
		"""
		pass

	def format(self,format="%s"):
		"""
		Formats as a string.

    Args:
      format (str): The format style to use.

    Returns:
      str: A string represantation of the instance Matrix44 object on which it was called.
    
		"""
		pass

	def getAxisAndAngleOfRotation(self):
		"""
		Returns the axis and angle from the rotation matrix
		"""
		pass

	def getDeterminant(self):
		"""
		Returns the matrix determinant.
		"""
		pass

	def getEulerAngles(self,degrees=False):
		"""
		Returns the Euler angles.

    Args:
      degrees (bool): Determines if the angle values are in degrees or not.

    Returns:
      list: The Euler angles.
    
		"""
		pass

	def getTrace(self):
		pass

	def getTranslation(self):
		"""
		Returns the position as a Point.
		"""
		pass

	def invert(self):
		"""
		Computes the inverse.

    Returns:
      Matrix44: The inverse of the instance Matrix44 object on which it was called.
    
		"""
		pass

	def isIdentity(self):
		"""
		Returns True if self is the identity matrix, False otherwise.
		"""
		pass

	@property
	def location(self):
		pass
	@location.setter
	def location(self):
		pass

	def multiply(self,other):
		"""
		Multiplies with other.

    Args:
      other (float | Point | Vector | Matrix44): The other to multiply with.

    Returns:
      Matrix44 | Vector | Point: The result of the multiplication.
    
		"""
		pass

	def multiplyPoint(self,x, y=None, z=None):
		"""
		Multiplies with a Point.
    
    Points are represented as mathematical column points and have a one in the 
    fourth position, which includes translation operations.

    Args:
      x (Point | list[float] | float): An itetable of 3 or the x value of a Point.
      y (float): The y value of a Point.
      z (float): The z value of a Point.

    Returns:
      Point: The result of the multiplication.
    
		"""
		pass

	def multiplyVector(self,x, y=None, z=None):
		"""
		Multiplies with the Vector specified with x, y, z.
    
    Vectors are represented as mathematical column vectors and have a zero in the 
    fourth position, which does not include translation operations.

    Args:
      x (Vector | list[float] | float): An itetable of 3 or the x value of a Vector.
      y (float): The y value of a Vector.
      z (float): The z value of a Vector.

    Returns:
      Vector: The result of the multiplication.
    
		"""
		pass

	def orientFromAxes(self,axes, dir1, dir2=(1, 0, 0)):
		"""
		Orients with the specified axes.

    Args:
      axes (str): The axis to orient by: 
        Valid choices are 'x', 'y', 'z', 'xy', 'xz', 'yx', 'yz', 'zx', 'zy'.
      dir1 (Vector | list[float]): The vector for the first axis.
      dir2 (Vector | list[float]): The vector for the second axis.

    Raises:
      RuntimeError: In case of unsupported axes specification

    Returns:
      Matrix44: A reference to the instance Matrix44 object on which it was called.
    
		"""
		pass

	def orientFromEulerAngles(self,e1, e2=None, e3=None, degrees=False):
		"""
		Orients with the specified Euler angles.

    Args:
      e1 (float): Rotation around x-axis.
      e2 (float): Rotation around y-axis.
      e3 (float): Rotation around z-axis.
      degrees (bool): Determines if the angle values are in degrees or not.

    Returns:
      Matrix44: A reference to the instance Matrix44 object on which it was called.
    
		"""
		pass

	def orientFromEulerParameters(self,e0, e1=None, e2=None, e3=None):
		"""
		Orients with the specified Euler parameters.

    Args:
      e0 (float): Euler parameter.
      e1 (float): Euler parameter.
      e2 (float): Euler parameter.
      e3 (float): Euler parameter.

    Returns:
      Matrix44: A reference to the instance Matrix44 object on which it was called.
    
		"""
		pass

	@property
	def origin(self):
		pass
	@origin.setter
	def origin(self):
		pass

	def orthogonalize(self):
		"""
		Orthogonalizes the axes (x, y, z).

    Raises:
      RuntimeError: If Matrix44 can not be orthogonalized.

    Returns:
      Matrix44: A Matrix44 with x, y, z being orthogonal.
    
		"""
		pass

	@property
	def phi(self):
		pass
	@phi.setter
	def phi(self):
		pass

	@property
	def psi(self):
		pass
	@psi.setter
	def psi(self):
		pass

	def pt(self,x, y=None, z=None):
		"""
		Multiplies with a Point.
    
    Points are represented as mathematical column points and have a one in the 
    fourth position, which includes translation operations.

    Args:
      x (Point | list[float] | float): An itetable of 3 or the x value of a Point.
      y (float): The y value of a Point.
      z (float): The z value of a Point.

    Returns:
      Point: The result of the multiplication.
    
		"""
		pass

	def pts(self,pts):
		"""
		Returns the result of multiplying each Point in the specified list of 
    Points with self.

    Args:
      pts (Point | list[float]): A Point (or list).

    Returns:
      list[Point]: The result of the pieswise multiplication.
    
		"""
		pass

	def rotate(self,axis, angle, degrees=True):
		"""
		Rotates around the specified axis.

    This is a body rotation.

    Args:
      axis (Vector | str): The rotation axis.
        Valid choices are "x", "y", "z" or any Vector.
      angle (float): The rotation angle.
      degrees (bool): Determines if angles is in degrees or not.

    Returns:
      Matrix44: A newly created Matrix44.
    
		"""
		pass

	def rotateAroundAxis(self,axis, angle, degrees=True):
		"""
		Rotates around the axis.

    This is a body rotation.

    Args:
      axis (Vector): The rotation axis.
      angle (float): The rotation angle.
      degrees (bool): Determines if angles is in degrees or not.

    Returns:
      Matrix44: A newly created Matrix44.
    
		"""
		pass

	def rotx(self,angle, degrees=True):
		"""
		Rotates around the x-axis.

    This is a body rotation.

    Args:
      angle (float): The rotation angle.
      degrees (bool): Determines if angles is in degrees or not.

    Returns:
      Matrix44: A newly created Matrix44.
    
		"""
		pass

	def roty(self,angle, degrees=True):
		"""
		Rotates around the y-axis.

    This is a body rotation.

    Args:
      angle (float): The rotation angle.
      degrees (bool): Determines if angles is in degrees or not.

    Returns:
      Matrix44: A newly created Matrix44.
    
		"""
		pass

	def rotz(self,angle, degrees=True):
		"""
		Rotates around the z-axis.

    This is a body rotation.

    Args:
      angle (float): The rotation angle.
      degrees (bool): Determines if angles is in degrees or not.

    Returns:
      Matrix44: A newly created Matrix44.
    
		"""
		pass

	def scale(self,x, y=None, z=None):
		"""
		Scales by the specified amount in x, y, z.

    If y is None, x is assumed to be a list of 3 floats.

    Args:
      x (float): The factor to multiply the 'x' vector with.
      y (float): The factor to multiply the 'y' vector with.
      z (float): The factor to multiply the 'z' vector with.

    Returns:
      Matrix44: A newly created Matrix44.
    
		"""
		pass

	def setTranslation(self,x, y=None, z=None):
		"""
		Sets the position as a Point.

    If y is None, x is assumed to be a list of 3 floats.

    Args:
      x (float): The vector to set the 'x' vector.
      y (float): The vector to set the 'y' vector.
      z (float): The vector to set the 'z' vector.

    Returns:
      Matrix44: A reference to the instance Matrix44 object on which it was called.
    
		"""
		pass

	@property
	def theta(self):
		pass
	@theta.setter
	def theta(self):
		pass

	def translate(self,x="0", y=None, z=None):
		"""
		Translates by the specified distance each x, y, z vector.

    If y is None, x is assumed to be a list of 3 floats.

    Args:
      x (float): The distance to translate the 'x' vector.
      y (float): The distance to translate the 'y' vector.
      z (float): The distance to translate the 'z' vector.

    Returns:
      Matrix44: A reference to the instance Matrix44 object on which it was called.
    
		"""
		pass

	def transpose(self):
		"""
		Returns the transpose.
		"""
		pass

	def update(self,other):
		"""
		Copies the data from other to self.

    Args:
      other (Matrix44): The Matrix44 to copy values from.

    Returns:
      Matrix44: A reference to the instance Matrix44 object on which it was called.
    
		"""
		pass

	def vec(self,x, y=None, z=None):
		"""
		Multiplies with the Vector specified with x, y, z.
    
    Vectors are represented as mathematical column vectors and have a zero in the 
    fourth position, which does not include translation operations.

    Args:
      x (Vector | list[float] | float): An itetable of 3 or the x value of a Vector.
      y (float): The y value of a Vector.
      z (float): The z value of a Vector.

    Returns:
      Vector: The result of the multiplication.
    
		"""
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

	def zeroSmallValues(self,zero=1e-10):
		"""
		Sets all components that are less than the specified value to zero.

    Args:
      zero (float): The tolerance on what to zero.

    Returns:
      Matrix44: A reference to the instance Matrix44 object on which it was called.
    
		"""
		pass

	def zp(self,pt1, pt2=None):
		"""
		Depricated
		"""
		pass

class Point:
	def __init__(self,x="0", y="0", z="0"):
		"""
A mathematical representation of a point in 3D space.
"""
		pass

	def along(self,towards, distance):
		"""
		Computes the point along the line segment.

    Defined by self and 'towards', at 'distance' from self.

    Args:
      towards (Point): The end point.
      distance (float): The distance from the Point defined in self.

    Returns:
      Point: The newly created point.
    
		"""
		pass

	def angle(self,x, y=None, z=None, degrees=False):
		"""
		Computes the angle with the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.
      degrees (bool): Determines if the return value will be in degrees or not.

    Returns:
      float: The angle.
    
		"""
		pass

	def close(self,x, y=None, z=None, tol=1e-07):
		"""
		Determines if the distance to the Vector defined by x, y, z is less or 
    equal than tolerance.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.
      tolerance (float): The tolerance to consider when checking condition.

    Returns:
      bool: True if Vectors are close, False otherwise.
    
		"""
		pass

	def copy(self,x=None, y=None, z=None):
		"""
		Creates a copy of self.

    If x, y, z are given then the copy has these as coordinates.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      Vector: The newly created object.
    
		"""
		pass

	def cross(self,x, y=None, z=None):
		"""
		Computes the cross product with the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      Vector: The cross product.
    
		"""
		pass

	def distance(self,x, y=None, z=None):
		"""
		Computes the distance to the point defined by x, y, z.
    
    If y is None, x is assumed to be a point (or list).

    Args:
      x (float | Point | list[float]): The x coordinate or a point.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      float: The distance.
    
		"""
		pass

	def distanceTo(self,x, y=None, z=None):
		"""
		Computes the distance to the point defined by x, y, z.
    
    If y is None, x is assumed to be a point (or list).

    Args:
      x (float | Point | list[float]): The x coordinate or a point.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      float: The distance.
    
		"""
		pass

	def distanceToPlane(self,a, b=None, c=None, d=None):
		"""
		Computes the distance to the parametric plane.
    
    The parametric plane is given by the equation is ax + by + cz + d = 0.
    
    If b is None, a is assumed to be a list.

    Args:
      a (float, list[float]): The constant 'a' or a list of all constants.
      b (float): The constant 'b'.
      c (float): The constant 'c'.
      d (float): The constant 'd'.

    Returns:
      float: The distance.
    
		"""
		pass

	def dot(self,x, y=None, z=None):
		"""
		Computes the dot product with the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      float: The dot product.
    
		"""
		pass

	def findAngle(self,pt1, pt2, pt3, degrees=False):
		"""
		Computes the angle subtended between (pt2-pt1) and (pt3-pt1).

    Args:
      pt1 (Vector): The first Vector.
      pt2 (Vector): The second Vector.
      pt3 (Vector): The third Vector.
      degrees (bool): Determines if the return value will be in degrees or not.

    Returns:
      float: The angle.
    
		"""
		pass

	def isAlignedWith(self,x, y=None, z=None, tolerance=1e-05, normalize=True):
		"""
		Determines if self is parallel to the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.
      tolerance (float): The tolerance to consider when checking condition.
      normalize (bool): Determines whether to normalize self before checking the condition.

    Returns:
      bool: True if Vectors are aligned, False otherwise.
    
		"""
		pass

	def iszero(self):
		"""
		Returns True if x, y and z are set to zero, False otherwise.
		"""
		pass

	def magnitude(self):
		"""
		Returns the magnitude.
		"""
		pass

	def midpt(self,x, y=None, z=None):
		"""
		Computes the middle point of the line segment between self and the point
    defined by x, y, z.

    If y is None, x is assumed to be a Point (or list).
    
    Args:
      x (float | Point | list[float]): The x coordinate or a Point.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      Point: The middle point.
    
		"""
		pass

	def normalize(self):
		"""
		Returns the normalized Vector.
		"""
		pass

	def perpendicularize(self):
		"""
		Computes a Vector perpendicular to self.

    If any of the coordinates are zero, returns a Vector along that coordinate, 
    otherwise returns the cross product with (1, 0, 0).
    
		"""
		pass

	def planeFromPoints(self,pt1, pt2, pt3):
		"""
		Computes the plane defined by the three points.

    Args:
      pt1 (Point): The first point.
      pt2 (Point): The second point.
      pt3 (Point): The third point.

    Returns:
      tuple: The constants of the a parametric plane equation.
    
		"""
		pass

	def scale(self,x, y=None, z=None):
		"""
		Scales by a single value 'x' or a tripple (x, y, z), elementwise.

    Args:
      x (float): The x scale factor.
      y (float): The y scale factor.
      z (float): The z scale factor.

    Returns:
      Vector: The scaled Vector.
    
		"""
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

class Spline:
	def __init__(self,x, y=None, unitSystem=None,xunits: str="time",yunits: str="length"):
		"""
A two element list of (x, y) values.
  
  Spline has methods to convert to/from units, add/insert/delete rows, interpolate, 
  get the derivative and read/write CSV files. 
  
  The length of x should be the same as y and at least 4. Also, x should be 
  increasing i.e. x[i] < x[i+1].
  
"""
		pass

	def addInterpolated(self,row):
		"""
		Adds a linear interpolated value after the specified row.

    Args:
      row (int): The row where to add the value after.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def appendInterpolated(self):
		"""
		Appends a linear interpolated value.
    
    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def copy(self,**kwds):
		"""
		Return a copy of self.
    
    It is updated with kwds if specified to support derived classes.
    
		"""
		pass

	def deleteRows(self,*deleteRows):
		"""
		Removes the specified rows.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def derivative(self,order=1, npts=None, type="akima", scaled=True):
		"""
		Computes the derivative.

    Scale the derivative so it is not too big but can still be viewed.

    Args:
      order (int): Order of the derivative.
      npts (int): Number of points to interpolate.
      type (str): Type of Interpolation.
      scaled (bool | float): The factor to scale y values.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def fromBaseUnits(self):
		"""
		Makes the Spline values work like other Double values.
    
		"""
		pass

	def getFormattedStrings(self,format=5):
		"""
		Returns the values suitable for display in the gui fields or table cells.

    Args:
      format (int | str): The format of the values as strings.

    Returns:
      list[list[float], list[float]]: The x, y values.
    
		"""
		pass

	def getXFromY(self,y):
		"""
		Returns a computed x value from the specified y value.

    This uses linear interpolation since we can not assume the y values are 
    monotonically increasing.
    
    Args:
      y (float): The y value.

    Returns:
      float: The x value.
    
		"""
		pass

	def insertInterpolated(self,row):
		"""
		Adds a linear interpolated value before the specified row.

    Args:
      row (int): The row where to add the value before.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def interpolate(self,npts=None, type="akima", order="0", x=None):
		"""
		Recalculates x and y by interpolation.

    This is used to get equally spaced values of x, kind can be "akima" or any 
    scipy.interpolate.inter1d.

    If x is specified, returns the computed y value.

    Args:
      npts (int): Number of samples to generate, if x is None.
      type (str): The type of interpolation.
        Possible choices are "akima", "linear", "cubic", "zero", "natural".
        If none of these is given then "splev" is used.
      order (int): The order of interpolation.
      x (float): The x value used to return the interpolated y.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def isValid(self):
		"""
		Determines if self can be interpolated and if the derivative can be computed.

    Returns:
      bool: True if it is valid, False otherwise.
    
		"""
		pass

	def prependInterpolated(self):
		"""
		Adds a linear interpolated value in the beginning.
    
    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def readCsv(self,fname, validationMethod=None):
		"""
		Reads a csv file to populate the x/y values.

    Args:
      fname (str): The path to the csv file.
      validationMethod (func): A function used to validate the csv reading.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def reflect(self):
		"""
		Reflects the data across X and Y.
		"""
		pass

	def removeNegativeX(self):
		"""
		Removes x, y pairs with negative x values.
		"""
		pass

	def scalex(self,factor):
		"""
		Mulitplies the x values by a scale factor.

    Args:
      factor (float): The factor to multiply the values with.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def scaley(self,factor):
		"""
		Mulitplies the y values by a scale factor.

    Args:
      factor (float): The factor to multiply the values with.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def setComponent(self,row, col, value):
		"""
		Sets a single value.

    Args:
      row (int): The row value to set.
      col (int): The column value to set.
      value (float): The value to set.

    Raises:
      SplineValueError: If value is not numeric.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def setValues(self,x, y=None):
		"""
		Sets the list of x and y values.

    Args:
      x (list): The list of x values.
      y (list): The list of y values.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def shiftx(self,offset):
		"""
		Shifts the x values by an offset.

    Args:
      offset (float): The offset to shift the values with.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def shifty(self,offset):
		"""
		Shifts the y values by an offset.

    Args:
      offset (float): The offset to shift the values with.

    Returns:
      Spline: A reference to the instance Spline object on which it was called.
    
		"""
		pass

	def toBaseUnits(self):
		"""
		Makes the Spline values work like other Double values.
    
		"""
		pass

	def writeCsv(self,fname=None):
		"""
		Writes x/y values to a csv file.

    Args:
      fname (str): The path to the csv file.
    
		"""
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

class Vector:
	def __init__(self,x="0", y="0", z="0"):
		"""
A mathematical represenation of a Vector in 3D space.
"""
		pass

	def angle(self,x, y=None, z=None, degrees=False):
		"""
		Computes the angle with the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.
      degrees (bool): Determines if the return value will be in degrees or not.

    Returns:
      float: The angle.
    
		"""
		pass

	def close(self,x, y=None, z=None, tol=1e-07):
		"""
		Determines if the distance to the Vector defined by x, y, z is less or 
    equal than tolerance.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.
      tolerance (float): The tolerance to consider when checking condition.

    Returns:
      bool: True if Vectors are close, False otherwise.
    
		"""
		pass

	def copy(self,x=None, y=None, z=None):
		"""
		Creates a copy of self.

    If x, y, z are given then the copy has these as coordinates.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      Vector: The newly created object.
    
		"""
		pass

	def cross(self,x, y=None, z=None):
		"""
		Computes the cross product with the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      Vector: The cross product.
    
		"""
		pass

	def dot(self,x, y=None, z=None):
		"""
		Computes the dot product with the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.

    Returns:
      float: The dot product.
    
		"""
		pass

	def findAngle(self,pt1, pt2, pt3, degrees=False):
		"""
		Computes the angle subtended between (pt2-pt1) and (pt3-pt1).

    Args:
      pt1 (Vector): The first Vector.
      pt2 (Vector): The second Vector.
      pt3 (Vector): The third Vector.
      degrees (bool): Determines if the return value will be in degrees or not.

    Returns:
      float: The angle.
    
		"""
		pass

	def isAlignedWith(self,x, y=None, z=None, tolerance=1e-05, normalize=True):
		"""
		Determines if self is parallel to the Vector defined by x, y, z.

    Args:
      x (float): The x coordinate.
      y (float): The y coordinate.
      z (float): The z coordinate.
      tolerance (float): The tolerance to consider when checking condition.
      normalize (bool): Determines whether to normalize self before checking the condition.

    Returns:
      bool: True if Vectors are aligned, False otherwise.
    
		"""
		pass

	def iszero(self):
		"""
		Returns True if x, y and z are set to zero, False otherwise.
		"""
		pass

	def magnitude(self):
		"""
		Returns the magnitude.
		"""
		pass

	def normalize(self):
		"""
		Returns the normalized Vector.
		"""
		pass

	def perpendicularize(self):
		"""
		Computes a Vector perpendicular to self.

    If any of the coordinates are zero, returns a Vector along that coordinate, 
    otherwise returns the cross product with (1, 0, 0).
    
		"""
		pass

	def scale(self,x, y=None, z=None):
		"""
		Scales by a single value 'x' or a tripple (x, y, z), elementwise.

    Args:
      x (float): The x scale factor.
      y (float): The y scale factor.
      z (float): The z scale factor.

    Returns:
      Vector: The scaled Vector.
    
		"""
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

class acos:
	def __init__(self,x):
		"""
Return the arc cosine (measured in radians) of x.
"""
		pass

class acosh:
	def __init__(self,x):
		"""
Return the inverse hyperbolic cosine of x.
"""
		pass

class asin:
	def __init__(self,x):
		"""
Return the arc sine (measured in radians) of x.
"""
		pass

class asinh:
	def __init__(self,x):
		"""
Return the inverse hyperbolic sine of x.
"""
		pass

class atan:
	def __init__(self,x):
		"""
Return the arc tangent (measured in radians) of x.
"""
		pass

class atan2:
	def __init__(self,y, x):
		"""
Return the arc tangent (measured in radians) of y/x.

Unlike atan(y/x), the signs of both x and y are considered.
"""
		pass

class atanh:
	def __init__(self,x):
		"""
Return the inverse hyperbolic tangent of x.
"""
		pass

class ceil:
	def __init__(self,x):
		"""
Return the ceiling of x as an Integral.

This is the smallest integer >= x.
"""
		pass

class comb:
	def __init__(self,n, k):
		"""
Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.
"""
		pass

class copysign:
	def __init__(self,x, y):
		"""
Return a float with the magnitude (absolute value) of x but the sign of y.

On platforms that support signed zeros, copysign(1.0, -0.0)
returns -1.0.

"""
		pass

class cos:
	def __init__(self,x):
		"""
Return the cosine of x (measured in radians).
"""
		pass

class cosh:
	def __init__(self,x):
		"""
Return the hyperbolic cosine of x.
"""
		pass

class degrees:
	def __init__(self,x):
		"""
Convert angle x from radians to degrees.
"""
		pass

class dist:
	def __init__(self,p, q):
		"""
Return the Euclidean distance between two points p and q.

The points should be specified as sequences (or iterables) of
coordinates.  Both inputs must have the same dimension.

Roughly equivalent to:
    sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
"""
		pass

class e:
	"""
Convert a string or number to a floating point number, if possible.
"""
	pass

class erf:
	def __init__(self,x):
		"""
Error function at x.
"""
		pass

class erfc:
	def __init__(self,x):
		"""
Complementary error function at x.
"""
		pass

class exp:
	def __init__(self,x):
		"""
Return e raised to the power of x.
"""
		pass

class expm1:
	def __init__(self,x):
		"""
Return exp(x)-1.

This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
"""
		pass

class fabs:
	def __init__(self,x):
		"""
Return the absolute value of the float x.
"""
		pass

class factorial:
	def __init__(self,x):
		"""
Find x!.

Raise a ValueError if x is negative or non-integral.
"""
		pass

class floor:
	def __init__(self,x):
		"""
Return the floor of x as an Integral.

This is the largest integer <= x.
"""
		pass

class fmod:
	def __init__(self,x, y):
		"""
Return fmod(x, y), according to platform C.

x % y may differ.
"""
		pass

class frexp:
	def __init__(self,x):
		"""
Return the mantissa and exponent of x, as pair (m, e).

m is a float and e is an int, such that x = m * 2.**e.
If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
"""
		pass

class fsum:
	def __init__(self,seq):
		"""
Return an accurate floating point sum of values in the iterable seq.

Assumes IEEE-754 floating point arithmetic.
"""
		pass

class gamma:
	def __init__(self,x):
		"""
Gamma function at x.
"""
		pass

class gcd:
	def __init__(self,x, y):
		"""
greatest common divisor of x and y
"""
		pass

class hypot:
	def __init__(self):
		"""
hypot(*coordinates) -> value

Multidimensional Euclidean distance from the origin to a point.

Roughly equivalent to:
    sqrt(sum(x**2 for x in coordinates))

For a two dimensional point (x, y), gives the hypotenuse
using the Pythagorean theorem:  sqrt(x*x + y*y).

For example, the hypotenuse of a 3/4/5 right triangle is:

    >>> hypot(3.0, 4.0)
    5.0

"""
		pass

class inf:
	"""
Convert a string or number to a floating point number, if possible.
"""
	pass

class isclose:
	def __init__(self,a, b, rel_tol=1e-09, abs_tol="0.0"):
		"""
Determine whether two floating point numbers are close in value.

  rel_tol
    maximum difference for being considered "close", relative to the
    magnitude of the input values
  abs_tol
    maximum difference for being considered "close", regardless of the
    magnitude of the input values

Return True if a is close in value to b, and False otherwise.

For the values to be considered close, the difference between them
must be smaller than at least one of the tolerances.

-inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
is, NaN is not close to anything, even itself.  inf and -inf are
only close to themselves.
"""
		pass

class isfinite:
	def __init__(self,x):
		"""
Return True if x is neither an infinity nor a NaN, and False otherwise.
"""
		pass

class isinf:
	def __init__(self,x):
		"""
Return True if x is a positive or negative infinity, and False otherwise.
"""
		pass

class isnan:
	def __init__(self,x):
		"""
Return True if x is a NaN (not a number), and False otherwise.
"""
		pass

class isqrt:
	def __init__(self,n):
		"""
Return the integer part of the square root of the input.
"""
		pass

class ldexp:
	def __init__(self,x, i):
		"""
Return x * (2**i).

This is essentially the inverse of frexp().
"""
		pass

class lgamma:
	def __init__(self,x):
		"""
Natural logarithm of absolute value of Gamma function at x.
"""
		pass

class log:
	def __init__(self):
		"""
log(x, [base=math.e])
Return the logarithm of x to the given base.

If the base not specified, returns the natural logarithm (base e) of x.
"""
		pass

class log10:
	def __init__(self,x):
		"""
Return the base 10 logarithm of x.
"""
		pass

class log1p:
	def __init__(self,x):
		"""
Return the natural logarithm of 1+x (base e).

The result is computed in a way which is accurate for x near zero.
"""
		pass

class log2:
	def __init__(self,x):
		"""
Return the base 2 logarithm of x.
"""
		pass

class modf:
	def __init__(self,x):
		"""
Return the fractional and integer parts of x.

Both results carry the sign of x and are floats.
"""
		pass

class nan:
	"""
Convert a string or number to a floating point number, if possible.
"""
	pass

class perm:
	def __init__(self,n, k=None):
		"""
Number of ways to choose k items from n items without repetition and with order.

Evaluates to n! / (n - k)! when k <= n and evaluates
to zero when k > n.

If k is not specified or is None, then k defaults to n
and the function returns n!.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.
"""
		pass

class pi:
	"""
Convert a string or number to a floating point number, if possible.
"""
	pass

class pow:
	def __init__(self,x, y):
		"""
Return x**y (x to the power of y).
"""
		pass

class prod:
	def __init__(self,iterable, start=1):
		"""
Calculate the product of all the elements in the input iterable.

The default start value for the product is 1.

When the iterable is empty, return the start value.  This function is
intended specifically for use with numeric values and may reject
non-numeric types.
"""
		pass

class radians:
	def __init__(self,x):
		"""
Convert angle x from degrees to radians.
"""
		pass

class remainder:
	def __init__(self,x, y):
		"""
Difference between x and the closest integer multiple of y.

Return x - n*y where n*y is the closest integer multiple of y.
In the case where x is exactly halfway between two multiples of
y, the nearest even value of n is used. The result is always exact.
"""
		pass

class sin:
	def __init__(self,x):
		"""
Return the sine of x (measured in radians).
"""
		pass

class sinh:
	def __init__(self,x):
		"""
Return the hyperbolic sine of x.
"""
		pass

class sqrt:
	def __init__(self,x):
		"""
Return the square root of x.
"""
		pass

class tan:
	def __init__(self,x):
		"""
Return the tangent of x (measured in radians).
"""
		pass

class tanh:
	def __init__(self,x):
		"""
Return the hyperbolic tangent of x.
"""
		pass

class tau:
	"""
Convert a string or number to a floating point number, if possible.
"""
	pass

class trunc:
	def __init__(self,x):
		"""
Truncates the Real x to the nearest Integral toward 0.

Uses the __trunc__ magic method.
"""
		pass

