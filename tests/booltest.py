#!/usr/bin/python

from gi.repository import Gio
import subprocess

def applens():
    gsettings=Gio.Settings("com.canonical.Unity.ApplicationsLens")
    if "display-recent-apps" in gsettings.list_keys():
        if gsettings.get_boolean("display-recent-apps") is True:
            print "Unsetted default"
            gsettings.set_boolean("display-recent-apps",False)
        print gsettings.get_boolean("display-recent-apps")

def filelens():
    nsettings=Gio.Settings("com.canonical.Unity.FilesLens")
    if "use-locate" in nsettings.list_keys():
        if nsettings.get_boolean("use-locate") is True:
            print "Unsetted defaults"
            nsettings.set_boolean("use-locate",False)
        print nsettings.get_boolean("use-locate")
        subprocess.call("/home/jokerdino/Tests/unity-reset.py", shell=True)
        if nsettings.get_boolean("use-locate") is True:
            print "Successfully reset boolean types in Applens and Filelens."

applens()
filelens()
