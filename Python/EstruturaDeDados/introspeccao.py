import functools

#? Introspecção | habilidade da função ser identificada pelo próprio nome 
def exibe_nomes(funcao):
    def envelope(*args, **kwargs):
        return funcao(*args, **kwargs)
    return envelope

@exibe_nomes
def lista_nomes(lista):
    for item in lista:
        print(item)
        

def exibe_lista(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        return funcao(*args, **kwargs)
    return envelope

@exibe_lista
def lista(lista:list):
    for item in lista:
        print(item)
        
        
if __name__ == '__main__':
    print(lista_nomes.__name__) #? Retorna "envelope" 
    print(lista.__name__) #? Retorna seu nome "lista" 
