def proteins(strand):
    phenylalanine = ['UUU', 'UUC']
    leucine = ['UUA', 'UUG']
    methionine = ['AUG']
    serine = ['UCU', 'UCC', 'UCA', 'UCG']
    tyrosine = ['UAU', 'UAC']
    cysteine = ['UGU', 'UGC']
    tryptophan = ['UGG']
    stop = ['UAA', 'UAG', 'UGA']

    groups = []
    codons = []

    for char in range(0, len(strand), 3):
        codons.append(strand[char : char + 3])


    for codon in codons:
        if codon in phenylalanine:
            groups.append("Phenylalanine")
        elif codon in leucine:
            groups.append("Leucine")
        elif codon in methionine:
            groups.append("Methionine")
        elif codon in serine:
            groups.append("Serine")
        elif codon in tyrosine:
            groups.append("Tyrosine")
        elif codon in cysteine:
            groups.append("Cysteine")
        elif codon in tryptophan:
            groups.append("Tryptophan")
        elif codon in stop:
            break
    return groups


print(proteins("AUGUUUUCUUAAAUG"))