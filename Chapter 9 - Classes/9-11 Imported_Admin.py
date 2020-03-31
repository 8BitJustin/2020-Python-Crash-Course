"""
Start with your work from Exercise 9-8. Store the classes User, Privileges,
and Admin in one module. Create a separate file, make an Admin instance,
and call show_privileges() to show that everything is working correctly
"""

# Imported specific class (Admin) from user_module module
from user_module import Admin

# Creates superuser variable using Admin class.
superuser = Admin('justin', 'olson')

# Uses the describe_admin method within Admin class.
superuser.describe_admin()

# Uses the 'self.privileges' within Admin to access the Privileges class,
# then use the show_privileges method.
superuser.privileges.show_privileges()

"""
From top to bottom:

superuser variable was created using the imported Admin class. Then 
superuser used the describe_admin() within the Admin class. Finally, 
the superuser accessed the show_privileges() method within the Privileges 
class by accessing self.privileges (privileges) within Admin class. This is 
tied to Privileges(), which is a backdoor so-to-speak with accessing the 
Privileges class, which wasn't actually imported into this file.
"""