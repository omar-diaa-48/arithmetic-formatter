def arithmetic_arranger(problems, include_result = False):
	if len(problems) > 5:
		return print("Error: Too many problems")

	operators = ["+", "-"]

	printed_lines = [[], [], [], []]

	dash = "-"
	space = " "

	for value in problems:
		operation = value.split(" ")

		max_spaces_to_fill = max(len(x) for x in operation)

		if operation[1] not in operators:
			return print("Error: Operator must be '+' or '-'")

		first_operand = operation[0]
		second_operand = operation[2]

		if first_operand.isdigit() == False or second_operand.isdigit() == False:
			return print("Error: Numbers must only contain digits")

		if len(first_operand) > 4 or len(second_operand) > 4:
			return print("Error: Numbers cannot be more than four digits")

		if operation[1] == "+":
			result = str(int(first_operand) + int(second_operand))
		elif operation[1] == "-":
			result = str(int(first_operand) - int(second_operand))

		printed_lines[0].append(first_operand.rjust(max_spaces_to_fill + 2) + space * 4)
		printed_lines[1].append(operation[1] + space + second_operand.rjust(max_spaces_to_fill) + space*4)
		printed_lines[2].append(dash * (max_spaces_to_fill + 2) + space*4)
		printed_lines[3].append(result.rjust(max_spaces_to_fill + 2) + space*4)

	line1 = ''.join(printed_lines[0])
	line2 = ''.join(printed_lines[1])
	line3 = ''.join(printed_lines[2])
	line4 = ''.join(printed_lines[3])
	
	arranged_problems = line1 + "\n" + line2 + "\n"+ line3

	if include_result:
		arranged_problems = arranged_problems + + "\n"+ line4

	print(arranged_problems)

	return arranged_problems