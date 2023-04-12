import os, signal


def process():
    # Ask user for the name of process
    name = "tor"
    try:

        # iterating through each instance of the process
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()

            # extracting Process ID from the output
            pid = fields[0]

            # terminating process
            os.kill(int(pid), signal.SIGKILL)
        print("Process Successfully terminated")

    except:
        print("Error Encountered while running script")


import io
import socket
import urllib.request

import socks
import stem.process
from stem.util import term

SOCKS_PORT=9050
def print_bootstrap_lines(line):
    if "Bootstrapped " in line:
        print(term.format(line, term.Color.BLUE))

def bootstrap():
    # Start an instance of Tor configured to only exit through Russia. This prints
    # Tor's bootstrap information as it starts. Note that this likely will not
    # work if you have another Tor instance running.
    print(term.format("Starting Tor:\n", term.Attr.BOLD))

    tor_process = stem.process.launch_tor_with_config(
        config={
            "SocksPort": str(SOCKS_PORT),
            "ExitNodes": "{ru}",
        },
        init_msg_handler=print_bootstrap_lines,
    )