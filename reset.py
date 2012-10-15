# Unity reset script for Quantal.
# born at http://chat.stackexchange.com/rooms/6118/unity-reconfiguration

#Better version

#!/usr/bin/python
import subprocess
plugins=['core', 'composite', 'opengl', 'decor', 'vpswitch', 'snap', 'mousepoll', 'resize', 'place', 'move', 'wall', 'grid', 'session', 'animation', 'fade', 'unitymtgrabhandles', 'workarounds', 'scale', 'expo', 'ezoom', 'unityshell']
for plugin in plugins:
    schema='org.compiz.'+plugin
    path="/org/compiz/profiles/unity/plugins/"+plugin+"/"
    resetter="gsettings reset-recursively "+schema+":"+path
    subprocess.call(resetter,shell=True)
subprocess.call("setsid unity",shell=True)

