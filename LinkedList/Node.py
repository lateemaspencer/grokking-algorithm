class Node(object):
    def __init__(self, data = None):

        self.data = data
        self.next_node = None

    def get_data(self):

        return self.data

    def get_next(self):

        return self.next_node

    def set_next(self, new_next):

        self.next_node = new_next