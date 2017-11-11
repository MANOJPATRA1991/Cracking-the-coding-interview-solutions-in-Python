# from Stacks_and_Queues.queue.main import Queue
from Linked_Lists.main.linkedList import LinkedList, Element

from dogs import Dog
from cats import Cat


class AnimalQueue(object):
    """
    A Queue to store animals(cats and dogs)
    Attributes:
        dogs(LinkedList): A linked list to store dogs
        cats(LinkedList): A linked list to store cats
        order(Integer): Time when an animal is added to the queue
    """
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.order = 0

    def enqueue(self, a):
        """
        Enqueues an animal to the queue
        Args:
            a(Animal): Animal to add to the queue
        """
        a.set_order(self.order)
        self.order += 1
        if type(a).__name__ == 'Dog':
            self.dogs.append(Element(a))
        elif type(a).__name__ == 'Cat':
            self.cats.append(Element(a))

    def dequeue(self):
        """
        Removes an animal from the queue
        Returns:
            Animal: Returned animal
        """
        if self.dogs.size() == 0:
            return self.dequeue_cats()
        elif self.cats.size() == 0:
            return self.dequeue_dogs()

        if self.dogs.peek().value.is_older_than(self.cats.peek().value):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()

    def dequeue_dogs(self):
        return self.dogs.remove_head()

    def dequeue_cats(self):
        return self.cats.remove_head()


x = AnimalQueue()
x.enqueue(Dog('Dog1'))
x.enqueue(Cat('Cat1'))
x.enqueue(Cat('Cat2'))
x.enqueue(Dog('Dog2'))
x.enqueue(Dog('Dog3'))
x.enqueue(Dog('Dog4'))
x.enqueue(Cat('Cat3'))
x.enqueue(Cat('Cat4'))
x.enqueue(Dog('Dog5'))

print(x.dequeue_cats().value.name)
print(x.dequeue().value.name)
print(x.dequeue_dogs().value.name)