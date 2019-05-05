#!/usr/bin/python

"""
This is the main python file to run.
"""

import sys
from application import Application

# -- Functions ---------------------------------------------------------------
def main():
    """
    The main function.
    """
    app = Application(sys.argv)
    app.run()

# -- Main entry point --------------------------------------------------------
if __name__ == "__main__":
  main()
