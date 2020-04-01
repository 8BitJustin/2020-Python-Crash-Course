from collections import OrderedDict

languages = OrderedDict()

languages['fortran'] = 1954
languages['c++'] = 1983
languages['python'] = 1991
languages['brainfuck'] = 1993
languages['javascript'] = 1995

for l, y in languages.items():
    print(l.title() + ' was created in ' + str(y) + '.')
