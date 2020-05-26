import unittest
import api_calls
class SimpleTest(unittest.TestCase):
    def test_early_date(self):
        date = "2019-03-17"
        response = api_calls.get_nasa_news(date)
        self.assertEqual(response[0],"Please give a valid date.","Early date control failed")
    #news

if(__name__ == "__main__"):
    unittest.main()

# 1 ay 1 gün öncesi fırat
# ileri tarih fırat
# input formatı date değil ibrahim
# output format ibrahim
