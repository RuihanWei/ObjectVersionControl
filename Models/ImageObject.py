class ImageObject:
  def __init__(self, label, mid_point_x, mid_point_y, reference_path="", length=0, width=0):
    self.mid_point_y = mid_point_y
    self.mid_point_x = mid_point_x
    self.Label = label
    self.Width = width
    self.Length = length
    self.Reference_path = reference_path
