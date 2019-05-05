#!/usr/bin/python

"""
This is application's main class
"""

from lovebrotGenerator import LovebrotGenerator

class Application:

    # -- Constants ---------------------------------------------------------------
    STR_APP_NAME      = "pyLovebrot"
    STR_APP_VERSION   = "v1.0"
    INT_MIN_IMAGE_SIZE = 100

    # -- Constructor -------------------------------------------------------------
    def __init__(self, arguments):
        self.__arguments = arguments

    # -- Public functions and methods --------------------------------------------
    def run(self):
        """
        The main function of the application.
        """
        boolSuccess, intImgWidth, strOutputFileName = self.__getParametersIfValid()

        if not boolSuccess:
            self.__showHelp()
        else:
            self.__generateOutput(intImgWidth, strOutputFileName)

    # -- Private functions and methods -------------------------------------------
    def __showHeader(self, strAppName, strAppVersion):
        """
        Prints the header and draws an underline under it.
        """
        strAppHeaderText = strAppName + " " + strAppVersion
        intAppHeaderTextLength = len(strAppHeaderText)
        strUnderline = "=" * intAppHeaderTextLength
        print(strAppHeaderText)
        print(strUnderline)
        print()

    def __showHelp(self):
        """
        Prints the help to the user.
        """
        print("Usage:")
        print("------")
        print()
        print("    python lovebrot.py <intImgSize> <strOutputFilename>")
        print()
        print("    Generates the heart-shaped Mandelbrot-set and saves it as an image file.")
        print("    Image size: intImgSize * intImgSize")
        print("    Minimum image size: " + str(self.INT_MIN_IMAGE_SIZE) + ".")
        print()
        print("Example:")
        print("--------")
        print()
        print("    python lovebrot.py 600 output.png")
        print()

    def __getParametersIfValid(self):
        """
        Returns 3 results:
          boolSuccess:       True if the input arguments are valid, otherwise False.
          intImgWidth:       The image size if the arguments are valid, otherwise None
          strOutputFileName: The output filename
        """
        if len(self.__arguments) != 3:
            return False, None, None

        intImgWidth = self.INT_MIN_IMAGE_SIZE
        strOutputFileName = self.__arguments[2]

        try:
            intImgWidth = int(self.__arguments[1])
        except ValueError:
            return False, None, None

        return True, intImgWidth, strOutputFileName

    def __generateOutput(self, intImageWidth, strOutputFileName):
        """
        Main function to generate Mandelbrot-set.
        """
        generator = LovebrotGenerator(intImageWidth, 2, strOutputFileName)
        generator.generateOutput()
