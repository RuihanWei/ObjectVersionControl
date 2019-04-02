from DataAccess import DataAccess as DataAccess
from PIL import Image
import os
import datetime
from Models import ImageScene as ImageScene

class ImageService:

  def __init__(self, results, image_name):
    self.DataAccess = DataAccess.DataAccess()
    self.Results = results
    self.Image_name = image_name

  def UpdateImage(self, identifier):
    current_time = datetime.datetime.now()
    image_id = self.DataAccess.InsertImage(identifier, current_time)
    return image_id

  def UpdateBoundingBoxes(self, object_id, result):
    #todo: add support logic to deal with duplicate labels (requires another service to check before creating object)
    midpoint = ((result['bottomright']['x'] + result['topleft']['x']) / 2, (result['bottomright']['y'] + result['topleft']['y']) / 2)
    length = result['bottomright']['x'] - result['topleft']['x']
    width = result['bottomright']['y'] - result['topleft']['y']
    self.DataAccess.InsertBoundingBox(object_id, float(midpoint[0]), float(midpoint[1]), float(length), float(width))

    # print(result['label'] + " confidence: " + str(result['confidence']))

  def UpdateGeneralObject(self, result, image_id, image_identifier):
    image = Image.open(self.Image_name)
    cropBox = (result['topleft']['x'], result['topleft']['y'], result['bottomright']['x'], result['bottomright']['y'])
    crop = image.crop(cropBox)
    image_directory = os.getenv("LOCALAPPDATA") + "\\ObjectVersionControl\\" + image_identifier
    image_path = image_directory + "\\" + result['label'] + ".png"

    if not os.path.exists(image_directory):
      os.makedirs(image_directory)

    crop.save(image_path, "PNG")
    return self.DataAccess.InsertObject(image_id, result['label'], float(result['confidence']), image_path)

  def UpdateObjects(self, image_id, image_identifier, results):
    labels = []  # temp to remove duplicate labels
    for result in results:
      if result['label'] not in labels:
        labels.append(result['label'])
        object_id = self.UpdateGeneralObject(result, image_id, image_identifier)
        self.UpdateBoundingBoxes(object_id, result)

  def CreateObjects(self, identifier):
    image_id = self.UpdateImage(identifier)
    self.UpdateObjects(image_id, identifier, self.Results)
