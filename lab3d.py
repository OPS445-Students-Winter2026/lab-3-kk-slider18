#!/usr/bin/env python3
#
# Author ID: kmitchell34

import subprocess

def free_space():
    with subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE) as df:
        with subprocess.Popen(['grep', '/$'], stdin=df.stdout, stdout=subprocess.PIPE) as grep:
            with subprocess.Popen(['awk', '{print $4}'], stdin=grep.stdout, stdout=subprocess.PIPE) as awk:
                output, _ = awk.communicate()
                return output.decode('utf-8').strip()