def to_rna(dna_strand):
    new_strand = ''

    for char in list(dna_strand):
        if char == 'G':
            new_strand += 'C'
        elif char == 'C':
            new_strand += 'G'
        elif char == 'T':
            new_strand +='A'
        elif char == 'A':
            new_strand += 'U'
    return ''.join(new_strand)


print(to_rna('ACGTGGTCTTAA'))