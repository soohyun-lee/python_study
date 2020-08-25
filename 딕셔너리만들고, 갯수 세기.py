#딕셔너리로 만들고, 갯수 세기

my_list = ['one',2,3,2,'one']
new_dic = {}
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
for k in new_list:
    new_dic[k] = my_list.count(k)
print(new_dic)

#result {'one': 2, 2: 2, 3: 1}
