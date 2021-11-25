
problems = ['1 + 2', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
def arithmetic_arranger(problems, solve = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    forth_line = ""

    for problem in problems:
        num1 = problem.split(" ")[0]
        num2 = problem.split(" ")[2]
        operation = problem.split(" ")[1]

        #  checking rules
        if (len(num1) and len(num2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not (num1.isnumeric() and num2.isnumeric()):
            return "Error: Numbers must only contain digits."

        if operation != "+" and operation != "-":
            return "Error: Operator must be '+' or '-'."

        # math equation
        total = 0
        if operation == "+":
            total = int(num1) + int(num2)
        elif operation == "-":
            total = int(num1) - int(num2)

        # printing result
        width = max(len(num1),len(num2))+2
        if first_line == "":
            spacer = ""
        else:
            spacer = (" " * 4)
        first_line += spacer + num1.rjust(width)
        second_line += spacer + operation + (num2).rjust(width-1)
        third_line += spacer + ("-" * width)
        forth_line += spacer + str(total).rjust(width)



    output = first_line + "\n" + second_line + "\n" + third_line
    if solve:
        output = output + "\n" + forth_line
    return output


print(arithmetic_arranger(problems))