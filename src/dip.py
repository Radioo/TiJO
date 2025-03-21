from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Light(Device):
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

class Fan(Device):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan is stopped")

class Button:
    def __init__(self, device: Device):
        self._device = device

    def press(self):
        self._device.turn_on()

# Usage
light = Light()
light_button = Button(light)
light_button.press()

# Now we can also use it with a fan
fan = Fan()
fan_button = Button(fan)
fan_button.press()