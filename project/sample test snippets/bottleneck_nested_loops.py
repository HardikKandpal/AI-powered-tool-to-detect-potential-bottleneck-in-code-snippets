def inefficient_function(n):
    result = []
    for i in range(n):
        for j in range(n):
            result.append(i * j)
    return result

print(inefficient_function(1000))
