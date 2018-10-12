name = "cvtools"
__version__ = '0.1.3'
from cv_load_image import cv_load_image
from colors import get_color, COLORS
from clamp import clamp
__all__ = [cv_load_image, get_color, COLORS, clamp]
