class Animal(object):
    """
    Defines an animal
    Attributes:
        name(String): The name of the animal
        order(Integer): Time when the animal is added
    """
    def __init__(self, name):
        self.name = name
        self.order = None

    def set_order(self, order):
        """
        Sets the time when the animal is added
        Args:
            order(Integer): The time when animal is added
        """
        self.order = order

    def get_order(self):
        """
        Get the order of the animal
        Returns:
            Integer: The time when the animal is added
        """
        return self.order

    def is_older_than(self, a):
        """
        Finds the older of this animal and animal "a"
        Args:
            a(Animal): The animal to compare with
        Returns:
            Boolean: Indicates whether this animal is older than animal "a" or not
        """
        return self.order < a.get_order()


