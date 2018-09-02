#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
import shutil

cwd = os.getcwd()
run = os.system

archs = ['x86', 'armeabi-v7a']

for arch in archs:
    os.chdir(cwd)
    shutil.rmtree(arch, ignore_errors=True)
    os.mkdir(arch)
    os.chdir(os.path.join(cwd, arch))
    cmd = 'cmake -DANDROID_ABI=%s -DCMAKE_TOOLCHAIN_FILE=%s/build/cmake/android.toolchain.cmake -DANDROID_NATIVE_API_LEVEL=16 -GNinja ../..' % (arch,os.getenv("NDK_ROOT"))
    run(cmd)
    cmd = 'ninja'
    run(cmd)

