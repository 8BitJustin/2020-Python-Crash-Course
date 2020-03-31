"""
Store the User class in one module, and store the Privileges and Admin
classes in a separate module. In a separate file, create an Admin instance
and call show_privileges() to show that everything is still working correctly.
"""

import admin_priv_912

superuser = admin_priv_912.Admin('justin', 'olson')
superuser.describe_admin()
superuser.privileges.show_privileges()