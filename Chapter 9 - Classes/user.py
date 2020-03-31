# Imported specific class (Admin) from user_module module
from user_module import Admin

superuser = Admin('justin', 'olson')
superuser.describe_admin()
superuser.privileges.show_privileges()