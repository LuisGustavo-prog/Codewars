def DNA_strand(dna):
    lis_dna = list(dna)
    new_lis = []

    for x in lis_dna:
        if x == 'A':
            new_lis.append('T')
        elif x == 'T':
            new_lis.append('A')
        elif x == 'G':
            new_lis.append('C')
        elif x == 'C':
            new_lis.append('G')

    return ''.join(new_lis)