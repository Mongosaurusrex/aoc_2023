import os


class DayFive:
    def __init__(self, puzzle_repository):
        self.input = puzzle_repository.get_and_save_puzzle_from_day_with_raw_data(
            os.path.abspath("calendar/five/input.txt"), 5
        )

    def split_title(self, raw_map: str) -> list:
        return raw_map.split("\n")[1:]

    def split_numbers(self, map_numbers: str) -> list:
        result = []
        for x in map_numbers:
            new_array_to_add = []
            for y in x.split(" "):
                new_array_to_add.append(int(y))
            result.append(new_array_to_add)
        return result

    def convert_value_through_map(self, value: int, map: list) -> int:
        diff = 0
        found_in_map = False
        for item in map:
            from_nr = item[1]
            to_nr = item[1] + item[2] - 1  # Potential error where
            if value in range(from_nr, to_nr):
                diff = (value - item[1]) + item[0]
                found_in_map = True
                return diff

        return value

    def solution(self) -> None:
        print("~~ Day five ~~")

        (
            seeds,
            seed_to_soil_map,
            soil_to_fertilizer,
            fertilizer_to_water,
            water_to_light,
            light_to_temperature,
            temperature_to_humidity,
            humidity_to_location,
        ) = tuple(self.input.split("\n\n"))
        seeds = [int(x) for x in seeds.split(":")[1].split(" ")[1:]]
        seed_to_soil_map = self.split_numbers(self.split_title(seed_to_soil_map))
        soil_to_fertilizer = self.split_numbers(self.split_title(soil_to_fertilizer))
        fertilizer_to_water = self.split_numbers(self.split_title(fertilizer_to_water))
        water_to_light = self.split_numbers(self.split_title(water_to_light))
        light_to_temperature = self.split_numbers(
            self.split_title(light_to_temperature)
        )
        temperature_to_humidity = self.split_numbers(
            self.split_title(temperature_to_humidity)
        )
        humidity_to_location = self.split_numbers(
            self.split_title(humidity_to_location)
        )
        result_dict_a = {seed: None for seed in seeds}

        for seed in seeds:
            soil = self.convert_value_through_map(seed, seed_to_soil_map)
            fertilizer = self.convert_value_through_map(soil, soil_to_fertilizer)
            water = self.convert_value_through_map(fertilizer, fertilizer_to_water)
            light = self.convert_value_through_map(water, water_to_light)
            temperature = self.convert_value_through_map(light, light_to_temperature)
            humidity = self.convert_value_through_map(
                temperature, temperature_to_humidity
            )
            location = self.convert_value_through_map(humidity, humidity_to_location)

            result_dict_a[seed] = location

        print("A", min(result_dict_a.values()))
        """
        DO NOT RUN, SLOW AND NAIVE
        result_dict_b = {seed: None for seed in seeds}

        seed_b = []
        for index, seed in enumerate(seeds[::2]):
            for num in range(seed, seed + seeds[1::2][index]):
                seed_b.append(num)

        for seed_b in seeds:
            soil = self.convert_value_through_map(seed, seed_to_soil_map)
            fertilizer = self.convert_value_through_map(soil, soil_to_fertilizer)
            water = self.convert_value_through_map(fertilizer, fertilizer_to_water)
            light = self.convert_value_through_map(water, water_to_light)
            temperature = self.convert_value_through_map(light, light_to_temperature)
            humidity = self.convert_value_through_map(
                temperature, temperature_to_humidity
            )
            location = self.convert_value_through_map(humidity, humidity_to_location)

            result_dict_b[seed] = location

        print("B", min(result_dict_b.values()))
        """
