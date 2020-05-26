import unittest
import api_calls
class SimpleTest(unittest.TestCase):
    def test_early_date_nasa(self):
        date = "2019-03-17"
        response = api_calls.get_nasa_news(date)
        self.assertEqual(response[0],"Please give a valid date.","Early date control failed")
    #news
    def test_early_date_news(self):
        date = "2019-03-17"
        response = api_calls.get_news(date)
        self.assertEqual(response[0],"Please give a valid date.","Early date control failed")

    def test_input_format_nasa(self):
        date = "1234567890"
        response = api_calls.get_nasa_news(date)
        self.assertEqual(response[0],"Wrong input format","Input format test failed")

    def test_input_format_news(self):
        date = "1234567890"
        response = api_calls.get_news(date)
        self.assertEqual(response[0],"Wrong input format","Input format test failed")

    def test_output_format_nasa(self):
        date = "2020-05-25"
        response = api_calls.get_nasa_news(date)
        articleFileds = ["author","content","description","publishedAt","source","title","url","urlToImage"]
        result = True
        for (keys,fields) in zip(response[0],articleFileds):
            if not keys in articleFileds:
                result=False
            if not fields in response[0]:
                result=False 
        self.assertTrue(result,"wrong format")

    def test_output_format_news(self):
        date = "2020-05-25"
        response = api_calls.get_news(date)
        articleFileds = ["author","content","description","publishedAt","source","title","url","urlToImage"]
        result = True
        for (keys,fields) in zip(response[0],articleFileds):
            if not keys in articleFileds:
                result=False
            if not fields in response[0]:
                result=False 
        self.assertTrue(result,"wrong format")


if(__name__ == "__main__"):
    unittest.main()

# 1 ay 1 gün öncesi fırat
# ileri tarih fırat
# input formatı date değil ibrahim
# output format ibrahim
