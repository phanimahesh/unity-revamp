#!/usr/bin/python

import unittest
import unityreset

Gio=unityreset.Gio

class TestUnityReset(unittest.TestCase):
    '''Unittest for unity --reset'''
    def setUp(self):
        # Get defaults
        compizPlugins=unityreset.UnityReset.snapshotCompizPlugins()
        unityChildren=unityreset.UnityReset.snapshotUnityChildren()

    def test_reset_display_recent_apps(self):
        schema="com.canonical.Unity.ApplicationsLens"
        key="display-recent-apps"
        default=unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_boolean(key,False)
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)



if __name__ == '__main__':
    unittest.main()
