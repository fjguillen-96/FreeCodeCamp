def arithmetic_arranger(input_list,cond):
    list_top = ''
    list_bot = ''
    list_lines = ''
    list_res = ''
    for op in input_list:
        if "+" in op:
            sign = "+"
        else:
            sign = "-"
        
        top,bot = op.split(" " + sign + " ")
        list_top = list_top + '  '
        list_bot = list_bot + sign + ' '
        list_lines = list_lines + '--'

        max_dig = max(len(list(top)),len(list(bot)))
        for i in range(max_dig-len(list(top))):
            list_top = list_top + ' '
        for i in range(max_dig-len(list(bot))):
            list_bot = list_bot + ' '
        for i in range(max_dig):
            list_lines = list_lines + '-'
        list_top = list_top + top
        list_bot = list_bot + bot

        if  sign == "+":
            res = str(int(top) + int(bot))
        else:
            res = str(int(top) - int(bot))

        total_len = max_dig + 2
        for i in range(total_len-len(list(res))):
            list_res = list_res + ' '
        list_res = list_res + res


        list_top = list_top + '    '
        list_bot = list_bot + '    '
        list_lines = list_lines + '    '
        list_res = list_res + '    '

    print(list_top)
    print(list_bot)
    print(list_lines)
    if cond:
        print(list_res)
        
    