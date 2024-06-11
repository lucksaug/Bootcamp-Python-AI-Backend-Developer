
def meu_gerador(numeros:list[int]):
    for numero in numeros:
        yield numero * 3
    


if __name__ == '__main__':
    for i in meu_gerador(numeros=[0,1,2,3]):
        print(i)