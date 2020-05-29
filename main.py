from abc import ABC, abstractmethod


class Sort(ABC):

    def __init__(self):
        pass

    def set_data(self, data):
        if isinstance(data, list):
            if len(data) < 1:
                raise ValueError('Data has length of zero.')
            try:
                self._data = [int(d) for d in data]
            except:
                raise ValueError('Not all elements are integers.')
        else:
            raise ValueError('Input provided is not a list.')

    def get_data(self):
        return self._data

    @abstractmethod
    def sort(self):
        pass


class BubbleSort(Sort):

    def __init__(self):
        super().__init__()

    def sort(self):
        n = len(self._data) 
        if n == 1:
            return
         
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if self._data[j] > self._data[j+1] : 
                    self._data[j], self._data[j+1] = self._data[j+1], self._data[j] 
