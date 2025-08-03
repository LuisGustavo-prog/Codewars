def high_and_low(numbers):
    array = numbers.split() # usando o split enquanto os números estão em formato de string, pois, esse metodo só pode ser usado em string.
    number_array = [int(x) for x in array] # Convertendo para o tipo inteiro.
    
    max_ = max(number_array) # Pegando o maior número da lista.
    min_ = min(number_array) # Pegando o menor número da lista.

    final = [max_, min_] # colocando os números dentro de uma nova lista.
    return " ".join([str(x) for x in final]) # O join só funciona com String, para eu poder devolver sem ser em formato de lista eu preciso usar um mini for para mudar o tipo para string.
    