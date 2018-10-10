# -*- coding: UTF-8 -*-
# cwToggler main implementation file
# Written by: Yukio Nozawa <personal@nyanchangames.com>
# Released under GPL(See ../COPYING.txt for license)

import config
import globalPluginHandler
import eventHandler
import controlTypes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	previousRole=controlTypes.ROLE_UNKNOWN#Role of the last focused control
	enabled=False#True when NVDA is focusing on an edit control and this addon is enabled (means unmasking the user settings)
	# Cach of the global settings (supposed to be updated dynamically as user changes them from the settings panel).
	enableCharacterReadout=None
	enableWordReadout=None

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.fetchSettings()
		# It starts with "disabled" status. When NVDA finds an editable control, it will fire the event after constructor calling
		config.conf["keyboard"]["speakTypedCharacters"]=False
		config.conf["keyboard"]["speakTypedWords"]=False

#Creates the recent cach of the user settings
	def fetchSettings(self):
		self.enableCharacterReadout=config.conf["keyboard"]["speakTypedCharacters"]
		self.enableWordReadout=config.conf["keyboard"]["speakTypedWords"]
		# Defaults when not present
		if self.enableCharacterReadout is None: self.enableCharacterReadout=True
		if self.enableWordReadout is None: self.enableWordReadout=False

# Event listener
	def event_gainFocus(self, obj, nextHandler):
		if self.previousRole!=obj.role: self.doCheck(obj)#Decrease the total amount of unnecessary checks a little bit
		nextHandler()

# Examines the role of focused control and performs required action
	def doCheck(self,obj):
		self.previousRole=obj.role
		if obj.role in (controlTypes.ROLE_EDITABLETEXT, controlTypes.ROLE_TERMINAL, controlTypes.ROLE_RICHEDIT, controlTypes.ROLE_TEXTFRAME, controlTypes.ROLE_PASSWORDEDIT, controlTypes.ROLE_DOCUMENT):# Enable it
			self.enabled=True
			config.conf["keyboard"]["speakTypedCharacters"]=self.enableCharacterReadout
			config.conf["keyboard"]["speakTypedWords"]=self.enableWordReadout
		elif self.enabled:# Disable it
			self.enabled=False
			self.fetchSettings()
			config.conf["keyboard"]["speakTypedCharacters"]=False
			config.conf["keyboard"]["speakTypedWords"]=False

	def terminate(self):# Reverts the settings
			config.conf["keyboard"]["speakTypedCharacters"]=self.enableCharacterReadout
			config.conf["keyboard"]["speakTypedWords"]=self.enableWordReadout
