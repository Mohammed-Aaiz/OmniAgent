import re
from tools.calculator import calculate

def use_tool(user_input):

    expression = re.sub(r"[^0-9+\-*/().%]", "", user_input)

    if expression:

        try:
            return calculate(expression)

        except:
            return None

    return None