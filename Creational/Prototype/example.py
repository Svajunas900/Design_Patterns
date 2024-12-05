import copy

class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self) -> str:
        return "{} | {} | {}".format(self.name, self.color, self.options)


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister_object(self, name):
        del self._objects[name] 
    
    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

c = Car()
p = Prototype()

p.register_object("skylark", c)
c1 = p.clone("skylark")

print(c1)