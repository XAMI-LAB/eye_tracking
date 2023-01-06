
import numpy as np
import matplotlib.pyplot as plt

from mimic.Annotation import Annotation

class BoundingBox(Annotation):

  def __init__(self, xmin : float, xmax : float, ymin : float, ymax : float, label : str):
    super().__init__(xmin, xmax, ymin, ymax, label)

  def process_shape(self):
    """returns a patch with a polygon"""
    return super().process_shape()

  def area(self):
    """computes the area of a polygon"""
    return super().area()

  def perimeter(self):
    """Computes the perimeter of a polygon"""
    return super().perimeter()

  def is_point_inside_shape(self, x: float, y: float):
    """returns a Boolean that checks whether a point (x,y) sits inside a bounding box"""
    return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax

  def plot_shape_and_point(self, x : float, y : float):
    """visualise if a point sits inside a polygon"""
    super.plot_shape_and_point(x,y)
    plt.plot([self.xmin, self.xmax, self.xmax, self.xmin, self.xmin], \
             [self.ymin, self.ymin, self.ymax, self.ymax, self.ymin], 'b-')
    plt.plot(x, y, 'ro')
    plt.axis('equal')
    plt.show()


