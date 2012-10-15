#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author:
#   J Phani Mahesh <phanimahesh@gmail.com>
#
# Description:
#   Python wrapper to reset unity.
#   Born at http://chat.stackexchange.com/rooms/6118/unity-reconfiguration
#
# Special Thanks to:
#   Barneedhar (jokerdino on Ask Ubuntu)
#   Amith (Amithkk on Ask Ubuntu)
#
# Legal Stuff:
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUTa
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import subprocess
from gi.repository import Gio

allSchemas=Gio.Settings.list_schemas()
allRelocatableSchemas=Gio.Settings.list_relocatable_schemas()

def resetrecursive(schema,path=None):
    if (schema not in allSchemas) and (schema not in allRelocatableSchemas):
        print "The schema %s is not installed. hence ignored"%schema
        return
    gsettings=Gio.Settings(schema=schema,path=path)
    for key in gsettings.list_keys():
        gsettings.reset(key)
    gsettings.apply()

def resetPlugins():
    plugins=['core', 'composite', 'opengl', 'decor', 'vpswitch', 'snap', 'mousepoll', 'resize', 'place', 'move', 'wall', 'grid', 'session', 'animation', 'fade', 'unitymtgrabhandles', 'workarounds', 'scale', 'expo', 'ezoom', 'unityshell']
    for plugin in plugins:
        schema='org.compiz.'+plugin
        path="/org/compiz/profiles/unity/plugins/"+plugin+"/"
        resetrecursive(schema=schema,path=path)

def resetUnityChildren():
    unityChildren=["com.canonical.Unity","com.canonical.Unity.Launcher","com.canonical.Unity.ApplicationsLens","com.canonical.Unity.Lenses","com.canonical.Unity.Dash","com.canonical.Unity.Panel","com.canonical.Unity.Devices","com.canonical.Unity.Runner","com.canonical.Unity.FilesLens"]
    for childSchema in unityChildren:
         resetrecursive(childSchema)

resetPlugins()
resetUnityChildren()
subprocess.call("unity --replace",shell=True)

