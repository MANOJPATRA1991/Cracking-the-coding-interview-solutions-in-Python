from animal import Animal


class Dog(Animal):
    """
    Creates an animal of type Dog
    Attributes:
        name(String): Name of the dog
    """
    def __init__(self, name):
        super().__init__(name)
