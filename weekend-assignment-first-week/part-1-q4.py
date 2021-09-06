def rotateLeft(array_list , num_rotate ):
    alist = list(array_list)
    rotated_list = alist[num_rotate :]+alist[:num_rotate ]
    return rotated_list

array_list = []
n = int(input("Enter number of elements in array list : "))
for i in range(0, n):
    elem = int(input())
    array_list.append(elem)

num_rotate=int(input('Enter Number of rotations to be made: '))
print("The List after rotations is: ")
print(rotateLeft(array_list, num_rotate))