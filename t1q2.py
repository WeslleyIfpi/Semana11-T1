def calculaMedia():
    total = 0 
    quantidadeNumeros = 0

    while True:
        num = float(input())
        if num != 0:
            total += num
            quantidadeNumeros += 1
        if num == 0: break
    if quantidadeNumeros != 0 :
        media = total / quantidadeNumeros
    else: 
        media = ''
    return media

def main():
    media = calculaMedia()
    if media != '':
        print(f'{media}')

if __name__ == '__main__':
    main()