number_str = input("Provide a list of numbers (comma-separated): ")
list = list(map(int, number_str.split(',')))

sorted_list = sorted(list)
maxmin = []
maxmin.append(sorted_list[0])
maxmin.append(sorted_list[-1])

print(maxmin)
