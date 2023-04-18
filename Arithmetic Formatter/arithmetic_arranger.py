def arithmetic_arranger(problems, show=False):
    # This function takes arithmetic problems horizontally and rearranges them vertically side by side.

    x = 0
    first_string = ''
    second_string = ''
    lines_result = ''
    result_string = ''

    # First rule:
    if len(problems) >= 5:
        return 'Error: Too many problems.'

    while len(problems) > x:
        partition = problems[x].split()
        firstNumber = partition[0]
        operator = partition[1]
        secondNumber = partition[2]

        # Second Rule:
        if len(firstNumber) < 5 or len(secondNumber) < 5:
            # Third rule:
            if firstNumber.isnumeric() and secondNumber.isnumeric():
                # Fourth rule:
                if operator == '+':
                    result = str(int(firstNumber) + int(secondNumber))
                elif operator == '-':
                    result = str(int(firstNumber) - int(secondNumber))
                else:
                    return 'Error: Operator must be "+" or "-".'
            else:
                return 'Error: Numbers must only contain digits.'
        else:
            return "Error: Numbers cannot be more than four digits."

        # Space between equations arrangement:
        space_btw = max(len(firstNumber), len(secondNumber)) + 2

        first_string += ' ' * (space_btw - len(firstNumber)) + firstNumber + ' ' * 4
        second_string += operator + ' ' * (space_btw - len(secondNumber) - 1) + secondNumber + ' ' * 4
        lines_result += space_btw * '-' + ' ' * 4
        result_string += ' ' * (space_btw - len(result)) + result + ' ' * 4
        x += 1
    # Show results:
    if show:
        arranged_problems = first_string + '\n' + second_string + '\n' + lines_result + '\n' + result_string
    else:
        arranged_problems = first_string + '\n' + second_string + '\n' + lines_result

    return arranged_problems



print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))