from imghdr import what
import urllib.request
import json
import unittest

from unittest.mock import patch
from io import StringIO


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)

def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


class TestCurrentYear(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_current_response(self, mock_get):
        mock_get.return_value.__enter__.return_value = StringIO('{"$id":"1",\
            "currentDateTime":"2022-10-11T06:29Z","utcOffset":"00:00:00",\
            "isDayLightSavingsTime":false,"dayOfTheWeek":"Tuesday","timeZoneName":"UTC",\
            "currentFileTime":133099433939589211,"ordinalDate":"2022-284","serviceResponse":null}')
        self.assertEqual(what_is_year_now(), 2022)

    @patch('urllib.request.urlopen')
    def test_other_format(self, mock_get):
        mock_get.return_value.__enter__.return_value = StringIO('{"$id":"1",\
            "currentDateTime":"11.10.2022T06:29Z","utcOffset":"00:00:00",\
            "isDayLightSavingsTime":false,"dayOfTheWeek":"Tuesday","timeZoneName":"UTC",\
            "currentFileTime":133099433939589211,"ordinalDate":"2022-284","serviceResponse":null}')
        self.assertEqual(what_is_year_now(), 2022)

    @patch('urllib.request.urlopen')
    def test_past(self, mock_get):
        mock_get.return_value.__enter__.return_value = StringIO('{"$id":"1",\
            "currentDateTime":"2019-03-01T06:29Z","utcOffset":"00:00:00",\
            "isDayLightSavingsTime":false,"dayOfTheWeek":"Tuesday","timeZoneName":"UTC",\
            "currentFileTime":133099433939589211,"ordinalDate":"2022-284","serviceResponse":null}')
        self.assertEqual(what_is_year_now(), 2019)

    @patch('urllib.request.urlopen')
    def test_invalid(self, mock_get):
        mock_get.return_value.__enter__.return_value = StringIO('{"$id":"1",\
            "currentDateTime":"Not a real date","utcOffset":"00:00:00",\
            "isDayLightSavingsTime":false,"dayOfTheWeek":"Tuesday","timeZoneName":"UTC",\
            "currentFileTime":133099433939589211,"ordinalDate":"2022-284","serviceResponse":null}')
        with self.assertRaises(ValueError) as ex:
            what_is_year_now()

if __name__ == '__main__':
    unittest.main()