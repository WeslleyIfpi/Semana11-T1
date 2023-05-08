def main():
    valorInicial = float(input())
    taxaDeJuros = float(input())/100
    anos = 0
    valorTotal = valorInicial

    while True:
        juros = valorTotal * taxaDeJuros
        valorTotal += juros
        anos += 1
        if valorTotal >=  valorInicial * 2: break

    print(anos)

if __name__ == '__main__':
    main()
