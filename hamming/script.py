"""
Determines the difference between two DNA strands
"""


def distance(strand_a, strand_b):
    """
    Parameters:
        strand_a (str): First strand
        strand_b (str): Second strand

    Returns:
        int: the number of different nucleotides on both DNA strands 

    Examples:
        >>> distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        7
    """
    hamming_distance = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    for nucleotide_a, nucleotide_b in zip(strand_a, strand_b):
        if nucleotide_a != nucleotide_b:
            hamming_distance += 1

    return hamming_distance