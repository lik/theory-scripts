#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

try:
    input = sys.argv[1]
except IndexError:
    print("Usage: ./info.py <file>")
    sys.exit(1)

tree = ET.parse(input)

measures = 0;
for measure in tree.findall(".//measure"):
    measures += 1

"""
Converts the units used in the tempo listing into a number
For simplicity only supporting the most commonly used ones
"""
beat_unit = tree.find(".//beat-unit").text
if beat_unit == "whole":
    beat_unit = 1
elif beat_unit == "half":
    beat_unit = 2
elif beat_unit == "quarter":
    beat_unit = 4
elif beat_unit == "eighth":
    beat_unit = 8
else:
    print("Beat-unit not supported")
    sys.exit(1)

bpm = float(tree.find(".//per-minute").text)
if bpm == "":
    print("Beats per measure not found")
    sys.exit(1)

numerator = int(tree.find(".//beats").text)
denominator = int(tree.find(".//beat-type").text)

time = denominator / beat_unit * (1 / bpm) * numerator * measures

print("This piece if played to the marked tempo will take %f minutes" % (time))
sys.exit(1)

tree = ET.parse(input)
