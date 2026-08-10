def array_diff(a, b):
    """Computes the difference between two lists. 

        Parameters:
            a (list): First list to compare b
            b (list): Second list to compare with a
        Returns:
            list: The elements in list a not in list b
    """
    return [x for x in a if x not in b]