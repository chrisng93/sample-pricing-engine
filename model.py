from config import base_cost, base_cost_age_gap, base_cost_increase, health_conditions, discounts


# Pricing model with separate methods for calculating each section of the pricing model
class PricingEngine():

    def __init__(self, first_name, age, gender, health_conditions):
        self.first_name = first_name
        self.age = int(age)
        self.gender = gender.lower()
        self.health_condition = health_conditions.replace(' ', '_').lower()

    def calculate_age_cost(self):
        if self.age < 18:
            return 'Too young for life insurance!'
        return (self.age-18)/base_cost_age_gap*base_cost_increase

    def calculate_health_condition_multiplier(self):
        multiplier = 0
        if self.health_condition in health_conditions:
            multiplier = health_conditions[self.health_condition]
        return 1+multiplier

    def calculate_gender_discount(self):
        return discounts[self.gender]

    def calculate_total_cost(self):
        if self.age < 18:
            return 'Too young for life insurance!'
        cost = base_cost
        cost += self.calculate_age_cost()
        cost *= self.calculate_health_condition_multiplier()
        cost -= self.calculate_gender_discount()
        return '{:.2f}'.format(cost)

    def print_cost(self):
        print('%s - $%s' % (self.first_name, self.calculate_total_cost()))
