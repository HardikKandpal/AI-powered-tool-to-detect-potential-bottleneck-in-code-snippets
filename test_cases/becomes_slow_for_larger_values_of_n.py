def inefficient_string_concatenation(n):
    result = ""
    for i in range(n):
        result += f"Item {i}\n"
    return result

print(inefficient_string_concatenation(10000))
