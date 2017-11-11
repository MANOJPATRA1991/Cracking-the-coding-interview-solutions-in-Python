from animal import Animal


class Cat(Animal):
    """
    Creates an animal of type Cat
    Attributes:
        name(String): Name of the cat
    """
    def __init__(self, name):
        super().__init__(name)
