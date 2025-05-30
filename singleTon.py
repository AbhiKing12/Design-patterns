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

# In the below method it refered to different memeory location but shared the state