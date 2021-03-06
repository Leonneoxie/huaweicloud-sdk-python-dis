#!/usr/bin/python
# -*- coding:utf-8 -*-
from dis_sdk_python import *

streamname = "dis_test1"
task_name="113"

def describe_dump_task_test():
    cli = disclient(endpoint='', ak='', sk='', projectid='', region='')
    try:
        r=cli.describe_dump_task(streamname,task_name)
        print(r.statusCode)
        if IS_PYTHON2:
            print(json.dumps(r.body))
        else:
            print(r.body)

    except Exception as ex:
        print(str(ex))



if __name__ == '__main__':
    print("describe dump_task")
    describe_dump_task_test()




