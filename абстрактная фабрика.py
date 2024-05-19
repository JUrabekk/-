# Абстрактная фабрика
class CarFactory:
    def produce_electric_car(self):
        pass

    def produce_petrol_car(self):
        pass

    def produce_hybrid_car(self):
        pass

# Конкретные фабрики
class ElectricCarFactory(CarFactory):
    def produce_electric_car(self):
        return ElectricCar()

    def produce_petrol_car(self):
        return None

    def produce_hybrid_car(self):
        return None

class PetrolCarFactory(CarFactory):
    def produce_electric_car(self):
        return None

    def produce_petrol_car(self):
        return PetrolCar()

    def produce_hybrid_car(self):
        return None

class HybridCarFactory(CarFactory):
    def produce_electric_car(self):
        return None

    def produce_petrol_car(self):
        return None

    def produce_hybrid_car(self):
        return HybridCar()

# Абстрактный класс Car
class Car:
    def drive(self):
        pass

# Конкретные классы автомобилей
class ElectricCar(Car):
    def drive(self):
        print("Driving an electric car.")

class PetrolCar(Car):
    def drive(self):
        print("Driving a petrol car.")

class HybridCar(Car):
    def drive(self):
        print("Driving a hybrid car.")

# Использование фабрик
electric_factory = ElectricCarFactory()
petrol_factory = PetrolCarFactory()
hybrid_factory = HybridCarFactory()

electric_car = electric_factory.produce_electric_car()
petrol_car = petrol_factory.produce_petrol_car()
hybrid_car = hybrid_factory.produce_hybrid_car()

electric_car.drive()
petrol_car.drive()
hybrid_car.drive()
