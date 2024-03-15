def segmentate(input):
    out = []
    for i in range(len(input) - 3):
        out.append(input[i:i+4])
    return out