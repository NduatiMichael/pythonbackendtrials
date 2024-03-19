# data types
a = 2
b = 3
c = 3.4
status = True
name = "Virtuosi"

#operators
d = a + c
e = a * b
f = b / a
g = b % a
h = b ** a

#list
estates = ["Karen", "Roselyne","Muthaiga", "Runda"]
print(estates)
estates.append("Limuru")
print(estates)
estates.append("Gikambura")
print(estates)
estates.pop()
print(estates)
estates.remove("Runda")
print(estates)
print(estates[1])
estates.sort()
print (estates)
estates[1] = "Limuru1"
print(estates)

#Tuple
fare = (200,500,600)
print (fare)

#dictionaries
staff = {
    "name": "Virtuosi",
    "designation": "Software engineer",
    "department" : "Secuviz",
    "credit_amount":2000
}
print (staff)
print(staff["name"])
staff["credit_amount"] = 5000
print (staff)
staff["preference"] = "Cash"
print(staff)
del staff["preference"]
print(staff)

#if statement
if "Karen" in estates:
    print("Karen is in Estate")
else:
    print("Karen is not in estates")

#for loop
for estate in estates:
    print(estate)

for items in staff:
    print (items)
#Validate Number
#Check length
phone = "+254706443677"
if len(phone) == 13:
    print("Process payment")
else:
    print("Please enter a correct number")