import random
class Service:
    def __init__(self, land):
        self.land = land()

    def update_year(self, acres_to_buy_or_sell, units_to_feed, acres_to_plant):
        """
        This function updates the year and the land's attributes
        :param acres_to_buy_or_sell: an integer representing the number of acres to buy or sell
        :param units_to_feed: an integer representing the number of units to feed the people
        :param acres_to_plant: an integer representing the number of acres to plant
        :return: "game over, more than half people starved" if more than half people starved
        """

        # increase the year
        self.land.year += 1

        # for point 3
        if acres_to_buy_or_sell >=0:
            self.land.acres += acres_to_buy_or_sell
            self.land.grain_stocks -= acres_to_buy_or_sell*self.land.land_price_per_acre
        else:
            self.land.acres -= acres_to_buy_or_sell
            self.land.grain_stocks += acres_to_buy_or_sell*self.land.land_price_per_acre

        self.land.land_price_per_acre = random.randint(15, 25)

        # for point 4
        if units_to_feed*20 < self.land.number_people * 20:
            self.land.starved_people = (self.land.number_people * 20 - units_to_feed*20) // 20

            if self.land.starved_people > self.land.number_people // 2:
                return "game over, more than half people starved"
            self.land.number_people -= self.land.starved_people

        else:
            self.land.new_people += random.randint(1, 10)
            self.land.number_people += self.land.new_people

        self.land.grain_stocks -= units_to_feed




        # for point 5
        self.land.acres += acres_to_plant
        if self.land.number_people * 10 <= self.land.acres:
            self.land.grain_stocks += self.land.number_people * 10 * self.land.unit_per_acre
        else:
            self.land.grain_stocks += self.land.acres * self.land.unit_per_acre

        self.land.unit_per_acre = random.randint(1, 6)

        # for point 6
        rat_infestation_chance = random.randint(1, 10)
        if rat_infestation_chance == 1 or rat_infestation_chance == 2:
            percent = random.randint(1, 10)
            self.land.rats_ate_units = (percent // 100) * self.land.grain_stocks
            self.land.grain_stocks -= self.land.rats_ate_units

        # if everything is ok, return "ok"
        return "ok"



