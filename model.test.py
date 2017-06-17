import unittest
from model import PricingEngine
from config import health_conditions, discounts


base_data = {
    'first_name': 'Test User',
    'age': 30,
    'gender': 'female',
    'health_conditions': 'sleep_apnea'
}

edge_data = {
    'first_name': 'Edge Test User',
    'age': 17,
    'gender': 'male',
    'health_conditions': ''
}

base_test = PricingEngine(**base_data)
edge_test = PricingEngine(**edge_data)


class TestModelMethods(unittest.TestCase):

    def test_init(self):
        self.assertEqual(base_test.first_name, 'Test User')
        self.assertEqual(base_test.age, 30)
        self.assertEqual(base_test.gender, 'female')
        self.assertEqual(base_test.health_condition, 'sleep_apnea')

        self.assertEqual(edge_test.first_name, 'Edge Test User')
        self.assertEqual(edge_test.age, 17)
        self.assertEqual(edge_test.gender, 'male')
        self.assertEqual(edge_test.health_condition, '')

    def test_calculate_age_cost(self):
        self.assertEqual(edge_test.calculate_age_cost(), 'Too young for life insurance!')
        self.assertEqual(base_test.calculate_age_cost(), 40)

    def test_calculate_health_condition_multiplier(self):
        self.assertEqual(edge_test.calculate_health_condition_multiplier(), 1)
        self.assertEqual(base_test.calculate_health_condition_multiplier(), 1+health_conditions[base_test.health_condition])

    def test_calculate_gender_discount(self):
        self.assertEqual(edge_test.calculate_gender_discount(), discounts[edge_test.gender])
        self.assertEqual(base_test.calculate_gender_discount(), discounts[base_test.gender])

    def test_calculate_total_cost(self):
        self.assertEqual(edge_test.calculate_total_cost(), 'Too young for life insurance!')
        self.assertEqual(base_test.calculate_total_cost(), '136.40')


if __name__ == '__main__':
    unittest.main()
