from Stacks_and_Queues.stacks.main import Stack


class Tower(object):
    """
    Creates a tower instance
    Attributes:
        disks(Stack): Stack to store disks
        index(Integer): Index of tower
    """
    def __init__(self, index):
        # Each tower has a stack size of 5
        self.disks = Stack()
        self.index = index

    def add(self, disk):
        """
        Adds a disk to this tower
        Args:
            disk(Integer): Disk to add
        """
        if not self.disks.is_empty() and self.disks.peek() <= disk:
            print("Error placing disk {0} !!".format(disk))
        else:
            self.disks.push(disk)
            # print(self.disks.size())

    def move_top_to(self, dest):
        """
        Moves top disk of this tower to tower "dest"
        Args:
            dest(Tower): The tower to which the disk should be moved to
        """
        top = self.disks.pop()
        dest.add(top)
        print("Move disk {0} from tower {1} to tower {2}".format(top, self.index, dest.index))

    def move_disks(self, n, destination, buffer):
        """
        Move disks from origin to destination
        Args:
            n(Integer): Number of disks to move
            destination(Tower): The destination for the disks
            buffer(Tower): Helper tower to move disks between origin and destination
        """
        if n > 0:
            self.move_disks(n-1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n-1, destination, self)
