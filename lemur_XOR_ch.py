import numpy as np
from PIL import Image

lemur = np.array(Image.open("lemur.png"))
flag = np.array(Image.open("flag.png"))

result = np.bitwise_xor(lemur, flag)

Image.fromarray(result).show()

