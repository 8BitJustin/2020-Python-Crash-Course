def build_car(make, model, **added):
    car = {'make': make, 'model': model}
    for k, v in added.items():
        car[k] = v
    return car


subaru = build_car('subaru', 'wrx', color='silver', completed=10)

print(subaru)


"""
added for funsies
"""

for k, v in subaru.items():
    if k == 'completed':
        print(k.title() + ': ' + str(v) + '%')
    else:
        print(k.title() + ': ' + v.title())

