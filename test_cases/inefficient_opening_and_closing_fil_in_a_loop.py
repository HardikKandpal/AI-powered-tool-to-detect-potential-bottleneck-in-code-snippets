def inefficient_file_reading(n):
    result = []
    for i in range(n):
        with open('large_file.txt', 'r') as file:
            result.append(file.read())  
    return result

print(inefficient_file_reading(10))
