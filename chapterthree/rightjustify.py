def right_justify(s):
    """Takes a string named s as a parameter and prints the string with enough leading
    spaces so that the last letter of the string is in column 70 of the display
    """
    s = ' ' * (70 - len(s)) + s
    print(s)