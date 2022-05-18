var_list1 = [12, 16, 0, -100, "1234", True]  # массив переменных

# цикл, который "итерируется"(пробегается) по массиву объектов и
# берёт каждый цикл этот объект себе в переменную (i)
# for list_element in [12, 16, 0, -100]:
# for i in var_list1:
#     print(
#         "элемент 'списка': ", var_list1.index(i),
#         i, type(i)
#     )

# for i in var_list1:
#     print(
#         "элемент 'списка': ", var_list1.index(i),
#         i, type(i)
#     )
#     # код до цикла
#     for j in var_list1:
#         # код в цикле
#         print(
#             "элемент 'списка': ", var_list1.index(j),
#             j, type(j)
#         )
#     # код после цикла

var_int1 = 12
# код до цикла
while var_int1 < 500:
    # код в цикле
    var_int1 = var_int1 + 1
    print(var_int1)
    if var_int1 == 500:
        print('мы дошли до 500')
# код после цикла
print('цикл завершён')

