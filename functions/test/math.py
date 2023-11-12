

def handle_function_test_math(query):
    x = query["x"]
    y = query["y"]
    op = query["op"]

    result = None
    if op == "add":
        result = x + y
    elif op == "sub":
        result = x - y
    elif op == "mul":
        result = x * y
    elif op == "div":
        result = x / y

    return result
