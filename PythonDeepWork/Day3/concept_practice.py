#Why do we use try/except? - to catch errors so the program doesn't crash

#Simple example
try:
    x=10/0
except ZeroDivisionError:
    print("You cannot divide by zero")
except ZeroDivisionError:
    print('cannot dive by zero')

#Example with multiple exempts
try:
    value = int("Sachin")
except ValueError:
    print("Cannot convert text to number")


#Example with finally(always runs)
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Done checking file")

#Reading json(very common in API testing)
#Suppose we have JSON text:
import json
json_str = '{"firstname":"aditi","mid_name":"sachin","l_name":"mate","skills":["AI","Python"],"age":30}'
#Convert string to python dict
data = json.loads(json_str)
print(data["firstname"])
print(data["mid_name"])
print("l_name")
print(data["age"])

#Reading json from file
import json
with open("user.json") as f:
    data = json.load(f)
print(data["user"])
print(data["role"])
print(data)

#Functions with return
#Basic example
def add(a,b):
    return a+b
result =  add(5,4)
print(result)

#Function returning multiple value
def get_user():
    return "sachin", 30, "QA engineer"
name, age, role = get_user()
print(name, age, role )

#Function returning dict(common in API framework)
def get_user_payload():
    return {
    "firstname":"sachin",
    "lastname":"Mate",
    "position": "QA Enginerr",
    "totalPrice":25000
    }
paload = get_user_payload()
print(paload["firstname"])
print(paload["lastname"])
#This is EXACTLY how you build requests in API automation.

#List and Dict operations
#✔️List operations
nums = [10,20,30,40,50]

nums[1] #get item 20

nums[2]=35 #Modify item

nums.append(21) #Append

nums.pop() #removes last
nums.pop(1) #removes index 1

# ✔️Dict operations
user = {
     "name":"sachin",
     "l_name":"mate",
     "role":"QA",
     "exp":7
 }

print(user["name"]) #get value
user["role"]="SDET" #Set value
user["location"]="Pune" #Add new key

#Check key exist
if "name" in user:
    print("Yes")

#Iterate
for key,value in user.items():
    print(key, value)

#Safe get
print(user.get("exp",0)) #default 0

#Mini practice example
# a = input("Enter a value")
# try:
#     if a==int(a):
#         print("Yes")
# except ValueError:
#     print("Error not a number")

#Parse following json
import json
lapy = '{"id": 101, "product": "Laptop", "price": 55000}'
data = json.loads(lapy)
print(data["price"])

#create dict form list
names = ["sachin","subhash","mate"]
dict = {}
for name in names:
    l = len(name)
    dict[name]=l
print(dict)

#Dict comprehension
len_dict ={ name: len(name) for name in names}
print(len_dict)