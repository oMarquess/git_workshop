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
    elif op == "power":
        return a ** b
    # Make sure to keep the correct indentation level.
    
    raise ValueError(f"Unknown operation: {op}")
