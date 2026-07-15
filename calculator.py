def calculate(op, a, b):
    """
    Perform mathematical operations.
    Teams will extend this function.
    """
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    
    # [INSTRUCTION] Teams: Add your new operations directly below this line!
    # Make sure to keep the correct indentation level.
    elif op == "modulo":
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        return a % b
    
    raise ValueError(f"Unknown operation: {op}")
