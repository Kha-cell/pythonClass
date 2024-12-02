my_dict = {"name":"alice","age":25,"city":"new York"}
print(my_dict["age"])

if "myname" in my_dict:
	print("myname is in the dictionary.")
else:
	print("not in your dictionary")

del my_dict["city"]
print(my_dict)

print(my_dict.get("name"))
print(my_dict.get("salary","not Available")) 

for key,value in my_dict.items():
	print(f" {key}: {value}")

squared = {x: x**2 for x in range(1,6)}
print(squared)

key = ["name", "age", "city",]
values = ["alice",25,"new York"]
 
for key,value in zip(key,values):
	my_dict[key] = value 
print(my_dict)