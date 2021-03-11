#!/usr/bin/python3

import os

dependencies =
    [
        "sudo apt-get update",
        "sudo apt-get install build-essential git subversion cmake libx11-dev libxxf86vm-dev libxcursor-dev libxi-dev libxrandr-dev libxinerama-dev libglew-dev"
    ]
sources =
    [
        "mkdir ~/blender-git",
        "cd ~/blender-git",
        "git clone https://git.blender.org/blender.git"
    ]
libs =
    [
        "mkdir ~/blender-git/lib",
        "cd ~/blender-git/lib",
        "svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64"
    ]
setup =
    [
        "mkdir ~/blender-git/build",
        "cd ~/blender-git/build",
        "cmake ../blender"
    ]
build =
    [
        "cd ~/blender-git/blender",
        "make update",
        "make bpy"
    ]
install =
    [
        "make install"
    ]
steps = [dependencies, sources, libs, build, install]

def build():
    for each in steps:
        for x in each:
            os.system(x)

if __name__ in '__main__':
    build()
