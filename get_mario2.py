def multiples_of_3():
    multiples = []
    for i in range(3, 31):
        if i % 3 == 0:
            multiples.append(i)
    return multiples
result = multiples_of_3()
print(result) : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
