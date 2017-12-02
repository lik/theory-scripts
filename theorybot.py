#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

try:
    input = sys.argv[1]
except IndexError:
    print("Usage: ./theorybot.py <file>")
    sys.exit(1)

tree = ET.parse(input)

notes = []
intervals = []

highest_voice = 0
for voice in tree.iter(tag='voice'):
    if voice.text > highest_voice:
        highest_voice = voice.text
    
print("Highest voice: " + highest_voice)

for pitch in tree.findall(".//pitch"):
    notes.append([pitch.find('step').text, pitch.find('octave').text])

print(notes)

for i in range(len(notes) / 2):
    intervals.append((ord(notes[i][0]) + 2 % 7) - ((ord(notes[len(notes) / 2 + i][0])) + 2 % 7))

print(intervals)
