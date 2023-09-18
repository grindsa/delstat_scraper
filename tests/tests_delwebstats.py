#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" unittests for dkb_robo """
import sys
import os
import unittest
from unittest.mock import patch, MagicMock, Mock, mock_open


sys.path.insert(0, '.')
sys.path.insert(0, '..')
from delstats import DelStats
import logging

class TestDeöstats(unittest.TestCase):
    """ test class """

    maxDiff = None

    def setUp(self):
        self.delstats = DelStats()
        # self.logger = logging.getLogger('delstats')
        from delstats.delstats import value_convert
        self.value_convert = value_convert

    def test_001_value_convert(self):
        """ test value_convert() """
        value = 10
        self.assertEqual((10, None), self.value_convert(value))

    def test_002_value_convert(self):
        """ test value_convert() """
        value = 'aaa'
        self.assertEqual(('aaa', None), self.value_convert(value))

    def test_003_value_convert(self):
        """ test value_convert() """
        value = '10'
        self.assertEqual((10, None), self.value_convert(value))

    def test_004_value_convert(self):
        """ test value_convert() """
        value = '10,0'
        self.assertEqual((10, None), self.value_convert(value))

    def test_005_value_convert(self):
        """ test value_convert() """
        value = '10,25'
        self.assertEqual((10.25, None), self.value_convert(value))

    def test_006_value_convert(self):
        """ test value_convert() """
        value = '35.574'
        self.assertEqual((35574.0, None), self.value_convert(value))

    def test_007_value_convert(self):
        """ test value_convert() """
        value = '35.574,25'
        self.assertEqual((35574.25, None), self.value_convert(value))

    def test_008_value_convert(self):
        """ test value_convert() """
        value = '-19'
        self.assertEqual((-19, None), self.value_convert(value))

    def test_009_value_convert(self):
        """ test value_convert() """
        value = '19.04'
        self.assertEqual((19.04, None), self.value_convert(value))

    def test_010_value_convert(self):
        """ test value_convert() """
        value = '119.04'
        self.assertEqual((119.04, None), self.value_convert(value))

    def test_011_value_convert(self):
        """ test value_convert() """
        value = '-119.04'
        self.assertEqual((-119.04, None), self.value_convert(value))

    def test_012_value_convert(self):
        """ test value_convert() """
        value = '-119,04'
        self.assertEqual((-119.04, None), self.value_convert(value))

    def test_013_value_convert(self):
        """ test value_convert() """
        value = '17:58'
        self.assertEqual(('17:58', None), self.value_convert(value))

    def test_014_value_convert(self):
        """ test value_convert() """
        value = '00:41:00'
        self.assertEqual(('00:41:00', None), self.value_convert(value))

    def test_015_value_convert(self):
        """ test value_convert() """
        value = '100:41:00'
        self.assertEqual(('100:41:00', None), self.value_convert(value))

    def test_016_value_convert(self):
        """ test value_convert() """
        value = '8.143 m'
        self.assertEqual((8143.0, 'm'), self.value_convert(value))

    def test_017_value_convert(self):
        """ test value_convert() """
        value = '8.143,23 m'
        self.assertEqual((8143.23, 'm'), self.value_convert(value))

    def test_018_value_convert(self):
        """ test value_convert() """
        value = '0'
        self.assertEqual((0, None), self.value_convert(value))

if __name__ == '__main__':

    unittest.main()