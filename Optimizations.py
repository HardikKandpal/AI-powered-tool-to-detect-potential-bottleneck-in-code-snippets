# Function to suggest optimizations
def suggest_optimizations(bottlenecks: list) -> dict:
    suggestions = {}
    for issue in bottlenecks:
        if "list comprehensions" in issue:
            suggestions[issue] = "Use list comprehensions for better performance and readability."
        if "function calls" in issue:
            suggestions[issue] = "Consider reducing function calls by combining functionality."
        if "nested loops" in issue:
            suggestions[issue] = "Consider using more efficient looping methods, such as list comprehensions or optimized libraries."
        if "redundant code" in issue:
            suggestions[issue] = "Refactor redundant code into reusable functions or classes."
        if "inefficient algorithm" in issue:
            suggestions[issue] = "Consider replacing the algorithm with a more efficient one"
        if "function" in issue:
            suggestions["Too many function definitions"] = "Refactor the code to minimize excessive function definitions and improve readability."
    return suggestions
