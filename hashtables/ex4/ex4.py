def has_negatives(a):
    data = {}
    result = []
    for index in a:
        if index not in data:
            data[index] = 1
            data[-index] = 1
        else:
            if index < 0:
                result.append(-index)
            else:
                result.append(index)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
