class Borg:
    _shared_data = {}
    
    def __init__(self):
        self.__dict__ = self._shared_data

    def __str__(self):
        return str(self._shared_data)


class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)


x = Singleton(HTTP = "Hyper Text Transfer Protocol")

print(x)