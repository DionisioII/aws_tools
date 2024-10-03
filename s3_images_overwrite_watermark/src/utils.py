import re
# from PIL import Image
import cv2
import base64
import io
import numpy as np



def ends_with_any(string, suffixes):
  """Checks if a string ends with any of the strings in a list.

  Args:
    string: The string to check.
    suffixes: A list of strings to check against.

  Returns:
    True if the string ends with any of the suffixes, False otherwise.
  """

  for suffix in suffixes:
    if string.endswith(suffix):
      return True
  return False



def WatermarkImage(Image, WatermarkPath):
    # Resizing watermark image keeping the aspect ratio
    # Resize is done such that watermark's height is equal to 10% of the image's height
    #boundary_distance = 70

    Watermark = cv2.imread(WatermarkPath, cv2.IMREAD_GRAYSCALE)
    
    #NewHeight = int(Image.shape[0]*0.1)
    NewHeight = int(Image.shape[0]* 0.7)
    NewWidth = int(NewHeight * (Watermark.shape[1]/Watermark.shape[0]))
    Watermark = cv2.resize(Watermark, (NewWidth, NewHeight), interpolation=cv2.INTER_AREA)

    boundary_distance_h = int((Image.shape[0] - NewHeight)/2)
    boundary_distance_w = int((Image.shape[1] - NewWidth)/2)
    
    # Creating 3 channeled watermark image and alpha image(range -> [0.0-1.0])
    Watermark = cv2.merge((Watermark, Watermark, Watermark))
    # Transparency of the watermark is 60% (0.4 is opacity)
    Alpha = (Watermark.astype(float) * 0.4)/255
    
    # Applying watermark on the bottom right corner leaving boundary_distance pixels from both the boundaries
    WatermarkedImage = Image.copy()
    ah, aw = Alpha.shape[:2]
    
    
    WatermarkedImage[-(ah+boundary_distance_h):-boundary_distance_h, -(aw+boundary_distance_w):-boundary_distance_w] = cv2.add(cv2.multiply(Alpha, Watermark, dtype=cv2.CV_64F),
                                cv2.multiply(1.0-Alpha, Image[-(ah+boundary_distance_h):-boundary_distance_h, -(aw+boundary_distance_w):-boundary_distance_w], dtype=cv2.CV_64F))
    WatermarkedImage = np.uint8(WatermarkedImage)
    
    return WatermarkedImage