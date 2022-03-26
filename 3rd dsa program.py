# 1 Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
num_list=[]
max_num=int(input("maximum number is: "))
for i in range(0,max_num):
    if i%2==0:
        continue
    else:
        num_list.append(i)
print(num_list)

