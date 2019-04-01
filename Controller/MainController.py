import YoloService as YoloService
from Models.ModelServices import ImageService as ImageService

yoloService = YoloService.YoloService("Samplesetup1.jpg")
Results = yoloService.interpret_image()

imageService = ImageService.ImageService()
imageService.CreateObjects(Results, "Samplesetup1.jpg")

