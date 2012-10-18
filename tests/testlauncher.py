#!/usr/bin/python

from gi.repository import Gio
from gi.repository import GLib


gsettings=Gio.Settings("com.canonical.Unity.Launcher")
if "favorites" in gsettings.list_keys():
	#print gsettings.is_writable("favorites")
	#favorlist=[]
	print gsettings.get_value("favorites")
	gsettings.reset("favorites")
	#favorval=GLib.Variant('as',"application://terminal.desktop")
	#gsettings.set_value("favorites","[application://gnome-terminal.desktop]")
    


	#variant=GLib.Variant('as',"application://nautilus.desktop")
	#variant.g_variant_new(favorlist)
	#gsettings.set_value(variant,"favorites")
	#print favorlist
