# singleton is used to achieve single object behaviour to have a shared resource
# below metioned are the 4 methods to achieve that

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
class singleTonDecorator(object):
    def __init__(self, dec_class):
        self.dec_class = dec_class
        self.instance = None
    def __call__(self, *args, **kwds):  
        if self.instance == None:
            self.instance = self.dec_class(*args,**kwds)  # initializing the decorator class i.e from next time onward the instance will be available
        return self.instance
@singleTonDecorator
class logging(object):    # whenever the object for this class object created it will call decorator class first
    def __init__(self):
        self.start = None
    def write(self,message):
        if self.start:
            print(self.start, message)
        else:
            print(message)
l1 = logging()
l1.start = "test"
print(l1)
l1.write("l1 data entered")
l2 = logging()     # it won't create a new instance
l2.start = "l2_test"
print(l1,l2)          # both l1 and l2 pointed toward same instance
l2.write("l2 data entered")

# metaclass method to call the shared instance or object
class singletonMeta(type):   # type has a call method of super class
    __instances = {}
    def __call__(self, *args, **kwds):
        if self not in self.__instances:
            self.__instances[self] = super().__call__(*args, **kwds)  # to instialize the shared instance
        print(self.__instances)
        return self.__instances[self]
class connector(metaclass=singletonMeta):
    def __init__(self):
        self.status = "NC"
    def discon(self):
        self.status = "DisC"
    def conn(self):
        self.status = "Conn"
l1 = connector()
print("L1 : ",l1," status : ",l1.status)
l2 = connector()
print("l2 : ",l2," status : ",l2.status)
l2.conn()
print("l2 : ",l2," status : ",l2.status)
l3 = connector()
print("l3 : ",l3," status : ",l3.status)
l3.discon()
print("l3 : ",l3," status : ",l3.status)