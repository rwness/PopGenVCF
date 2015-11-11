#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File        : IO.py
Author      : ?
Bugs        : ?
To do       : ?
"""

from __future__ import division
import re
import subprocess
import commands

def parse_list(infile):
    parsed_list = []
    with open(infile) as fh:
        for line in fh:
            parsed_list.append(line.rstrip("\n"))
    return parsed_list

if __name__ == "__main__": 
    pass
