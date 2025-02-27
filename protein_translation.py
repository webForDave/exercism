def proteins(strand):
    phenylalanine = ['UUU', 'UUC']
    leucine = ['UUA', 'UUG']
    methionine = ['AUG']
    serine = ['UCU', 'UCC', 'UCA', 'UCG']
    tyrosine = ['UAU', 'UAC']
    cysteine = ['UGU', 'UGC']
    tryptophan = ['UGG']
    stop = ['UAA', 'UAG', 'UGA']

    groups = [strand[i:i+3] for i in range(0, len(strand), 3)]


print(proteins("AUGUUUUCUUAAAUG"))