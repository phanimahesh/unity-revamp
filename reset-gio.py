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
        print "Ignoring missing Schema %s"%schema
        return
    gsettings=Gio.Settings(schema=schema,path=path)
    for key in gsettings.list_keys():
        gsettings.reset(key)
    gsettings.apply()
    print "Schema %s successfully reset"%schema

def resetPlugins():
    import re
	from gi.repository import Gio
	plugins=[]
	unity=re.compile(r'com.canonical.Unity')
	pluginRe=re.compile(r'(?P<plugin>org.compiz.)')
	allSchemas=Gio.Settings.list_schemas()
	allRelocatableSchemas=Gio.Settings.list_relocatable_schemas()
	for schema in allSchemas:
		match=pluginRe.match(schema)
		if match:
			plugins.append(pluginRe.sub('',schema))
	for schema in allRelocatableSchemas:
		match=pluginRe.match(schema)
		if match:
			plugins.append(print pluginRe.sub('',schema))
    for plugin in plugins:
		schema='org.compiz.'+plugin
		path="/org/compiz/profiles/unity/plugins/"+plugin+"/"
		resetrecursive(schema=schema,path=path)

def resetUnityChildren():
    #unityChildren=["com.canonical.Unity","com.canonical.Unity.Launcher","com.canonical.Unity.ApplicationsLens","com.canonical.Unity.Lenses","com.canonical.Unity.Dash","com.canonical.Unity.Panel","com.canonical.Unity.Devices","com.canonical.Unity.Runner","com.canonical.Unity.FilesLens"]
    parentSchema="com.canonical.Unity"
    if (parentSchema not in allSchemas) and (parentSchema not in allRelocatableSchemas):
        print "Unable to locate Schema %s"%parentSchema
        print "Unable to reset Unity preferences"
        return
    unity=Gio.Settings(schema=parentSchema)
    for childSchema in unity.list_children():
         resetrecursive(childSchema)

resetPlugins()
resetUnityChildren()
subprocess.call("unity --replace",shell=True)

