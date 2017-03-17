""" This is the utility class. Contains utility classes for time and room representation"""

import re

class Time:
	""" A class representing time objects"""

	def __init__(self, hour, minute):
		""" 
			Initializes a Time object using hour and minute.
			Both hour and minute are integers, in 24 hour format
			From 00:00 to 23:59 with noon at 12:00
		"""
		self.hour = hour;
		self.minute = minute;

	@classmethod
	def fromString(cls, timeStr):
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
			if (hr > 24 or mn > 59):
				# print("Not a valid time")
				return None
			return cls(hr, mn)
		# times separated by :, no AM/PM
		mo2 = re.fullmatch(r'[0-9]{1,2}:[0-9]{1,2}', time)
		if (mo2):
			lst = time.split(":")
			hr = int(lst[0])
			mn = int(lst[1])
			if (hr > 24 or mn > 59):
				# print("Not a valid time")
				return None
			return cls(hr, mn)
		# digits + AM/PM
		mo3 = re.fullmatch(r'[0-9]{3,4}(am|pm)', time, re.I)
		if (mo3):
			apm = time[-2:].lower()
			hr = int(time[:-4])
			mn = int(time[-4:-2])
			if (apm == "am"):	
				if (hr > 11 or mn > 59):
					# print("Not a valid time")
					return None
				return cls(hr, mn)
			else:
				if (hr > 12 or hr < 1 or mn > 59):
					# print("Not a valid time")
					return None
				if ( not hr == 12):
					hr = hr+12
				return cls(hr, mn)
		# digits:digits + AM/PM
		mo4 = re.fullmatch(r'[0-9]{1,2}:[0-9]{2}(am|pm)', time, re.I)
		if (mo4):
			apm = time[-2:].lower()
			lst = time[:-2].split(":")
			hr = int(lst[0])
			mn = int(lst[1])
			if (apm == "am"):
				if (hr > 11 or mn > 59):
					# print("Not a valid time")
					return None
				return cls(hr, mn)
			else:
				if (hr > 12 or hr < 1 or mn > 59):
					# print("Not a valid time")
					return None
				if ( not hr == 12):
					hr = hr+12
				return cls(hr, mn)
		# print("Not a supported time format")
		return None


	def __add__(self, other):
		""" overloading + operator for Time objects"""

	def __sub__(self, other):
		""" Overloading - operator for Time objects"""

	def __eq__(self, other):
		""" Overloading == operator for Time objects"""

	def __ne__(self, other):
		""" Overloading != operator for time objects"""

	def __lt__(self, other):
		""" Overlaoding < operator for time objects"""

	def __le__(self, other):
		""" Overloading <= operator for time objects"""

	def __gt__(self, other):
		""" Overloading > operator for time objects"""

	def __ge__(self, other):
		""" Overloading >= operator for time objects"""