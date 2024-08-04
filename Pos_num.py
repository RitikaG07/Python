def print_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers
list1 = [15, -3, 7, 82, -21]
list2 = [22, 18, -100, 9]
print("Input: list1 =", list1, "Output:", print_positive_numbers(list1))
print("Input: list2 =", list2, "Output:", print_positive_numbers(list2))
