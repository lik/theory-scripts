#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

try:
    input = sys.argv[1]
except IndexError:
    print("Usage: ./theorybot.py <file>")
    sys.exit(1)

tree = ET.parse(input)

#for elem in tree.iter(tag='step'):
#    print(elem.text)

for pitch in tree.findall(".//pitch"):
    print(pitch.find('step').text)
    print(pitch.find('octave').text)
    
# Use if-statements to determine which array the notes will go under    
# print(note.find('voice').text) 

# Have two counters and increment when you add up duration a certain way
# print(note.find('duration').text)
