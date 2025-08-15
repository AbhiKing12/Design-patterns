#in this both obj refered to the same instance i.e. same memory location
class single(object):
    def __new__(cls):
        if not hasattr(cls,'_ins'):
            cls._ins=super().__new__(cls)
        return cls._ins
    
o1=single()
print(o1)
o1.data=10
print(o1.data)
o2=single()
print(o2,o2.data)
o2.data=5
print(o1.data,o2.data)

# In the below method it refered to different memeory location but shared the state also known as Mono State Pattern i.e. different object same property
class temp(object):
    _shared = {}
    def __init__(self):
        self.__dict__ = self._shared
class single_2(temp):
    def __init__(self, arg):
        temp.__init__(self)
        self.val = arg
o1 = single_2("HII")
print(o1, o1.val, o1.__dict__)
o2 = single_2("Hello")
print(o2,o2.val,o2.__dict__)
print(o1, o1.val, o1.__dict__)

# The below method is decorator method