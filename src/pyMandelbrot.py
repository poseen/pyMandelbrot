#!/usr/bin/python

"""
This is the main module.
"""

import sys

# ----------------------------------------------------------------------------
# -- Constants ---------------------------------------------------------------
# ----------------------------------------------------------------------------
STR_APP_NAME      = "pyMandelbrot"
STR_APP_VERSION   = "v1.0"
INT_MIN_IMAGE_SIZE = 100

# ----------------------------------------------------------------------------
# -- Functions ---------------------------------------------------------------
# ----------------------------------------------------------------------------
def showHeader(strAppName, strAppVersion):
    """
    Prints the header and draws an underline under it.
    """
    strAppHeaderText = strAppName + " " + strAppVersion
    intAppHeaderTextLength = len(strAppHeaderText)
    strUnderline = "=" * intAppHeaderTextLength
    print(strAppHeaderText)
    print(strUnderline)
    print()
    return

def showHelp():
    """
    Prints the help to the user.
    """
    print("Usage:")
    print("------")
    print()
    print("    python pyMandelbrot.py <intImgSize> <strOutputFilename>")
    print()
    print("    Generates the Mandelbrot-set and saves it as a PNG file. (Image size: intImgSize * intImgSize)")
    print("    Minimum image size: " + str(INT_MIN_IMAGE_SIZE) + ".")
    print()
    print("Example:")
    print("--------")
    print()
    print("    python pyMandelbrot 600 output.png")
    print()
    return

def getParametersIfValid():
    """
    Returns 3 results:
      boolSuccess:       True if the input arguments are valid, otherwise False.
      intImgWidth:       The image size if the arguments are valid, otherwise None
      strOutputFileName: The output filename
    """
    if len(sys.argv) != 3:
        return False, None, None

    intImgWidth = INT_MIN_IMAGE_SIZE
    strOutputFileName = sys.argv[2]

    try:
        intImgWidth = int(sys.argv[1])
    except ValueError:
        return False, None, None

    return True, intImgWidth, strOutputFileName

def generateOutput(intImageWidth, strOutputFileName):
    """
    Main function to generate Mandelbrot-set.
    """
    print("TODO : Generate mandelbrot here in " + str(intImageWidth) + " * " + str(intImageWidth) + " size and save it to " + strOutputFileName + " file.")
    return

def appRun():
    """
    The main function of the application.
    """
    boolSuccess, intImgWidth, strOutputFileName = getParametersIfValid()

    if not boolSuccess:
        showHelp()
    else:
        generateOutput(intImgWidth, strOutputFileName)
    return

# ----------------------------------------------------------------------------
# -- Main entry point --------------------------------------------------------
# ----------------------------------------------------------------------------
appRun()
