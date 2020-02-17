users = ["justin", "james", "nick", "admin"]

for user in users:
    if user == 'admin':
        print("Hello " + user.title() + ", would you like to see a status "
                                     "report?")
    else:
        print("Hello " + user.title() + ".")