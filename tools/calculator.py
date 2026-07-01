def calculate(expression: str):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Invalid expression"