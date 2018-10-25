# import re
# i = str('а-б')
#
# if i == re.i():
#     print('Ok')


# a, b, c = map(int, input().split())

# print(1, 2, 3, sep=', ')
# a = 10
# b = 5
# print('У меня есть %s рублей %s копеек'%(a,b))
# print('У меня есть {0} рублей {1} копеек'.format(a, b))


a = 'Привет'
#
# print(a.ljust(10, '!'))
# print(a.rjust(10, '!'))
# print('Хай'.ljust(10, '%'))

# w = 'Ivanov Ivan Ivanovich'
# w.split()
# a = w.split()
# print(w)
# print(a)
# print(type(a))
#
# a, b, c = input().split()
# print(a,b,c, end='')
#
# # i = '12346'
# # print(i[-3:len(i) + 1])


# a = input()
# print(a)
# print(a.replace('0', ''))
# print(len(a.replace('0', '')))
# print(
#     type(len(a.replace('0', '')))
# )
#
# inputVsp = input().replace('0', '').split()
# print(inputVsp)
# print(inputVsp[0])
# print(inputVsp[0][-3:len(inputVsp[0])])


# inputVsp = input().replace('а', '!').split()
# inputVsp = input().split()
# print(inputVsp)
# print(inputVsp[0])
# print(inputVsp[0][-3:len(inputVsp[0])])

# inputVsp[0] = inputVsp[-3:len(inputVsp)]
# print(inputVsp[0][-3:len(inputVsp)
# searchVsp = inputVsp.split()[-3:len(inputVsp)]
# print(searchVsp)


a = input().split()
print(a)
if a.count(0) or a.count('0'):
    print('Test')
