import re

def arithmetic_arranger(problems, solved=False):
    arranged_problems = 'no problems'
    problemsArray = []
    temp = []
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for item in problems:
        parts = item.split(' ')

        # validate the problem
        if parts[1] != '+' and parts[1] != '-':
            return "Error: Operator must be '+' or '-'."
        elif not re.match('^\d+$', parts[0]) or not re.match('^\d+$', parts[2]):
            return "Error: Numbers must only contain digits."
        elif not re.match('^\d{,4}$', parts[0]) or not re.match('^\d{,4}$', parts[2]):
            return "Error: Numbers cannot be more than four digits."
        
        # reformat the problem parts
        width = len(parts[0]) + 2
        if len(parts[2]) > len(parts[0]):
            width = len(parts[2]) + 2

        a = parts[0].rjust(width)
        b = parts[1] + ' ' + parts[2].rjust(len(parts[0]))
        c = '-' * width
        tempArray = [ a, b, c]
        if solved:
            d = str(eval(parts[0] + parts[1] + parts[2]))
            tempArray.append(d.rjust(width))
        problemsArray.append(tempArray)
    
    # reformat problemsArray to string output
    for i in range(len(problemsArray[0])):
        line = []
        for j in range(len(problemsArray)):
            line.append(problemsArray[j][i])
        temp.append('    '.join(line) + '\n')

    arranged_problems = ''.join(temp).rstrip()

    return arranged_problems