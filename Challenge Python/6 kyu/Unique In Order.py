def unique_in_order(sequence):
    lis = []

    for x in range(len(sequence) - 1):
        if sequence[x] != sequence[x + 1]: # Pega índice, mas mostra o conteúdo, por causa do sequence[x] que consequentemente mostra apenas o conteúdo do índice respectivo.
            lis.append((sequence[x])) #Adiciona os válores não repetidos dentro da nova lista.
    # Esse loop pega o índice dos itens, nesse caso não pode ter itens repetidos um atrás do outro. 

    if sequence: # Esse if adiciona o ultimo valor da lista por que no loop acima não estava adicionando.
        lis.append(sequence[-1])
    return lis


print(unique_in_order([-1, -1, -2]))