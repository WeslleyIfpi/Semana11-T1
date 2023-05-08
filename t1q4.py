def inverteNumero():
    numero = input()
    saida = ''
    tamanho  = len(numero)
    for i in range(tamanho-1, -1, -1):
        saida += numero[i]
    return saida

def main():
    print(inverteNumero())

if __name__ == '__main__':
    main()