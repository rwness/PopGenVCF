#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File        : bless.py
Author      : ?
Bugs        : ?
To do       : ?
"""

from __future__ import division
import sys 

def region_list(region_list):
    for region in region_list:
    	try:
    		chrom, coordinates = region.split(":")
    		start, end = coordinates.split("-")
    		if int(start) >= 1 and int(start) <= int(end):
    			pass
    		else:
    			sys.exit('[ERROR] : invalid region %s. Should be CHROM:START-STOP, 1-based.' % region)
    	except:
    		sys.exit('[ERROR] : invalid region %s. Should be CHROM:START-STOP, 1-based.' % region)

if __name__ == "__main__": 
    pass
