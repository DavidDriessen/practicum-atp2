import inspect
import time

from Simulator import Simulator
from pygame.threads import Thread


def decorator(function_to_decorate):
    def decorated(*args, **kwargs):
        function_to_decorate(*args, **kwargs)
        # print(i)
        # return i

    return decorated


class Effector:
    def __init__(self, effector):
        self.effector = effector

    def on(self):
        self.effector.switchOn()

    def off(self):
        self.effector.switchOff()

    def is_on(self):
        return self.effector.isOn()


class Sensor:
    def __init__(self, sensor):
        self.sensor = sensor

    def read(self):
        return self.sensor.readValue()


class LCD(Effector):
    def clear(self):
        self.effector._LCD__cursor = (0, 0)
        self.effector.clear()

    def get_lines(self):
        return self.effector.getLines()

    def push_string(self, string):
        self.effector.pushString(string)

class KeyPad(Sensor):
    def pop(self):
        return self.sensor.pop()

class LemonProxy:

    def __init__(self):
        simulator = Simulator(True)  # use Simulator(False) to disable the GUI
        effectors = simulator._Simulator__controller._Controller__effectors
        sensors = simulator._Simulator__controller._Controller__sensors

        self.pumpA = Effector(effectors["pumpA"])
        self.pumpB = Effector(effectors["pumpB"])
        self.valveA = Effector(effectors["valveA"])
        self.valveB = Effector(effectors["valveB"])
        self.heater = Effector(effectors["heater"])
        self.redA = Effector(effectors["redA"])
        self.redB = Effector(effectors["redB"])
        self.greenA = Effector(effectors["greenA"])
        self.greenB = Effector(effectors["greenB"])
        self.greenM = Effector(effectors["greenM"])
        self.yellowM = Effector(effectors["yellowM"])
        self.lcd = LCD(effectors["lcd"])

        self.colour = Sensor(sensors["colour"])
        self.temp = Sensor(sensors["temp"])
        self.level = Sensor(sensors["level"])
        self.presence = Sensor(sensors["presence"])
        self.keypad = KeyPad(sensors["keypad"])
        print(sensors.keys())

        # print(sensors["keypad"].__dict__.keys())
        # print([i[0] for i in inspect.getmembers(sensors["keypad"], predicate=inspect.ismethod)])
        # print(inspect.getfullargspec(sensors["lcd"].pushString)[0])

        process = Thread(target=self.run, args=[simulator])
        process.setDaemon(True)
        process.start()
        simulator.run()

    def run(self, simulator):
        while (True):
            k = self.keypad.pop()
            if k:
                print(k)
            #     self.lcd.push_string(k)
            # time.sleep(5)


if __name__ == "__main__":
    """Only perform actions when invoked directly!"""

    LemonProxy()

    # simulator.run()

    # simulator._Simulator__plant._vessels['mix'].getFluidAmount = decorator(
    #     simulator._Simulator__plant._vessels['mix'].getFluidAmount)

    # simulator._Simulator__controller.update = decorator(simulator._Simulator__controller.update)
    #
    # print(simulator._Simulator__controller._Controller__effectors.keys())
    # print(simulator._Simulator__controller._Controller__sensors.keys())
    # print(inspect.getmembers(simulator._Simulator__controller, predicate=inspect.ismethod))
    #
    # print(simulator._Simulator__controller._Controller__effectors['lcd'].__dict__.keys())
    # print(simulator._Simulator__controller._Controller__effectors['lcd']._LCD__cursor)
    # simulator._Simulator__controller._Controller__effectors['lcd']._LCD__lines[0] = ["H", "a", "l", "l", "o"]
    # print(simulator._Simulator__controller._Controller__effectors['lcd']._LCD__lines)

    # print(simulator.__dict__.keys())
    # print(inspect.getmembers(simulator._Simulator__plant._vessels['mix'], predicate=inspect.ismethod))
    # print(simulator._Simulator__plant._vessels['mix'].getFluidAmount())
    # # print(simulator._Simulator__plant._vessels['a'].__dict__.keys())
    # # print(simulator._Simulator__plant._vessels['b'].__dict__.keys())
    # # print(simulator._Simulator__plant._vessels.__dict__.keys())
    # # print(inspect.getmembers(simulator._Simulator__plant._vessels, predicate=inspect.ismethod))
    # # simulator.run()
    # while(True):
    #     time.sleep(1)
    #     simulator._Simulator__plant.update()
    #     simulator._Simulator__controller.update()
    #     simulator._Simulator__monitor.update()
    #     # simulator._Simulator__gui.update()
    #     # print(simulator._Simulator__plant._vessels['mix'].getFluidAmount())
    #     # print(simulator._Simulator__plant._vessels['a'].getFluidAmount())
    #     # print(simulator._Simulator__plant._vessels['b'].getFluidAmount())
