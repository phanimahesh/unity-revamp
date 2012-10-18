#!/usr/bin/python

from gi.repository import Gio

gsettings=Gio.Settings("com.canonical.Unity.Launcher")
for key in gsettings.list_keys():
	if key == "favorites":
		gsettings.reset(key)
		print "WIN"
