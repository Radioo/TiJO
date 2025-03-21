from abc import ABC, abstractmethod

class IWorkable(ABC):
    @abstractmethod
    def work(self):
        pass

class IEatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(IWorkable, IEatable):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")

class RobotWorker(IWorkable):
    def work(self):
        print("Robot worker working")

# Usage
human = HumanWorker()
robot = RobotWorker()

human.work()  # Works!
human.eat()  # Works!
robot.work()  # Works!
# robot.eat() is not available, which is good!