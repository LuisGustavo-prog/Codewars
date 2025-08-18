def alphabet_position(text):
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    text = text.lower() # Tranformando tudo em minúsculo para não dar erro caso tenha uma maiúscula.
    lis = []

    for x in text:
        if x in alphabet: # Verificando se as letras do text estão dentro do alfabeto, caso esteja ele irá pra próxima parte.
            number = alphabet.index(x) + 1 # Adicionando mais 1 para que o índice comece por 1. Tranforma a letra do alfabeto em números.
            lis.append(str(number)) # Alterando o tipo para str.
    
    return ' '.join(lis) 


print(alphabet_position('abc'))
