file1 = open('Articles.txt', "r")
value = file1.read()

list1 = value.split("-------------------")

print (len(list1))