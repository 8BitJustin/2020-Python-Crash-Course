current_users = ['james', 'justin', 'nick', 'roger', 'marco', 'nikk']
new_users = ['kaitlyn', 'skyler', 'leah', 'bexley', 'nick']

for nuser in new_users:
    if nuser.lower() in current_users:
        print("Sorry, " + nuser + " is taken.")
    else:
        print("Welcome, " + nuser + '!')
