class Car:
    def __init__(self, color):
        self._color = color
        self.__manufacturer = "Ford"

    @property
    def color(self):
        hex_color = '#' + ''.join(f'{val:02X}' for val in self._color)
        return hex_color

    @color.setter
    def color(self, color):
        colors = {'red': (255, 0, 0),
                  'green': (0, 255, 0),
                  'blue': (0, 0, 255),
                  'yellow': (255, 255, 0),
                  'magenta': (255, 0, 255),
                  'cyan': (0, 255, 255),
                  }
        if color in colors:
            self._color = colors[color]
        else:
            raise NameError(f"{color} is not an allowed color")


my_car = Car((255, 0, 0))
print(my_car.color)
my_car.color = 'cyan'
print(my_car.color)