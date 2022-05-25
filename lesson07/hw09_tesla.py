class Tesla:
    tesla_class_attr = "electrocar"

    def __init__(self,
                 obj_attr_car_name,
                 obj_attr_car_acceleration,
                 obj_property_current_velocity
                 ):
        if type(obj_attr_car_name) is not str:
            raise TypeError("obj_attr_car_name must be str, received value:"
                             f"{obj_attr_car_name}")
        elif not obj_attr_car_name:
            raise ValueError("obj_attr_car_name must contain one or more letter, it cannot be empty string")
        else:
            self.car_name = obj_attr_car_name

        if type(obj_attr_car_acceleration) is not int:
            raise TypeError("obj_attr_car_acceleration must be int, received value:"
                             f"{obj_attr_car_acceleration}")
        elif obj_attr_car_acceleration <= 0:
            raise ValueError(f"obj_attr_car_acceleration cannot be lte 0, received value:"
                             f"{obj_attr_car_acceleration}")
        else:
            self.car_acceleration = obj_attr_car_acceleration

        self.set_speed = obj_property_current_velocity


    def raise_speed(self):
        """
        Raises speed of the car
        :return: speed after raising it
        """
        self.current_velocity += self.car_acceleration

    def reduce_speed(self):
        """
        Reduces speed of the car
        :return: speed after reducing it
        """
        self.current_velocity -= self.car_acceleration

    @property
    def set_speed(self) -> int:
        """
        Getter for current velocity
        :return: current_velocity parameter
        """
        return self.current_velocity

    @set_speed.setter
    def set_speed(self, speed_from_user: int):
        """
        Setter for current velocity
        :param speed_from_user: speed to be set as current
        :return:
        """
        if type(speed_from_user) is not int:
            raise TypeError("obj_property_current_velocity must be int, received value:"
                             f"{speed_from_user}")
        elif speed_from_user <= 0:
            raise ValueError(f"obj_property_current_velocity cannot be lte 0, received value:"
                             f"{speed_from_user}")
        else:
            self.current_velocity = speed_from_user

    def calculate_speed_adjust(self, car_speed_goal: int) -> float:
        """
        Calculates how many times should be increases/decreased velocity to
        reach car_speed_goal parameter
        :param car_speed_goal:
        :return: how many times should be increases/decreased velocity to
        reach car_speed_goal parameter
        """
        if type(car_speed_goal) is not int:
            raise TypeError(f"car_speed_goal must be of int type")
        elif car_speed_goal <= 0:
            raise ValueError(f"car_speed_goal should be gte 0")
        else:
            if self.current_velocity < car_speed_goal:
                increase = round(car_speed_goal / self.current_velocity, 1)
                print(f'You should increase speed in {increase} times')
                return increase
            elif self.current_velocity > car_speed_goal:
                decrease = round(self.current_velocity / car_speed_goal, 1)
                print(f'You should decrease speed by {decrease} times')
                return decrease
            else:
                return self.current_velocity


car = Tesla(obj_attr_car_name = "Banana", obj_attr_car_acceleration = 3, obj_property_current_velocity = 45)
attr = car.tesla_class_attr
print(f'Class attr -> {attr}')
car.raise_speed()
print(f'speed after increasing {car.set_speed}')
car.reduce_speed()
print(f'speed after reducing {car.set_speed}')
car.set_speed = 66
print(f"{car.set_speed} - speed after setting it by user")
car.calculate_speed_adjust(90)
print("---END--")
