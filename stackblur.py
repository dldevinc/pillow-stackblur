import multiprocessing
from PIL import ImageFilter
from cstackblur import stackblur


class StackBlur(ImageFilter.Filter):
    """Stack blur filter.

    :param radius: Blur radius.
    """
    name = "StackBlur"

    def __init__(self, radius=2):
        self.radius = radius
        self.cores = multiprocessing.cpu_count()

    def filter(self, image):
        w, h = image.size
        image.putdata(stackblur(list(image), w, h, self.radius, self.cores))
        return image
