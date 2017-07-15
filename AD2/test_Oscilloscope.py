import AD2
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ad2 = AD2.AD2()

    def test_buffersize(self):
        self.ad2.scope.buffersize = 1000
        self.assertEqual(1000,self.ad2.scope.buffersize,"scope buffersize incorrect")
        self.ad2.scope.buffersize = 512
        self.assertEqual(512,self.ad2.scope.buffersize,"scope buffersize incorrect")
        self.ad2.scope.buffersize = 10000
        self.assertEqual(8192,self.ad2.scope.buffersize,"scope buffersize incorrect")

    @unittest.skip("channelrange skipping")
    def test_channelrange(self):
        self.ad2.scope.ch1.range = 5.0
        self.assertEqual(50,int(round(self.ad2.scope.buffersize*10)),"scope ch1 range incorrect")
        self.ad2.scope.ch1.range = 3.21
        self.assertEqual(32,int(round(self.ad2.scope.buffersize*10)),"scope ch1 range incorrect")

    @classmethod
    def tearDownClass(self):
        self.ad2.close()

