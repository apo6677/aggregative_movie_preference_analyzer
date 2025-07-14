import unittest
from Unit_testing_phase import find_movies_between_T1_T2, find_top_movies, find_user_pairs, dominance, iceberg, top_users



class Test_find_movies_between_T1_T2(unittest.TestCase):
    def test_check_outcome(self):
        with open("rating_4.9_5.0.txt", "r", encoding="utf-8") as searched_ratings:
            self.assertEqual(find_movies_between_T1_T2(4.9, 5.0, 0), searched_ratings.read())



class Test_find_top_movies(unittest.TestCase):
    def test_check_outcome(self):
        with open("top_movies_1.txt", "r", encoding="utf-8") as searched_ratings:
            self.assertEqual(find_top_movies(1, 0), searched_ratings.read())



class Test_find_user_pairs(unittest.TestCase):
    def test_check_outcome(self):
        with open("user_pairs_1.txt", "r", encoding="utf-8") as searched_ratings:
            self.assertEqual(find_user_pairs(1, 0), searched_ratings.read())



class Test_dominance(unittest.TestCase):
    def test_check_outcome(self):
        with open("dominance.txt", "r", encoding="utf-8") as searched_ratings:
            self.assertEqual(dominance(0), searched_ratings.read())



class Test_top_users(unittest.TestCase):
    def test_check_outcome(self):
        with open("top_user_1.txt", "r", encoding="utf-8") as searched_ratings:
            self.assertEqual(top_users(1, 0), searched_ratings.read())



class Test_iceberg(unittest.TestCase):
    def test_check_outcome(self):
        with open("iceberg_100_4.0.txt", "r", encoding="utf-8") as searched_ratings:
            self.assertEqual(iceberg(100, 4.0,0), searched_ratings.read())

if __name__ == "__main__":
    unittest.main()
