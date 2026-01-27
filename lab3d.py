#!/usr/bin/env python3
#
# Author ID: kmitchell34

def free_space():
    import subprocess
    disk_space = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"])
    print(disk_space.strip())