#!/usr/bin/python

"""
The Mandelbrot-generator class
"""

class MandelbrotGenerator:

    # -- Constructor -------------------------------------------------------------
    def __init__(self, intImageWidth, strOutputFileName):
        self.__intImageWidth = intImageWidth
        self.__strOutputFileName = strOutputFileName

    # -- Public functions and methods --------------------------------------------
    def generateOutput(self):
        """
        Main function to generate Mandelbrot-set.
        """
        print("TODO : Generate mandelbrot here in "
              + str(self.__intImageWidth) + " * " + str(self.__intImageWidth)
              + " size and save it to " + self.__strOutputFileName + " file.")
