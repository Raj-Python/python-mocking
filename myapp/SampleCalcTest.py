import unittest
import json
from mock import patch, MagicMock
from SampleCalc import add
from Sum import sum


class samplecalctest(unittest.TestCase):

    @patch("myapp.SampleCalc.add")
    @patch("myapp.Sum")
    def test_add(self, mock_add,mock_sum):
        sum.sum.return_value=3
        c= add(4,4)
        self.assertTrue(c==3,"sum not equal")




