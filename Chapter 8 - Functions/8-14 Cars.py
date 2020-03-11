def build_car(make, model, **added):
    car = {'make': make, 'model': model}
    for k, v in added.items():
        car[k] = v
    return car


subaru = build_car('subaru', 'wrx', color='silver')

print(subaru)
