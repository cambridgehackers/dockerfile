
import os, sys
import subprocess

import boto
import boto.ec2

instance_id = subprocess.check_output(['curl', '-s', 'http://169.254.169.254/latest/meta-data/instance-id'])

ec2 = boto.ec2.connect_to_region('us-east-1')
instances = ec2.get_all_instances(instance_ids=[instance_id])
print instances
tags = ec2.get_all_tags(filters={'resource-id':instance_id})

instance_name = instance_id
for t in tags:
    print t, t.name, t.value
    if t.name == 'Name':
       instance_name = t.value

sys.exit(0)
from buildslave.bot import BuildSlave
from twisted.application import service

basedir = '/scratch/buildbot/worker'
rotateLength = 10000000
maxRotatedFiles = 10

# if this is a relocatable tac file, get the directory containing the TAC
if basedir == '.':
    import os.path
    basedir = os.path.abspath(os.path.dirname(__file__))

# note: this line is matched against to check that this is a buildslave
# directory; do not edit it.
application = service.Application('buildslave')

try:
  from twisted.python.logfile import LogFile
  from twisted.python.log import ILogObserver, FileLogObserver
  logfile = LogFile.fromFullPath(os.path.join(basedir, "twistd.log"), rotateLength=rotateLength,
                                 maxRotatedFiles=maxRotatedFiles)
  application.setComponent(ILogObserver, FileLogObserver(logfile).emit)
except ImportError:
  # probably not yet twisted 8.2.0 and beyond, can't set log yet
  pass

buildmaster_host = '10.0.0.61'
port = 9989
slavename = 'worker-ip-10-0-0-61'
slavename = instance_name
passwd = 'xbsv-rules-atomically'
keepalive = 600
usepty = 0
umask = None
maxdelay = 300
allow_shutdown = None

s = BuildSlave(buildmaster_host, port, slavename, passwd, basedir,
               keepalive, usepty, umask=umask, maxdelay=maxdelay,
               allow_shutdown=allow_shutdown)
s.setServiceParent(application)

