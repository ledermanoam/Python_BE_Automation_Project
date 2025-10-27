greeting = "Good morning"

if greeting == "Morning":
    print("condition matches")
else:
    print("condition do not matches")
print("if else condition code is completed")

print("##########################")

#for loop

obj = [2,3,4,5,6,7,8,9]
for a in obj:
    print(a + 10)

# you can add 10 to i and increase in 10


print("####################################")

# sum of first natural numbers 1+2+3+4+5 = 15

num = [1+2+3+4+5]
sum = 0
for i in range(1,6):
    sum = sum + i + i
    print(i)

print("#############################################")

for k in range(1,10,2):
    print(k)

print("######### skip the first index ##############")
for m in range(10):
    print(m)

print("########## While loop ######################")

it = 4
while it>1:
    print(it)
    it = it-1
print("while loop execution is done")


noam = 40
while noam>1:
    if noam == 39:
        break
    print(noam)

    noam = noam -2

noam = 40
while noam>1:
    if noam == 39:
        break
    print(noam)

    noam = noam -2