"""Checks to see if the process is already running.  If not, runs it"""

import logging
import socket
import sys
import main

lock_available = main.check_and_aquire_lock():
if not lock_available:
    sys.exit()
else:
    main.main(greeting=False)

