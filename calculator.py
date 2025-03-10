# remember, in Python classes are easier to use than Java.
#
import math
from math import nan
from math import *


class Calculator:

    def __init__(self):
        self.currentValue = 0.0
        self.currentMsg = ""
        self.stored_value = 0.0
        self.trigUnitMode='degrees'     #my code

    def switchUnitsMode(self, uMode = 'none'):  #my code
        if uMode == 'none':
            if self.trigUnitMode =='degrees':
                self.trigUnitMode  = 'radians'
            else:
                self.trigUnitMode = 'degrees'
        else:
            self.trigUnitMode=uMode

    def set_value(self):
        if self.currentValue == 0.0:
            x = float(input("Enter a value:"))
            self.currentValue = x

    def getTrigUnitMode(self):
        return self.trigUnitMode
    def __str__(self):
        return str(self.currentValue)

    def set_value(self, user_in): # chris' code
        try:
            self.currentValue = float(user_in)
                 # x = float(input("Enter a number:"))
               # self.currentValue = x
        except ValueError:
                print("nan")
                self.set_value(input("Enter a number: "))

    # def set_value(self): # chris' code
    #        try:
     #           if self.currentValue == 0.0:
      #              x = float(input("Enter a number:"))
       #             self.currentValue = x
        #    except ValueError:
         #       print("Please enter a number")
          #      self.set_value()




    def clear(self):
        self.currentValue = 0.0

    def value(self):
        return self.currentValue

    # evaluation routines
    def add(self, x, y):
        self.currentValue = x + y
        return self.currentValue

    def sub(self, x, y):
        self.currentValue = x - y
        return self.currentValue

    def mul(self, x, y):
        self.currentValue = x * y
        return self.currentValue

    def div(self, x, y):
        try:
            value = x / y
            self.currentValue = value
            return self.currentValue
        except ZeroDivisionError:
            self.currentValue = None
            self.currentMsg = 'DIV BY ZERO'

    def square(self):   #my code
        self.currentValue = self.currentValue * self.currentValue
        return self.currentValue

    def square_root(self, x):  #my code
        self.currentValue = math.sqrt(x)
        return self.currentValue

    def factorial(self, x):
        if self.currentValue >=0:
            self.currentValue = math.factorial(x)
            return self.currentValue
        else:
            for i in range(int(self.currentValue)+1, 1):
                self.currentValue *= float(i)

    def common_log(self, x):
        try:
            self.currentValue = math.log10(x)
            return self.currentValue
        except ValueError:
            if x <= 0:
                self.currentValue = None
                self.currentMsg = 'NEG NUM ERROR'

    def inverse_common_log(self, x):
        self.currentValue = math.pow(10, x)
        return self.currentValue

    def multiplicative_inverse(self):
        try:
            self.currentValue = 1 / self
            return self.currentValue
        except ZeroDivisionError:
            if self == 0:
                self.currentValue = None
                self.currentMsg = 'DIV BY ZERO'

    def inverse_of_number(self, x):
        try:
            if self != 0:
                self.currentValue = self.currentValue - (x * 2) #couldn't get this to work -chris abs(self)
                return self.currentValue
        except ValueError:
            if self == 0:
                self.currentValue = None
                self.currentMsg = 'ZERO INVALID'

    def save_to_memory(self):
        self.stored_value = self.currentValue

    def reset_memory(self):
        self.stored_value = 0.0

    def recall_from_memory(self):
        self.currentValue = self.stored_value

    def get_sin(self, x):
        self.currentValue = sin(x)
        return self.currentValue

    def get_cos(self, x):
        self.currentValue = cos(x)
        return self.currentValue

    def get_tan(self, x):
        self.currentValue = tan(x)
        return self.currentValue

    def get_asin(self, x):
        try:
            self.currentValue = asin(x)
            return self.currentValue
        except ValueError:
            while True:
                self.currentValue = input("Enter a number: between -1 and 1: ")
                if -1 < float(self.currentValue) < 1:
                    return asin(float(self.currentValue))

    def get_acos(self, x):
        self.currentValue = acos(x)
        return self.currentValue
    def get_atan(self, x):

        self.currentValue = atan(x)
        return self.currentValue

    def nat_log(self, x):
        self.currentValue = log(x)
        return self.currentValue

    def in_nat_log(self, x):
        self.currentValue = exp(x)
        return self.currentValue

    def displayModeBin(self):
        self.currentValue = bin(int(self.currentValue))
        #return ("The decimal value of", displayMode, "is:" + bin(displayMode), "in binary.")

    def displayModeOct(self):
        self.currentValue = oct(int(self.currentValue))
        #return ("The decimal value of", displayMode, "is:"+ float(oct(displayMode)), "in octal.")
    #
    def displayModeHex(self):
#        self.currentValue = hex(x)
        return hex(int(self.currentValue))

    # def displayModeDec(self):
    #     self.currentValue = dec(int(self.currentValue))
    #     #return ("The decimal value of", displayMode, "is:" + float(dec(displayMode)), "in decimal.")



# add lots more methods to this calculator class.
