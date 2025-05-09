def proteins(strand):
    seq = {
    'UUU' : "Phenylalanine",
    'UUC' : "Phenylalanine",
    'UUA' : "Leucine",
    'UUG': "Leucine",
    'AUG' : "Methionine",
    'UCU' : "Serine",
    'UCC': "Serine" ,
    'UCA' : "Serine",
    'UCG' : "Serine",
    'UAU' : "Tyrosine",
    'UAC' : "Tyrosine",
    'UGU' : "Cysteine",
    'UGC' : "Cysteine",
    'UGG' : "Tryptophan",
    'UAA' : "Stop",
    'UAG' : "Stop",
    'UGA' : "Stop"
    }

    amino_acids = []
    codons = [strand[char: char + 3] for char in range(0, len(strand), 3)]

    for codon in codons:
        if codon in ["UAA", "UAG", "UGA"]:
            break
        amino_acids.append(seq.get(codon))

    return amino_acids

print(proteins("AUGUUUUCUUAAAUG"))