class Element(object):
    """This class creates elements that can be inserted into a
        LinkedList instance"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """This class can be used to create a Linked List"""

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """Appends a new element to the linked list
            Args:
                new_element: An Element instance
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        # if no element in linked list
        else:
            self.head = new_element

    def is_empty(self):
        """
        Checks if the linked list is empty
        Returns:
            A Boolean indicating if the list is empty or not
        """
        return self.head is None

    def get_position(self, position):
        """
        Gets the element at the position specified
        Args:
            position: A number specifying position at which
            element is to be returned
        Returns:
            An Element instance at the specified position
            within the Linked list
        """
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def search(self, item):
        """
        Search for an item in the linked list
        Args:
            item: An Element instance
        Returns:
            A Boolean"""
        current = self.head
        while current:
            if current.value == item:
                return True
            else:
                current = current.next
        return False

    def peek(self):
        """
        Get a peek at the last element in the linked list
        Returns:
            Any: The value of the last element of the linked list
        """
        return self.head

    def insert(self, new_element, position):
        """
        Inserts a new element at a specified position in
        the linked list
        Args:
            new_element: An Element instance
            position: A number specifying the position
                at which the new element is to be inserted
        """
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        # if position is 1, make the new element as
        # the new head of the linked list
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """
        Search for a value in the linked list and if found,
        delete it
        Args:
            value: value to delete from the linked list
        """
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next
        # if value equals self.head.value, then previous will be None
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
            current.next = None

    def remove_head(self):
        """
        Remove the head of the linked list
        Returns:
            Element: The head of the linked list
        """
        temp, self.head = self.head, self.head.next
        return temp

    def pop(self):
        """
        Removes the last element from the linked list
        Returns:
            An Element instance
        """
        current = self.head
        previous = None
        while current is not None:
            if current.next:
                previous = current
            current = current.next
        # if only one element in the linked list
        if previous is None:
            temp = self.head
            self.head = None
            return temp
        else:
            temp = previous.next
            previous.next = None
            return temp

    def size(self):
        """
        Returns the size of the linked list
        Returns:
            An integer
        """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    @staticmethod
    def reverse(ll):
        """
        Reverse the linked list
        """
        lst = ll
        prev = None
        current = lst.head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        # finally, reverse the head
        lst.head = prev
        return lst