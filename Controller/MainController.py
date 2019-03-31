from Services import YoloService as YoloService
from Services import ImageService as ImageService

yoloService = YoloService.YoloService("Samplesetup1.jpg")
Results = yoloService.interpret_image()

imageService = ImageService.ImageService()
imageService.CreateObjects(Results)

