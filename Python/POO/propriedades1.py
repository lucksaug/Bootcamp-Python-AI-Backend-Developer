class Foo:
    def __init__(self,x=None):
        self._x = x
    
    #Transforma um Método em atributo  
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        self._x += valor
    
    @x.deleter
    def x(self):
        self._x = -1
    
if __name__ == "__main__":
    foo = Foo(10)
    print(foo.x)
    foo.x = 10
    print(foo.x)
    del foo.x
    print(foo.x)