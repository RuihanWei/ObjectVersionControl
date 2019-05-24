# import darkflow.YoloService as YoloService
from Models.ModelServices import ImageStorageService as ImageStorageService
from Models.ModelServices import RelationMapper as RelationMapper
import datetime
from Models.ModelServices.ComparisonService import CompareRelations
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# yoloService = YoloService.YoloService()
# Results = yoloService.interpret_image("Samplesetup1.jpg")
# Results = yoloService.interpret_image("Samplesetup2.jpg")

# imageService = ImageService.ImageService(Results, "Samplesetup1.jpg")
# imageService = ImageStorageService.ImageStorageService(Results, "Samplesetup2.jpg")
# imageService.CreateObjects("SampleRoom")

# session1_datetime = datetime.datetime(2019, 4, 1, 23, 58, 25)
# session2_datetime = datetime.datetime(2019, 4, 3, 1, 26, 18)

def Diff(session1_datetime, session2_datetime):
  (Relations1, Objects1) = RelationMapper.MapRelation(session1_datetime)
  (Relations2, Objects2) = RelationMapper.MapRelation(session2_datetime)

  ComparisonResult = CompareRelations(Relations1, Relations2, Objects1, Objects2)
  return ComparisonResult