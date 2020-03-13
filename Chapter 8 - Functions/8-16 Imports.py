from create_car import build_car as bc

"""
Using with create_car.py
"""

"""
Other ways to import:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

subaru = bc('subaru', 'wrx', color='silver', completed=10)

print(subaru)