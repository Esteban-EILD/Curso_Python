def number_pattern(n):
    if type(n) is not int:
        return "Argument must be an integer value"
    elif n<1:
        return "Argument must be an integer greater than 0"
    pattern = ""
    for i in range(1, n + 1):
        pattern += str(i) + " "
    return pattern.strip()

print(number_pattern(4))
print(number_pattern(12))