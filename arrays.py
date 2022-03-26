expense_list=[{
    "january":2200,
    "february":2350,
    "march":2000,
    "april":2130,
    "may":2190
}]
extra=expense_list[0]['february']-expense_list[0]['january']
print(extra)

total_expense=0
for i in expense_list[0]:
     total_expense+=expense_list[0][i]
print(total_expense)

total=0
for i in expense_list[0]:
     total+=expense_list[0][i]
     if i=="april":
         break
     print(total)

for i in expense_list[0]:
     if expense_list[0][i]==2000:
        print(i)


expense_list[0]["june"]=1980
print(expense_list)

del expense_list[0]["april"]
print(expense_list)


