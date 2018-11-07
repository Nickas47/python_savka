class Reverse:

    def __init__(self, data):
        self._data = data           
        self._index = len(data)     

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:        
            raise StopIteration     
        self._index = self._index - 1
        return self._data[self._index]
r = Reverse([4,[],45,[],34,[],3,[],23,5,[],4])
str_list = list(filter(None, r)) 
print(str_list)
