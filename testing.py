import unittest
from os import path, remove

from CloseToUs import CloseToUs

TEST_LOCAL_FILE = 'test_data/customers.txt'
MALFORMED_TEST_LOCAL_FILE = 'test_data/customers_wrong_json.txt'
TEST_URL = 'https://s3.amazonaws.com/intercom-take-home-test/customers.txt'

class TestFileRead(unittest.TestCase):
    def test_file_from_local(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(TEST_LOCAL_FILE)
        result = cl.read_file()
        print("Test if local file works as input")
        self.assertTrue(result['success'])

    def test_local_with_local_flag_as_false(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(TEST_LOCAL_FILE,localFile=False)
        with self.assertRaises(SystemExit) as cm:
            result = cl.read_file()
            print("local file as input and local flag set to false returns success=False")
        #self.assertFalse(result['success'])
    
    def test_file_from_url(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(
            filename=TEST_URL,
            localFile=False
            )
        result = cl.read_file()
        print("Test if file from url works as input")
        self.assertTrue(result['success'])

    def test_url_with_no_local_flag(self):
        """
        Test read funtion should fail if url given with no local flag
        """
        with self.assertRaises(SystemExit) as cm:
            cl = CloseToUs(
                filename=TEST_URL
                )
            result = cl.read_file()
            print("funtion should fail if url given with localFile=True then success=False")
        #self.assertFalse(result['success'])

    def test_file_with_empty_filename(self):
        """
        Test to verify local file read is working
        """
        with self.assertRaises(SystemExit) as cm:
            cl = CloseToUs("")
            
            result = cl.read_file()
            print("If input filename is '' return success=False")
        #self.assertFalse(result['success'])


class TestDecodeJson(unittest.TestCase):
    def test_json_decode_local(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(TEST_LOCAL_FILE)
        result = cl.read_file()
        if result['success']:
            decode_json = cl.decode_json()
        print("Test if decode_json is completed LOCAL: return success=True")
        self.assertTrue(decode_json['success'])
    
    def test_json_decode_url(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(
            filename=TEST_URL,
            localFile=False
        )
        result = cl.read_file()
        if result['success']:
            decode_json = cl.decode_json()
        print("Test if decode_json is completed URL: return success=True")
        self.assertTrue(decode_json['success'])
    
    def test_decoded_data_loaded_url(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(
            filename=TEST_URL,
            localFile=False
        )
        result = cl.read_file()
        if result['success']:
            decode_json = cl.decode_json()
        print("Test if decode_json is completed URL: return success=True")
        self.assertTrue(cl.customers is not None)
    
    def test_decoded_data_loaded_local(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(TEST_LOCAL_FILE)
        result = cl.read_file()
        if result['success']:
            decode_json = cl.decode_json()
        print("Test if decode_json is completed LOCAL: return success=True")
        self.assertTrue(cl.customers is not None)
    
    def test_decoded_data_loaded_local(self):
        """
        Test to verify local file read is working
        """
        cl = CloseToUs(MALFORMED_TEST_LOCAL_FILE)
        result = cl.read_file()
        if result['success']:
            decode_json = cl.decode_json()
        print("Test if decode_json malformed entries are filtered LOCAL: loaded customers count <32")
        self.assertTrue(len(cl.customers) < 32)

class TestCalculations(unittest.TestCase):

    cl = CloseToUs(TEST_LOCAL_FILE)

    def test_distance_calculation(self):
        """
        Test to verify local file read is working
        """
        distance = self.cl.distance(53.339428, -6.257664, 52.986375, -6.043701)
        
        print("Distance calculator works: return true if 42")
        self.assertEqual(distance,42)
    
    def test_distance_calculation_string(self):
        """
        Test to verify local file read is working
        """
        distance = self.cl.distance(53.339428, -6.257664, "52.986375", -6.043701)
        
        print("Distance calculator Works on string input: casts string to float return 42")
        self.assertEqual(distance,42)
    
    def test_closest_customer(self):
        """
        Test to verify local file read is working
        """
        read = self.cl.read_file()
        if read['success']:
            decode = self.cl.decode_json()
            if decode['success']:
                self.cl.closest_customer()
        #distance = self.cl.distance(53.339428, -6.257664, "52.986375", -6.043701)
        
        print("Closest customers: inviting+not_inviting+invalid_json == total entry")
        self.assertEqual(self.cl._inviting+self.cl._not_inviting+self.cl._invalid_json,32)
    
    def test_creates_output_file(self):
        cl = CloseToUs(
            filename=TEST_LOCAL_FILE,
            outfile='test_out.txt'
            )
        result = cl.run()
        
        print("test RUN function to create output file")
        self.assertTrue(path.exists('test_out.txt'))
        remove('test_out.txt')


if __name__ == '__main__':
    unittest.main()