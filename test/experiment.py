from PIL import Image
from typing import *

# opens MemeMe'd.png
def openImage() -> None:
    try:
        img = Image.open("MemeMe'd.png")
        img.show()
    except:
        raise "MemeMe'd.png does not exist."

openImage()
