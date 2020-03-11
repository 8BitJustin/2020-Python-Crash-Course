def build_car(make, model, **addl):
    car = {}
    car['make'] = make
    car['model'] = model
    for k,v in addl.items():
        car[k] = v
    return car

subaru = build_car('subaru', 'wrx', color='silver')

print(subaru)