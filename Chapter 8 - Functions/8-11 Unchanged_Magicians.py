def make_great(not_yet_great, now_great):
    while not_yet_great:
        popping = not_yet_great.pop()
        popping = popping + ', the Great'
        now_great.append(popping)
    # added .reverse to now_great as to keep it in order, as using pop will
    # change the order of the list, going from last to first
    now_great.reverse()


def show_magicians(names):
    for name in names:
        print(name.title() + '.')


magicians = ['houdini', 'copperfield', 'blaine']
greats = []

make_great(magicians[:], greats)
show_magicians(magicians)
show_magicians(greats)