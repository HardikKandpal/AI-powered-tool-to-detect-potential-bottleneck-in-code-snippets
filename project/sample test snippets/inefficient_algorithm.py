def inefficient_algorithm(data, target):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] + data[j] == target: 
                return (data[i], data[j])  
    return None

data = list(range(10000))
print(inefficient_algorithm(data, 15000))
