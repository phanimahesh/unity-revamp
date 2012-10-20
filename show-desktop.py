#!/usr/bin/python

from gi.repository import Gio
import argparse

parser = argparse.ArgumentParser(description='Enable or disable show-desktop icon')
optiongroup=parser.add_mutually_exclusive_group(required=True)
optiongroup.add_argument('-e','--enable',action='store_true',help='Add show-desktop icon to launcher')
optiongroup.add_argument('-d','--disable',action='store_true',help='Remove show-desktop icon from launcher')
args=parser.parse_args()

gsettings=Gio.Settings("com.canonical.Unity.Launcher")
launcherfav=gsettings.get_strv('favorites')
shwdsktp="unity://desktop-icon"
def remove_show_desktop():
  if shwdsktp in launcherfav:
    print "Show desktop is currently enabled."
    print "Removing show desktop"
    launcherfav.remove(shwdsktp)
    gsettings.set_strv('favorites',launcherfav)
    print "DONE"
  else:
    print "Looks like the show desktop icon is already hidden"
    print "Nothing to do then. Tada!"

def add_show_desktop():
    if shwdsktp not in launcherfav:
        print "Show desktop icon is currently hidden"
        print "Adding it to launcher"
        launcherfav.append(shwdsktp)
        gsettings.set_strv('favorites',launcherfav)
        print "DONE"
    else:
        print "Looks like the show-desktop icon is already visible"
        print "Nothing to do then. Tada!"

if args.enable :
    add_show_desktop()
if args.disable :
    remove_show_desktop()
