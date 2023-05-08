def main():
    salario = float(input())
    divida = float(input())
    mesCorrente = 10
    anoCorrente = 2016

    while True:

        divida *= 1.15

        if mesCorrente == 3:
            salario *= 1.05
        
        mesCorrente += 1

        if mesCorrente == 13:
            mesCorrente = 1
            anoCorrente += 1
        
        if salario < divida: break
    print(f'{mesCorrente}/{anoCorrente}')

if __name__ == '__main__':
    main() 