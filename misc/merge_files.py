"""
There are two large files containing SORTED key value pairs, where keys are strings and values are integers. e.g.

File 1:

aaa: 1
bbb: 5
bbb: 3
ccc: 2

File 2:

bbb: 9
ccc: 10
ddd: 11

We want to merge the two files together to produce an output file where keys are still sorted. Consecutive pairs with the same key in the output are merged, by summing up their values. e.g. merging the files above produces the output:

aaa: 1
bbb: 17
ccc: 12
ddd: 11

"""


# API to read from the input file. Example usage:
#
#   while input_stream.is_valid():
#       key, val = input_stream.read()
#       ......
#       input_stream.next()
#
# Testing can be done by providing data via the constructor.
class InputStream:
    # For testing, InputStream can be constructed from a list.
    def __init__(self, data):
        self._data = data
        self._current = 0
    
    # Checks whether the stream has data at the current position.
    # Returns false if the stream is already ended.
    def is_valid(self):
        return self._current < len(self._data)
    
    # Gets the current pair.
    # NOTE: does not advance position in the stream.
    # Returns None if the stream has already ended.
    # If data exists, returns as tuple (String, Int).
    def read(self):
        if self.is_valid():
            return self._data[self._current]
        return None
    
    # Advances to the next item in the stream.
    def next(self):
        if self.is_valid():
            self._current += 1


# API to write to the output file.
# During testing, data written can be accessed via the data() method.
class OutputStream:
    def __init__(self):
        self._data = []
    
    # Writes pair to output file.
    # data = (string, int)
    def write(self, data):
        self._data.append(data)
            
    # For testing, OutputStream data is saved in memory.
    def data(self):
        return self._data


# Implement this:
def merge_input_files(input_1: InputStream, input_2: InputStream, output: OutputStream):
    (x, x_count) = read_key(input_1)
    (y, y_count) = read_key(input_2)
    # edge cases: when a stream ends, handle that
    # read_key handles all next operations
    while True:
        # Both streams are done, break
        if (x is None) and (y is None):
            break
            
        # y != None and x == None
        print(x, y)
        if (x is not None and y is None) or (False if x is None else (x < y)):
            output.write((x, x_count))
            (x, x_count) = read_key(input_1)
        elif (x is None and y is not None) or (False if y is None else (y < x)):
            output.write((y,y_count))
            (y, y_count) = read_key(input_2)
        elif x == y:
            total_count = x_count if x is not None else 0
            total_count += (y_count if y is not None else 0)
            # This is only true if at least one of the keys is not None
            if total_count > 0:
                output.write((x,total_count))
                (x, x_count) = read_key(input_1)
                (y, y_count) = read_key(input_2)

# Returns (key, total_count) for the next contiguous key in `inp`.
# If `inp` is empty, returns `None`.
def read_key(inp: InputStream):
    x_val = inp.read()
    inp.next()
    if x_val is None:
        return (None, 0)
    
    (x, x_count) = x_val
    while True:
        y_val = inp.read()
        if y_val is None:
            break
        (y, y_count) = y_val
        if y != x:
            break
        else:
            x_count += y_count
            inp.next()
    return (x, x_count)



in1 = InputStream([("aaa", 1), ("bbb", 5), ("bbb", 3), ("ccc", 2)])
in2 = InputStream([("bbb", 9), ("ccc", 10), ("ddd", 11)])
out_s = OutputStream()
merge_input_files(in1, in2, out_s)
print(out_s.data())
