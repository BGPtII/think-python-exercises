def nested_sum(t):
    """Takes a list of lists of integers and adds up the
    elements from all of the nested lists
    """
    list_sum = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            list_sum += t[i][j]
    return list_sum
