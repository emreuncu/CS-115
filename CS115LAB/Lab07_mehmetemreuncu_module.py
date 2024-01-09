class Cab:
    def __init__(self, cab_type, kms, year):
        self.__cab_type = cab_type
        self.__kms = kms
        self.__year = year

    def get_type(self):
        return self.__cab_type

    def get_kms(self):
        return self.__kms

    def get_year(self):
        return self.__year

    def __gt__(self, other):
        if self.get_type() == other.get_type():
            return other.get_year() > self.get_year()

    def __eq__(self, other):
        if self.get_year() == other.get_year() and self.get_type() == other.get_type():
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__cab_type}, {self.get_kms()}, {self.__year}\n"


class Sedan(Cab):
    def __init__(self, cab_type, kms, year, price_per_km=2.5):
        super().__init__(cab_type, kms, year)
        self.__price_per_km = price_per_km

    def get_price(self):
        return self.__price_per_km

    def calculate_fare(self):
        return self.get_price() * self.get_kms()


class Hatchback(Cab):
    def __init__(self, cab_type, kms, year, price_per_km=2.2):
        super().__init__(cab_type, kms, year)
        self.__price_per_km = price_per_km

    def get_price(self):
        return self.__price_per_km

    def calculate_fare(self):
        return self.get_price() * self.get_kms()
