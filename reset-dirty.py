# Unity reset script for Quantal.
# born at http://chat.stackexchange.com/rooms/6118/unity-reconfiguration
# Dirty one

#!/usr/bin/python
import subprocess
plugins=['core', 'composite', 'opengl', 'decor', 'vpswitch', 'snap', 'mousepoll', 'resize', 'place', 'move', 'wall', 'grid', 'session', 'animation', 'fade', 'unitymtgrabhandles', 'workarounds', 'scale', 'expo', 'ezoom', 'unityshell']
for plugin in plugins:
    schema='org.compiz.'+plugin
    n="gsettings list-keys "+schema+":/org/compiz/profiles/unity/"
    out,err=subprocess.Popen(n,shell=True, stdout=subprocess.PIPE).communicate()
    keys=out.splitlines()
    path="/org/compiz/profiles/unity/plugins/"+plugin+"/"
    for key in keys:
        resetter="gsettings reset "+schema+":"+path+" "+key
        subprocess.call(resetter,shell=True)
subprocess.call("setsid unity",shell=True)
