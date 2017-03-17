""" This is the utility class. Contains utility classes for time and room representation"""

import re

class Time:
	""" A class representing time objects"""

	def __init__(self, hour, minute):
		""" 
			Initializes a Time object using hour and minute.
			Both hour and minute are integers, in 24 hour format
		"""
		self.hour = hour;
		self.minute = minute;

	@classmethod
	def fromString(cls):
		"""
			Creates a Time object from a string.
			Format supported:
			"1115" (assumed to be AM)
			"11:15" (assumed to be AM)
			"13:25"
			"11:15 am"
			"115" (assumed to be 1:15 AM)

		"""
		time = timeStr.replace(" ","")
		# three or four digit times
		mo1 = re.fullmatch(r'[0-9]{3,4}', time)
		if (mo1):
			hr = int( time[:-2] )
			mn = int( time[-2:] )
			return cls(hr, mn)
		# times separated by :, no AM/PM
		mo2 = re.fullmatch(r'[0-9]{1,2}:[0-9]{1,2}', time)
		if (mo2):
			lst = time.split(":")
			hr = int(lst[0])
			mn = int(lst[1])
			return cls(hr, mn)
		# digits + AM/PM
		mo3 = re.fullmatch(r'[0-9]{3,4}(am|pm)', time, re.I)
		# digits:digits + AM/PM
		mo4 = re.fullmatch(r'[0-9]{1,2}:[0-9]{2}(am|pm)', time, re.I)