b = input ("Enter a binary : ")
my_list = []
for char in b:
    my_list.append(char)
k = 0
sum = 0
for i in reversed(my_list):
    sum = sum + int(i)*(2**k)
    k=k+1
print ("Your character is {}".format(chr(sum)))
print ()  
input("Enter any key to exit")