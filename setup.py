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

from setuptools import setup
from openplotterRs485 import version

setup (
	name = 'openplotterRs485',
	version = version.version,
	description = 'Attach a customized sensor device via RS485 to OpenPlotter.',
	license = 'GPLv3',
	author="Milan Broum",
	author_email='midlis@gmail.com',
	url='https://github.com/midlis/openplotter-rs485',
	packages=['openplotterRs485'],
	classifiers = ['Natural Language :: English',
	'Operating System :: POSIX :: Linux',
	'Programming Language :: Python :: 3'],
	include_package_data=True,
	entry_points={'console_scripts': ['openplotter-rs485=openplotterRs485.openplotterRs485:main','rs485PostInstall=openplotterRs485.rs485PostInstall:main','rs485PreUninstall=openplotterRs485.rs485PreUninstall:main']},
	### entry_points: creating entry points you will be able to run these python scripts from everywhere.
		### openplotter-rs485 = This is the GUI of your app
		### rs485PostInstall = This file must be executed after the package installation and it should contain any extra task like installing pip packages, creating services...
		### rs485PreUninstall = This file must be executed before the package uninstallation. Here you should revert all changes in rs485PostInstall.
	data_files=[('share/applications', ['openplotterRs485/data/openplotter-rs485.desktop']),('share/pixmaps', ['openplotterRs485/data/openplotter-rs485.png']),],
	### data_files = Add files to the host system. This will work only when installed as debian package, not as python module.
	)

	### MORE REQUIRED CHANGES
	### use Poedit program to update the translations sources in openplotterMyapp/locale/en/LC_MESSAGES/openplotter-myapp.po
