import YoloService as YoloService
from Models.ModelServices import ImageService as ImageService

yoloService = YoloService.YoloService()
Results = yoloService.interpret_image("Samplesetup1.jpg")

imageService = ImageService.ImageService("Samplesetup1.jpg")
imageService.CreateObjects(Results)

