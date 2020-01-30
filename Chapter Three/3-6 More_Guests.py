guest_list = ["Jack Bauer", "Jack Ryan", "Jack Shit"]

print(guest_list[0] + " is going to the party.")
print(guest_list[1] + " is going to the party.")
print(guest_list[2] + " is not going to the party.\n")

guest_list[2] = "Jack Skellington"

print(guest_list[0] + " is going to the party.")
print(guest_list[1] + " is going to the party.")
print(guest_list[2] + " is going to the party.\n")

print("We got a bigger table!\n")

guest_list.append("Jack Sparrow")
guest_list.insert(0, "Jack Frost")
guest_list.insert(2, "Jack Reacher")

print(guest_list[0] + " is going to the party.")
print(guest_list[1] + " is going to the party.")
print(guest_list[2] + " is going to the party.")
print(guest_list[3] + " is going to the party.")
print(guest_list[4] + " is going to the party.\n")