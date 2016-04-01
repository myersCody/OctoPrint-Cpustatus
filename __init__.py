# authors: Angela Reinhard, Cody Myers
#
# Purpose: Plugin that allows CPU usage to be displayed

from __future__ import absolute_import

import octoprint.plugin
import psutil
import string

class cpuStatus(octoprint.plugin.StartupPlugin,
		octoprint.plugin.TemplatePlugin):
		#octoprint.plugin.SettingsPlugin):

	def on_after_startup(self):
		self._logger.info("CPU Status")

__plugin_name__ 	  = "OctoPrint-Cpustatus"
'''
__plugin_version__ 	  = "1.0.0"
__plugin_description__ 	  = "A plugin to display the cpu status"
'''
__plugin_implementation__ = cpuStatus()


cpuUsage = psutil.cpu_percent(interval=1)
testFile = open("test.txt", "w")
testFile.write(cpuUsage)
testFile.close()

