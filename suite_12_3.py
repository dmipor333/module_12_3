import unittest
import tests_12_3

sport = unittest.TestSuite()
sport.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
sport.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

sports = unittest.TextTestRunner(verbosity=2)
sports.run(sport)