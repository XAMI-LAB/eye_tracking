
import numpy as np

class BoundingBox:

  def __init__(self, xmin : float, xmax : float, ymin : float, ymax : float, label : str):
    self.xmin : float = xmin
    self.xmax : float = xmax
    self.ymin : float = ymin
    self.ymax : float = ymax
    self.label : str = label

    self.width : float = np.abs( xmax - xmin)
    self.height : float = np.abs( ymax - ymin)
    self.area : float = self.width * self.height
    self.perim : float = 2*self.width + 2*self.height

