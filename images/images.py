from images.image import Image

class IMAGE:
    PLAYER      = 0
    BULLET      = 1
    LASER       = 2
    PARTICLE    = 3

IMAGES = {}
def set_images():
    IMAGES[IMAGE.PLAYER] = Image.from_string(


"""
 ^ 
/_\\
""",            1, 0)


    IMAGES[IMAGE.BULLET] = Image.from_string(


"""
o
""",            0, 0)

    IMAGES[IMAGE.LASER] = Image.from_string(


"""
|
""",            0, 0)

    IMAGES[IMAGE.PARTICLE] = Image.from_string(


"""
|
""",            0, 0)

