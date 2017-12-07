# theory-scripts
Medley of scripts related to music theory

## Info 
I've included some example XML files to use but you could make more examples on [Noteflight](https://www.noteflight.com/) or [MuseScore](https://www.musescore.org/) as examples.

### errorcheck.py
Usage: `./errorcheck.py <file>`

Warns you if you have successive fifths and eighths<sup>[1]</sup> in your voice leading. Only works on one measure two-part voice leading without the use of accidentals, one line being in the bass clef and one in the treble clef. Included are test .xml files that start with error which are compatible with this script. Or make your own as long as it follows the aforementioned specifications.

<sup>[1] For example, C and G and D and G are both fifths apart from each other (see keyboard diagram [here](http://www.piano-keyboard-guide.com/wp-content/uploads/2015/05/piano-keyboard-diagram.gif)). Since fifths and eighths can be further divided into more specific types, it's not necessarily always wrong for them to lead into each other. As such, I've opted for a warning message instead of an error when two fifths or eighths appear in succession. 

### info.py
Usage: `/.info.py <file>`

Computes information from a given .xml file. This one is much less picky than `errorcheck.py`, any MusicXML file should be able to compute the time it takes to perform a piece and the amount of notes and rests in it. Assumes that there are no irregular measures (e.g. time signature changes in the middle of a piece, making the time calculation formula inaccurate). Much like `errorcheck.py` I've included some test files, this time beginning with info, but making your own and testing it out should work just fine as well.
