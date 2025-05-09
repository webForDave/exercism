def codon_split(strand):
    amino_acids = []
    codons = [strand[char: char + 3] for char in range(0, len(strand), 3)]

    return codons