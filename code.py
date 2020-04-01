import itertools

home = 0
home = int(input())

all_list = list()
idx = 0
# listmatengtanpaspace = [] 
for x in range(home):
    input_listnya= input()
    listmatengtanpaspace = input_listnya.split()
    all_list.append(listmatengtanpaspace)
joinedlist=list(itertools.chain(*all_list))
coba = 0
awalan = 0
d = 0
jarak = home + 1
zero = 0
toadd = 0

b = home - 1
jarakdiagonaldua = b
# 3

# 3 4 5 
# 7 8 9 
# 2 3 9
a = home + 1
jarak = a
for y in range(home):
    # diagonal1=0
    # diagonal2=0
    
    if y == 0 :
        awal = 0 + int(joinedlist[zero])            #---------------> 3 
        simpan = awal
    elif y!=0: 
        simpan = simpan + int(joinedlist[jarak])     #---------------> 3 + 8 = simpan
        jarak = jarak + a
    
    # awalan = int(joinedlist[d])                 #value nya 4
    # d = d + (home+1)                            #d nya jadi 4
    # coba   = awalan + int(joinedlist[d])        #4 + 8 = 12

    # d = d + (home+1)                            # 0 + 4 = 4
    
    # print(coba)
    # awalan = awalan + home
    #

    # coba = coba + joinedlist[home]
    # diagonal1 = int(coba)
    # diagonal1 = int(joinedlist[0])+int(joinedlist[0+home])+int(joinedlist[])
    # diagonal2 = int(joinedlist[2])+int(joinedlist[4])+int(joinedlist[6])

# sum = diagonal1 - diagonal2

# sum_abs = abs(sum)
# print(sum_abs)

# print(simpan)

# 3

# 3 4 5 
# 7 8 9 
# 2 3 9

for j in range(home):
    if j == 0:
        awaldiagonalsatunyalagi = 0 + int(joinedlist[jarakdiagonaldua]) #------> 0 + 5
        simpansatunyalagi = awaldiagonalsatunyalagi
        jarakdiagonaldua = jarakdiagonaldua + b

    if j != 0:
        simpansatunyalagi = simpansatunyalagi + int(joinedlist[jarakdiagonaldua])
        jarakdiagonaldua = jarakdiagonaldua + b

# print (simpansatunyalagi)


kuranginlahsekarang = simpansatunyalagi - simpan

print(abs(kuranginlahsekarang))













