def conta_digitos(n):
    quantidade = 0
    while n > 0:
        quantidade += 1
        n //= 10
    return quantidade

def main():
    n = int(input("Numero inteiro positivo: "))
    q = conta_digitos(n)
    print(f"{n} tem {q} dígitos")

if __name__ == '__main__':
    main()