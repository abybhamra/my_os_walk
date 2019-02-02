from unittest import TestCase

from my_os_walk import print_directory_contents

VALID_OP = ['/tmp/F7C71944B49B446081C0603DE90E4855_OUT',
            '/tmp/E9DB4223-AF52-4760-8B5E-B43B611BB2C6_OUT',
            '/tmp/com.adobe.AdobeIPCBroker.ctrl-abhineetbhamra',
            '/tmp/FB922AA7-3291-41C4-9EC9-E8E397FF4001_IN',
            '/tmp/E9DB4223-AF52-4760-8B5E-B43B611BB2C6_IN',
            '/tmp/adobegc.log',
            '/tmp/F7C71944B49B446081C0603DE90E4855_IN',
            '/tmp/brew.1',
            '/tmp/sperion',
            '/tmp/FB922AA7-3291-41C4-9EC9-E8E397FF4001_OUT']


class TestMyOSWalk(TestCase):

    def test_with_a_valid_path_returns(self):
        self.assertEqual(VALID_OP, print_directory_contents("/tmp"))
