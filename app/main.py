class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: [Car]) -> float:
        income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:

        income = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * self.average_rating / self.distance_from_city_center)
        return income

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        total = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)


car_wash_station = CarWashStation(6, 7, 3.9, 11)
car_list = [Car(3, 3, "BMW"), Car(4, 5, "Audi"), Car(7, 1, "Mercedes")]
car_wash_station.serve_cars(car_list)
