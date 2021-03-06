#!/usr/bin/env python

import sys
import os

# Configure your favorite diff program here.
# route to git ext merge tool
DIFF = "/Applications/p4merge.app/Contents/MacOS/p4merge"
# Subversion provides the paths we need as the last two parameters.
LEFT  = sys.argv[-2]
RIGHT = sys.argv[-1]
# Call the diff command (change the following line to make sense for
# your diff program).
cmd = [DIFF, LEFT, RIGHT]
os.execv(cmd[0], cmd)
# Return an errorcode of 0 if no differences were detected, 1 if some were.
# Any other errorcode will be treated as fatal.
