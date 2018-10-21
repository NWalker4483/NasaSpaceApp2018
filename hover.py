from scipy import misc
import cv2
f = cv2.imread("unnamed.jpg")

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc as sc
np.random.seed(0)
x = np.random.uniform(0.0,10.0,15)
y = np.random.uniform(0.0,10.0,15)
img = sc.imread
plt.scatter(x,y,zorder=1)
plt.imshow(img,zorder=0)
plt.show()
"""