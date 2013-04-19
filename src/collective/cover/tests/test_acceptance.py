# -*- coding: utf-8 -*-

from collective.cover.testing import FUNCTIONAL_TESTING
from plone.testing import layered

import os
import robotsuite
import unittest

dirname = os.path.dirname(__file__)
files = os.listdir(dirname)
tests = [f for f in files if f.startswith('test_') and f.endswith('.txt')]

# FIXME: test randomly failing under Plone 4.3.x
#        see https://github.com/collective/collective.cover/issues/155
import pkg_resources
PLONE_VERSION = pkg_resources.require("Plone")[0].version

if '4.3' in PLONE_VERSION:
    tests.remove('test_contentchooser_search_tab.txt',)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite(t), layer=FUNCTIONAL_TESTING)
        for t in tests
    ])
    return suite
