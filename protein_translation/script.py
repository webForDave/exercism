"""
Translates RNA sequences into proteins.

RNA strands are made up of three-nucleotide sequences called codons. 
Each codon translates to an amino acid.
When joined together, those amino acids make a protein.
"""

from itertools import batched

def proteins(strand: str):
    """
    Parameters:
        strand (str): RNA strand to examine

    Returns:
        list: amino acids to form protein

    Examples:
        >>> proteins("AUGUUUUCU")
        ["Methionine", "Phenylalanine", "Serine"]
    """
    if len(strand) < 1:
        return []

    new_strand, protein_strand = [], []

    while len(strand) > 0:
        for nucleotide in strand[0 : 3]:
            new_strand.append("".join(nucleotide))
            strand = strand.removeprefix(nucleotide)

    actual_strand = ["".join(batch) for batch in batched(new_strand, 3)]

    for nucleotide in actual_strand:
        if nucleotide in {"UAA", "UAG", "UGA"}:
            return protein_strand

        if nucleotide in {"AUG"}:
            protein_strand.append("Methionine")

        if nucleotide in {"UUU", "UUC"}:
            protein_strand.append("Phenylalanine")

        if nucleotide in {"UUA", "UUG"}:
            protein_strand.append("Leucine")

        if nucleotide in {"UCU", "UCC", "UCA", "UCG"}:
            protein_strand.append("Serine")

        if nucleotide in {"UAU", "UAC"}:
            protein_strand.append("Tyrosine")

        if nucleotide in {"UGU", "UGC"}:
            protein_strand.append("Cysteine")

        if nucleotide in {"UGG"}:
            protein_strand.append("Tryptophan")

    return protein_strand
