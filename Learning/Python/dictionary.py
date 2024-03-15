#A dictionary of recording
recording = {
    "Name":"Tomatoes",
    "Town":"Kimana",
    "Market":"Kisumu"
}

#Output the dictionary
print(recording)

#Update the dictionary
recording["Market"] = "Kampala"
print(recording)

#Add an Item in the dictionary
recording["Price"] = "10500"
recording["Quantity"] = 14
print(recording)

#Remove an item

del recording["Quantity"]
print(recording)
