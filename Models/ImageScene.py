class ImageScene:
  def __init__(self, identifier, datetime):
    self.Identifier = identifier
    self.DateTime = datetime
    self.Predictions = []
    self.ImageObjects = []
    self.ObjectRelations = []
