#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

try:
    input = sys.argv[1]
except IndexError:
    print("Usage: ./theorybot.py <file>")
    sys.exit(1)

tree = ET.parse(input)

# Array to store info parsed from XML file
notes = []
intervals = []

# Finds and appends the appropriate elements to respective arrays
for pitch in tree.findall(".//pitch"):
    notes.append([pitch.find('step').text, pitch.find('octave').text])

# Calculation of intervals
for i in range(len(notes) / 2):
    interval = (ord(notes[i][0]) + 2 % 7) - ((ord(notes[len(notes) / 2 + i][0])) + 2 % 7) + 1
    if interval < 0:
        interval += 7;
    intervals.append(interval)

# Prints intervals between the two lines and if applicable, any potential places for error
print("Intervals:")
for i in range(len(intervals) - 1):
    print(intervals[i])
    if intervals[i] == intervals[i + 1]:
        if intervals[i] == 5:
            print("\tWarning: repeated fifths. Check to make sure they are not in parallel motion.")
        elif intervals[i] == 8:
            print("Warning: repeated eighths. Check to make sure they are not in parallel motion.")


