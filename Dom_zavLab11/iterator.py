class Reverse:
    def __init__(self, data):
        self._data = data          
        self._len = len(data)
        self._start = self._len + 1 if self._len % 2 else self._len #через термінант

    def __iter__(self): # ініціалізація яка повртає сам ітератор 
        return self

    def __next__(self): # крок ітерації
        if self._start <= 0:       
            raise StopIteration
        self._start -= 2
        return self._data[self._start]
r = Reverse([4,45,34,3,23,5,4])
for x in r:
    print(x)
#побудувати ітератор 
#який проходить всі елементи списку 
#повертаючи тільки елементи з парними індексами 
#у зворотньому порядку
