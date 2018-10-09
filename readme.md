# cwToggler : character / word readout toggler
## Overview
This add-on retrieves your "speak typed words" and "speak typed characters" settings and masks it when you're outside of any kind of editable text controls. You'll hear character / word echo only when you're actually editing texts. I'm sure gamers who like pressing space bar like the faimous keyboard crasher or non-gamers who use character-related shortcuts a lot really appreciate this(myself included of course).

## Usage
prebuilt package: 
Or do `scons` to build for yourself
Install and feel the usefulness.

## TODO
* Code optimization

## Localizing
Use the included cwToggler.pot. Make sure you save the file in UTF-8 without BOM.

# Translating
Run `scons pot`
Edit the generated pot file (make sure you save the file in UTF-8 without BOM)
Move and rename it as addon/locale/<YOUR_LANGUAGE_IDENTIFIER>/LC_MESSAGES/nvda.po
run `scons` to repackage

## Requests welcomed
i18n, optimizations, suggestions, bug reports, impressions, ETC