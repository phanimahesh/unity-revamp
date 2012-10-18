#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Authors:
#   J Phani Mahesh <phanimahesh@gmail.com>
#   Barneedhar (jokerdino) <barneedhar@ubuntu.com>
#   Amith KK <amithkumaran@gmail.com>
#
# Description:
#   Python wrapper to reset unity.
#   Born at http://chat.stackexchange.com/rooms/6118/unity-reconfiguration
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
import re

allSchemas=Gio.Settings.list_schemas()
allRelocatableSchemas=Gio.Settings.list_relocatable_schemas()

def resetAllKeys(schema,path=None):
    """Reset all keys in given Schema."""
    if (schema not in allSchemas) and (schema not in allRelocatableSchemas):
        print "Ignoring missing Schema %s"%schema
        return
    gsettings=Gio.Settings(schema=schema,path=path)
    for key in gsettings.list_keys():
        gsettings.reset(key)
    gsettings.apply()
    print "Schema %s successfully reset"%schema

def resetPlugins():
    """Reset Compiz Plugins"""
    compizPluginRe=re.compile(r'(?P<plugin>org.compiz.)')
    for schema in allRelocatableSchemas:
        if compizPluginRe.match(schema):
            plugin=compizPluginRe.sub('',schema)
            schema='org.compiz.'+plugin
            path="/org/compiz/profiles/unity/plugins/"+plugin+"/"
            resetAllKeys(schema=schema,path=path)

def resetUnityChildren():
    """Reset keys in child schemas of Unity"""
    unitySchema='com.canonical.Unity'
    blacklists=['com.canonical.Unity.Launcher','com.canonical.Unity.webapps','com.canonical.Unity.Lenses']
    unityChildRe=re.compile(unitySchema)
    for schema in allSchemas:
	if (schema not in blacklists) and (unityChildRe.match(schema)):
	    resetAllKeys(schema)

if __name__=='__main__':
    resetPlugins()
    resetUnityChildren()
    subprocess.call("unity")

