# Unity reset script for Quantal.
# born at http://chat.stackexchange.com/rooms/6118/unity-reconfiguration

#Better version

#!/usr/bin/python
import subprocess
import argparse
def resetPlugins():
# List of Compiz plugins to be reset
    plugins=['core', 'composite', 'opengl', 'decor', 'vpswitch', 'snap', 'mousepoll', 'resize', 'place', 'move', 'wall', 'grid', 'session', 'animation', 'fade', 'unitymtgrabhandles', 'workarounds', 'scale', 'expo', 'ezoom', 'unityshell']
    for plugin in plugins:
        schema='org.compiz.'+plugin
        path="/org/compiz/profiles/unity/plugins/"+plugin+"/"
        pluginresetter="gsettings reset-recursively "+schema+":"+path
        subprocess.call(pluginresetter,shell=True)

def resetUnityChildren():
    unityChildren=["com.canonical.Unity","com.canonical.Unity.Launcher","com.canonical.Unity.ApplicationsLens","com.canonical.Unity.Lenses","com.canonical.Unity.Dash","com.canonical.Unity.Panel","com.canonical.Unity.Devices","com.canonical.Unity.Runner","com.canonical.Unity.FilesLens"]
    for child in unityChildren:
#    subprocess.Popen(unityresetter,shell=True, stdout=subprocess.PIPE).communicate()
         subprocess.call("gsettings reset-recursively "+child)
# Replace the current session, reloading settings.
subprocess.call("unity --replace",shell=True)

