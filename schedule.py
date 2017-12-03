#!/usr/bin/env python
# coding = utf-8

import subprocess, os
import datetime

def mr_job():
    mypath = os.path.dirname(os.path.abspath(__file__))
    # print "mypath is  ",mypath
    inputpath = '/input/nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv'
    outputpath = '/output/'
    mapper = mypath + '/test_mapper.py'
    reducer = mypath + '/test_reducer.py'
    cmds = ['/usr/local/Cellar/hadoop/2.8.2', 'jar', '/usr/local/Cellar/hadoop/2.8.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar',
            '-input', inputpath,
            '-output', outputpath,
            '-mapper', mapper,
            '-reducer', reducer,
            '-file', mapper,
            '-file', reducer, ]
    for f in os.listdir(mypath):
        cmds.append(mypath + '/' + f)
    cmd = ['/usr/local/Cellar/hadoop/2.8.2', 'fs', '-rmr', outputpath]
    subprocess.call(cmd)
    subprocess.call(cmds)


def main():
    mr_job()


if __name__ == '__main__':
    main()