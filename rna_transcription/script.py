"""Determines the RNA complement of a given DNA sequence
"""

def to_rna(dna_strand):
    """
    Parameters:
        dna_strand (str): strand whose complement to return.

    Returns:
        str: Complement strand.
    """

    nucelotides = {
        "C": "G",
        "G": "C",
        "T": "A", 
        "A": "U"
    }

    if len(dna_strand) == 0:
        return ""

    new_dna_strand =[]

    for nucleotide in list(dna_strand):
        new_dna_strand.append(nucelotides[nucleotide])

    return "".join(new_dna_strand)