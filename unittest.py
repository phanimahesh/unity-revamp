#!/usr/bin/python

import unittest
import unityreset
from gi.repository import Gio

class TestUnityReset(unittest.TestCase):
'''Unittest for unity --reset'''
    def setUp(self):
        # Get defaults
        compizPlugins=unityreset.UnityReset.snapshotCompizPlugins()
        unityChildren=unityreset.UnityReset.snapshotUnityChildren()

    def test_reset(self):
        # TODO : Try changing, resetting and check




if __name__ == '__main__':
    unittest.main()
