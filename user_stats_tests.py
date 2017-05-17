import unittest
import csv
import ast
from user_stats import UserStats

class TestUserStats(unittest.TestCase):
    def setUp(self):
        firms = self.read_csv('firms.csv')
        users = self.read_csv('user-compensation-records.csv')
        self.user_stats = UserStats(users, firms)

    def read_csv(self, filename):
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)

            data = [ row for row in reader ]

            columns = range(len(data[0]))
            return [ { data[0][idx]: self.parse(row[idx]) for idx in columns }  for row in data[1:] ]

    def parse(self, value):
        try:
            return ast.literal_eval(value)
        except:
            return value

    def test_user_889(self):
        input = {"user_id": 889, "firm_id": 2, "title": "Analyst"}
        result = self.user_stats.calculate_stats(input)

        expected = { 'user_id': 889, 'user_base': 114028, 'user_bonus': 180944, 'percentile_base': 43.18181818181818, 'percentile_bonus': 86.36363636363636 }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
