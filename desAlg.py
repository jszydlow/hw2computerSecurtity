import numpy as np
pcDashOne = [57,49,41,33,25,17,9,
            1,58,50,42,34,26,18,
            10,2,59,51,43,35,27,
            19,11,3,60,52,44,36,
            63,55,47,39,31,23,15,
            7,62,54,46,38,30,22,
            14,6,61,53,45,37,29,
            21,13,5,28,20,12,4
            ] #arrray of positions in key that are taken in first permutation based on pc-1 table

binaryKey = "0001001100110100010101110111100110011011101111001101111111110001"
originalKeyBits = []

for bit in binaryKey: 
    originalKeyBits.append(bit)

originalKeyDict = {}
countBits = 1
for bit in originalKeyBits:
    originalKeyDict[countBits] = bit
    countBits +=1


permutedKey = []
for index in pcDashOne:
    permutedKey.append(originalKeyDict[index])


c0 = []
for i in range(0,28): #First half of permuted key becomes c0
    c0.append(permutedKey[i])

d0 = []
for i in range(28,56): #second half of permuted key becomes d0
    d0.append(permutedKey[i])




#function for left shift
def leftShift(key):
    temp = key[0]
    for i in range(1,len(key)):
        key[i-1] = key[i]
    key[len(key)-1] = temp
    return key
#kept overwriting when I stored in a dictionary and did this iteratively
c1 = leftShift(c0)

c1temp = c1
c2 = leftShift(c1temp)


c3 = leftShift(c2)
c3 = leftShift(c3)
c4 = leftShift(c3)
c4 = leftShift(c4)
c5 = leftShift(c4)
c5 = leftShift(c5)
c6 = leftShift(c5)
c6 = leftShift(c6)
c7 = leftShift(c6)
c7 = leftShift(c7)
c8 = leftShift(c7)
c8 = leftShift(c8)
c9 = leftShift(c8)
c10 = leftShift(c9)
c10 = leftShift(c10)
c11 = leftShift(c10)
c11 = leftShift(c11)
c12 = leftShift(c11)
c12 = leftShift(c12)
c13 = leftShift(c12)
c13 = leftShift(c13)
c14 = leftShift(c13)
c14 = leftShift(c14)
c15 = leftShift(c14)
c15 = leftShift(c15)
c16 = leftShift(c15)

d1 = leftShift(d0)
d2 = leftShift(d1)
d3 = leftShift(d2)
d3 = leftShift(d3)
d4 = leftShift(d3)
d4 = leftShift(d4)
d5 = leftShift(d4)
d5 = leftShift(d5)
d6 = leftShift(d5)
d6 = leftShift(d6)
d7 = leftShift(d6)
d7 = leftShift(d7)
d8 = leftShift(d7)
d8 = leftShift(d8)
d9 = leftShift(d8)
d10 = leftShift(d9)
d10 = leftShift(d10)
d11 = leftShift(d10)
d11 = leftShift(d11)
d12 = leftShift(d11)
d12 = leftShift(d12)
d13 = leftShift(d12)
d13 = leftShift(d13)
d14 = leftShift(d13)
d14 = leftShift(d14)
d15 = leftShift(d14)
d15 = leftShift(d15)
d16 = leftShift(d15)




cKeys = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16]
dKeys = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]

'''
def copyArray(arr,newArr):
    newArr = []
    for item in arr:
        newArr.append(item)
        
#Generate c keys:
cDict = {}
cCount = 0
nextC = []

while cCount <= 3:
    nextC = []
    thisC = []
    if cCount == 0:
        cDict[0] = c0
        cCount += 1
    elif cCount in [1, 2, 9, 16] :
        if cCount not in cDict:
            nextC = leftShift(cDict[cCount -1])
            cDict[cCount] = nextC
        cCount += 1
    elif cCount in [3,4,5,6,7,8,10,11,12,13,14,15]: 
        if cCount not in cDict:
            nextC= leftShift(cDict[cCount -1])
            nextC = leftShift(nextC)
            cDict[cCount] = nextC
        cCount += 1
print(cDict)
    

#Generate d keys:
dDict = {}
dCount = 0
nextD = []

while dCount <= 16:
    if dCount == 0:
        dDict[0] = d0
        dCount += 1
    elif dCount in [1, 2, 9, 16] :
        nextD = leftShift(dDict[dCount -1])
        dDict[dCount] = nextD
        dCount += 1
    else: 
        thisD = leftShift(dDict[dCount - 1])
        nextD = leftShift(thisD)
        dDict[dCount] = nextD
        dCount += 1

    
# combine c and d keys into one key
       
cdDict = {}


for i in range(17):
    currCD = []
    for j in range(28):
        currCD.append(cKeys[i][j])
    for l in range(28):
        currCD.append(dKeys[i][l])
    cdDict[i] = currCD
def permuteString(str,permute):
    strBits = []
    for bit in str: 
        strBits.append(bit)
    strBitsDict = {}
    countBits = 1
    for bit in strBits:
        strBitsDict[countBits] = bit
        countBits +=1
    

    permutedStr = []
    for index in permute: 
        permutedStr.append(strBitsDict[index])

    return permutedStr

#create K values using pc-2 1 and indexes of cd arrays
pc2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,2,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

kdict = {}

for item in cdDict:
    kdict[item] = permuteString(''.join(cdDict[item]), pc2)




#--------------------Begin decoding using the keys stored in kdict ------------

#create some needed tables

IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
eBit = [ 32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]


initMessage = "0000000100100011010001010110011110001001101010111100110111101111"


    

messageInitPermute = permuteString(initMessage,IP)

#Create R0 and L0 by splitting array in half
l0 = messageInitPermute[:32]
r0 = messageInitPermute[32:]


#flip keys since we're decrypting
'''
k1 = kdict[16]
k2 = kdict[15]
k3 = kdict[14]
k4 = kdict[13]
k5 = kdict[12]
k6 = kdict[11]
k7 = kdict[10]
k8 = kdict[9]
k9 = kdict[8]
k10 = kdict[7]
k11 = kdict[6]
k12 = kdict[5]
k13 = kdict[4]
k14 = kdict[3]
k15 = kdict[2]
k16 = kdict[1]
'''

l1 = r0
#r1 = l0 + f(r0,k1)
def eBitFunc(r,e):
    er = []
    for index in e:
        er.append(r[int(index)-1]) 
    return er

er = eBitFunc(r0,eBit) # get the ebits using the function and the r value

def xor(a,b): 
    c = []
    for i in range(len(a)):
        if int(a[i]) == int(b[i]):
            c.append(0)
        else: 
            c.append(1)
    return c

a = ["0","0","0","1","1","0"]
b = ["0","1","1","1","1","0"]
xortest = xor(a,b)




    


'''