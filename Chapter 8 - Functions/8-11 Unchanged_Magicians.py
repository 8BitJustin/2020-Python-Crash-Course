def make_great(not_yet_great, now_great):
    while not_yet_great:
        popping = not_yet_great.pop()
        popping = popping + ', the Great'
        now_great.append(popping)


def show_magicians(names):
    for name in names:
        print(name.title() + '.')


magicians = ['houdini', 'copperfield', 'blaine']
greats = []

make_great(magicians[:], greats)
show_magicians(magicians)
show_magicians(greats)