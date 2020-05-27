import unittest
import api_calls

class SimpleTest(unittest.TestCase):
    def test_early_date_weather(self):
        date = "2019-02-10"
        response = api_calls.get_weather(date)
        self.assertEqual(response[0],"Please give a valid date.","Early date control failed")

    def test_input_format_weather(self):
        date = "1234567890"
        response = api_calls.get_weather(date)
        self.assertEqual(response[0],"Wrong input format","Input format test failed")


    def test_output_format_weather(self):
        date = "2020-05-25"
        response = api_calls.get_weather(date)
        articleFileds = ["columns","locations"]
        result = True
        for (keys,fields) in zip(response,articleFileds):
            if not keys in articleFileds:
                result=False
            if not fields in response:
                result=False
        self.assertTrue(result,"wrong format")

    def test_output_format_weather_today(self):
        response = api_calls.get_weather_today()
        articleFileds = ["columns","locations"]
        result = True
        for (keys,fields) in zip(response,articleFileds):
            if not keys in articleFileds:
                result=False
            if not fields in response:
                result=False
        self.assertTrue(result,"wrong format")

    def test_forward_date_weather(self):
        date = "2022-08-18"
        response = api_calls.get_weather(date)
        self.assertEqual(response[0], "Please give a valid date.", "Late date control failed")




if(__name__ == "__main__"):
    unittest.main()