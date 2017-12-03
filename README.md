# theory-scripts
Medley of scripts related to music theory

## Info 
I've included some example XML files to use but you could make more examples on [Noteflight](https://www.noteflight.com/) or [MuseScore](https://www.musescore.org/) as examples.

### errorcheck.py
Usage: `./errorcheck.py <file>`

Warns you if you have successive fifths and eighths<sup>[1]</sup> in your voice leading. Only works on one measure two-part voice leading, one line being in the bass clef and one in the treble clef. Included are some test .xml files that are compatible with this script. 

<sup>[1] For example, C and G and D and G are both fifths apart from each other (see keyboard diagram [here](http://www.piano-keyboard-guide.com/wp-content/uploads/2015/05/piano-keyboard-diagram.gif)). Since fifths and eighths can be further divided into more specific types, it's not necessarily always wrong for them to lead into each other. As such, I've opted for a warning message instead of an error when two fifths or eighths appear in succession. 
