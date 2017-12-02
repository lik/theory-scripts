#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

try:
    input = sys.argv[1]
except IndexError:
    print("Usage: ./theorybot.py <file>")
    sys.exit(1)

with open(input, 'rU') as i:
    for line in i:
        print(line)
