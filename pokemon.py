""" actually trying out class inheritance """


class Pokemon():
    """ pocket monsters """

    def __init__(self, species, element):
        self.species = species
        self.element = element

    def print_info(self):
        """ prints relevant info """
        print(self.species, self.element)

    def add_info(self, field):
        """ adds properties to pokemon """
        self.field = field


class Animal(Pokemon):
    """ pokemon are animals too """
    def __init__(self, *args, **kwargs):
        Pokemon.__init__(self, species, element)
        self.mammal = mammal




def main():
    """ main function """
    pikachu = Pokemon('pikachu', 'electric')
    pikachu.print_info()
    turtle = Animal('turtle')
    turtle.print_info()


if __name__ == "__main__":
    main()
