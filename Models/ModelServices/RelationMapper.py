import datetime
import Repository.DataAccess as DataAccess
import Models.ImageObject as ImageObject
import Models.ObjectRelations as ObjectRelations
import math as math


class Point:
  def __init__(self, x, y):
    self.X = x
    self.Y = y


class RelationMapper:
  def CompareObjects(self, object_1, object_2):
    if object_1.Label > object_2.Label:
      return object_1, object_2
    else:
      return object_2, object_1

  def ClockDirection(self, point_1, point_2):
    radianAngle = math.atan2(point_2.Y - point_1.Y, point_2.X - point_1.X)
    if math.pi / 12 > radianAngle >= -math.pi / 12:
      return 3
    elif math.pi / 4 > radianAngle >= math.pi / 12:
      return 2
    elif 5*math.pi / 12 > radianAngle >= math.pi / 4:
      return 1
    elif 7*math.pi / 12 > radianAngle >= 5*math.pi / 12:
      return 12
    elif 11*math.pi / 12 > radianAngle >= 3*math.pi / 4:
      return 10
    elif 11*math.pi / 12 <= radianAngle and radianAngle < -11*math.pi / 12:
      return 9
    elif -11*math.pi / 12 <= radianAngle < -3*math.pi / 4:
      return 8
    elif -3*math.pi / 4 <= radianAngle < -7*math.pi / 12:
      return 7
    elif -7*math.pi / 12 <= radianAngle < -5*math.pi / 12:
      return 6
    elif -5*math.pi / 12 <= radianAngle < -math.pi / 4:
      return 5
    elif -math.pi / 4 <= radianAngle < -math.pi / 12:
      return 4

  def MapRelation(self, session1_datetime):
    objectTuple = DataAccess.DataAccess.FetchByDateTime(session1_datetime)
    objects = []
    for object in objectTuple:
      objects.append(ImageObject.ImageObject(object[0], object[1], object[2]))

    relations = {}
    relations[objects[0].Label] = {}

    for i in range(0, len(objects)):
      for j in range(0, len(objects)):
        orderedObjects = self.CompareObjects(objects[i], objects[j])
        distance = math.hypot(objects[i].mid_point_x - objects[j].mid_point_x,
                              objects[i].mid_point_y - objects[j].mid_point_y)
        point_1 = Point(orderedObjects[0].mid_point_x, orderedObjects[0].mid_point_y)
        point_2 = Point(orderedObjects[1].mid_point_x, orderedObjects[1].mid_point_y)
        relations[orderedObjects[0].Label][orderedObjects[1].Label] = ObjectRelations.ObjectRelations(distance, self.ClockDirection(point_1, point_2))
