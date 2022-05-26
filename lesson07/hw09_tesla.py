class Tesla:
    tesla_class_attr = "electrocar"

    def __init__(self,
                 obj_attr_car_name,
                 obj_attr_car_acceleration,
                 current_speed
                 ):
        if type(obj_attr_car_name) is not str:
            raise TypeError("obj_attr_car_name must be str, received value:"
                             f"{obj_attr_car_name}")
        elif not obj_attr_car_name:
            raise ValueError("obj_attr_car_name must contain one or more letter, it cannot be empty string")
        else:
            self.obj_attr_car_name = obj_attr_car_name

        if type(obj_attr_car_acceleration) is not int:
            raise TypeError("obj_attr_car_acceleration must be int, received value:"
                             f"{obj_attr_car_acceleration}")
        elif obj_attr_car_acceleration <= 0:
            raise ValueError(f"obj_attr_car_acceleration cannot be lte 0, received value:"
                             f"{obj_attr_car_acceleration}")
        else:
            self.obj_attr_car_acceleration = obj_attr_car_acceleration

        self._current_speed = current_speed # property, see below

    def raise_speed(self):
        """
        Raises speed of the car
        :return: speed after raising it
        """
        self._current_speed += self.obj_attr_car_acceleration

    def reduce_speed(self):
        """
        Reduces speed of the car
        :return: speed after reducing it
        """
        self._current_speed -= self.obj_attr_car_acceleration

    @property
    def current_speed(self) -> int:
        """
        Getter for current velocity
        :return: current_velocity parameter
        """
        return self._current_speed

    @current_speed.setter
    def current_speed(self, speed_from_user: int):
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
            self._current_speed = speed_from_user

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
            if self._current_speed < car_speed_goal:
                increase = round(car_speed_goal / self._current_speed, 1)
                print(f'You should increase speed in {increase} times')
                return increase
            elif self._current_speed > car_speed_goal:
                decrease = round(self._current_speed / car_speed_goal, 1)
                print(f'You should decrease speed by {decrease} times')
                return decrease
            else:
                print("Current speed equals to speed goal")
                return self._current_speed


car = Tesla(obj_attr_car_name="Banana", obj_attr_car_acceleration=3, current_speed=45)
attr = car.tesla_class_attr
print(f'Class attr -> {attr}')
car.raise_speed()
print(f'speed after increasing {car.current_speed}')
car.reduce_speed()
print(f'speed after reducing {car.current_speed}')
car.current_speed = 66
print(f"{car.current_speed} - speed after setting it by user")
car.calculate_speed_adjust(90)
print("---END--")
