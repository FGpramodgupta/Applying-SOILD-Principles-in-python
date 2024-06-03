'''
SOLID Design Principles
The 5 that represent SOLID are the most crucial ones a software developer should know.

Liskov Substitution Principle
    A derived class can assume the place of its super class, and everything should work
'''

class KitchenAppliance():
    """
    Represents a kitchen appliance.

    Methods:
    - on(): Turns on the kitchen appliance.
    - off(): Turns off the kitchen appliance.
    - set_temperature(): Sets the temperature of the kitchen appliance.
    """
    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self):
        pass

class Toaster (KitchenAppliance):

    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self):
        pass


## Till here Above example follow Liskov subsitution Principle

class Juicer (KitchenAppliance):

    def on(self):
        pass

    def off(self):
      pass

    ## But Juicer does not have temparature feature
    ## it will give error when not implementated in subclass
    def set_temperature(self):
        pass

## solution

class KitchenAppliance():

    def on(self):
        pass

    def off(self):
        pass

class KitchenAppliancewithTemp(KitchenAppliance):

    def set_temperature(self):
        pass

class Toaster (KitchenAppliancewithTemp):

    def on(self):
        #Turn on Toaster
        pass

    def off(self):
        #Turn off Toaster
        pass

    def set_temperature(self):
        #Set temp on Toaster
        pass

class Juicer(KitchenAppliance):

    def on(self):
        #Turn on Toaster
        pass

    def off(self):
        #Turn off Toaster
        pass
