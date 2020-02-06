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

print("Well shit, looks like only two people can go.\n")

print("I'm sorry " + guest_list.pop() + ", you are no longer invited.")
print("I'm sorry " + guest_list.pop() + ", you are no longer invited.")
print("I'm sorry " + guest_list.pop() + ", you are no longer invited.")
print("I'm sorry " + guest_list.pop() + ", you are no longer invited.\n")

print(guest_list[0] + ", you are still invited.")
print(guest_list[1] + ", you are still invited.\n")

del guest_list[0]
del guest_list[0]
del guest_list[0]

print(guest_list)