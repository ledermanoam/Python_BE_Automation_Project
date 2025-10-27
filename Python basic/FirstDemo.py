print("hello")

a = 3
print(a)


str = "hello world"
print(str)
b, c, d = 5,6.4, "Great" # call all the b,c,d same value

print("{} {}".format("value is",b))
print(type(b))
#---------------------------------------------------------------------------------------------------------------------------------

# Python List

values = [1, 2, "noam", 4, 5]
print(values[0])
print(values[1:3])
print(values[-1])

values.insert(3,"shetty")
print(values)

values.append("End")
print(values)

### Update list ###
values[2] = "Lederman"
print(values)

### Delete values from the list ###
del values[0]
print(values)


### Tuple and Directory Data type ###
val = (1,2, "noam", 4.5)
print(val[1])
#val[2] = "lederman" --> will rase error

# Directory
dic = {"a":2,  4: "abc", "z": 123, "c": "Hello world" }
print(dic[4])
print(dic["c"])

print("insert to directory")
# insert to directory
my_dict = {}
my_dict["firstname"] = "NoamYosef"
my_dict["lastname"] = "Lederman"
my_dict ["gender"] = "man"

print(my_dict)






