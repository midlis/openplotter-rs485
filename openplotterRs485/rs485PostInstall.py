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

import os, sys, subprocess
from openplotterSettings import conf
from openplotterSettings import language
from openplotterSettings import platform
from .version import version

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	package = 'openplotter-rs485'
	language.Language(currentdir, package, currentLanguage)
	platform2 = platform.Platform()

	app = {
	'name': 'RS485',
	'platform': 'both', ### rpi, debian or both
	'package': package,
	'preUninstall': platform2.admin+' '+'rs485PreUninstall',
	'uninstall': package,
	'sources': ['https://dl.cloudsmith.io/public/milan-broum/openplotter-quaranta/deb/debian buster'],
	'dev': 'yes', ### set to "yes" if you do not want your app to be updated from repositories yet.
	'entryPoint': 'openplotter-rs485',
	'postInstall': platform2.admin+' '+'rs485PostInstall',
	'reboot': 'no', ### set to "yes" if you want to shown a message "Reboot to apply changes" after updating from openplotter-settings.
	'module': 'openplotterRs485'
	}
	gpgKey = currentdir+'/data/rs485.gpg.key'
	sourceList = currentdir+'/data/openplotter-rs485.list'

	print(_('Adding app to OpenPlotter...'))
	try:
		externalApps1 = []
		try:
			externalApps0 = eval(conf2.get('APPS', 'external_apps'))
		except: externalApps0 = []
		for i in externalApps0:
			if i['package'] != package: externalApps1.append(i)
		externalApps1.append(app)
		conf2.set('APPS', 'external_apps', str(externalApps1))
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Checking sources...'))
	try:
		sources = subprocess.check_output('apt-cache policy', shell=True).decode(sys.stdin.encoding)
		exists = True
		for i in app['sources']:
			if not i in sources: exists = False
		if not exists:
			os.system('cp '+sourceList+' /etc/apt/sources.list.d')
			os.system('apt-key add - < '+gpgKey)
			os.system('apt update')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	###
	### Do here whatever you need after package installation. This file will be executed as sudo.
	###

	print(_('Setting version...'))
	try:
		conf2.set('APPS', 'rs485', version)
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()
