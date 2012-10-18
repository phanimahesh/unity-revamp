#!/usr/bin/python
import unityreset

compizPlugins=unityreset.UnityReset.snapshotCompizPlugins()
unityChildren=unityreset.UnityReset.snapshotUnityChildren()

for schema,keydict in compizPlugins.iteritems():
    print "---",schema,"---"
    for key,value in keydict.iteritems():
        print "   ",key,"\t\t: ",value
    print
for schema,keydict in unityChildren.iteritems():
    print "---",schema,"---"
    for key,value in keydict.iteritems():
        print "   ",key,"\t\t: ",value
    print

