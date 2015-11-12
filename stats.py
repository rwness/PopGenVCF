#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""usage: popgenvcf stats       -f VCF [-r REGION] [-o OUT] [--h|--help] 
    
    Options:
        --h --help              show this
        -f, --vcf VCF           VCF file 
        -r, --region REGION     String or file of regions (format : CHROM:START-STOP, 1-based)
        -o, --out OUT           Output file [default: VCF.stats.txt]
"""

from __future__ import division
from docopt import docopt
from os.path import isfile, abspath, dirname
import lib.IO as IO
import lib.bless as bless

if __name__ == '__main__':
    main_dir = dirname(__file__)
    #print data_dir
    args = docopt(__doc__)
    print args
    vcf_f = args['--vcf']
    region_arg = args['--region']
    out_f = args['--out']

    # Deal with regions ...
    region_f = None
    region_list = []
    if isfile(region_arg):
        region_f = abspath(region_arg)
        region_list = IO.parse_list(region_f)
    else: 
        region_list.append(region_arg)
    bless.region_list(region_list)

    




