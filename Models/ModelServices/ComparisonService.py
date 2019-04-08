def OrderObjects(object_1, object_2):
  if object_1.Label > object_2.Label:
    return object_1, object_2
  else:
    return object_2, object_1


def CompareObjects(objects_1, objects_2):
  ComparisonResult = ""
  for object in objects_1:
    if not any(object2.Label == object.Label for object2 in objects_2):
      ComparisonResult += ("%s was removed\n", object.Label)
  return ComparisonResult

def NumberToOrdinal(number):
  if 10 < number < 21:
    return str(number)+"th"

  if number % 10 == 1:
    return str(number)+"st"
  if number % 10 == 2:
    return str(number)+"nd"
  if number % 10 == 3:
    return str(number)+"rd"

  return str(number)+"th"


def CompareRelations(relation_1, relation_2, objects_1, objects_2):
  ComparisonResult = ""
  for i in range(0, len(objects_1)):
    for j in range(0, len(objects_1)):
      if objects_1[i].Label != objects_1[j].Label:
        (object1, object2) = OrderObjects(objects_1[i], objects_1[j])
        try:
          relation1 = relation_1[object1.Label][object2.Label]
          relation2 = relation_2[object1.Label][object2.Label]
          if relation1.Clock_direction != relation2.Clock_direction:
            Comparison = ("Clock Direction from %s to %s used to be %s and is now %s\n" % (object1.Label,
                                                                                                  object2.Label,
                                                                                              relation1.Clock_direction,
                                                                                              relation2.Clock_direction))
            if Comparison not in ComparisonResult:
              ComparisonResult += Comparison

          if relation1.Order != relation2.Order and relation1.Clock_direction == relation2.Clock_direction:
            Comparison = ("%s used to be %s closes to %s and is now %s\n" % (object2.Label,
                                                                                    NumberToOrdinal(relation1.Order),
                                                                                    object1.Label,
                                                                                    NumberToOrdinal(relation2.Order)))
            if Comparison not in ComparisonResult:
              ComparisonResult += Comparison

        except KeyError:
          pass

  ObjectComparisonResults = CompareObjects(objects_1, objects_2)
  return ComparisonResult + ObjectComparisonResults
