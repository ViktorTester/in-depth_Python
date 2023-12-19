"""The 'DictItemsIterator 'class generates iterators,
whose constructor takes one argument:

data - dictionary

The DictItemsIterator class's iterator generates a sequence of tuples
representing the key-value pairs of the 'data' dictionary
and then raises a StopIteration exception."""


class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = list(data)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.data[key]
            self.index += 1
            return key, value
        else:
            raise StopIteration
