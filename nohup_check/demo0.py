#!/bin/env python

import subprocess

time = '0.01'
return_code = subprocess.call("./reconstruct0.sh "+time, shell=True)
