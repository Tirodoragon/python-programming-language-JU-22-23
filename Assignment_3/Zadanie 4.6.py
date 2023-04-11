def sum_seq(sequence):
    s = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            s += sum_seq(item)
        else:
            s += item
    return s


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(sum_seq(seq))
