# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


my_dict = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"},{"VI" : "S005"}, {"VII" : "S005"}, {"V" : "S009"},{" VIII" : "S007"}]
my_list = []
for i in range(len(my_dict)):
    my_list += my_dict[i].values()
print(set(my_list))