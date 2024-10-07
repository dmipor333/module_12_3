import runner
import unittest
import runner_and_tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        item_walk = runner.Runner('Ran1')
        for i in range(10):
            item_walk.walk()
        self.assertEqual(item_walk.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        item_run = runner.Runner('Ran2')
        for i in range(10):
            item_run.run()
        self.assertEqual(item_run.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        item1 = runner.Runner('Ran3')
        item2 = runner.Runner('Ran4')
        for i in range(10):
            item1.walk()
            item2.run()
        self.assertNotEqual(item1.distance, item2.distance)


class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усейн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        first_run = runner_and_tournament.Tournament(90, self.usain, self.nik)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        second_run = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        third_run = runner_and_tournament.Tournament(90, self.andrey, self.usain,
                                                         self.nik)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

if __name__ == '__main__':
    unittest.main()