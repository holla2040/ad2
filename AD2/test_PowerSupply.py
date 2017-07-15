import AD2
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ad2 = AD2.AD2()

        # my unit's offsets
        self.ad2.vpos.setOffset = 0.0007
        self.ad2.vpos.getOffset = -0.0007
        self.ad2.vneg.setOffset = 0.0049
        self.ad2.vneg.getOffset = 0.1195

    def test_vpos_voltage(self):
        self.ad2.vpos.voltage = 1.23
        self.assertEqual(123,int(round(self.ad2.vpos.voltage*100)),"vpos voltage incorrect")

    def test_vneg_voltage(self):
        self.ad2.vneg.voltage = -1.23
        self.assertEqual(-123,int(round(self.ad2.vneg.voltage*100)),"vneg voltage incorrect")

    @classmethod
    def tearDownClass(self):
        self.ad2.close()

