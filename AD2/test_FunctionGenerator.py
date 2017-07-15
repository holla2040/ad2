import AD2
import unittest
from AD2.dwfconstants import *

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ad2 = AD2.AD2()

    def test_fg1_frequency(self):
        self.ad2.fg1.frequency = 1234.56
        self.assertEqual(123456,int(round(self.ad2.fg1.frequency*100)),"fg1 frequency incorrect")
    def test_fg1_amplitude(self):
        self.ad2.fg1.amplitude = 1.23
        self.assertEqual(123,int(round(self.ad2.fg1.amplitude*100)),"fg1 amplitude incorrect")
    def test_fg1_offset(self):
        self.ad2.fg1.offset = 1.23
        self.assertEqual(123,int(round(self.ad2.fg1.offset*100)),"fg1 offset incorrect")
    def test_fg1_function(self):
        self.ad2.fg1.function = funcSine
        self.assertEqual(funcSine.value,(self.ad2.fg1.function).value,"fg1 function incorrect")

    def test_fg2_frequency(self):
        self.ad2.fg2.frequency = 6543.21
        self.assertEqual(654321,int(round(self.ad2.fg2.frequency*100)),"fg2 frequency incorrect")
    def test_fg2_amplitude(self):
        self.ad2.fg1.amplitude = 3.21
        self.assertEqual(321,int(round(self.ad2.fg1.amplitude*100)),"fg2 amplitude incorrect")
    def test_fg2_offset(self):
        self.ad2.fg2.offset = 3.21
        self.assertEqual(321,int(round(self.ad2.fg2.offset*100)),"fg2 offset incorrect")
    def test_fg2_function(self):
        self.ad2.fg2.function = funcSquare
        self.assertEqual(funcSquare.value,(self.ad2.fg2.function).value,"fg2 function incorrect")

    @classmethod
    def tearDownClass(self):
        self.ad2.close()

