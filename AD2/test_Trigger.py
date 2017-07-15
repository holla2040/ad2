import AD2
import unittest
from AD2.dwfconstants import *


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ad2 = AD2.AD2()

    @unittest.skip("autotimeout skipping") 
    def test_autotimeout(self):
        self.ad2.trigger.autotimeout = 1.213
        print self.ad2.trigger.autotimeout
        # print int(round(self.ad2.trigger.autotimeout*1000))
        self.assertEqual(1213,int(round(self.ad2.trigger.autotimeout*1000)),"trigger autotimeout incorrect")

    def test_holdoff(self):
        self.ad2.trigger.holdoff = 1.213
        self.assertEqual(1213,int(round(self.ad2.trigger.holdoff*1000)),"trigger holdoff incorrect")

    def test_hysteresis(self):
        self.ad2.trigger.hysteresis = 1.213
        # print int(round(self.ad2.trigger.hysteresis*1000))
        self.assertEqual(1213,int(round(self.ad2.trigger.hysteresis*1000)),"trigger hysteresis incorrect")

    def test_source(self):
        self.ad2.trigger.source = trigsrcAnalogIn
        self.assertEqual(trigsrcAnalogIn.value,(self.ad2.trigger.source).value,"trigger source incorrect")

    def test_lengthcondition(self):
        self.ad2.trigger.lengthcondition = triglenLess
        self.assertEqual(triglenLess.value,(self.ad2.trigger.lengthcondition).value,"trigger lengthcondition incorrect")

    def test_length(self):
        self.ad2.trigger.length = 1.213
        self.assertEqual(1213,int(round(self.ad2.trigger.length*1000)),"trigger length incorrect")

    def test_type(self):
        self.ad2.trigger.type = trigtypeEdge
        self.assertEqual(trigtypeEdge.value,(self.ad2.trigger.type).value,"trigger type incorrect")
        self.ad2.trigger.type = trigtypePulse
        self.assertEqual(trigtypePulse.value,(self.ad2.trigger.type).value,"trigger type incorrect")
        self.ad2.trigger.type = trigtypeTransition
        self.assertEqual(trigtypeTransition.value,(self.ad2.trigger.type).value,"trigger type incorrect")

    def test_channel(self):
        self.ad2.trigger.channel = 0
        self.assertEqual(0,self.ad2.trigger.channel,"trigger channel incorrect")
        self.ad2.trigger.channel = 1
        self.assertEqual(1,self.ad2.trigger.channel,"trigger channel incorrect")

    def test_level(self):
        self.ad2.trigger.level = 0.123
        self.assertEqual(123,int(round(self.ad2.trigger.level*1000)),"trigger level incorrect")
        self.ad2.trigger.level = 0.321
        self.assertEqual(321,int(round(self.ad2.trigger.level*1000)),"trigger level incorrect")

    def test_filter(self):
        self.ad2.trigger.filter = filterDecimate
        self.assertEqual(filterDecimate.value,(self.ad2.trigger.filter).value,"trigger filter incorrect")
        self.ad2.trigger.filter = filterAverage
        self.assertEqual(filterAverage.value,(self.ad2.trigger.filter).value,"trigger filter incorrect")
        self.ad2.trigger.filter = filterDecimate
        self.assertEqual(filterDecimate.value,(self.ad2.trigger.filter).value,"trigger filter incorrect")

    def test_condition(self):
        self.ad2.trigger.condition = trigcondRisingPositive
        self.assertEqual(trigcondRisingPositive.value,(self.ad2.trigger.condition).value,"trigger condition incorrect")
        self.ad2.trigger.condition = trigcondFallingNegative
        self.assertEqual(trigcondFallingNegative.value,(self.ad2.trigger.condition).value,"trigger condition incorrect")

    @classmethod
    def tearDownClass(self):
        self.ad2.close()

