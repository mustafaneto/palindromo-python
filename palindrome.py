palavraOufrase = input("Escreva uma palavra ou frase para verificar se é palíndromo: ")

if len(palavraOufrase) > 1:
    verificacao = palavraOufrase.replace(" ", "")
    i = 0
    for x in verificacao:
        if i > len(verificacao)/2:
            break
        else:
            if x != verificacao[len(verificacao) - i - 1]:
                break
        i = i + 1
    if i == int(len(verificacao)/2) + 1:
        print("A frase ou palavra é um palíndromo")
    else:
        print("A frase ou palavra não é um palíndromo.")

