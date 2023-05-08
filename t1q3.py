def maiorMenor():

    maior = 0
    menor = 9999999999999999999999999999999999999999999999999

    while True:
        entrada = int(input())
        if entrada > maior:
            maior = entrada
        elif entrada < menor and entrada != 0:
            menor = entrada
        elif entrada == 0 : 
            break
    
    return maior, menor


def main():
    maior, menor = maiorMenor()
    if maior != 0:
        print(maior)
        print(menor)

if __name__=='__main__':
    main()