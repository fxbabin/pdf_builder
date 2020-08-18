#!/usr/bin/env python3

##################
#   LIBRAIRIES   #
##################

import subprocess
import sys


#################
#   FUNCTIONS   #
#################


def error(s, Warn=False, infile=None, line_nb=-1):
    """
    Description of error

    Args:
        s (undefined)           : error message
        Warn=False (undefined)  : Warn flag (true if warning, else error)
        infile=None (undefined) : file name
        line_nb=-1 (undefined)  : line number

    Raises error or warning at file/line precision.
    """
    out = "[Error]" if not Warn else "[Warning]"
    out += " {}".format(infile) if infile else ""
    out += ":{}".format(line_nb + 1) if line_nb > -1 else ""

    if not Warn:
        raise Exception("{} :: {}".format(out, s))
    print("{} : {}".format(out, s))


def sub_decorator(func):
    """
    Description of sub_decorator

    Args:
        func (undefined):

    Decorator for subprocess run (try catch errors)
    """
    def wrapper_func(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return (res)
        except Exception as e:
            print("{} Exception Detected !\n{}".format(*args, e))
            sys.exit(-1)

    return wrapper_func


@sub_decorator
def sub_run(command):
    """
    Description of sub_run

    Args:
        command (undefined):
    """
    out = subprocess.run(command,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    return (out)
