def arithmetic_arranger(input_list, cond=False):
    # Initialize strings for the arranged parts of the arithmetic problems
    list_top = ''
    list_bot = ''
    list_lines = ''
    list_res = ''

    # Iterate through the input_list and process each arithmetic problem
    for op in input_list:
        # Determine the operator (+ or -)
        if "+" in op:
            sign = "+"
        else:
            sign = "-"

        # Split the problem into the two operands
        top, bot = op.split(" " + sign + " ")

        # Add spacing and operator to the strings
        list_top += '  '
        list_bot += sign + ' '
        list_lines += '--'

        # Determine the max number of digits in the operands
        max_dig = max(len(top), len(bot))

        # Add padding to align the numbers
        list_top += ' ' * (max_dig - len(top))
        list_bot += ' ' * (max_dig - len(bot))
        list_lines += '-' * max_dig

        # Append the operands to the strings
        list_top += top
        list_bot += bot

        # Calculate the result
        if sign == "+":
            res = str(int(top) + int(bot))
        else:
            res = str(int(top) - int(bot))

        # Add padding to the result and append it to the string
        total_len = max_dig + 2
        list_res += ' ' * (total_len - len(res))
        list_res += res

        # Add spacing between the problems
        list_top += '    '
        list_bot += '    '
        list_lines += '    '
        list_res += '    '

    # Print the arranged parts of the arithmetic problems
    print(list_top)
    print(list_bot)
    print(list_lines)
    if cond:
        print(list_res)
        