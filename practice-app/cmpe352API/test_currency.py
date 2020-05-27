import unittest
import api_calls

class SimpleTest(unittest.TestCase):
    def test_early_date_currency(self):
        date = "1999-02-10"
        response = api_calls.get_currencies(date)
        self.assertEqual(response["error"],"Base 'TRY' is not supported.","Early date control failed")

    def test_input_format_currency(self):
        date = "1234567890"
        response = api_calls.get_currencies(date)
        self.assertEqual(response["error"],"time data '1234567890' does not match format '%Y-%m-%d'","Input format test failed")


    def test_output_format_currency(self):
        date = "2020-05-25"
        response = api_calls.get_currencies(date)
        fields = ["base","date","rates"]
        result = True
        for field in fields:
            if response.get(field) is None:
                result= False
        self.assertTrue(result,"wrong format")

    def test_output_format_currency_today(self):
        response = api_calls.get_currenciesToday()
        fields = ["base","date","rates"]
        result = True
        for field in fields:
            if response.get(field) is None:
                result= False
        self.assertTrue(result,"wrong format")


    def test_forward_date_currency(self):
        date = "2022-08-18"
        response = api_calls.get_currencies(date)
        self.assertTrue(not (response["date"] == date),"Invalid future date control failed.")


if(__name__ == "__main__"):
    unittest.main()
