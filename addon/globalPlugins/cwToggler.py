# -*- coding: UTF-8 -*-
# cwToggler main implementation file
import config
import globalPluginHandler
import eventHandler
import controlTypes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	previousRole=controlTypes.ROLE_UNKNOWN#Role of the last focused control
	enabled=False#True when NVDA is focusing on an edit control and this addon is enabled (means unmasking the user settings)
	#Cach of the global settings (supposed to be updated dynamically as user changes them from the settings panel).
	# TODO: Find out how to make custom constructor works without destroying NVDA, maybe super?
	enableCharacterReadout=None
	enableWordReadout=None
	isFirstRun=True#Could be optimized and removed if constructor worked

#Creates the recent cach of the user settings
	def fetchSettings(self):
		self.enableCharacterReadout=config.conf["keyboard"]["speakTypedCharacters"]
		self.enableWordReadout=config.conf["keyboard"]["speakTypedWords"]
		# Defaults when not present
		if self.enableCharacterReadout is None: self.enableCharacterReadout=True
		if self.enableWordReadout is None: self.enableWordReadout=False
		self.isFirstRun=False

# Event listener
	def event_gainFocus(self, obj, nextHandler):
		if self.previousRole!=obj.role: self.doCheck(obj)#Decrease the total amount of unnecessary checks a little bit
		nextHandler()

# Examines the role of focused control and performs required action
	def doCheck(self,obj):
		self.previousRole=obj.role
		if obj.role==controlTypes.ROLE_EDITABLETEXT or obj.role==controlTypes.ROLE_TERMINAL:# Enable it
			self.enabled=True
			if self.isFirstRun: self.fetchSettings() # Fired when NVDA first focused on an edit box after startup
			config.conf["keyboard"]["speakTypedCharacters"]=self.enableCharacterReadout
			config.conf["keyboard"]["speakTypedWords"]=self.enableWordReadout
		elif self.enabled or self.isFirstRun:# These two conditions are required
			self.enabled=False
			self.fetchSettings()
			config.conf["keyboard"]["speakTypedCharacters"]=False
			config.conf["keyboard"]["speakTypedWords"]=False

	def terminate(self):# I seriously wonder why the init version of this function is not declared in globalPluginHandler
		if not self.isFirstRun:# Prevent None's from being written to the global settings
			config.conf["keyboard"]["speakTypedCharacters"]=self.enableCharacterReadout
			config.conf["keyboard"]["speakTypedWords"]=self.enableWordReadout
