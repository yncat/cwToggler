# cwToggler : character / word readout toggler  
## Overview  
git URL: https://github.com/yncat/cwToggler  
My website: https://www.nyanchangames.com/  
This add-on retrieves your "speak typed words" and "speak typed characters" settings and masks it when you're outside of any kind of editable text controls. You'll hear character / word echo only when you're actually editing texts. I'm sure gamers who like pressing space bar like the faimous keyboard crasher or non-gamers who use character-related shortcuts a lot really appreciate this(myself included of course).  
  
## Usage  
prebuilt package: https://www.nyanchangames.com/softs/count/download.php?download=9  
Or do `scons` to build for yourself  

#Notes  
If you install this addon, you can no longer change "speak typed characters" and "speak typed words" settings from NVDA's global configuration dialog. Even if you do so, the changes will be overwritten by CwToggler. Other settings are kept intact.
Instead, CwToggler detects NVDA+2 and NVDA+3 shortcuts respectively. The commands will behave exactly same as previous, but cwToggler is able to update the settings correctly in this way.  


