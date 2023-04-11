def flatten(sequence):
    s = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            s.extend(flatten(item))
        else:
            s.append(item)
    return s


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]
