#!/usr/bin/python
import os
import decimal
import time
import math
import cmath
import sys
from PIL import Image, ImageDraw

"""
The Mandelbrot-generator class
"""
class MandelbrotGenerator:

    # -- Constructor -------------------------------------------------------------
    def __init__(self, intImageWidth, intRadius, strOutputFileName):
        self.__intImageWidth = intImageWidth
        self.__intImageHeight = intImageWidth
        self.__strOutputFileName = strOutputFileName
        self.__intRadius = intRadius
        self.__maxIteration = 40

    # -- Public functions and methods --------------------------------------------
    def generateOutput(self):
        """
        Main function to generate Mandelbrot-set and save it to file.
        """

        print("Generating Mandelbrot fractal with resolution of  "
              + str(self.__intImageWidth) + " * " + str(self.__intImageHeight)
              + " and save it to " + self.__strOutputFileName + " file.")
        
        MandelbrotGenerator.__startProgress("Drawing")
        start = time.time()
        
        img = Image.new('HSV', (self.__intImageWidth, self.__intImageHeight))

        d = ImageDraw.Draw(img)

        # Find center of image, that's the origo
        cX = (self.__intImageWidth - 1) / 2
        cY = (self.__intImageHeight - 1) / 2

        # Draw axises
        #d.line([(0, cY), (self.__intImageWidth, cY)], 1)
        #d.line([(cX, 0), (cX, self.__intImageHeight)], 1)

        # Render:
        for i in range(0, self.__intImageWidth):
            for j in range(0, self.__intImageHeight):
                z = self.__getNumberOfPosition(i, j)
                iteration = self.__getStepsInMandelbrotSet(z, self.__maxIteration)

                hue = int(255 * iteration / self.__maxIteration)
                saturation = 255 - hue
                value = 255 if iteration < self.__maxIteration else 0

                d.point([i, j], (hue, saturation, value))
            if i % 100 == 0:
                partTime = time.time()
                MandelbrotGenerator.__progress(decimal.Decimal(i) / self.__intImageWidth * 100)

        del d
        img.convert('RGB').save(self.__strOutputFileName)

        end = time.time()
        
        MandelbrotGenerator.__endProgress()
        print("DONE in %f seconds." % (end - start))

        # Just for debugging, works only in Windows, can be safely removed or commented:
        os.system("start "+self.__strOutputFileName)

        return

    def __getNumberOfPosition(self, x, y):
        """
        Calculates the complex number from pixel position.
        """

        _origoXModifier = self.__intImageWidth % 2;
        _origoYModifier = self.__intImageHeight % 2;

        _cX = decimal.Decimal((self.__intImageWidth - 1) / 2) + _origoXModifier
        _cY = decimal.Decimal((self.__intImageHeight - 1) / 2) + _origoYModifier

        if x == _cX:
            re = 0
        else:
            _nX = decimal.Decimal(x) - _cX
            if _nX > 0:
                _nX = _nX + _origoXModifier
            _dX = _nX / _cX
            re = _dX * self.__intRadius

        if y == _cY:
            im = 0
        else:
            _nY = _cY - decimal.Decimal(y)
            if _nY < 0:
                _nY = _nY - _origoYModifier
            _dY = _nY / _cY
            im = _dY * self.__intRadius

        return complex(re, im)

    def __getComplexDistance(self, z: complex):
        """
        Gets the complex number distance from origo.
        """
        return math.sqrt((z.real*z.real + z.imag*z.imag))

    def __getStepsInMandelbrotSet(self, z:complex, maxIteration: int):
        """
        Returns the maximum steps for the given z complex number while it was still part of the set.
        """
        iteration = 0
        x = complex(0, 0)
        while self.__getComplexDistance(x) <= 2 and iteration < maxIteration:
            # Classic Mandelbrot:
            x = x*x + z

            # Another type of fractal:
            #xconj = x.conjugate()
            #x = xconj * xconj + z

            # And yet another type of fractal:
            #x = x*x*x + z

            # And so on... :)
            #x = x*x*x*x*x*x + z

            iteration = iteration + 1
        return iteration

    def __startProgress(title):
        """
        Prepares a progress bar with a title.
        https://stackoverflow.com/questions/6169217/replace-console-output-in-python
        """
        global progress_x
        sys.stdout.write(title + ": [" + " "*40 + "]" + chr(8)*41)
        sys.stdout.flush()
        progress_x = 0

    def __progress(x):
        """
        Modifies the progress in the prepared progress bar. (Accepts percentage.)
        https://stackoverflow.com/questions/6169217/replace-console-output-in-python
        """
        global progress_x
        x = int(x * 40 // 100)
        sys.stdout.write("-" * (x - progress_x))
        sys.stdout.flush()
        progress_x = x

    def __endProgress():
        """
        Closes the progress bar.
        https://stackoverflow.com/questions/6169217/replace-console-output-in-python
        """
        sys.stdout.write("-" * (40 - progress_x) + "]\n")
        sys.stdout.flush()
