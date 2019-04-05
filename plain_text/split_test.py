from __future__ import print_function
from __future__ import division

import sys
import argparse

parser = argparse.ArgumentParser(description='Split input into mulitple file on lines based on character count')
parser.add_argument('--c', type=int, default=5000, help='Maximum number of characters per file (Default: 5000)')
parser.add_argument('--name', type=str,default='split', help='Base name of split files (Default:split')
args = parser.parse_args()

file_counter = 0
char_count = args.c+1
for line in sys.stdin:
    line = line.rstrip()
    line_len = len(line)+1
    if(char_count + line_len > args.c): 
        fh = open('{}{:03d}'.format(args.name,file_counter),"w")
        char_count = 0
        file_counter += 1
    print(line,file=fh)
    char_count += line_len
