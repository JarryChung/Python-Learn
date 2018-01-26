# 条件判断
s = input('birth: ')
age = int(s)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

print("----------------------------")

# 循环
#for
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

l = list(range(5))
for x in l:
    print(x)

for y in range(2):
    print(y, "\n")
#while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)