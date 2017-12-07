#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

try:
    input = sys.argv[1]
except IndexError:
    print("Usage: ./info.py <file>")
sys.exit(1)

tree = ET.parse(input)
