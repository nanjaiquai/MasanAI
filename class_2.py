class Car_name:

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def car_config(self):
        print('car name is {}, color is {}, speed is {}' .format(self.name, self.color, self.speed))


a_car = Car_name('nabi', 'black', '50km')
b_car = Car_name('nero', 'white', '80km')
c_car = Car_name('mimi', 'brown', '120km')

a_car.car_config()
b_car.car_config()
c_car.car_config()

