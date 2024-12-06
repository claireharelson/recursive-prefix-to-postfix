# This script creates functions to validate a prefix string and to convert prefix to postfix notation using recursion

def preToPostRec(exp):
    operators = ['+', '-', '*', '/', '$', '^']
    operands = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    op = exp.pop(0)
    if (exp[0][0]) in operators:
        op1 = preToPostRec(exp)
        op2 = preToPostRec(exp)
        res = [op1, op2, op]
        return res
    else:
        exp.pop(0)


def recursion(prefix) -> str:
    """
    Takes in a string in valid prefix form and uses recursion to convert directly to postfix form
    return: string in postfix form
    """
    # Define acceptable operators and operands that can be converted from prefix to postfix
    operators = ['+', '-', '*', '/', '$', '^']
    operands = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_operands = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']

    if len(prefix) == 0:
        return ''
    char = prefix[0]
    if char == '\n':
        return ''
    elif char == ' ':
        return ''
    elif char in lower_operands:
        return char.upper() + str(recursion(prefix[1:]))
    elif char in operands:
        return char + str(recursion(prefix[1:]))
    elif char in operators:
        left_op = str(recursion(prefix[1:]))
        right_op = str(recursion(prefix[len(prefix)+1:]))
        return left_op + right_op + char

    # Error checking to ensure that a prefix statement has the correct ratio of operators to operands
    total_operands = 0
    total_operators = 0
    for item in prefix:

        if item in operators:
            total_operators += 1
        elif item in operands or lower_operands:
            total_operands += 1
        else:
            raise AssertionError(f"{item} is not a proper prefix input character.")
            # raises error if any non-compatible characters get passed in as string objects (i.e. '5', '%')

    if total_operands == 0 and total_operators == 0:  # skips over empty lines
        pass
    elif total_operands != (total_operators + 1):
        raise AssertionError(f"Incorrect ratio of operators to operands in {prefix}.")
        # accounts for statements with more operators than operands
