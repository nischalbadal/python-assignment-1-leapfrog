#Q1(a)
lst1=[100, 200, 300, 400, 500]
lst2=[1,10,100,1000,10000]

lst3 = list(map(lambda x, y: x + y, lst1, lst2))
print(lst3)

#Q1(b)
def myfunc(mystr):
    nums = [item for sublist in mystr for item in sublist]
    dict_num = {}
    for num in nums:
        if num in dict_num.keys():
            dict_num[num] += 1
        else:
            key = num
            value = 1
            dict_num[key] = value
    return dict_num

result  = myfunc("aaaaabbbbcccdde")
print(result)

# Q1(c)
dict={
"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110
}

final_list = list(map(lambda x: x.upper(), {key:value for (key, value) in dict.items() if value>5000}))
print(final_list)