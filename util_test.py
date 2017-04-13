import util
import unittest

""" This is a test file for module Util """

class TestTimeMethods(unittest.TestCase):

    def test_fromStringCorretFormat(self):
        print("\nStart testing on correctly formatted time strings")
        
        timeStr2 = "116"
        time2 = util.Time.fromString(timeStr2)
        self.assertEqual(time2.hour, 1)
        self.assertEqual(time2.minute, 16)

        timeStr3 = "2345"
        time3 = util.Time.fromString(timeStr3)
        self.assertEqual(time3.hour, 23)
        self.assertEqual(time3.minute, 45)

        timeStr4 = "23:45"
        time4 = util.Time.fromString(timeStr4)
        self.assertEqual(time4.hour, 23)
        self.assertEqual(time4.minute, 45)

        timeStr5 = " 7:45 am"
        time5 = util.Time.fromString(timeStr5)
        self.assertEqual(time5.hour, 7)
        self.assertEqual(time5.minute, 45)

        timeStr6 = " 6 : 47 Pm  "
        time6 = util.Time.fromString(timeStr6)
        self.assertEqual(time6.hour, 18)
        self.assertEqual(time6.minute, 47)

        timeStr7 = " 6 08"
        time7 = util.Time.fromString(timeStr7)
        self.assertEqual(time7.hour, 6)
        self.assertEqual(time7.minute, 8)

        timeStr8 = " 734pM  "
        time8 = util.Time.fromString(timeStr8)
        self.assertEqual(time8.hour, 19)
        self.assertEqual(time8.minute, 34)

        timeStr9 = "1240pm"
        time9 = util.Time.fromString(timeStr9)
        self.assertEqual(time9.hour, 12)
        self.assertEqual(time9.minute, 40)

        timeStr10 = "0000"
        time10 = util.Time.fromString(timeStr10)
        self.assertEqual(time10.hour, 0)
        self.assertEqual(time10.minute, 0)

        timeStr9 = "1240pm"
        time9 = util.Time.fromString(timeStr9)
        self.assertEqual(time9.hour, 12)
        self.assertEqual(time9.minute, 40)

        print("PASSED")

    def test_fromStringWrongFormat(self):
        print("\nStart testing on wrongly formatted time strings")
        timeStr1 = "abc"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = ""
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = "1245am"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = "4567"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = "1287"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = "4556"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = "0023 pm"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = "068"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)

        timeStr1 = "1:45pma"
        time1 = util.Time.fromString(timeStr1)
        self.assertEqual(time1, None)
        print("PASSED")

if __name__ == '__main__':
    unittest.main()