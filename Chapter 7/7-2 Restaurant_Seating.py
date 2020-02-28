party = input("How many in your party today? ")

party = int(party)

if party > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")