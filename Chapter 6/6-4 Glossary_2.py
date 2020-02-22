languages = {
    'fortran': 1954,
    'c++': 1983,
    'python': 1991,
    'brainfuck': 1993,
    'ruby': 1995,
    'javascript': 1995,
    'c#:': 1995,
    'kotlin': 2011
}

for k, v in languages.items():
    print('\nLanguage: ' + k.title())
    print('\tCreated: ' + str(v))