#!/usr/bin/python

import unittest
import unityreset

Gio=unityreset.Gio

class TestUnityReset(unittest.TestCase):
    '''Unittest for unity --reset'''
    def setUp(self):
        # Get defaults
        self.compizPlugins=unityreset.UnityReset.snapshotCompizPlugins()
        self.compizChildren=unityreset.UnityReset.snapshotCompizChildren()
        self.unityChildren=unityreset.UnityReset.snapshotUnityChildren()

    def test_reset_display_recent_apps(self):
        schema="com.canonical.Unity.ApplicationsLens"
        key="display-recent-apps"
        default=self.unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_boolean(key,False)
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)

    def test_runner_history(self):
        schema="com.canonical.Unity.Runner"
        key="history"
        default=self.unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_strv(key,['abc','def'])
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)
    
    def test_dash_lens_ordering(self):
        schema="com.canonical.Unity.Dash"
        key="home-lens-ordering"
        default=self.unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_strv(key,['video.lens','gwibber.lens'])
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)
    
    def test_show_hud(self):
        schema="org.compiz.integrated"
        key="show-hud"
        default=self.compizChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_strv(key,['<Super>'])
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)

    def test_launcher_hide_mode(self):
        schema="org.compiz.unityshell"
        key="launcher-hide-mode"
        #path="/org/compiz/profiles/unity/plugins/unityshell/"
        default=self.compizPlugins[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_boolean(key,False)
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)

if __name__ == '__main__':
    unittest.main()
