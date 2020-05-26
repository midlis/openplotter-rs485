#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2020 by Sailoog <https://github.com/openplotter/openplotter-myapp>
#
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.

import time, os, subprocess, sys
from openplotterSettings import language

class Start(): ### This class will be always called at startup. You should start here only GUI programs. Non GUI progrmas should be started as a services.
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(os.path.abspath(__file__))
		language.Language(currentdir,'openplotter-rs485',currentLanguage)

		self.initialMessage = _('Opening "RS485 app"...')

	def start(self): ### this funtion will be called only if "self.initialMessage" has content.
		green = '' ### green messages will be printed in green after the "self.initialMessage"
		black = '' ### black messages will be printed in black after the green message
		red = '' ### red messages will be printed in red in a new line

		### start here any GUI program that needs to be started at startup and set the messages.
		green = _('This message should be green')
		black = _('This message should be black')
		red = _('"RS485" should open. Uninstall "RS485" to remove this.')
		subprocess.Popen('openplotter-rs485')

		time.sleep(1) ### "check" function is always called after "start" function, so if we start any program here we should wait some seconds before checking it.
		return {'green': green,'black': black,'red': red}

class Check(): ### This class is always called after "start" function and when the user checks the system.
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(os.path.abspath(__file__))
		language.Language(currentdir,'openplotter-rs485',currentLanguage)

		self.initialMessage = _('Checking "RS485"...') ### "self.initialMessage" will be printed when checking the system. If it is empty the function check will not be called. Use trasnlatable text: _('Checking My App...')

	def check(self): ### this funtion will be called only if "self.initialMessage" has content.
		green = '' ### green messages will be printed in green after the "self.initialMessage"
		black = '' ### black messages will be printed in black after the green message
		red = '' ### red messages will be printed in red in a new line

		### check here any feature and set the messages
		green = _('"RS485" is installed')
		test = subprocess.check_output(['ps','aux']).decode(sys.stdin.encoding)
		if 'openplotter-rs485' in test: black = _('"RS485" is running')
		else: black = _('"RS485" is not running')
		red = _('Warning example. Uninstall "RS485" to remove this.')

		return {'green': green,'black': black,'red': red}
