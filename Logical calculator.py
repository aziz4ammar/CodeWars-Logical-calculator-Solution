def logical_calc(array, op):
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        result = False
        for value in array:
            result ^= value
        return result
    else:
        return None