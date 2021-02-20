# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


number = 6
float_point = 1.6

string = "this is a string"

array = ['a', 'b', 'c', 'd', 'e', '3']

array2 = [9, 1.2, 2, 3, 7, 5, 6]

the_number_i_want = array[3]


class FancyPrinter:
    def __init__(self, banner="This is the default banner"):
        self.banner = banner

    def print_out(self, message="this is the default message"):
        print(self.banner)
        print("The message is : {0}".format(message))

    def __del__(self):
        print("I'm dying")


class FancierPrinter(FancyPrinter):
    def even_fancier_print(self, message):
        self.print_out(message)

    def print_out(self, message):
        super(self)



FP = FancyPrinter()
FP.print_out()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
