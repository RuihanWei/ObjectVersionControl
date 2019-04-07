import datetime
import Repository.DataAccess as DataAccess
import Models.ImageObject as ImageObject
import Models.ObjectRelations as ObjectRelations
import math as math


class Point:
  def __init__(self, x, y):
    self.X = x
    self.Y = y


# large -> small
def InsertRelationInOrder(list_, newValue):
  for i in range(0, len(list_)):
    if newValue.Distance > list_[i].Distance:
      list_.insert(i, newValue)
    elif i == len(list_) - 1:
      list_.append(newValue)
  if len(list_) == 0:
    list_.append(newValue)


# def CompareObjects(object_1, object_2):
#   if object_1.Label > object_2.Label:
#     return object_1, object_2
#   else:
#     return object_2, object_1

def ClockDirection(point_1, point_2):
  # note y flipped from math coordinates
  radianAngle = math.atan2(point_2.Y - point_1.Y, point_2.X - point_1.X)
  if math.pi / 12 > radianAngle >= -math.pi / 12:
    return 3
  elif math.pi / 4 > radianAngle >= math.pi / 12:
    return 4
  elif 5 * math.pi / 12 > radianAngle >= math.pi / 4:
    return 5
  elif 7 * math.pi / 12 > radianAngle >= 5 * math.pi / 12:
    return 6
  elif 3 * math.pi / 4 > radianAngle >= 7 * math.pi / 12:
    return 7
  elif 11 * math.pi / 12 > radianAngle >= 3 * math.pi / 4:
    return 8
  elif 11 * math.pi / 12 <= radianAngle or radianAngle < -11 * math.pi / 12:
    return 9
  elif -11 * math.pi / 12 <= radianAngle < -3 * math.pi / 4:
    return 10
  elif -3 * math.pi / 4 <= radianAngle < -7 * math.pi / 12:
    return 11
  elif -7 * math.pi / 12 <= radianAngle < -5 * math.pi / 12:
    return 12
  elif -5 * math.pi / 12 <= radianAngle < -math.pi / 4:
    return 1
  elif -math.pi / 4 <= radianAngle < -math.pi / 12:
    return 2


def MapOrder(relations, objects):
  for i in range(0, len(objects)):
    orderList = []
    for k in range(0, 12):
      new_list = []
      orderList.append(new_list)

    for j in range(0, len(objects)):
      if objects[i].Label != objects[j].Label:
        InsertRelationInOrder(orderList[relations[objects[i].Label][objects[j].Label].Clock_direction - 1],
                              relations[objects[i].Label][objects[j].Label])

    for k in range(0, 12):
      for l in range(0, len(orderList[k])):
        orderList[k][l].Order = l + 1


def MapRelation(session1_datetime):
  dataAccess = DataAccess.DataAccess()
  objectTuple = dataAccess.FetchByDateTime(session1_datetime)
  objects = []
  for object_ in objectTuple:
    objects.append(ImageObject.ImageObject(object_[0], object_[1], object_[2]))

  relations = {}

  for i in range(0, len(objects)):
    for j in range(0, len(objects)):
      if objects[i].Label != objects[j].Label:
        distance = math.hypot(objects[i].mid_point_x - objects[j].mid_point_x,
                              objects[i].mid_point_y - objects[j].mid_point_y)
        point_1 = Point(objects[i].mid_point_x, objects[i].mid_point_y)
        point_2 = Point(objects[j].mid_point_x, objects[j].mid_point_y)

        if objects[i].Label not in relations:
          relations[objects[i].Label] = {}
        relations[objects[i].Label][objects[j].Label] = ObjectRelations.ObjectRelations(distance,
                                                                                        ClockDirection(point_1,
                                                                                                       point_2))

  MapOrder(relations, objects)
  return relations
