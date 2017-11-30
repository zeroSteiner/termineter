#  termineter/modules/get_identification_info.py
#
#  Copyright 2017 Spencer J. McIntyre <SMcIntyre [at] SecureState [dot] net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from __future__ import unicode_literals

import c1218.data
from termineter.templates import TermineterModuleOptical

class Module(TermineterModuleOptical):
	require_connection = False
	attempt_login = False
	def __init__(self, *args, **kwargs):
		TermineterModuleOptical.__init__(self, *args, **kwargs)
		self.version = 1
		self.author = ['Spencer McIntyre']
		self.description = 'Read And Parse The Identification Information'
		self.detailed_description = 'This module allows individual tables to be read from the smart meter.'

	def run(self):
		conn = self.frmwk.serial_connection
		conn.send(c1218.data.C1218IdentRequest())
		resp = c1218.data.C1218Packet(conn.recv())

		self.frmwk.print_status('Received Identity Response:')
		self.frmwk.print_hexdump(resp.data)
