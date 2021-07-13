x=input('多少小朋友?')
x=int(x)
list=[]
for i in range(x):
    score=int(input('成績?'))
    name=input('名子?')
    list.append(score)
    list.append(name)
print (list)
i=0
max=-1
min=101
max_i=0
min_i=0
while i < x :
    if list [i*2]:
        max_i=i*2
    if list[i*2]:
        min=list[i*2]
        min_i=i*2
        i=i+1
print('高分',list[max_i+1],list[max_i])
print('低分',list[min_i+1],list[min_i])
      