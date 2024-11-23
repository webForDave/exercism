def to_rna(dna_strand):
    new_strand = []

    for char in list(dna_strand):
        if char == 'G':
            new_strand.append('C')
        elif char == 'C':
            new_strand.append('G')
        elif char == 'T':
            new_strand.append('A')
        elif char == 'A':
            new_strand.append('U')
    return ''.join(new_strand)


print(to_rna('ACGTGGTCTTAA'))