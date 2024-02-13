def nested_sum(lst):
    """Takes a list of lists of integers and adds up the elements from all of the nested lists"""
    total_sum = 0
    for inner_list in lst:
        total_sum += sum(inner_list)
    return total_sum
