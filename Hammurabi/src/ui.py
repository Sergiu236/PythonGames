class UI:
    def __init__(self, service):
        self.service = service

    def ui(self):
        while True:
            print(f"In year {self.service.land.year}, {self.service.land.starved_people} people starved")
            print(f"{self.service.land.new_people} people came to the city")
            print(f"City population is {self.service.land.number_people}")
            print(f"City owns {self.service.land.acres} acres of land")
            print(f"Harvest was {self.service.land.unit_per_acre} units per acre")
            print(f"Rats ate {self.service.land.rats_ate_units} units")
            print(f"Land price is {self.service.land.land_price_per_acre} units per acre")
            print(f"Grain stocks are {self.service.land.grain_stocks} units")
            print("\n")

            if self.service.land.year + 1 == 6:
                if self.service.land.number_people > 100 and self.service.land.acres > 1000:
                    print("Congratulations, you won!")
                    break
                else:
                    print("GAME Over! You didn't do well!")
                    break

            try:
                acres_to_buy_or_sell = int(input("How many acres to buy/sell? "))
                if acres_to_buy_or_sell >= 0:
                    if acres_to_buy_or_sell * self.service.land.land_price_per_acre > self.service.land.grain_stocks:
                        # to raise an exception
                        raise ValueError
                else:
                    if abs(acres_to_buy_or_sell) > self.service.land.acres:
                        # to raise an exception
                        raise ValueError

                units_to_feed = int(input("How many units to feed the people? "))
                if units_to_feed > self.service.land.grain_stocks:
                    # to raise an exception
                    raise ValueError

                acres_to_plant = int(input("How many acres to plant? "))
                print("\n")
                if acres_to_plant > self.service.land.acres:
                    # to raise an exception
                    raise ValueError


                consequence = self.service.update_year(acres_to_buy_or_sell, units_to_feed, acres_to_plant)
                if consequence == "game over, more than half people starved":
                    print(consequence)
                    break
                elif consequence == "ok":
                    continue
            except ValueError as e:
                print("Invalid input, try again")
                continue
