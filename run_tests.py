#!/usr/bin/env python2

import sys
import unittest
from src.tests import Tests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
