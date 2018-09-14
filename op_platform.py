#! /usr/bin/env python
# -*- coding: utf-8 -*-

# judgement of operation system

import os
import platform

def run_task():
    os_platfrom=platform.platform()
    if os_platfrom.startswith('Darwin'):
       print('this is mac os system')
       os.system('ls')
    elif os_platfrom.startswith('Window'):
       print( 'this is win system' )
       os.system('dir')

