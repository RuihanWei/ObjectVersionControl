class Image:
  def __init__(self, label, confidence, reference_path, mid_point, length, width):
    self.Label = label
    self.Width = width
    self.Length = length
    self.Mid_point = mid_point
    self.Reference_path = reference_path
    self.Confidence = confidence
