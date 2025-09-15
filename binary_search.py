class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push_back(self, obj):
        if isinstance(obj, StackObj):
            current = self.top
             

            if current is None:
                self.top = obj
                self.length += 1
                return

            while current.next != None:
                current = current.next
            current.next = obj
            self.length += 1
            return

    def push_front(self, obj):
        if isinstance(obj, StackObj):
            obj.next = self.top
            self.top = obj
            self.length += 1
            return

    def __getitem__(self, indx):
        if not 0<=indx<self.length:
            raise IndexError('неверный индекс')
        count = 0
        current = self.top
        while count != indx:
            current = current.next
            count += 1
            
        return current.data

    def __setitem__(self, indx, newvalue):
        if not 0<=indx<self.length:
            raise IndexError('неверный индекс')
        count = 0
        current = self.top
        while count != indx:
            current = current.next
            count += 1

        current.data = newvalue

    def __iter__(self):
        self.current = self.top
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        obj = self.current
        self.current = self.current.next
        return obj
        
    

class StackObj:

    # Геттеры, сеттеры
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, (StackObj, type(None))):
            self.__next = obj

 
