class Iteradores:
    def __init__(self, numeros:list[int]):
        self.numeros = numeros
        self.contador = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero *2
        except IndexError:
            raise StopIteration 
    

class Tabuada:
    def __init__(self, lista:list[int]):
        self.numero = numero
        self.multiplicador = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        resultado = self.numero * self.multiplicador 
        self.multiplicador += 1
        if self.multiplicador > 11:
            raise StopIteration
        return resultado


class Fibonacci:
    numero:int
    sequencia = [0, 1]    
    def __iter__(self):
        return self
    
    def __next__(self):
        for x in range(20):
            for num in range(len(self.sequencia)):
                self.sequencia.append(self.sequencia[num] + self.sequencia[num + 1])
                self.numero = self.sequencia[-1]
                return self.numero
        raise StopIteration
         
        
if __name__ == '__main__':
    # for i in Iteradores([1,2,3,4,5,6,7,8,9,10]):
    #     print(i)
    # for x in Tabuada(5):
    #     print (x)
    print(Fibonacci())