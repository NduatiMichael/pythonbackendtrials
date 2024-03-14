guestlist = ["Dad","Mum", 'Sue']

print(f'Welcome to the gala {guestlist[0]}')
print(f'You will be required to attend {guestlist[1]}')
print(f'Please purpose to attend {guestlist[2]}')

print (f"{guestlist[0]} can not make it")
guestlist[0] = 'Myles'

print(f'Welcome to the gala {guestlist[0]}')
print(f'You will be required to attend {guestlist[1]}')
print(f'Please purpose to attend {guestlist[2]}')

print("Hello Everyone, I've found a bigger table")

guestlist.insert(0,"Steve")
listsize = len(guestlist)
guestlist.insert(listsize//2,"Johnny")
guestlist.append('Esther')
print(guestlist)

print(f"Welcome to Michael's gala {guestlist[0]}")
print(f"Welcome to Michael's gala {guestlist[1]}")
print(f"Welcome to Michael's gala {guestlist[2]}")
print(f"Welcome to Michael's gala {guestlist[3]}")
print(f"Welcome to Michael's gala {guestlist[4]}")
print(f"Welcome to Michael's gala {guestlist[5]}")


print(f"I will be expecting {len(guestlist)} guests")

print("I'm sorry, I will have only two spots for the Gala")

poppedmember = guestlist.pop()
print(f"Sorry {poppedmember}, I will not have a space for you.")
print(guestlist)

poppedmember = guestlist.pop()
print(f"Sorry {poppedmember}, I will not have a space for you.")
print(guestlist)

poppedmember = guestlist.pop()
print(f"I'm Sorry {poppedmember}, I will have to cancel your reservation")
print(guestlist)

poppedmember = guestlist.remove("Johnny")
print(f"I'm sorry {poppedmember}, I had to cancel your application")
print(guestlist)

print(f"dear {guestlist[0]} you are still invited to the gala")
print(f"dear {guestlist[1]} you are still invited to the gala")
print(guestlist)

del guestlist[0]
print (guestlist)
del(guestlist[0])
print(guestlist)