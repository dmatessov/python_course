class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        cases = ['string', 1.5]
        for x in cases:
            with self.subTest(case=x):
                with self.assertRaises(TypeError):
                    factorize(x)

    def test_negative(self):
        cases = [-1, -10, -100]
        for x in cases:
            with self.subTest(case=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        cases = [0, 1]
        for x in cases:
            with self.subTest(case=x):
                self.assertEqual((x,), factorize(x))

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        for x in cases:
            with self.subTest(case=x):
                self.assertEqual((x,), factorize(x))

    def test_two_simple_multipliers(self):
        cases = [[6, (2, 3)], [26, (2, 13)], [121, (11, 11)]]
        for x in cases:
            with self.subTest(case=x[0]):
                self.assertCountEqual(x[1], factorize(x[0]))

    def test_many_multipliers(self):
        cases = [
            [1001, (7, 11, 13)],
            [9699690, (2, 3, 5, 7, 11, 13, 17, 19)]
        ]
        for x in cases:
            with self.subTest(case=x[0]):
                self.assertCountEqual(x[1], factorize(x[0]))

def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass