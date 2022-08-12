my_list1 = [line.split(',') for line in open("data1.txt")]
a= my_list1

my_list2 = [line.split(',') for line in open("data2.txt")]
b=my_list2

print(a, b)